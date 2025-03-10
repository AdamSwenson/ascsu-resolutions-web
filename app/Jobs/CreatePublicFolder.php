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

class CreatePublicFolder implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels, HandleScriptTrait;

    const SCRIPT_FILE = 'web_copy_first_readings_for_feedback.py';
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

            $this->handleScript(self::SCRIPT_FILE, $this->plenary->id);

            Log::info("Public folder created for plenary {$this->plenary->id}");

        } catch (PythonScriptError $error) {
            Log::error($error->getMessage());
            throw $error;
        } catch (\Exception $exception) {
            Log::error($exception->getMessage());
            throw $exception;
        }

    }
}
