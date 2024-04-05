<?php

namespace Tests\Models;

use App\Models\Committee;
use App\Models\Plenary;
use App\Models\Resolution;

//use PHPUnit\Framework\TestCase;
use Illuminate\Database\Eloquent\ModelNotFoundException;
use Illuminate\Http\Request;
use Tests\TestCase;


class ResolutionTest extends TestCase
{
    /**
     * @var \Illuminate\Database\Eloquent\Collection|\Illuminate\Database\Eloquent\Model|mixed
     */
    public mixed $plenary;

    public function setUp(): void
    {
        parent::setUp();
        $this->plenary = Plenary::factory()->create();
    }

    /** @test */
    public function firstReadingPlenary()
    {
        $resolution = Resolution::factory()->create();
        $resolution->plenaries()->attach($this->plenary, ['is_first_reading' => true]);
        $resolution->save();
        $resolution->refresh();
        //call
        $result = $resolution->firstReadingPlenary;

        //check
        $this->assertInstanceOf(Plenary::class, $result);
        $this->assertEquals($this->plenary->id, $result->id);
    }

    /** @test */
    public function actionPlenariesWithOnePlenary()
    {
        $resolution = Resolution::factory()->create();
        $resolution->plenaries()->attach($this->plenary, ['is_first_reading' => 0]);
        $resolution->save();
        $resolution->refresh();
        //call
        $result = $resolution->actionPlenaries;

        //check
        $this->assertTrue(sizeof($result) === 1);
        $this->assertInstanceOf(Plenary::class, $result[0]);
        $this->assertEquals($this->plenary->id, $result[0]->id);
    }

    /** @test */
    public function actionPlenariesWithTwoPlenaries()
    {
        $plenary2 = Plenary::factory()->create();
        $resolution = Resolution::factory()->create();
        $resolution->plenaries()->attach($this->plenary, ['is_first_reading' => 0]);
        $resolution->plenaries()->attach($plenary2, ['is_first_reading' => 0]);

        $resolution->save();
        $resolution->refresh();

        //call
        $result = $resolution->actionPlenaries;

        //check
        $this->assertTrue(sizeof($result) === 2);
        $this->assertInstanceOf(Plenary::class, $result[0]);
        $this->assertEquals($this->plenary->id, $result[0]->id);

        $this->assertInstanceOf(Plenary::class, $result[1]);
        $this->assertEquals($plenary2->id, $result[1]->id);


    }


    // ============

    /** @test */
    public function setFirstReading()
    {
        $resolution = Resolution::factory()->create();
        $resolution->plenaries()->attach($this->plenary, ['is_first_reading' => 0]);
        $resolution->save();
        $resolution->push();
        $resolution->refresh();

        $this->assertEmpty($resolution->firstReadingPlenary, 'Check no first reading exists yet');

        //call
        $resolution->setFirstReading($this->plenary);
        $resolution->refresh();

        //check
        $this->assertEquals('first', $resolution->readingType);
        $this->assertNotEmpty($resolution->firstReadingPlenary);
    }

    /** @test */
    public function setApproved()
    {
        $resolution = Resolution::factory()->create();

        //call
        $resolution->setApproved();
        $resolution->refresh();

        //check
        $this->assertEquals('approved', $resolution->status);
//        $this->assertTrue($resolution->is_approved);
    }

    /** @test */
    public function setFailed()
    {
        $resolution = Resolution::factory()->create();

        //call
        $resolution->setFailed();
        $resolution->refresh();

        //check
        $this->assertEquals('failed', $resolution->status);
//        $this->assertFalse($resolution->is_approved);
    }

    /** @test */
    public function setActionWithoutPreexistingPlenary()
    {
        //simulates setting as action when there's no second
        //reading plenary already associated
        $resolution = Resolution::factory()->create();

        //call
        $resolution->setAction($this->plenary);
        $resolution->refresh();

        //check
        $this->assertEquals('action', $resolution->readingType);
        $this->assertNotEmpty($resolution->actionPlenaries);
    }

    /** @test */
    public function setActionWithPreexistingPlenary()
    {
        //Simulates the case where an item may have been referred back
        //thus there is already a second reading plenary present. Still should
        //associate it with the passed in one.
        $resolution = Resolution::factory()->create();
        $resolution->plenaries()->attach($this->plenary, ['is_first_reading' => 0]);
        $resolution->save();


        //call
        $plenary2 = Plenary::factory()->create();
        $resolution->setAction($plenary2);
        $resolution->refresh();

        //check
        $this->assertEquals('action', $resolution->readingType);
        $this->assertNotEmpty($resolution->actionPlenaries);
        $this->assertEquals(2, sizeof($resolution->actionPlenaries));
    }

    /** @test */
    public function approvalstatus()
    {
        $r = Resolution::factory()->create();
        $r->status = 'failed';
        $r->save();
        $og = $r->status;
        $r->status = 'approved';
        $r->save();
        $this->assertEquals('failed', $og);
    }

//========= Reading type

    /** @test */
    public function readingTypeFirst()
    {
        $resolution = Resolution::factory()->create();
        $resolution->plenaries()->attach($this->plenary, ['is_first_reading' => 1]);
        $resolution->save();
        $resolution->push();
        $resolution->refresh();

        //check
        $this->assertEquals('first', $resolution->readingType);
    }

    /** @test */
    public function readingTypeFirstWaiver()
    {
        $resolution = Resolution::factory()->create();
        $resolution->plenaries()->attach($this->plenary,
            ['is_first_reading' => 1,
                'is_waiver' => 1]);
        $resolution->save();
        $resolution->push();
        $resolution->refresh();

        $this->assertEquals('waiver', $resolution->readingType);
    }

    /** @test */
    public function readingTypeAction()
    {
        $resolution = Resolution::factory()->create();
        $resolution->plenaries()->attach($this->plenary,
            ['is_first_reading' => 0]);
        $resolution->save();
        $resolution->push();
        $resolution->refresh();

        $this->assertEquals('action', $resolution->readingType);
    }

    //========= Toggle waiver

    /** @test */
    public function toggleIsWaiverOffToOn()
    {
        $resolution = Resolution::factory()->create();
        $resolution->plenaries()->attach($this->plenary,
            ['is_first_reading' => 1,
                'is_waiver' => 0
            ]);
        $resolution->save();
        $resolution->push();
        $resolution->refresh();
        $this->assertFalse($resolution->isWaiver);

        //call
        $resolution->toggleIsWaiver();

        //check
        $resolution->refresh();

        $this->assertTrue($resolution->isWaiver);
    }

    /** @test */
    public function toggleIsWaiverOnToOff()
    {
        $resolution = Resolution::factory()->create();
        $resolution->plenaries()->attach($this->plenary,
            ['is_first_reading' => 1,
                'is_waiver' => 1
            ]);
        $resolution->save();
        $resolution->push();
        $resolution->refresh();
        $this->assertTrue($resolution->isWaiver);

        //call
        $resolution->toggleIsWaiver();

        //check
        $resolution->refresh();

        $this->assertFalse($resolution->isWaiver);
    }

    /** @test */
    public function toggleIsWaiverFailsIfActionItem()
    {
        $resolution = Resolution::factory()->create();
        $resolution->plenaries()->attach($this->plenary,
            ['is_first_reading' => 0,
                'is_waiver' => 0
            ]);
        $resolution->save();
        $resolution->push();
        $resolution->refresh();
        $this->assertFalse($resolution->isWaiver);
        $this->assertEquals('action', $resolution->readingType);

        $this->expectException(ModelNotFoundException::class);

        //call
        $resolution->toggleIsWaiver();
    }

// ==================== Sponsors and cosponsors

/** @test */
public function getSponsorAttribute(){
    $c = Committee::first();
    $r = Resolution::factory()->create();
    $r->committees()->attach($c, ['is_sponsor' => true]);

    //call
    $result = $r->sponsor;

    //check
    $this->assertEquals($c->id, $result->id, "getSponsor attribute returns correct committee");

}

    /** @test */
    public function getCoponsorAttribute(){
        $r = Resolution::factory()->create();
        $committees = Committee::all();
        foreach ($committees as $c){
            $r->committees()->attach($c, ['is_cosponsor' => true]);
        }
        $r->save();

        //call
        $result = $r->cosponsors;

        //check
        $this->assertEquals(sizeof($committees), sizeof($result));
    }

}
