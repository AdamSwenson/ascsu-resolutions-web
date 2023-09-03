<?php

namespace App\Http\Controllers;

use App\Models\Plenary;
use App\Models\Resolution;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Process;

class PermissionsController extends Controller
{
    //



    public function lockEditingAll(Plenary $plenary)
    {
        $command = config('app.pythonBin');

//        $command = "../../ResolutionManager/rezzies/bin/python";
        $command .= " web_lock_all_plenary_files.py " . $plenary->id;

        $executablePath = config('app.pythonScript');

//        $executablePath = '../../ResolutionManager/executables';
        $result = Process::path($executablePath)
            ->run($command);

        if ($result->successful()) {
            return $result->output();
//$this->sendAjaxSuccess();
        }
        return $result->errorOutput();

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
        $command = config('app.pythonBin');

//        $command = "../../ResolutionManager/rezzies/bin/python";
        $command .= " web_unlock_all_plenary_files.py " . $plenary->id;

        $executablePath = config('app.pythonScript');

//        $executablePath = '../../ResolutionManager/executables';
        $result = Process::path($executablePath)
            ->run($command);

        if ($result->successful()) {
            return $result->output();
//$this->sendAjaxSuccess();
        }
        return $result->errorOutput();

        //return $this->sendAjaxFailure();
//        dd($result->output());
    }

    public function lockEditingOne(Resolution $resolution)
    {
        $command = config('app.pythonBin');

//        $command = "../../ResolutionManager/rezzies/bin/python";
        $command .= " web_lock_one_file.py " . $resolution->id;

        $executablePath = config('app.pythonScript');

//        $executablePath = '../../ResolutionManager/executables';
        $result = Process::path($executablePath)
            ->run($command);

        if ($result->successful()) {
//            dd($result->output());
//            $j = json_decode($result->output());
            //assumes that the anyoneWithLink will be the first permission
//            return response()->json($j->permissions[0]);
            //response()->json();
return $this->sendAjaxSuccess();
        }
        return $result->errorOutput();


    }

    public function unlockEditingOne(Resolution $resolution)
    {
        $command = config('app.pythonBin');

//        $command = "../../ResolutionManager/rezzies/bin/python";
        $command .= " web_unlock_one_file.py " . $resolution->id;

        $executablePath = config('app.pythonScript');

//        $executablePath = '../../ResolutionManager/executables';
        $result = Process::path($executablePath)
            ->run($command);

        if ($result->successful()) {
//            dd($result->output());
//            $j = json_decode($result->output());
            //assumes that the anyoneWithLink will be the first permission
//            return response()->json($j->permissions[0]);
            //response()->json();
return $this->sendAjaxSuccess();
        }
        return $result->errorOutput();


    }

    public function getPermissions(Resolution $resolution)
    {
        $command = config('app.pythonBin');

//        $command = "../../ResolutionManager/rezzies/bin/python";
        $command .= " web_get_file_permissions.py " . $resolution->id;

        $executablePath = config('app.pythonScript');

//        $executablePath = '../../ResolutionManager/executables';
        $result = Process::path($executablePath)
            ->run($command);

        if ($result->successful()) {
//            dd($result->output());
            $j = json_decode($result->output());
            //assumes that the anyoneWithLink will be the first permission
            return response()->json($j->permissions[0]);
            //response()->json();
//$this->sendAjaxSuccess();
        }
        return $result->errorOutput();


    }


}
