<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Process;

class DevController extends Controller
{
    //

    public function diagnostics(){
        $result = $this->runScript();

        if ($result->successful()) {
            return $result->output();
        }
        return $result->errorOutput();
    }

    public function runScript()
    {
        $executablePath = config('app.pythonScript');
//        $executablePath = config('app.pythonBin');

        $command = config('app.pythonBin');
        $command .= " test_directories.py ";

        $result = Process::path($executablePath)
            ->run($command);
        return $result;

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