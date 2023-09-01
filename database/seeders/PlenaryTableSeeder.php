<?php

namespace Database\Seeders;

use App\Models\Plenary;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Carbon;

class PlenaryTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        Plenary::factory()->create([
            'first_reading_folder_id' =>'1sv_4BUV5fk6Kcjss8HeSCJWnsLZJVpKC',
            'plenary_folder_id'=>'1ITs5N1qpTbqVqAhALrxqSsDwiSKsnSj5',
            'is_current' => true
        ]);
        Plenary::factory()->count(10)->create();
    }
}
