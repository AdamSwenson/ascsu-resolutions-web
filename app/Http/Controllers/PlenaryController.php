<?php

namespace App\Http\Controllers;

use App\Models\Plenary;
use Illuminate\Http\Request;

class PlenaryController extends Controller
{
    //

    public function index()
    {
        return response()->json(Plenary::all());
    }

    public function get(Plenary $plenary)
    {
        return response()->json($plenary);

    }

    public function store(Plenary $plenary)
    {

    }

    public function update(Plenary $plenary)
    {

    }

    public function setCurrent(Plenary $plenary)
    {
        $og = Plenary::where('is_current', true)->get();
        if (!is_null($og)) {
            foreach ($og as $o)
                $o->is_current = false;
            $o->save();
        }

        $plenary->is_current = true;
        $plenary->save();
        response()->json($plenary);
    }

    public function createPlenaryFoldersForYear($startYear)
    {

    }
}
