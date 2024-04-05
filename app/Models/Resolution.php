<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

/**
 * Resolution representation.
 *
 * Status: Approved, Failed, null (when has not received a vote)
 *     NB, Whether resolution has a waiver is a property of the plenary-resolution
 *     junction table, since it only applies in the first-reading plenary
 *
 *
 */
class Resolution extends Model
{
    const URL_BASE = 'https://docs.google.com/document/d/';

    use HasFactory;


    //acceptable statuses: null, approved, failed
    protected $fillable = [
        'document_id',
        'title',
        'number',
        'status'
    ];

    protected $appends = [
//        'is_first_reading', 'is_waiver',
        'readingType',
        'url', 'formattedNumber', 'firstReadingPlenary', 'actionPlenaries',
        'sponsor', 'cosponsors'];

    protected $casts = ['is_approved' => 'boolean'];


    public function setApproved()
    {
//        $this->is_approved = true;
        $this->status = 'approved';
        $this->save();
    }

    public function setFailed()
    {
//        $this->is_approved = false;
        $this->status = 'failed';
        $this->save();
    }

    public function setUnvoted()
    {
        $this->status = null;
        $this->save();
    }

    /**
     * Makes the resolution a first reading in the given plenary
     * @param Plenary $plenary
     * @return void
     */
    public function setFirstReading(Plenary $plenary)
    {
//        $this->status = 'first';
        //change plenary
        $this->plenaries()->updateExistingPivot($plenary->id, [
            'is_first_reading' => true,
        ]);
        $this->save();
    }

    /**
     * Adds a plenary to the list of action plenaries
     *
     * @param Plenary $plenary
     * @return void
     */
    public function setAction(Plenary $plenary)
    {
        //change plenary
        $this->plenaries()
            ->attach($plenary, ['is_first_reading' => false]);
//        $this->plenaries()->updateExistingPivot($plenary->id, [
//            'is_first_reading' => false,
//        ]);
        $this->save();
    }


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
        return $this->committees()->where('is_cosponsor', true)->get();

        //changed in AR-75
        //return $this->committees()->where('is_sponsor', '!=', true)->get();
    }

    public function getFormattedNumberAttribute()
    {
        //todo add year
        return "AS-" . $this->number; // . '-';
    }

    public function getReadingTypeAttribute()
    {
        if (sizeof($this->actionPlenaries) > 0) return 'action';

        if ($this->isWaiver) return 'waiver';

        return 'first';
    }

//    public function getisFirstReadingAttribute()
//    {
//        $p = $this->belongsToMany(Plenary::class)
//            ->wherePivot('is_first_reading', 1)
//            ->first();
//
//    }

    public function getisWaiverAttribute()
    {
        $p = $this->belongsToMany(Plenary::class)
            ->wherePivot('is_first_reading', 1)
            ->wherePivot('is_waiver', 1)
            ->first();
        return !is_null($p);
        return false;
//        return $this->belongsToMany(Plenary::class)
//            ->wherePivot('is_first_reading', 1)
//            ->first();
    }

    /**
     * Sets or unsets resolution as a waiver item
     * Added in AR-81
     */
    public function toggleIsWaiver()
    {
        $newValue = !$this->isWaiver;

        $plenary = $this->belongsToMany(Plenary::class)
            ->wherePivot('is_first_reading', 1)
            ->firstOrFail();

        $this->plenaries()->updateExistingPivot($plenary->id, [
            'is_waiver' => $newValue,
        ]);
        $this->save();
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

    /**
     * Whether the resolution was approved
     * @return bool
     */
    public function getIsApprovedAttribute()
    {
        return $this->status === 'approved';
    }

    /**
     * Whether the resolution failed to pass
     * @return bool
     */
    public function getIsFailedAttribute()
    {
        return $this->status === 'failed';
    }

    /**
     * Whether the resolution has not been voted upon
     * @return bool
     */
    public function getIsUnvotedAttribute()
    {
        return is_null($this->status);
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
        return $this->belongsToMany(Plenary::class)->withPivot(['is_first_reading', 'is_waiver']);
    }

//
//self.committee = committee
//self.cosponsors = cosponsors
//self.document_id = document_id
//self.title = title
//self.number = number


}
