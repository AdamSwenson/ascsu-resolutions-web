<?php

namespace Tests\Http\Controllers;

use App\Http\Controllers\CommitteeController;

//use PHPUnit\Framework\TestCase;
use App\Http\Requests\ResolutionRequest;
use Illuminate\Support\Str;
use Tests\TestCase;


class CommitteeControllerTest extends TestCase
{

    public function setUp(): void
    {
        parent::setUp();
    }

    /** @test */
    public function recordResolutionUpdatesTitleCase()
    {
        $s = 'THIS IS A TEST';
        $r = new ResolutionRequest();
        $r->title = $s;

        $r->title  = Str::title($r->title);
        $this->assertEquals('This Is A Test', $r->title);

    }
}
