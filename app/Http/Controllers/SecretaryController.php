<?php

namespace App\Http\Controllers;

use App\Exceptions\PythonScriptError;
use App\Jobs\UpdateAgenda;
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


    /**
     * Handles request to impose standard styling on all resolutions for the plenary
     * Updated to be plenary specific in AR-88
     * @param Plenary $plenary
     * @return \Illuminate\Http\JsonResponse|string
     */
    public function enforceStyling(Plenary $plenary)
    {
        try{
            $scriptfile = 'web_enforce_styling.py';
            $result = $this->handleScript($scriptfile, $plenary->id);
            return response()->json($result->output());
        }catch (PythonScriptError $error){
            return $error->getMessage();
        }
    }

    /**
     * Displays the secretary page
     * @return \Illuminate\Contracts\Foundation\Application|\Illuminate\Contracts\View\Factory|\Illuminate\Contracts\View\View|\Illuminate\Foundation\Application
     */
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

    /**
     * Handles the request to create the resolution list for the
     * given plenary
     * @param Plenary $plenary
     * @return \Illuminate\Http\JsonResponse|string
     */
    public function createAgenda(Plenary $plenary)
    {

//        UpdateAgenda::dispatchAfterResponse($plenary);
//return $this->sendAjaxSuccess();


        try{
            $scriptfile = 'web_make_agenda.py';
            $result = $this->handleScript($scriptfile, $plenary->id);
            return response()->json($result->output());
        }catch (PythonScriptError $error){
            return $error->getMessage();
        }

    }

    /**
     * Handles the request to create public, non editable versions of the resolutions
     * for the given plenary
     * @param Plenary $plenary
     * @return \Illuminate\Http\JsonResponse|string
     */
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
     * Updated to be plenary specific in AR-88
     * @param Plenary $plenary
     * @return \Illuminate\Http\JsonResponse|string
     */
    public function syncTitles(Plenary $plenary)
    {
        try{
            $scriptfile = 'web_sync_titles.py';
            $result = $this->handleScript($scriptfile, $plenary->id);
            return response()->json($result->output());

        }catch (PythonScriptError $error){
            return $error->getMessage();
        }

    }



}
