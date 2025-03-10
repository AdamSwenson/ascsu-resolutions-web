<?php

namespace App\Http\Controllers;

use App\Exceptions\PythonScriptError;
use App\Jobs\LockAllEditing;
use App\Jobs\UnlockAllEditing;
use App\Models\Plenary;
use App\Models\Resolution;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Process;

class PermissionsController extends Controller
{


    public function lockEditingAll(Plenary $plenary)
    {
        try{
            LockAllEditing::dispatch($plenary);
            return $this->sendAjaxSuccess();

//            $scriptfile = 'web_lock_all_plenary_files.py';
//            $result = $this->handleScript($scriptfile, $plenary->id);
//            return $result->output();
        }catch (PythonScriptError $error){
            return $error->getMessage();
        }

    }


    /**
     * Allows anyone with the link to edit any files in the plenary folder
     * @param Plenary $plenary
     * @return string
     */
    public function unlockEditingAll(Plenary $plenary)
    {
        try{
            UnlockAllEditing::dispatch($plenary);
            return $this->sendAjaxSuccess();
//            $scriptfile = 'web_unlock_all_plenary_files.py';
//            $result = $this->handleScript($scriptfile, $plenary->id);
//            return $result->output();
        }catch (PythonScriptError $error){
            return $error->getMessage();
        }

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

    }


}
