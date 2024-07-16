<?php

namespace App\Http\Controllers;

use App\Http\Requests\ResolutionRequest;
use App\Exceptions\PythonScriptError;
use App\Models\Committee;
use App\Models\Plenary;
use App\Models\Resolution;
use App\Repositories\IResolutionRepository;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Process;
use Illuminate\Support\Facades\Response;
use Illuminate\Support\Str;

class CommitteeController extends Controller
{
    //

    /**
     * @var \Illuminate\Config\Repository|\Illuminate\Contracts\Foundation\Application|\Illuminate\Foundation\Application|mixed
     */
    public mixed $executablePath;
    /**
     * @var \Illuminate\Config\Repository|\Illuminate\Contracts\Foundation\Application|\Illuminate\Foundation\Application|mixed
     */
    public mixed $command;

    /**
     * @var IResolutionRepository
     */
    public mixed $resolutionRepo;

    public function __construct()
    {
//        $this->middleware('auth');
        $this->command = config('app.pythonBin');
        $this->executablePath = config('app.pythonScript');

        $this->resolutionRepo = app()->make(IResolutionRepository::class);
    }

    public function getCommitteePage()
    {
        $plenary = Plenary::where('is_current', true)->first();

        // todo Add committee information
        $data = [
            'data' => [
                'url' => url(),
                'plenaryId' => $plenary->id,
                'plenary' => $plenary
            ],

        ];

        return view('committee', $data);

    }

    /**
     * Returns all committee objects
     * @return JsonResponse
     */
    public function getCommittees(){
        $committees = Committee::all();
        return response()->json($committees);
    }

    public function diagnostics()
    {
        $result = $this->runScript();

        if ($result->successful()) {
            return $result->output();
        }
        return $result->errorOutput();
    }

    /**
     * Handles parsing the sponsor out of the request and asking the repository
     * to take care of it.
     * @param Resolution $resolution
     * @param Request $request
     * @return Resolution
     */
    protected function addSponsor(Resolution $resolution, Request $request)
    {
        $sponsor = Committee::where('name', $request->sponsor)->first();
        $this->resolutionRepo->addSponsor($resolution, $sponsor);
//        $resolution->committees()->attach($sponsor, ['is_sponsor' => true]);
//        $r->committees()->pivot()->is_sponsor = true;
        $resolution->save();
        return $resolution;
    }

    /**
     * Handles parsing the cosponsors out of the request and asking the repository
     * to  take care of it
     * @param Resolution $resolution
     * @param Request $request
     * @return Resolution
     */
    protected function addCosponsors(Resolution $resolution, Request $request)
    {
        foreach ($request->cosponsors as $cosponsor) {
            if ($resolution->sponsor->name !== $cosponsor) {
                $c = Committee::where('name', $cosponsor)->first();
                $this->resolutionRepo->addCosponsor($resolution, $c);
//                $resolution->committees()->attach($c, ['is_cosponsor' => true]);
            }
        }
        $resolution->save();
        return $resolution;
    }

    public function getNextResolutionNumber()
    {
        $v = collect(Resolution::all())->pluck('number')->max();
        return $v + 1;
    }


    /**
     * Creates a new resolution for first reading at the provided plenary
     * @param Plenary $plenary
     * @param ResolutionRequest $request
     * @return JsonResponse|string
     */
    public function recordResolution(Plenary $plenary, ResolutionRequest $request)
    {
        $request->merge(['number' => $this->getNextResolutionNumber()]);

        // AR-65
        $request['title'] = Str::title($request->title);

        $resolution = Resolution::create($request->all());

        //add committees
        $resolution = $this->addSponsor($resolution, $request);
        $resolution = $this->addCosponsors($resolution, $request);

        //set as first reading for plenary
        $readingType = $request->waiver ? 'waiver' : 'first';
        $resolution->plenaries()->attach($plenary,
            ['is_first_reading' => true,
                'is_waiver' => $request->waiver,
                'reading_type' => $readingType
            ]);

//        $result = $this->createResolutionInDriveNew($plenary, $resolution);

        try{
            //Actually create the document in drive
            $scriptfile = 'web_create_resolution_from_template.py';
            $this->handleScript($scriptfile, [$plenary->id, $resolution->id]);
            $resolution->refresh();
            return response()->json($resolution);
        }catch (PythonScriptError $error){
            return $error->getMessage();
        }

//        if ($result->successful()) {
//            $resolution->refresh();
//            return response()->json($resolution);
//        }
//        return $result->errorOutput();

    }

    /**
     * Handles the request to alter the committees set as either
     * sponsor or cosponsors
     * @param Resolution $resolution
     * @param Request $request
     * @return JsonResponse
     */
    public function updateCommittees(Resolution $resolution, Request $request){
        //figure out which need to be changed
        $sponsor = Committee::where('name', $request->sponsor['name'])->first();

        $cosponsors = [];
        foreach($request->cosponsors as $c){
            $cosponsors[] = Committee::where('name', $c['name'])->first();
        }

        $this->resolutionRepo->updateSponsor($resolution, $sponsor);
        $this->resolutionRepo->updateCosponsors($resolution, $cosponsors);

        $resolution = $resolution->refresh();
        return response()->json($resolution);

    }

//    public function createResolutionInDriveNew(Plenary $plenary, Resolution $resolution)
//    {
//
//        try{
//            $scriptfile = 'web_create_resolution_from_template.py';
//            $result = $this->handleScript($scriptfile, $plenary->id);
//            return response()->json($result);
//
//        }catch (PythonScriptError $error){
//            return $error->getMessage();
//        }

//        $command = config('app.pythonBin');
//        $executablePath = config('app.pythonScript');
//
//        $command .= " web_create_resolution_from_template.py " . $plenary->id . " " . $resolution->id;
//         $result = Process::path($executablePath)
//            ->run($command);
//
//        if ($result->successful()) {
//            return $result;
//        }
//        return $result->errorOutput();
//    }

//    public function runScript()
//    {
////        $executablePath = config('app.pythonScript');
//        $executablePath = config('app.pythonBin');
//
//
////        $result = Process::run('pwd');
////        $result = Process::path('../../ResolutionManager/ResolutionManager/executables')
////            ->run('ls');
//        $result = Process::path($executablePath)
////            ->run('ls');
//            ->run('ls');
////return $result->errorOutput();
////        ->run('PYTHONPATH=/Users/ars62917/Dropbox/ResolutionManager/ResolutionManager python3 test.py 2');
////            ->run('PYTHONPATH=/Users/ars62917/Dropbox/ResolutionManager/ResolutionManager python3 test.py 2');
//        return $result;
//    }
//
//
//    public function createResolutionInDrive(Plenary $plenary, Resolution $resolution)
//    {
//        $command = config('app.pythonBin');
//        $executablePath = config('app.pythonScript');
//
//        $command .= " web_create_resolution_from_template.py " . $plenary->id . " " . $resolution->id;
//
//        $result = Process::path($executablePath)
//            ->run($command);
//
//        if ($result->successful()) {
//            return $result->output();
//        }
////        dd($result->output());
//        return $result->errorOutput();
//
//    }

}
