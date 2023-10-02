<?php

namespace App\Http\Controllers;

use App\Exceptions\PythonScriptError;
use Illuminate\Foundation\Auth\Access\AuthorizesRequests;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Routing\Controller as BaseController;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Process;
use Illuminate\Support\Facades\Response;

class Controller extends BaseController
{
    use AuthorizesRequests, ValidatesRequests;

    /**
     * Calls the python script and returns the response object or a
     * PythonScriptError
     *
     *
     * Call
    try{
    $scriptfile = 'web_copy_first_readings_for_feedback.py';
    $this->handleScript($scriptfile, $plenary->id);
    $plenary->refresh();
    return response()->json($plenary);

    }catch (PythonScriptError $error){
    return $error->getMessage();
    }

     * @param $filename string The name of the python script to run, ending in .py
     * @param $inputs integer|array|string
     * @return \Illuminate\Contracts\Process\ProcessResult|\Illuminate\Process\ProcessResult
     * @throws PythonScriptError
     */
    public function handleScript(string $filename, int|array|string $inputs=[]): \Illuminate\Process\ProcessResult|\Illuminate\Contracts\Process\ProcessResult
    {


        $command = config('app.pythonBin');
        $command .= " $filename ";

        //Add inputs to command string
        $inputs = is_array($inputs) ? $inputs : array($inputs);
        foreach ($inputs as $i) {
            $command .= " $i";
        }

        $executablePath = config('app.pythonScript');
        $result = Process::path($executablePath)
            ->run($command);

        if ($result->successful()) {
            return $result;
        }

        throw new PythonScriptError($result->errorOutput());
    }

    /**
     * Check with Auth to get the user and
     * set them as $this->user
     */
    protected function setLoggedInUser(){
        $this->user = Auth::user();
    }

    /**
     * Sends standard ajax request failure response with optional message string.
     * @param null|string $message
     * @param null|array $otherItems Array of items to include in the response
     * @return \Illuminate\Http\JsonResponse|boolean
     */
    public function sendAjaxFailure($message = null, $otherItems = null, $responseCode=500)
    {
        $sendMessage = $message ? $message : 'failure';
        $response = [
            'status' => 'fail',
            'message' => $sendMessage
        ];

        return response()->json($response, $responseCode);
    }

    /**
     * Sends standard ajax request success response with optional message string
     * @param null|string $message
     * @param null|array $otherItems Array of items to include in the response
     * @return \Illuminate\Http\JsonResponse|boolean
     */
    public function sendAjaxSuccess($message = null, $otherItems = null)
    {
        //event(new PleaseSendAjaxSuccess(null, $message, $otherItems));
        $sendMessage = $message ? $message : 'success';
        $response = [
            'status' => 'success',
            'message' => $sendMessage
        ];

        return Response::json($response);

    }

}
