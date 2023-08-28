<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Plenary extends Model
{
    use HasFactory;

    protected $fillable = ['first_reading_folder_id',
        'feedback_folder_id',
        'plenary_folder_id',
        'second_reading_folder_id',
        'thursday_date'];
//self.second_reading_folder_id = second_reading_folder_id
//self.feedback_folder_id = feedback_folder_id
//self.plenary_folder_id = plenary_folder_id
//self.first_reading_folder_id = first_reading_folder_id
//self.thursday_date = thursday_date
//self.month = month
//self.year = year
//self.friday_date = friday_date

//Month, year, and friday will be extrapolated from thursday date


}
