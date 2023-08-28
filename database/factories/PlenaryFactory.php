<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\Plenary>
 */
class PlenaryFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition(): array
    {
        return [
            'second_reading_folder_id' => fake()->sha1,
       'feedback_folder_id'=> fake()->sha1,
        'plenary_folder_id'=> fake()->sha1,
        'first_reading_folder_id' => fake()->sha1,
        'thursday_date' => fake()->date

        //
        ];
    }
}
