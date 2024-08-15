<?php

use App\Http\Controllers\CommitteeController;
use App\Http\Controllers\DevController;
use App\Http\Controllers\PermissionsController;
use App\Http\Controllers\PlenaryController;
use App\Http\Controllers\ResolutionController;
use App\Http\Controllers\SecretaryController;
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

Route::get('/logs/laravel', function(){
    $path = storage_path('logs/laravel.log');
   return response()->file($path);
});
Route::get('/logs/python', function(){
    $path = storage_path('logs/python.log');
    return response()->file($path);
});


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
Route::post('/resolution/action/{plenary}/{resolution}', [ResolutionController::class, 'setAction']);
Route::post('/resolution/{plenary}', [CommitteeController::class, 'recordResolution']);
Route::post('/resolution/waiver/toggle/{resolution}', [ResolutionController::class, 'toggleWaiver']);


// ============================= secretary
Route::get('/secretary', [SecretaryController::class, 'getSecretaryPage']);
Route::post('/secretary/folders', [PlenaryController::class, 'createPlenary']);
Route::post('secretary/public/{plenary}', [SecretaryController::class, 'createPublic']);

Route::post('plenary/current/{plenary}', [PlenaryController::class, 'setCurrent']);

Route::post('/secretary/agenda/{plenary}', [SecretaryController::class, 'createAgenda']);
Route::post('/secretary/styling/{plenary}', [SecretaryController::class, 'enforceStyling']);
Route::post('/secretary/sync/{plenary}', [SecretaryController::class, 'syncTitles']);

Route::resource('plenaries', PlenaryController::class);

//Resolutions
Route::post('/resolution/reading/{plenary}/{resolution}', [ResolutionController::class, 'setReadingType']);
Route::resource('resolutions', ResolutionController::class);


//Permissions
Route::post('secretary/permissions/all/lock/{plenary}', [PermissionsController::class, 'lockEditingAll']);
Route::post('secretary/permissions/all/unlock/{plenary}', [PermissionsController::class, 'unlockEditingAll']);
Route::post('secretary/permissions/one/lock/{resolution}', [PermissionsController::class, 'lockEditingOne']);
Route::post('secretary/permissions/one/unlock/{resolution}', [PermissionsController::class, 'unlockEditingOne']);
Route::get('secretary/permissions/one/{resolution}', [PermissionsController::class, 'getPermissions']);

Route::post('resolution/approval/{resolution}', [ResolutionController::class, 'setApprovalStatus']);
Route::get('plenary/resolutions/{plenary}', [ResolutionController::class, 'forPlenary']);
//Route::get('resolution/approval/{resolution}', [ResolutionController::class, 'getApproval']);

Route::get('diagnosis', [DevController::class, 'diagnostics']);
