<?php

namespace App\Http\Controllers;

use Illuminate\Foundation\Auth\Access\AuthorizesRequests;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Routing\Controller as BaseController;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Response;

class Controller extends BaseController
{
    use AuthorizesRequests, ValidatesRequests;

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
