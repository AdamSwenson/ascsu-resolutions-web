<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Resolution extends Model
{
    const URL_BASE = 'https://docs.google.com/document/d/';

    use HasFactory;

    protected $fillable = ['document_id', 'title', 'number', 'waiver'];
    protected $appends = ['url', 'formattedNumber', 'firstReadingPlenary', 'actionPlenaries'];
    protected $casts = ['is_approved' => 'boolean'];


    /**
     * Creates sponsor attribute which is the sponsoring committee
     * @return mixed|null
     */
    public function getSponsorAttribute()
    {
        return $this->committees()->where('is_sponsor', true)->first();
    }

    public function getCosponsorsAttribute()
    {
        return $this->committees()->where('is_sponsor', '!=', true)->get();
    }

    public function getFormattedNumberAttribute()
    {
        //todo add year
        return "AS-" . $this->number; // . '-';
    }

    /**
     * Returns the plenary object for the plenary at which received
     * first reading.
     * There will be at most one first-reading plenary. Waiver items aren't
     * first readings?
     * @return mixed|null
     */
    public function getFirstReadingPlenaryAttribute()
    {
        return $this->belongsToMany(Plenary::class)
            ->wherePivot('is_first_reading', 1)
            ->first();
    }

    /**
     * Returns a list of all plenaries that aren't marked as
     * first reading.
     *
     * This needs to be a list in case a resolution gets referred back
     * to committee
     *
     * @return \Illuminate\Database\Eloquent\Collection
     */
    public function getActionPlenariesAttribute()
    {
        return $this->belongsToMany(Plenary::class)
            ->wherePivot('is_first_reading', 0)
            ->get();
    }

    public function getUrlAttribute()
    {
        return self::URL_BASE . $this->document_id;
    }


    public function committees()
    {
        return $this->belongsToMany(Committee::class)->withPivot('is_sponsor');
    }

    public function plenaries()
    {
        return $this->belongsToMany(Plenary::class)->withPivot('is_first_reading');
    }

//
//self.committee = committee
//self.cosponsors = cosponsors
//self.document_id = document_id
//self.title = title
//self.number = number


}
