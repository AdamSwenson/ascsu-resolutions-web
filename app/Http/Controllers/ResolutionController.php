<?php

namespace App\Http\Controllers;

use App\Exceptions\PythonScriptError;
use App\Models\Plenary;
use App\Models\Resolution;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Process;

class ResolutionController extends Controller
{

    public function setApprovalStatus(Resolution $resolution, Request $request)
    {
        //Store this because we will need it for determininng
        //whether we need to alter the document
        $originalStatus = $resolution->status;

        $resolution->status = $request->status;
        $resolution->save();

        //Was failed; reset to null
        //Not marking document with failed, so nothing else need to do
        if($originalStatus === 'failed' && $resolution->isUnvoted){
            return response()->json($resolution);
        }

        //Was null; set to failed
        if(is_null($originalStatus) && $resolution->isFailed){
            return response()->json($resolution);
        }

        //==== Was null, failed, or approved
        //If it was already approved, do nothing.
        //This allows us to assume that it was originally unvoted or failed
        if($originalStatus === 'approved' && $resolution->isApproved){
            return response()->json($resolution);
        }

        $scriptfile = null;

        //Case 1: was null or failed; now approved
        if($resolution->isApproved){
            $scriptfile = 'web_add_approved_to_doc.py';
        }
        //Case 2: was approved, now failed or unvoted
        elseif ($resolution->isFailed || $resolution->isUnvotedstatus){
          $scriptfile = 'web_remove_approved_from_doc.py';
        }

        //todo AR-46: This should be the most recent plenary the resolution belongs to
        $plenary = $resolution->plenaries()->where('is_current', true)->first();


        try{
            $this->handleScript($scriptfile, [$plenary->id, $resolution->id]);
            return response()->json($resolution);

        }catch (PythonScriptError $error){
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
     *
     * @param Plenary $plenary
     * @param Resolution $resolution
     * @return \Illuminate\Http\JsonResponse
     */
    public function setAction(Plenary $plenary, Resolution $resolution)
    {
//        $resolution
//            ->plenaries()
//            ->attach($plenary, ['is_first_reading' => 0]);
        $resolution->setAction($plenary);
        $resolution->save();
        $resolution->refresh();
        return response()->json($resolution);

    }

    public function setFailed(Resolution $resolution){
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
