<?php

namespace Database\Seeders;

use App\Models\Plenary;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Carbon;

class ProductionSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {

        $this->call(CommitteeTableSeeder::class);

        $p = new Plenary([
            'thursday_date' => Carbon::today(),

            'first_reading_folder_id' =>'1m_tElzh9_b6ousdOVgM0cIID6vOvom3p',
            'plenary_folder_id'=>'1ITs5N1qpTbqVqAhALrxqSsDwiSKsnSj5',
            'is_current' => true
        ]);
    }
}
