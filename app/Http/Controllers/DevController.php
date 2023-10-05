<?php

namespace App\Http\Controllers;

use App\Exceptions\PythonScriptError;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Process;

class DevController extends Controller
{
    //

    public function testException(){
        throw new PythonScriptError("bad thing 2");

    }

    public function diagnostics(){
        try{
            $this->testException();


        }catch(PythonScriptError $result){
            return $result->getMessage();
        }

        //        $result = $this->runScript();
//
//        if ($result->successful()) {
//            return $result->output();
//        }
//        return $result->errorOutput();
    }

    public function runScript()
    {
        $executablePath = config('app.pythonScript');
        $command = config('app.pythonBin');
        $command .= " test1.py ";

//        $command = " pip install --upgrade mysql-connector-python google SQLAlchemy==1.4.0 google-api-python-client google-auth-httplib2 google-auth-oauthlib
//";

        return Process::path($executablePath)
            ->run($command);

//        $result = Process::run('pwd');
//        $result = Process::path('../../ResolutionManager/ResolutionManager/executables')
//            ->run('ls');
//        $result = Process::path($executablePath)
////            ->run('ls');
//            ->run('ls');
////return $result->errorOutput();
////        ->run('PYTHONPATH=/Users/ars62917/Dropbox/ResolutionManager/ResolutionManager python3 test.py 2');
////            ->run('PYTHONPATH=/Users/ars62917/Dropbox/ResolutionManager/ResolutionManager python3 test.py 2');
//        return $result;
    }


}
