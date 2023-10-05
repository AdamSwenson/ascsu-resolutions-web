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


//        $p = new Plenary([
//            'thursday_date' => Carbon::today(),
//
//            'first_reading_folder_id' =>'1-U0SBib3UmfiXybzARUViIEmwj3mLhY5',
//            'plenary_folder_id'=>'1ITs5N1qpTbqVqAhALrxqSsDwiSKsnSj5',
//            'is_current' => true
//        ]);
//        $p->save();
        
        $this->call(CommitteeTableSeeder::class);



    }
}
