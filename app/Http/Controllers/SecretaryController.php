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
        $plenary = Plenary::create(['thursday_date' => $request->thursday_date, 'is_current' => true]);
        $result = $this->runCreatePlenaryFoldersScript($plenary);
        $plenary->refresh();
        return response()->json($plenary);

    }

    public function enforceStyling()
    {
        $command = config('app.pythonBin');
        $executablePath = config('app.pythonScript');

        $command .= " web_enforce_styling.py ";

        $result = Process::path($executablePath)
            ->run($command);

//    dd($result);

        if ($result->successful()) {
            return $result->output();
        }
//        dd($result->output());
        return $result->errorOutput();
    }

    public function getSecretaryPage()
    {

        $plenary = Plenary::where('is_current', true)->first();

        $plenaryId = !is_null($plenary) ? $plenary->id : null;

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

    public function createAgenda(Plenary $plenary)
    {
        $command = config('app.pythonBin');
        $executablePath = config('app.pythonScript');

        $command .= " web_make_agenda.py " . $plenary->id;

        $result = Process::path($executablePath)
            ->run($command);

//    dd($result);

        if ($result->successful()) {
            return $result->output();
        }
//        dd($result->output());
        return $result->errorOutput();

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

        $command .= " web_make_folders_for_plenary.py " . $plenary->id;

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

        $command .= " web_copy_first_readings_for_feedback.py " . $plenary->id;

        $result = Process::path($executablePath)
            ->run($command);

        if ($result->successful()) {
            return $result->output();
        }
//        dd($result->output());
        return $result->errorOutput();

    }

    /**
     * Updates all titles in database from titles in resolution text
     * @return void
     */
    public function syncTitles()
    {
        $command = config('app.pythonBin');
        $executablePath = config('app.pythonScript');

        $command .= " web_sync_titles.py ";

        $result = Process::path($executablePath)
            ->run($command);

        if ($result->successful()) {
            return $result->output();
        }
//        dd($result->output());
        return $result->errorOutput();

    }

}
