<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Resolution extends Model
{
    const URL_BASE = 'https://docs.google.com/document/d/';

    use HasFactory;

    protected $fillable = ['document_id', 'title', 'number', 'waiver'];
protected $appends = ['url'];
    public function getSponsorAttribute(){
        return $this->committees()->where('is_sponsor', true)->first();
    }

    public function getCosponsorsAttribute(){
        return $this->committees()->where('is_sponsor', '!=', true)->get();
    }

    public function getUrlAttribute(){
        return self::URL_BASE . $this->document_id;
    }

    //not sure if need since resolution will be in multiple plenaries
    public function plenaries(){}

    public function committees(){
        return $this->belongsToMany(Committee::class)->withPivot('is_sponsor');
    }

//
//self.committee = committee
//self.cosponsors = cosponsors
//self.document_id = document_id
//self.title = title
//self.number = number


}
