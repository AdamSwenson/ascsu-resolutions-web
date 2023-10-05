<?php

namespace App\Http\Controllers;

use App\Exceptions\PythonScriptError;
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


    public function enforceStyling()
    {
        try{
            $scriptfile = 'web_enforce_styling.py';
            $result = $this->handleScript($scriptfile);
            return response()->json($result->output());
        }catch (PythonScriptError $error){
            return $error->getMessage();
        }
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
        try{
            $scriptfile = 'web_make_agenda.py';
            $result = $this->handleScript($scriptfile, $plenary->id);
            return response()->json($result->output());
        }catch (PythonScriptError $error){
            return $error->getMessage();
        }

    }

    public function createPublic(Plenary $plenary)
    {

        try{
            $scriptfile = 'web_copy_first_readings_for_feedback.py';
            $this->handleScript($scriptfile, $plenary->id);
            $plenary->refresh();
            return response()->json($plenary);

        }catch (PythonScriptError $error){
            return $error->getMessage();
        }

    }


    /**
     * Updates all titles in database from titles in resolution text
     */
    public function syncTitles()
    {
        try{
            $scriptfile = 'web_sync_titles.py';
            $result = $this->handleScript($scriptfile);
            return response()->json($result->output());

        }catch (PythonScriptError $error){
            return $error->getMessage();
        }

    }

}
