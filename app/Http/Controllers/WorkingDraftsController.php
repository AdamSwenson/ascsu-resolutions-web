<?php

namespace App\Http\Controllers;

use App\Exceptions\PythonScriptError;
use App\Models\Plenary;
use App\Models\Resolution;
use App\Repositories\PlenaryRepository;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;

/**
 * Handles moving resolutions between plenaries
 */
class WorkingDraftsController extends Controller
{

    public function __construct()
    {
        $this->plenaryRepo = new PlenaryRepository();
//        $this->middleware('auth');
    }

    /**
     * Moves resolutions in working drafts folder and non waiver first readings
     * from the provided plenary to the next plenary
     * @param Plenary $plenary
     * @return \Illuminate\Http\JsonResponse
     */
    public function bulk_move_from_plenary(Plenary $plenary)
    {
        $scriptfile = 'web_bulk_move_resolution_to_working_folder.py';

        $destinationPlenary = $this->plenaryRepo->getNextPlenary($plenary);

        try {

            $this->handleScript($scriptfile, [$plenary->id, $destinationPlenary->id]);

        } catch (PythonScriptError $error) {
            return response()->json(['code' => $error->getCode(), 'message' => $error->getMessage()]);
        }

        return $this->sendAjaxSuccess();
    }

    /**
     * Moves a single resolution to the working folder of the designated plenary
     * @param Plenary $plenary
     * @param Resolution $resolution
     * @return JsonResponse
     */
    public function move_to_plenary(Plenary $plenary, Resolution $resolution)
    {
        $scriptfile = 'web_move_resolution_to_working_folder.py';
        try {
            $this->handleScript($scriptfile, [$plenary->id, $resolution->id]);

            //toggle its status to working
            $resolution->setWorkingNew($plenary);

        } catch (PythonScriptError $error) {
            return response()->json(['code' => $error->getCode(), 'message' => $error->getMessage()]);
        }

        return response()->json($resolution);

    }

}
