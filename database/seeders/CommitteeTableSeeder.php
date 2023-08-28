<?php

namespace Database\Seeders;

use App\Models\Committee;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class CommitteeTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $names =[
            ['name' => 'Academic Affairs', 'abbreviation' => 'AA'],
                ['name' => 'Academic Preparation and Educational Programs', 'abbreviation' => 'APEP'],
                ['name' => 'Executive Committee', 'abbreviation' => 'Exec'],
                ['name' => 'Fiscal and Governmental Affairs', 'abbreviation' => 'FGA'],
                ['name' => 'Faculty Affairs', 'abbreviation' => 'FA'],
                ['name' => 'Justice, Equity, Diversity, and Inclusion', 'abbreviation' => 'JEDI'],
            ];
        foreach($names as $name){
            Committee::create($name);
        }



    }
}
