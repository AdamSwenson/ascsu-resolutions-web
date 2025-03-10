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

class EnforceStyling implements ShouldQueue
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
                $scriptfile = 'web_enforce_styling.py';

                $this->handleScript($scriptfile, $this->plenary->id);

                Log::info("Styling enforced for plenary {$this->plenary->id}");

            } catch (PythonScriptError $error) {
                Log::error($error->getMessage());
                throw $error;
            } catch (\Exception $exception) {
                Log::error($exception->getMessage());
                throw $exception;
            }
        }

}
