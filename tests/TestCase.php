<?php

namespace Tests;

use Faker\Factory;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\TestCase as BaseTestCase;




abstract class TestCase extends BaseTestCase
{
    use CreatesApplication;

//    use RefreshDatabase;

    const TEST_PLENARY_PROPS = [
        'id'=> 134,
        'second_reading_folder_id' => '1QHQARCgdomVTJwtk3Ve0ejPF0U4aJyyO',
        'feedback_folder_id' =>'1SoqL5NMtAk6ElGviiGeFZsg7SgihbNI5',
        'plenary_folder_id' => '1T2ax3veqABEx7GQhDbZ7RTVCvKqQ1GcK',
        'first_reading_folder_id' => '1n3d7sCh9wJYa76F5BRquYXVtda_jD6yI',
        'agenda_id' => '1OSUJfodzqPOo9udNcTsR1fSb4jXNulJcYC2Y2aXrr8s',
        'working_drafts_folder_id' => '1r7pBSO3CkdUl7p7TtoWhq5xoFynDSGFf'
    ];

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
