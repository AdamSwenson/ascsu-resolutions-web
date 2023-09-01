<?php

use App\Http\Controllers\CommitteeController;
use App\Http\Controllers\DevController;
use App\Http\Controllers\PlenaryController;
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

Route::get('/', function () {
    return view('welcome');
});


Route::get('/committee', [CommitteeController::class, 'getCommitteePage']);
Route::post('/committee', [CommitteeController::class, 'recordResolution']);

Route::get('/secretary', [SecretaryController::class, 'getSecretaryPage']);
Route::post('/secretary/folders', [SecretaryController::class, 'createPlenary']);
Route::post('secretary/public/{plenary}', [SecretaryController::class, 'createPublic']);
Route::post('secretary/permissions', [SecretaryController::class, 'togglePermissions']);

Route::post('plenary/current/{plenary}', [PlenaryController::class, 'setCurrent']);
Route::resource('plenaries', PlenaryController::class);

Route::get('diagnosis', [DevController::class, 'diagnostics']);
