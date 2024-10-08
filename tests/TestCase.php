<?php

namespace Tests;

use Faker\Factory;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\TestCase as BaseTestCase;

abstract class TestCase extends BaseTestCase
{
    use CreatesApplication;

//    use RefreshDatabase;
    public function setUp():void
    {
        parent::setUp();

        $this->faker = Factory::create();
    }

    public function tearDown(): void
    {
        parent::tearDown();
    }

}
