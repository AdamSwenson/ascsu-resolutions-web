<?php

namespace App\Jobs;

use App\Exceptions\PythonScriptError;
use App\Models\Plenary;
use App\Traits\HandleScriptTrait;
use Illuminate\Bus\Queueable;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Foundation\Bus\Dispatchable;
use Illuminate\Queue\InteractsWithQueue;
use Illuminate\Queue\SerializesModels;
use Illuminate\Support\Facades\Log;

class UpdateAgenda implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels, HandleScriptTrait;

    public Plenary $plenary;

    /**
     * Create a new job instance.
     */
    public function __construct(Plenary $plenary)
    {
        $this->plenary = $plenary;
    }

    /**
     * Execute the job.
     */
    public function handle(): void
    {
        try {
            $scriptfile = 'web_make_agenda.py';

            $this->handleScript($scriptfile, $this->plenary->id);

            Log::info("Agenda updated for plenary {$this->plenary->id}");
            //$result->output();

            SyncReadingTypes::dispatch($this->plenary);

//            SyncReadingTypes::dispatchAfterResponse($this->plenary);

        } catch (PythonScriptError $error) {
            Log::error($error->getMessage());
        }catch (\Exception $exception){
            Log::error($exception->getMessage());
        }

    }
}
