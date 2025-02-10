<?php

namespace Tests\Repositories;

use App\Models\Plenary;
use App\Repositories\PlenaryRepository;

//use PHPUnit\Framework\TestCase;
use App\Repositories\ResolutionRepository;
use Tests\TestCase;


class PlenaryRepositoryTest extends TestCase
{
    public function setUp(): void
    {
        parent::setUp();
        $this->object = new PlenaryRepository();
    }

    /** @test */
    public function getNextPlenary()
    {
        $og = Plenary::factory()->make();
        $nextId = $og->id + 1;
        $next = Plenary::factory()->make(['id' => $nextId]);

//call
        $result = $this->object->getNextPlenary($og);

        //check
        $this->assertEquals($nextId, $result->id);
    }
}
