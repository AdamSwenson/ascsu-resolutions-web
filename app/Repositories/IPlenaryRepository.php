<?php

namespace App\Repositories;

use App\Models\Plenary;

interface IPlenaryRepository
{
    public function setCurrentPlenary(Plenary $plenary);

    /**
     * Sets is_current on all plenaries to false
     * @return void
     */
    public function resetAllCurrentPlenaries();
}
