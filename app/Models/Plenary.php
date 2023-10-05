<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Support\Carbon;

class Plenary extends Model
{
    const URL_BASE = 'https://drive.google.com/drive/folders/';
    use HasFactory;

    protected $fillable = [
        'agenda_id',
        'first_reading_folder_id',
        'feedback_folder_id',
        'is_current',
        'plenary_folder_id',
        'second_reading_folder_id',
        'thursday_date'];

protected $casts = ['is_current' => 'boolean'];

protected $appends = ['publicUrl', 'plenaryUrl', 'plenaryName'];


    public function getPublicUrlAttribute(){
        return self::URL_BASE . $this->feedback_folder_id;
    }

    public function getPlenaryUrlAttribute(){
        return self::URL_BASE . $this->plenary_folder_id;
    }

    public function getPlenaryNameAttribute(){
       $d = new Carbon($this->thursday_date);
    return $d->format('Y F');
    }

    public function resolutions(){
        return $this->belongsToMany(Resolution::class)->withPivot(['is_first_reading', 'is_waiver']);

//        return $this->hasMany(Resolution::class);
    }

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
