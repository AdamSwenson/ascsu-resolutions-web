<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Support\Carbon;

class Plenary extends Model
{
    const URL_BASE = 'https://drive.google.com/drive/folders/';
    const DOCS_BASE = 'https://docs.google.com/document/d/';
    use HasFactory;

    protected $fillable = [
        'agenda_id',
        'first_reading_folder_id',
        'feedback_folder_id',
        'is_current',
        'plenary_folder_id',
        'second_reading_folder_id',
        'working_drafts_folder_id',
        'thursday_date',
        'is_agenda_locked'];

protected $casts = ['is_current' => 'boolean', 'is_agenda_locked' => 'boolean'];

protected $appends = ['publicUrl', 'plenaryUrl', 'plenaryName', 'resolutionListUrl'];


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

    public function getResolutionListUrlAttribute(){
        if (is_null($this->agenda_id)) return $this->agenda_id;
        return self::DOCS_BASE . $this->agenda_id;
    }

    public function resolutions(){
        return $this->belongsToMany(Resolution::class)->withPivot(['is_first_reading', 'is_waiver', 'reading_type']);

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
