<?php

namespace App\Traits;

use App\Exceptions\PythonScriptError;
use Illuminate\Support\Facades\Process;

trait HandleScriptTrait
{

    /**
     * @param $filename string The name of the python script to run, ending in .py
     * @param $inputs integer|array|string
     * @return \Illuminate\Contracts\Process\ProcessResult|\Illuminate\Process\ProcessResult
     * @throws PythonScriptError
     */
    public function handleScript(string $filename, int|array|string $inputs = []): \Illuminate\Process\ProcessResult|\Illuminate\Contracts\Process\ProcessResult
    {

        $command = config('app.pythonBin');
        $command .= " $filename ";

        //Add inputs to command string
        $inputs = is_array($inputs) ? $inputs : array($inputs);
        foreach ($inputs as $i) {
            $command .= " $i";
        }

        $executablePath = config('app.pythonScript');
        $result = Process::timeout(300)
            ->path($executablePath)
            ->run($command);

        if ($result->successful()) {
            return $result;
        }

        throw new PythonScriptError($result->errorOutput());
    }

}
