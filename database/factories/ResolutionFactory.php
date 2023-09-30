<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\Resolution>
 */
class ResolutionFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition(): array
    {
        return [
            'document_id' => fake()->sha1,
            'title' => fake()->sentence,
            'number' => fake()->numberBetween(3000, 10000),
            'waiver' => false,
            'is_approved' => false
        ];
    }
}
