<?php

namespace Tests\Jobs;

use App\Jobs\SyncReadingTypes;
use App\Jobs\UpdateAgenda;

//use PHPUnit\Framework\TestCase;
use App\Models\Plenary;
use Tests\TestCase;


class UpdateAgendaTest extends TestCase
{
    /** @test */
    public function handle()
    {
//$plenary = Plenary::factory()->create(['id' => 133]);
        $plenary = Plenary::find(self::TEST_PLENARY_PROPS['id']);

        UpdateAgenda::dispatch($plenary);


    }
}
