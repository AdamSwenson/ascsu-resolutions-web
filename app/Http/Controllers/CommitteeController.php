<?php

namespace App\Http\Controllers;

use App\Models\Committee;
use App\Models\Plenary;
use App\Models\Resolution;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Process;
use Illuminate\Support\Facades\Response;

class CommitteeController extends Controller
{
    //

    public function __construct()
    {
//        $this->middleware('auth');

    }

    public function getCommitteePage()
    {
        $plenary = Plenary::where('is_current', true)->first();

        // Return the page with student and activity data embedded
        $data = [
            'data' => [
                'url' => url(),
                'plenaryId' => $plenary->id,
                'plenary' => $plenary
//                'user' => $student,
//                'activity' => $activity,
            ],
//            'name' => $activity->name
        ];

        return view('committee', $data);


    }

    public function addSponsor(Resolution $resolution, Request $request)
    {
        $sponsor = Committee::where('name', $request->sponsor)->first();
        $resolution->committees()->attach($sponsor, ['is_sponsor' => true]);
//        $r->committees()->pivot()->is_sponsor = true;
        $resolution->save();
        return $resolution;
    }

    public function addCosponsors(Resolution $resolution, Request $request)
    {
        foreach ($request->cosponsors as $cosponsor) {
            $c = Committee::where('name', $cosponsor)->first();
            $resolution->committees()->attach($c, ['is_cosponsor' => true]);
        }
        $resolution->save();
        return $resolution;
    }

    public function getNextResolutionNumber(){
        $v =collect(Resolution::all())->pluck('number')->max();
    return $v +1;
    }


    public function recordResolution(Request $request)
    {
        $plenary = Plenary::where('id', 1)->first();
        $request->merge(['number' => $this->getNextResolutionNumber()]);
        $resolution = Resolution::create($request->all());
        $resolution = $this->addSponsor($resolution, $request);
        $resolution = $this->addCosponsors($resolution, $request);

        $result = $this->createResolutionInDrive($plenary, $resolution);
//        $result = $this->runScript();
//        dd($result);
        $resolution->refresh();
        return response()->json($resolution);
    }

    public function createResolutionInDrive(Plenary $plenary, Resolution $resolution){
//        $command = "PYTHONPATH=$(../../ResolutionManager/ResolutionManager) python3 test.py " . $plenary->id . " " . $resolution->id;
        $command = "../../ResolutionManager/rezzies/bin/python";

        $command .= " web_create_resolution_from_template.py " . $plenary->id . " " . $resolution->id;
//        $command = "python3 web_create_resolution_from_template.py " . $plenary->id . " " . $resolution->id;
//        $command = "python3 test.py " . $plenary->id;
        $executablePath = '../../ResolutionManager/executables';

//        $executablePath = '../../ResolutionManager/ResolutionManager/executables';

//        $executablePath = '../../ResolutionManager/ResolutionManager/executables';
        $result = Process::path($executablePath)
            ->run($command);

        if($result->successful()){
            return $result->output();
        }
//        dd($result->output());
        return $result->errorOutput();

    }

    public function runScript(){
//        $result = Process::run('pwd');
//        $result = Process::path('../../ResolutionManager/ResolutionManager/executables')
//            ->run('ls');
        $result = Process::path('../../ResolutionManager/executables')
//            ->run('ls');
            ->run('python3 test1.py 2');
//return $result->errorOutput();
//        ->run('PYTHONPATH=/Users/ars62917/Dropbox/ResolutionManager/ResolutionManager python3 test.py 2');
//            ->run('PYTHONPATH=/Users/ars62917/Dropbox/ResolutionManager/ResolutionManager python3 test.py 2');
    return $result->output();
    }

}
