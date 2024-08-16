<?php

namespace Tests\Unit\Repositories;

use App\Models\Committee;
use App\Models\Plenary;
use App\Models\Resolution;
use App\Repositories\ResolutionRepository;
use Tests\TestCase;

//use PHPUnit\Framework\TestCase;


class ResolutionRepositoryTest extends TestCase
{

    public function setUp(): void
    {
        parent::setUp();
        $this->object = new ResolutionRepository();
    }

    /** @test */
    public function addSponsor()
    {
        $resolution = Resolution::factory()->create();
        $committee = Committee::first();

        $this->object->addSponsor($resolution, $committee);

        //check
        $this->assertEquals($resolution->sponsor->id, $committee->id, "Sponsor added");
    }

    /** @test */
    public function addCosponsor()
    {
        $resolution = Resolution::factory()->create();
        $committee = Committee::first();

        //call
        $this->object->addCosponsor($resolution, $committee);

        //check
        $c = $resolution->cosponsors;
        $this->assertEquals(1, sizeof($c), "Only one cosponsor");
        $this->assertEquals($c[0]->id, $committee->id);
    }

    /** @test */
    public function removeSponsor()
    {
        $resolution = Resolution::factory()->create();
        $committees = Committee::all();
        $oldSponsor = $committees[0];
        $oldCosponsor = $committees[1];
        $oldCosponsor2 = $committees[2];

        $this->object->addSponsor($resolution, $oldSponsor);
        $this->object->addCosponsor($resolution, $oldCosponsor);
        $this->object->addCosponsor($resolution, $oldCosponsor2);

        //call
        $this->object->removeSponsor($resolution, $oldSponsor);

        //check
        $this->assertEmpty($resolution->sponsor);
        $this->assertEquals($resolution->cosponsors[0]->id, $oldCosponsor->id, "did not touch cosponsor 1");
        $this->assertEquals($resolution->cosponsors[1]->id, $oldCosponsor2->id, "did not touch cosponsor 2");
    }

    /** @test */
    public function removeCosponsor()
    {
        //prep
        $resolution = Resolution::factory()->create();
        $committees = Committee::all();
        $oldSponsor = $committees[0];
        $oldCosponsor1 = $committees[1];
        $oldCosponsor2 = $committees[2];

        $this->object->addSponsor($resolution, $oldSponsor);
        $this->object->addCosponsor($resolution, $oldCosponsor1);
        $this->object->addCosponsor($resolution, $oldCosponsor2);
        $this->assertEquals(2, sizeof($resolution->cosponsors));

        //call
        $this->object->removeSponsor($resolution, $oldCosponsor2);

        //check
        $this->assertEquals($oldSponsor->id, $resolution->sponsor->id);
        $this->assertEquals(1, sizeof($resolution->cosponsors), "Only one cosponsor left");
        $this->assertEquals($resolution->cosponsors[0]->id, $oldCosponsor1->id, "did not touch other cosponsor");
    }

    // ========================= updateSponsor

    /** @test */
    public function updateSponsorNoPreexistingSponsor()
    {
        //prep
        $resolution = Resolution::factory()->create();
        $committees = Committee::all();
        $oldCosponsor1 = $committees[1];
        $oldCosponsor2 = $committees[2];
        $newSponsor = $committees[3];

        $this->object->addCosponsor($resolution, $oldCosponsor1);
        $this->object->addCosponsor($resolution, $oldCosponsor2);
        $this->assertEquals(2, sizeof($resolution->cosponsors));

        //call
        $this->object->updateSponsor($resolution, $newSponsor);

        //check
        $this->assertEquals($newSponsor->id, $resolution->sponsor->id, "New sponsor added");
        $this->assertEquals(2, sizeof($resolution->cosponsors), "Correct number of cosponsors");
        $this->assertEquals($resolution->cosponsors[0]->id, $oldCosponsor1->id, "did not touch cosponsor1");
        $this->assertEquals($resolution->cosponsors[1]->id, $oldCosponsor2->id, "did not touch cosponsor2");
    }

    /** @test */
    public function updateSponsorSameAsPreexistingSponsor()
    {
        //prep
        $resolution = Resolution::factory()->create();
        $committees = Committee::all();
        $oldSponsor = $committees[0];
        $oldCosponsor1 = $committees[1];
        $oldCosponsor2 = $committees[2];

        $this->object->addSponsor($resolution, $oldSponsor);
        $this->object->addCosponsor($resolution, $oldCosponsor1);
        $this->object->addCosponsor($resolution, $oldCosponsor2);
        $this->assertEquals(2, sizeof($resolution->cosponsors));

        //call
        $this->object->updateSponsor($resolution, $oldSponsor);

        //check
        $this->assertEquals($oldSponsor->id, $resolution->sponsor->id, "No new sponsor added");
        $this->assertEquals(2, sizeof($resolution->cosponsors), "Correct number of cosponsors");
        $this->assertEquals($resolution->cosponsors[0]->id, $oldCosponsor1->id, "did not touch cosponsor1");
        $this->assertEquals($resolution->cosponsors[1]->id, $oldCosponsor2->id, "did not touch cosponsor2");
    }

    /** @test */
    public function updateSponsorChangesSponsor()
    {
        //prep
        $resolution = Resolution::factory()->create();
        $committees = Committee::all();
        $oldSponsor = $committees[0];
        $oldCosponsor1 = $committees[1];
        $oldCosponsor2 = $committees[2];
        $newSponsor = $committees[3];

        $this->object->addSponsor($resolution, $oldSponsor);
        $this->object->addCosponsor($resolution, $oldCosponsor1);
        $this->object->addCosponsor($resolution, $oldCosponsor2);
        $this->assertEquals(2, sizeof($resolution->cosponsors));

        //call
        $this->object->updateSponsor($resolution, $newSponsor);

        //check
        $this->assertEquals($newSponsor->id, $resolution->sponsor->id, "New sponsor added");

        $this->assertEquals(2, sizeof($resolution->cosponsors), "Correct number of cosponsors");
        $this->assertEquals($resolution->cosponsors[0]->id, $oldCosponsor1->id, "did not touch cosponsor1");
        $this->assertEquals($resolution->cosponsors[1]->id, $oldCosponsor2->id, "did not touch cosponsor2");
    }

    // ========================= updateCosponsors

    /** @test */
    public function updateCosponsorsKeepOneAddOne()
    {
        $resolution = Resolution::factory()->create();
        $committees = Committee::all();
        $oldSponsor = $committees[0];
        $oldCosponsor1 = $committees[1];
        $oldCosponsor2 = $committees[2];
        $newCosponsor = $committees[3];

        $this->object->addSponsor($resolution, $oldSponsor);
        $this->object->addCosponsor($resolution, $oldCosponsor1);
        $this->object->addCosponsor($resolution, $oldCosponsor2);
        $this->assertEquals(2, sizeof($resolution->cosponsors));

        //call
        $this->object->updateCosponsors($resolution, [$newCosponsor, $oldCosponsor2]);

        //check
        $this->assertEquals($oldSponsor->id, $resolution->sponsor->id, "Did not touch sponsor");
        $this->assertEquals(2, sizeof($resolution->cosponsors), "Correct number of cosponsors");
        $this->assertEquals($resolution->cosponsors[0]->id, $oldCosponsor2->id, "did not touch cosponsor 2");
        $this->assertEquals($resolution->cosponsors[1]->id, $newCosponsor->id, "Added new cosponsor");
    }

    /** @test */
    public function updateAllCosponsors()
    {
        $resolution = Resolution::factory()->create();
        $committees = Committee::all();
        $oldSponsor = $committees[0];
        $oldCosponsor1 = $committees[1];
        $oldCosponsor2 = $committees[2];
        $newCosponsor1 = $committees[3];
        $newCosponsor2 = $committees[4];

        $this->object->addSponsor($resolution, $oldSponsor);
        $this->object->addCosponsor($resolution, $oldCosponsor1);
        $this->object->addCosponsor($resolution, $oldCosponsor2);
        $this->assertEquals(2, sizeof($resolution->cosponsors));

        //call
        $this->object->updateCosponsors($resolution, [$newCosponsor1, $newCosponsor2]);

        //check
        $this->assertEquals($oldSponsor->id, $resolution->sponsor->id, "Did not touch sponsor");
        $this->assertEquals(2, sizeof($resolution->cosponsors), "Correct number of cosponsors");
        $this->assertEquals($resolution->cosponsors[0]->id, $newCosponsor1->id, "added cosponsor 1");
        $this->assertEquals($resolution->cosponsors[1]->id, $newCosponsor2->id, "Added new cosponsor 2");
    }

    /** @test */
    public function destroyResolution()
    {
        //prep
        $plenary = Plenary::factory()->create();
        $resolution = Resolution::factory()->create();
        $committees = Committee::all();
        $oldSponsor = $committees[0];
        $oldCosponsor1 = $committees[1];
        $oldCosponsor2 = $committees[2];

        $resolution->plenaries()->attach($plenary,
            [
                'reading_type' => 'first'
            ]);

        $this->object->addSponsor($resolution, $oldSponsor);
        $this->object->addCosponsor($resolution, $oldCosponsor1);
        $this->object->addCosponsor($resolution, $oldCosponsor2);
        $resolution->save();
        $resolution->refresh();

        //call
        $this->object->destroyResolution($resolution);

        //check
        $this->assertModelMissing($resolution);
        $this->assertDatabaseMissing('plenary_resolution', ['plenary_id' => $plenary->id, 'resolution_id' => $resolution->id]);
        $this->assertDatabaseMissing('committee_resolution', ['committee_id' => $oldSponsor->id, 'resolution_id' => $resolution->id]);
        $this->assertDatabaseMissing('committee_resolution', ['committee_id' => $oldCosponsor1->id, 'resolution_id' => $resolution->id]);
        $this->assertDatabaseMissing('committee_resolution', ['committee_id' => $oldCosponsor2->id, 'resolution_id' => $resolution->id]);
    }
}
