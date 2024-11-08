<?php

namespace Tests\Jobs;

use App\Jobs\SyncReadingTypes;

//use PHPUnit\Framework\TestCase;
use App\Models\Plenary;
use Tests\TestCase;


class SyncReadingTypesTest extends TestCase
{

    /** @test */
    public function handle()
    {
//$plenary = Plenary::factory()->create(['id' => 133]);
        $plenary = Plenary::find(133);

SyncReadingTypes::dispatch($plenary);
    }
}
