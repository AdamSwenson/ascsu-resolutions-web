<?php

namespace App\Http\Controllers;

use App\Exceptions\PythonScriptError;
use App\Models\Plenary;
use App\Models\Resolution;
use http\Env\Response;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Process;

class ResolutionController extends Controller
{

    public function setApprovalStatus(Resolution $resolution, Request $request)
    {
        //Store this because we will need it for determininng
        //whether we need to alter the document
        $originalStatus = $resolution->status;

        //Update the object and save
        $resolution->status = $request->status;
        $resolution->save();

        //Was failed; reset to null
        //Not marking document with failed, so nothing else need to do
        if ($originalStatus === 'failed' && $resolution->isUnvoted) {
            return response()->json($resolution);
        }

        //Was null; set to failed
        if (is_null($originalStatus) && $resolution->isFailed) {
            return response()->json($resolution);
        }

        //==== Was null, failed, or approved
        //If it was already approved, do nothing.
        //This allows us to assume that it was originally unvoted or failed
        if ($originalStatus === 'approved' && $resolution->isApproved) {
            return response()->json($resolution);
        }

        $scriptfile = null;

        //Case 1: was null or failed; now approved
        if ($resolution->isApproved) {
            $scriptfile = 'web_add_approved_to_doc.py';
        } //Case 2: was approved, now failed or unvoted
        elseif ($resolution->isFailed || $resolution->isUnvotedstatus) {
            $scriptfile = 'web_remove_approved_from_doc.py';
        }

        //todo AR-46: This should be the most recent plenary the resolution belongs to
        $plenary = $resolution->plenaries()->where('is_current', true)->first();

        try {
            $this->handleScript($scriptfile, [$plenary->id, $resolution->id]);
            return response()->json($resolution);

        } catch (PythonScriptError $error) {
            return $error->getMessage();
        }

        //        if (is_null($resolution->is_approved)) {
//            //If never been set, will be null
//            $resolution->setApproved();
////            $resolution->is_approved = true;
////            //AR-58
////            $resolution->status = 'approved';
//        } else {
//            //just toggle
//            //todo AR-58 WTF to do about this?
//            $resolution->is_approved = !$resolution->is_approved;
//        }
//
//        $resolution->save();

        //        $scriptfile = $resolution->isApproved ? 'web_add_approved_to_doc.py' :'web_remove_approved_from_doc.py';
//        if ($resolution->is_approved) {
//            $scriptfile = $resolution->is_approved ? 'web_add_approved_to_doc.py' :'web_remove_approved_from_doc.py';
//        } else {
//            $scriptfile = 'web_remove_approved_from_doc.py';
//        }

    }


    /**
     * Makes the resolution an action item in the indicated plenary
     * Changed this to a toggle in AR-87
     *
     * @param Plenary $plenary
     * @param Resolution $resolution
     * @return \Illuminate\Http\JsonResponse
     */
    public function setAction(Plenary $plenary, Resolution $resolution)
    {

        try {

            if ($resolution->readingType === 'action') {
                //toggle it back to a first reading
                $resolution->setFirstReading($plenary);
                $scriptfile = 'web_move_resolution_to_first_reading_folder.py';

            } else {
                //make it an action item
                $resolution->setAction($plenary);
                $scriptfile = 'web_move_resolution_to_action_folder.py';
            }
            $this->handleScript($scriptfile, [$plenary->id, $resolution->id]);

            $resolution->save();
            $resolution->refresh();

        } catch (PythonScriptError $error) {
            return response()->json(['code' => $error->getCode(), 'message' => $error->getMessage()]);

        }

        return response()->json($resolution);

    }

    /**
     * This is the new version
     * @param Plenary $plenary
     * @param Resolution $resolution
     * @param Request $request
     * @return \Illuminate\Http\JsonResponse
     * @version AR-92
     */
    public function setReadingType(Plenary $plenary, Resolution $resolution, Request $request)
    {
        try {

            switch ($request->readingType) {

                case 'action' :
                    $resolution->setActionNew($plenary);
                    $scriptfile = 'web_move_resolution_to_action_folder.py';
                    break;

                case 'first':
                    $resolution->setFirstReadingNew($plenary);
                    $scriptfile = 'web_move_resolution_to_first_reading_folder.py';
                    break;

                case 'waiver':
                    $resolution->setWaiverNew($plenary);
                    //todo Change waiver handling
                    $scriptfile = 'web_move_resolution_to_first_reading_folder.py';
                    break;

                case 'working':
                    $resolution->setWorkingNew($plenary);
                    $scriptfile = 'web_move_resolution_to_working_folder.py';
                    break;
            }

            $this->handleScript($scriptfile, [$plenary->id, $resolution->id]);

            $resolution->save();
            $resolution->refresh();

            $j = $resolution->toArray();
            $j['readingType'] = $resolution->getReadingType($plenary);

            return response()->json($j);

        } catch (PythonScriptError $error) {
            return response()->json(['code' => $error->getCode(), 'message' => $error->getMessage()]);

        }


    }

    public function setFailed(Resolution $resolution)
    {
        $resolution->setFailed();
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
        $rezzies = [];
        foreach ($plenary->resolutions as $r){
            //We need to add reading type manually
            $j = $r->toArray();
            $j['readingType'] = $r->getReadingType($plenary);
            array_push($rezzies, $j);
        }
        return response()->json($rezzies);
    }


    /**
     * Sets or unsets resolution as a waiver item
     * Added in AR-81
     * @return void
     */
    public function toggleWaiver(Resolution $resolution)
    {
        $resolution->toggleIsWaiver();
        $resolution->refresh();
        return response()->json($resolution);
    }

    // ******************************** CRUD

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
