<?php

namespace App\Http\Controllers;

use App\Models\Activity;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;

class SecretaryController extends Controller
{

    public function __construct()
    {
//        $this->middleware('auth');

    }

    public function getSecretaryPage(){

        // Return the page with student and activity data embedded
        $data = [
            'data' => [
                'url' => url()
//                'user' => $student,
//                'activity' => $activity,
            ],
//            'name' => $activity->name
        ];

        return view('secretary', $data);


    }

    public function unlockEditing(){

    }


    public function lockEditing(){

    }

}
