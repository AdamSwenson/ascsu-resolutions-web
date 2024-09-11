<?php

namespace App\Repositories;

use App\Models\Committee;
use App\Models\Resolution;

class ResolutionRepository implements IResolutionRepository
{

    /**
     * Returns the next unused resolution number
     * @return int|mixed
     */
    public function getNextResolutionNumber()
    {
        $v = collect(Resolution::all())->pluck('number')->max();
        return $v + 1;
    }


    // ===================== Committees
    /**
     * Sets sponsor.
     * Assumes that no other sponsor has been set.
     * @param Resolution $resolution
     * @param Committee $committee
     * @return Resolution
     */
    public function addSponsor(Resolution $resolution, Committee $committee){
        $resolution->committees()->attach($committee, ['is_sponsor' => true]);
        $resolution->push();
        return $resolution;
    }

    /**
     * Adds the committee as a cosponsor
     * @param Resolution $resolution
     * @param Committee $committee
     * @return Resolution
     */
    public function addCosponsor(Resolution $resolution, Committee $committee){
        $resolution->committees()->attach($committee, ['is_cosponsor' => true]);
        $resolution->push();
        return $resolution;
    }

    public function removeSponsor(Resolution $resolution, Committee $committee){
        $resolution->committees()->detach($committee);
        $resolution->push();
        return $resolution;
    }

    public function removeCoponsor(Resolution $resolution, Committee $committee){
        $resolution->committees()->detach($committee);
        $resolution->push();
        return $resolution;
    }


    /**
     * Adds or updates the committee set as sponsor
     * @param Resolution $resolution
     * @param Committee $committee
     * @return Resolution
     */
    public function updateSponsor(Resolution $resolution, Committee $committee){
        $oldSponsor = $resolution->sponsor;

        if(is_null($oldSponsor)) {
            //new, no existing rez}
            return $this->addSponsor($resolution, $committee);
        }

        //Existing sponsor
        // First check whether the new is the same as old
        if($oldSponsor->id === $committee->id) return $resolution;

        //Different sponsor
        $resolution->committees()->detach($oldSponsor);
        $resolution->committees()->attach($committee, ['is_sponsor' => true]);

        return $resolution;
    }

    /**
     * Adds or updates the committees set as cosponsors
     * @param Resolution $resolution
     * @param array $committees List of Committee objects
     * @return void
     */
    public function updateCosponsors(Resolution $resolution, $committees){
        //Check who is new
        $existingCosponsorIds = collect($resolution->cosponsors)->pluck('id');
        $committeeIds = collect($committees)->pluck('id');
        $to_remove = $existingCosponsorIds->diff($committeeIds)->all();
        $to_add = $committeeIds->diff($existingCosponsorIds)->all();

        //dev What about the case where a committee has been moved from cosponsor to sponsor already
        //  that would be a problematic race condition
        $resolution->committees()->detach($to_remove);
        $resolution->committees()->attach($to_add,  ['is_cosponsor' => true]);

        return $resolution;

    }


    /**
     * Deletes resolution after disassociating it from everything.
     * Mainly used to undo resolution creation if there is a error in creating
     * the document in drive
     * @param Resolution $resolution
     * @return void
     */
    public function destroyResolution(Resolution $resolution){
        # Get rid of plenary associations
        foreach($resolution->plenaries as $plenary){
            $resolution->plenaries()->detach($plenary);
        }

        foreach($resolution->committees as $committee){
            $resolution->committees()->detach($committee);
        }

        $resolution->delete();

    }
    //    /**
//     * Given a list of committees, this updates the associated cosponsors
//     * to have only those committees in the list
//     * @param Resolution $resolution
//     * @param $committees
//     * @return void
//     */
//    public function syncCosponsors(Resolution $resolution, $committees){
//     //does not work. also hoses sponsor
//        $resolution->committees()->sync($committees, ['is_cosponsor' => true]);
//        $resolution->push();
//        return $resolution;
//    }


}
