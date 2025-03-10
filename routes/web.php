<?php

use App\Http\Controllers\CommitteeController;
use App\Http\Controllers\DevController;
use App\Http\Controllers\PermissionsController;
use App\Http\Controllers\PlenaryController;
use App\Http\Controllers\ResolutionController;
use App\Http\Controllers\SecretaryController;
use App\Http\Controllers\WorkingDraftsController;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/



Route::get('/', function () {
    return view('welcome')->with(['data' => ['plenaryId' => null, 'plenary' => null]]);
});
Route::get('/privacy', function(){
   return view('privacy')->with(['data' => ['plenaryId' => null, 'plenary' => null]]);
});

// ============================= committee
Route::get('/committee', [CommitteeController::class, 'getCommitteePage']);
Route::get('/committees/all', [CommitteeController::class, 'getCommittees']);
Route::post('/committees/update/{resolution}', [CommitteeController::class, 'updateCommittees']);
Route::post('/resolution/{plenary}', [CommitteeController::class, 'recordResolution']);


// ============================= secretary
Route::get('/secretary', [SecretaryController::class, 'getSecretaryPage']);
Route::post('secretary/public/{plenary}', [SecretaryController::class, 'createPublic']);
Route::post('/secretary/agenda/{plenary}', [SecretaryController::class, 'createAgenda']);
Route::post('/secretary/styling/{plenary}', [SecretaryController::class, 'enforceStyling']);
Route::post('/secretary/sync/{plenary}', [SecretaryController::class, 'syncTitles']);

Route::post('secretary/plenary/{plenary}/start', [SecretaryController::class, 'startPlenary']);
Route::post('secretary/plenary/{plenary}/stop', [SecretaryController::class, 'stopPlenary']);

Route::post('/agenda/unlock/{plenary}', [SecretaryController::class, 'unlockAgenda']);
Route::post('/agenda/lock/{plenary}', [SecretaryController::class, 'lockAgenda']);

//Plenaries
Route::post('/secretary/folders', [PlenaryController::class, 'createPlenary']);
Route::post('plenary/current/{plenary}', [PlenaryController::class, 'setCurrent']);
Route::resource('plenaries', PlenaryController::class);
Route::get('plenary/resolutions/{plenary}', [ResolutionController::class, 'forPlenary']);

//Resolutions
Route::post('/resolution/reading/{plenary}/{resolution}', [ResolutionController::class, 'setReadingType']);
Route::resource('resolutions', ResolutionController::class);
Route::post('/resolution/action/{plenary}/{resolution}', [ResolutionController::class, 'setAction']);
Route::post('/resolution/waiver/toggle/{resolution}', [ResolutionController::class, 'toggleWaiver']);
Route::post('resolution/approval/{resolution}', [ResolutionController::class, 'setApprovalStatus']);
Route::post('resolution/working/bulk/{sourcePlenary}/{destinationPlenary}', [WorkingDraftsController::class, 'bulk_move_from_plenary']);
Route::post('resolution/working/{plenary}/{resolution}', [WorkingDraftsController::class, 'move_to_plenary']);


//Permissions
Route::post('secretary/permissions/all/lock/{plenary}', [PermissionsController::class, 'lockEditingAll']);
Route::post('secretary/permissions/all/unlock/{plenary}', [PermissionsController::class, 'unlockEditingAll']);
Route::post('secretary/permissions/one/lock/{resolution}', [PermissionsController::class, 'lockEditingOne']);
Route::post('secretary/permissions/one/unlock/{resolution}', [PermissionsController::class, 'unlockEditingOne']);
Route::get('secretary/permissions/one/{resolution}', [PermissionsController::class, 'getPermissions']);



//Route::get('resolution/approval/{resolution}', [ResolutionController::class, 'getApproval']);

// ============================== Dev and management
Route::get('diagnosis', [DevController::class, 'diagnostics']);

Route::get('/logs/laravel', function(){
    $path = storage_path('logs/laravel.log');
    return response()->file($path);
});
Route::get('/logs/python', function(){
    $path = storage_path('logs/python.log');
    return response()->file($path);
});
