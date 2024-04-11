<?php

namespace App\Repositories;

use App\Models\Plenary;

class PlenaryRepository implements IPlenaryRepository
{

    public function setCurrentPlenary(Plenary $plenary){

        $plenary->is_current = true;
        $plenary->save();
        return $plenary;
}

    /**
     * Sets is_current on all plenaries to false
     * @return void
     */
    public function resetAllCurrentPlenaries(){
        $og = Plenary::where('is_current', 1)->get();
        if (!is_null($og)) {
            foreach ($og as $o) {
                $o->is_current = false;
                $o->save();
            }
        }

    }
}
