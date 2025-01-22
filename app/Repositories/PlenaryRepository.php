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

    /**
     * Returns the next plenary in the session
     *
     * Done here to abstract. Right now just using the next
     * id, but may need to change that in the future to using
     * the date or something else
     * @param Plenary $plenary
     * @return Plenary
     */
    public function getNextPlenary(Plenary $plenary){
        $nextId = $plenary->id + 1;
        return Plenary::where('id', $nextId)->first();
    }

}
