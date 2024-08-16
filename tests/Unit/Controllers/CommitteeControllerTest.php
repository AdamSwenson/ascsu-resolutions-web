<?php

namespace Tests\Http\Controllers;

use App\Http\Controllers\CommitteeController;

//use PHPUnit\Framework\TestCase;
use App\Http\Requests\ResolutionRequest;
use App\Models\Committee;
use App\Models\Resolution;
use Illuminate\Support\Str;
use Tests\TestCase;


class CommitteeControllerTest extends TestCase
{

    public \Illuminate\Database\Eloquent\Collection $committees;
    /**
     * @var \Illuminate\Database\Eloquent\Collection|\Illuminate\Database\Eloquent\Model|mixed
     */
    public mixed $resolution;

    public function setUp(): void
    {
        parent::setUp();

        $this->resolution = Resolution::factory()->create();
        $this->committees = Committee::all();

    }

    /** @test */
    public function recordResolutionUpdatesTitleCase()
    {
        $s = 'THIS IS A TEST';
        $r = new ResolutionRequest();
        $r->title = $s;

        $r->title = Str::title($r->title);
        $this->assertEquals('This Is A Test', $r->title);
    }

    /** @test */
    public function updateCommitteesHappyPath()
    {

        $sponsor = $this->committees[0];
        $ogCosponsor1 = $this->committees[1];
        $ogCosponsor2 = $this->committees[2];
        $this->resolution->committees()->attach($sponsor, ['is_sponsor' => true]);
        $this->resolution->committees()->attach($ogCosponsor1, ['is_cosponsor' => true]);
        $this->resolution->committees()->attach($ogCosponsor2, ['is_cosponsor' => true]);

        $newSponsor = $this->committees[3];
        $newCosponsor = $this->committees[4];

        //call
        $data = ['sponsor' => $newSponsor,
            'cosponsors' => [$newCosponsor, $ogCosponsor2]];
$url = "committees/update/{$this->resolution->id}";
        $response = $this->post($url, $data);

//$response->dump();
        //check
        $response->assertSuccessful();
        $this->resolution->refresh();
        $this->assertEquals($newSponsor->id, $this->resolution->sponsor->id, "Sponsor updated");
        $cos = collect($this->resolution->cosponsors)->pluck('id');
        $this->assertContains($newCosponsor->id, $cos, "New cosponsor added");
        $this->assertContains($ogCosponsor2->id, $cos, "Existing cosponsor unchanged");
        $this->assertNotContains($ogCosponsor1->id, $cos, "Old cosponsor removed");

    }

    /** @test */
    public function updateCommitteesDoesNotCreateEmptySponsor()
    {

        $sponsor = $this->committees[0];
        $ogCosponsor1 = $this->committees[1];
        $ogCosponsor2 = $this->committees[2];
        $this->resolution->committees()->attach($sponsor, ['is_sponsor' => true]);
        $this->resolution->committees()->attach($ogCosponsor1, ['is_cosponsor' => true]);
        $this->resolution->committees()->attach($ogCosponsor2, ['is_cosponsor' => true]);

        $newSponsor = $this->committees[3];
        $newCosponsor = $this->committees[4];

        //call
        $data = ['sponsor' => null,
            'cosponsors' => [$newCosponsor, $ogCosponsor2]];
        $url = "committees/update/{$this->resolution->id}";
        $response = $this->post($url, $data);

//$response->dump();
        //check
        $response->assertServerError();
        $this->resolution->refresh();
        $this->assertEquals($sponsor->id, $this->resolution->sponsor->id, "Sponsor not updated");
        $cos = collect($this->resolution->cosponsors)->pluck('id');
        $this->assertContains($ogCosponsor1->id, $cos, "Existing cosponsor unchanged");
        $this->assertContains($ogCosponsor2->id, $cos, "Existing cosponsor unchanged");
        $this->assertNotContains($newCosponsor->id, $cos, "new cosponsor not added");

    }

    /** @test */
    public function updateCommitteesEmptyCosponsors()
    {
        $sponsor = $this->committees[0];
        $ogCosponsor1 = $this->committees[1];
        $ogCosponsor2 = $this->committees[2];
        $this->resolution->committees()->attach($sponsor, ['is_sponsor' => true]);
        $this->resolution->committees()->attach($ogCosponsor1, ['is_cosponsor' => true]);
        $this->resolution->committees()->attach($ogCosponsor2, ['is_cosponsor' => true]);

        $newSponsor = $this->committees[3];
        $newCosponsor = $this->committees[4];

        //call
        $data = ['sponsor' => $sponsor,
            'cosponsors' => []];
        $url = "committees/update/{$this->resolution->id}";
        $response = $this->post($url, $data);

//$response->dump();
        //check
        $response->assertSuccessful();
        $this->resolution->refresh();
        $this->assertEquals($sponsor->id, $this->resolution->sponsor->id, "Sponsor unchanged");
        $this->assertEmpty($this->resolution->cosponsors, "cosponsors now empty");
    }


}
