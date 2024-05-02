<?php

namespace App\Providers;


use App\Repositories\IPlenaryRepository;
use App\Repositories\IResolutionRepository;
use App\Repositories\PlenaryRepository;
use App\Repositories\ResolutionRepository;
use Illuminate\Support\ServiceProvider;

/**
 * Class RepositoryServiceProvider
 *
 *
 * Handles the registration of repositories which are in charge of
 * any complicated operations on the database layer.
 *
 * @package App\Providers
 */
class RepositoryServiceProvider extends ServiceProvider
{
    /**
     * Register services.
     *
     * @return void
     */
    public function register()
    {
        $this->app->bind(IPlenaryRepository::class, PlenaryRepository::class);
        $this->app->bind(IResolutionRepository::class, ResolutionRepository::class);
    }

    /**
     * Bootstrap services.
     *
     * @return void
     */
    public function boot()
    {
        //
    }
}
