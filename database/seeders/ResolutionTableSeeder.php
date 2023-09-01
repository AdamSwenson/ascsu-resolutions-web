<?php

namespace Database\Seeders;

use App\Models\Resolution;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class ResolutionTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        Resolution::factory()->create(['number' => 3010]);
    }
}
