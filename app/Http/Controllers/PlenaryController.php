<?php

namespace App\Http\Controllers;

use App\Exceptions\PythonScriptError;
use App\Jobs\UpdateAgenda;
use App\Models\Plenary;
use App\Repositories\IPlenaryRepository;
use App\Repositories\PlenaryRepository;
use Illuminate\Http\Request;

class PlenaryController extends Controller
{
    /**
     * @var PlenaryRepository|mixed
     */
    public PlenaryRepository $plenaryRepo;

    public function __construct()
    {
        $this->plenaryRepo = app()->make(IPlenaryRepository::class);
    }


    public function createPlenary(Request $request)
    {
        $this->plenaryRepo->resetAllCurrentPlenaries();

        $plenary = Plenary::create(
            ['thursday_date' => $request->thursday_date,
                'is_current' => true
            ]);

        try{
            $scriptfile = 'web_make_folders_for_plenary.py';
            $this->handleScript($scriptfile, $plenary->id);
            $plenary->refresh();

            UpdateAgenda::dispatchAfterResponse($plenary);

            return response()->json($plenary);
        }catch (PythonScriptError $error){
            return $error->getMessage();
        }

    }


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
        $this->plenaryRepo->resetAllCurrentPlenaries();
        $plenary = $this->plenaryRepo->setCurrentPlenary($plenary);
//        $og = Plenary::where('is_current', 1)->get();
//        if (!is_null($og)) {
//            foreach ($og as $o) {
//                $o->is_current = false;
//                $o->save();
//            }
//        }
//
//        $plenary->is_current = true;
//        $plenary->save();
        response()->json($plenary);
    }

    public function createPlenaryFoldersForYear($startYear)
    {

    }
}
