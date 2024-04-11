<?php

namespace App\Repositories;

use App\Models\Committee;
use App\Models\Resolution;

interface IResolutionRepository
{
    /**
     * Sets sponsor.
     * Assumes that no other sponsor has been set.
     * @param Resolution $resolution
     * @param Committee $committee
     * @return Resolution
     */
    public function addSponsor(Resolution $resolution, Committee $committee);

    /**
     * Adds the committee as a cosponsor
     * @param Resolution $resolution
     * @param Committee $committee
     * @return Resolution
     */
    public function addCosponsor(Resolution $resolution, Committee $committee);

    public function removeSponsor(Resolution $resolution, Committee $committee);

    public function removeCoponsor(Resolution $resolution, Committee $committee);

    /**
     * Adds or updates the committee set as sponsor
     * @param Resolution $resolution
     * @param Committee $committee
     * @return Resolution
     */
    public function updateSponsor(Resolution $resolution, Committee $committee);

    /**
     * Adds or updates the committees set as cosponsors
     * @param Resolution $resolution
     * @param array $committees List of Committee objects
     * @return void
     */
    public function updateCosponsors(Resolution $resolution, $committees);
}
