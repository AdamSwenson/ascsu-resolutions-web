<?php

namespace App\Http\Controllers;

use App\Models\Activity;
use App\Models\Plenary;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Process;

class SecretaryController extends Controller
{

    public function __construct()
    {
//        $this->middleware('auth');
    }

    public function createPlenary(Request $request)
    {
        $plenary = Plenary::create(['thursday_date' => $request->thursday_date]);
        $result = $this->runCreatePlenaryFoldersScript($plenary);
        $plenary->refresh();
        return response()->json($plenary);

    }

    public function getSecretaryPage()
    {

        $plenary = Plenary::where('is_current', true)->first();

        $plenaryId = ! is_null($plenary) ? $plenary->id  : null;

        // Return the page with student and activity data embedded
        $data = [
            'data' => [
                'url' => url(),
                'plenaryId' => $plenaryId,
                'plenary' => $plenary

            ],
        ];

        return view('secretary', $data);


    }



    public function createPublic(Plenary $plenary)
    {
        $result = $this->runCreatePublicScript($plenary);
        $plenary->refresh();
        return response()->json($plenary);

        return response()->json($plenary);
    }

    public function runCreatePlenaryFoldersScript(Plenary $plenary)
    {
        $command = config('app.pythonBin');
        $executablePath = config('app.pythonScript');

//        $command = "../../ResolutionManager/rezzies/bin/python";
        $command .= " web_make_folders_for_plenary.py " . $plenary->id;
  //      $executablePath = '../../ResolutionManager/executables';
        $result = Process::path($executablePath)
            ->run($command);

        if ($result->successful()) {
            return $result->output();
        }
//        dd($result->output());
        return $result->errorOutput();


    }

    public function runCreatePublicScript(Plenary $plenary)
    {
        $command = config('app.pythonBin');
        $executablePath = config('app.pythonScript');

//        $command = "../../ResolutionManager/rezzies/bin/python";
        $command .= " web_copy_first_readings_for_feedback.py " . $plenary->id;
  //      $executablePath = '../../ResolutionManager/executables';
        $result = Process::path($executablePath)
            ->run($command);

        if ($result->successful()) {
            return $result->output();
        }
//        dd($result->output());
        return $result->errorOutput();


    }

}
