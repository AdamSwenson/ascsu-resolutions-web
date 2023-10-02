<?php

namespace App\Http\Controllers;

use App\Exceptions\PythonScriptError;
use App\Models\Plenary;
use App\Models\Resolution;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Process;

class PermissionsController extends Controller
{
    //


    public function lockEditingAll(Plenary $plenary)
    {
        try{
            $scriptfile = 'web_lock_all_plenary_files.py';
            $result = $this->handleScript($scriptfile, $plenary->id);
            return $result->output();
//            return response()->json($result-);

        }catch (PythonScriptError $error){
            return $error->getMessage();
        }


//
//        $command = config('app.pythonBin');
//        $executablePath = config('app.pythonScript');
//
////        $command = "../../ResolutionManager/rezzies/bin/python";
//        $command .= " web_lock_all_plenary_files.py " . $plenary->id;
//
//
////        $executablePath = '../../ResolutionManager/executables';
//        $result = Process::path($executablePath)
//            ->run($command);
//
//        if ($result->successful()) {
//            return $result->output();
////$this->sendAjaxSuccess();
//        }
//        return $result->errorOutput();

        //return $this->sendAjaxFailure();
//        dd($result->output());


    }


    /**
     * Allows anyone with the link to edit any files in the plenary folder
     * @param Plenary $plenary
     * @return string
     */
    public function unlockEditingAll(Plenary $plenary)
    {
        try{
            $scriptfile = 'web_unlock_all_plenary_files.py';
            $result = $this->handleScript($scriptfile, $plenary->id);
            return $result->output();
        }catch (PythonScriptError $error){
            return $error->getMessage();
        }

//
//        $command = config('app.pythonBin');
//        $executablePath = config('app.pythonScript');
//
//        $command .= " web_unlock_all_plenary_files.py " . $plenary->id;
//
//        $result = Process::path($executablePath)
//            ->run($command);
//
//        if ($result->successful()) {
//            return $result->output();
//        }
//        return $result->errorOutput();

    }

    public function lockEditingOne(Resolution $resolution)
    {
        try{
            $scriptfile = 'web_lock_one_file.py';
            $this->handleScript($scriptfile, $resolution->id);
            return $this->sendAjaxSuccess();
        }catch (PythonScriptError $error){
            return $error->getMessage();
        }

//
//        $command = config('app.pythonBin');
//        $executablePath = config('app.pythonScript');
//
//        $command .= " web_lock_one_file.py " . $resolution->id;
//        $result = Process::path($executablePath)
//            ->run($command);
//
//        if ($result->successful()) {
//            return $this->sendAjaxSuccess();
//        }
//        return $result->errorOutput();


    }

    public function unlockEditingOne(Resolution $resolution)
    {
        try{
            $scriptfile = 'web_unlock_one_file.py';
            $this->handleScript($scriptfile, $resolution->id);
            return $this->sendAjaxSuccess();
        }catch (PythonScriptError $error){
            return $error->getMessage();
        }

//        $command = config('app.pythonBin');
//        $executablePath = config('app.pythonScript');
//
//        $command .= " web_unlock_one_file.py " . $resolution->id;
//
//        $result = Process::path($executablePath)
//            ->run($command);
//
//        if ($result->successful()) {
//            dd($result->output());
//            $j = json_decode($result->output());
            //assumes that the anyoneWithLink will be the first permission
//            return response()->json($j->permissions[0]);
            //response()->json();
//            return $this->sendAjaxSuccess();
//        }
//        return $result->errorOutput();


    }

    public function getPermissions(Resolution $resolution)
    {
        try{
            $scriptfile = 'web_get_file_permissions.py';
            $result = $this->handleScript($scriptfile, $resolution->id);
            $j = json_decode($result->output());
            //assumes that the anyoneWithLink will be the first permission
            return response()->json($j->permissions[0]);
        }catch (PythonScriptError $error){
            return $error->getMessage();
        }

//        $command = config('app.pythonBin');
//        $executablePath = config('app.pythonScript');
//
//        $command .= " web_get_file_permissions.py " . $resolution->id;
//
//        $result = Process::path($executablePath)
//            ->run($command);
//
//        if ($result->successful()) {
//            $j = json_decode($result->output());
//            //assumes that the anyoneWithLink will be the first permission
//            return response()->json($j->permissions[0]);
//        }
//
//        return $result->errorOutput();
    }


}
