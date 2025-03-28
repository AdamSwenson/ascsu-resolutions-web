<?php

namespace App\Http\Controllers;

use App\Exceptions\PythonScriptError;
use App\Jobs\CreatePublicFolder;
use App\Jobs\EnforceStyling;
use App\Jobs\LockAllEditing;
use App\Jobs\SyncReadingTypes;
use App\Jobs\SyncResolutionLocations;
use App\Jobs\SyncTitles;
use App\Jobs\UnlockAllEditing;
use App\Jobs\UpdateAgenda;
use App\Models\Activity;
use App\Models\Plenary;
use App\Repositories\PlenaryRepository;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Process;

class SecretaryController extends Controller
{

    public function __construct()
    {
//        $this->middleware('auth');
        $this->plenaryRepo = new PlenaryRepository();
    }


    /**
     * Handles request to impose standard styling on all resolutions for the plenary
     * Updated to be plenary specific in AR-88
     * @param Plenary $plenary
     * @return \Illuminate\Http\JsonResponse|string
     */
    public function enforceStyling(Plenary $plenary)
    {
        try {
            EnforceStyling::dispatch($plenary);
            return $this->sendAjaxSuccess();
//            $scriptfile = 'web_enforce_styling.py';
//            $result = $this->handleScript($scriptfile, $plenary->id);
//            return response()->json($result->output());
        } catch (PythonScriptError $error) {
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
        try {
            UpdateAgenda::dispatch($plenary);
            SyncResolutionLocations::dispatch($plenary);
            return $this->sendAjaxSuccess();
        } catch (PythonScriptError $error) {
            return $error->getMessage();
        }

//
//        try {
//            $scriptfile = 'web_make_agenda.py';
//            $result = $this->handleScript($scriptfile, $plenary->id);
//            return response()->json($result->output());
//        } catch (PythonScriptError $error) {
//            return $error->getMessage();
//        }

    }

    public function lockAgenda(Plenary $plenary)
    {
        $plenary = $this->plenaryRepo->lockAgenda($plenary);
        return response()->json($plenary);
    }

    public function unlockAgenda(Plenary $plenary)
    {
        $plenary = $this->plenaryRepo->unlockAgenda($plenary);
        return response()->json($plenary);
    }

    /**
     * Handles the request to create public, non editable versions of the resolutions
     * for the given plenary
     * @param Plenary $plenary
     * @return \Illuminate\Http\JsonResponse|string
     */
    public function createPublic(Plenary $plenary)
    {
        try {
            CreatePublicFolder::dispatch($plenary);
            $plenary->refresh();
            return response()->json($plenary);
        } catch (PythonScriptError $error) {
            return $error->getMessage();
        }

//
//
//        try {
//            $scriptfile = 'web_copy_first_readings_for_feedback.py';
//            $this->handleScript($scriptfile, $plenary->id);
//            $plenary->refresh();
//            return response()->json($plenary);
//
//        } catch (PythonScriptError $error) {
//            return $error->getMessage();
//        }

    }


    /**
     * Updates all titles in database from titles in resolution text
     * Updated to be plenary specific in AR-88
     * @param Plenary $plenary
     * @return \Illuminate\Http\JsonResponse|string
     */
    public function syncTitles(Plenary $plenary)
    {
        try {
            SyncTitles::dispatch($plenary);
            $this->sendAjaxSuccess();
        } catch (PythonScriptError $error) {
            return $error->getMessage();
        }

    }

    /**
     * One stop shop for everything which happens at beginning of plenary
     *
     * @param Plenary $plenary
     * @return \Illuminate\Http\JsonResponse
     */
    public function startPlenary(Plenary $plenary)
    {
        try{
//            SyncTitles::dispatch($plenary);
//            SyncResolutionLocations::dispatch($plenary);
//            SyncReadingTypes::dispatch($plenary);
//            UpdateAgenda::dispatch($plenary);
//            LockAllEditing::dispatch($plenary);
//            EnforceStyling::dispatch($plenary);
//
//            $this->plenaryRepo->lockAgenda($plenary);

            return $this->sendAjaxSuccess();
        }catch (PythonScriptError $error){
            return $error->getMessage();
        }

    }

    /**
     * One stop shop for everything that needs to happen at end of plenary
     *
     * @param Plenary $plenary
     * @return \Illuminate\Http\JsonResponse
     */
    public function stopPlenary(Plenary $plenary)
    {
        try{
//            SyncTitles::dispatch($plenary);
//            EnforceStyling::dispatch($plenary);
//            UnlockAllEditing::dispatch($plenary);

            return $this->sendAjaxSuccess();
        }catch (PythonScriptError $error){
            return $error->getMessage();
        }
    }

}
