<?php

namespace App\Http\Controllers;

use App\Exceptions\PythonScriptError;
use App\Models\Plenary;
use App\Models\Resolution;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Process;

class ResolutionController extends Controller
{

    public function toggleApproval(Resolution $resolution)
    {

        if (is_null($resolution->is_approved)) {
            //If never been set, will be null
            $resolution->is_approved = true;
        } else {
            //just toggle
            $resolution->is_approved = !$resolution->is_approved;
        }

        $resolution->save();

        //todo AR-46: This should be the most recent plenary the resolution belongs to
        $plenary = $resolution->plenaries()->where('is_current', true)->first();

//        $executablePath = config('app.pythonScript');
//        $command = config('app.pythonBin');
//        $command .= " web_add_approved_to_doc.py $plenary->id $resolution->id ";

        if ($resolution->is_approved) {
            $scriptfile = 'web_add_approved_to_doc.py';
//            $result = $this->runAddApprovedScript($resolution);
        } else {
            $scriptfile = 'web_remove_approved_from_doc.py';
//            $result = $this->runRemoveApprovedScript($resolution);
        }
//        $result = Process::path($executablePath)
//            ->run($command);
        try{
            $this->handleScript($scriptfile, [$plenary->id, $resolution->id]);
            return response()->json($resolution);

        }catch (PythonScriptError $error){
            return $error->getMessage();
        }

//        if ($result->successful()) {
//            return response()->json($resolution);
//        }
//        //todo error handling
//        return $result->errorOutput();

    }


//    public function runAddApprovedScript(Resolution $resolution)
//    {
//        $plenary = $resolution->plenaries()->where('is_current', true)->first();
//
//        $executablePath = config('app.pythonScript');
//        $command = config('app.pythonBin');
//        $command .= " web_add_approved_to_doc.py $plenary->id $resolution->id ";
//
//        $result = Process::path($executablePath)
//            ->run($command);
//
//        return $result;
//    }
//
//    public function runRemoveApprovedScript(Resolution $resolution)
//    {
//        $plenary = $resolution->plenaries()->where('is_current', true)->first();
//
//        $executablePath = config('app.pythonScript');
//        $command = config('app.pythonBin');
//        $command .= " web_remove_approved_from_doc.py $plenary->id $resolution->id ";
//
//        $result = Process::path($executablePath)
//            ->run($command);
//
//        return $result;
//    }


    /**
     * Makes the resolution an action item in the indicated plenary
     *
     * @param Plenary $plenary
     * @param Resolution $resolution
     * @return \Illuminate\Http\JsonResponse
     */
    public function setAction(Plenary $plenary, Resolution $resolution)
    {
        $resolution
            ->plenaries()
            ->attach($plenary, ['is_first_reading' => 0]);
        $resolution->save();
        $resolution->refresh();
        return response()->json($resolution);

    }

    /**
     * Gets all the resolutions for a given plenary
     * @param Plenary $plenary
     * @return \Illuminate\Http\JsonResponse
     */
    public function forPlenary(Plenary $plenary)
    {
        return response()->json($plenary->resolutions);
    }

    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        return Resolution::all();
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        //
    }

    /**
     * Display the specified resource.
     */
    public function show(string $id)
    {
        $resolution = Resolution::find($id);
        return response()->json($resolution);
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(string $id)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, string $id)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(string $id)
    {
        //
    }
}
