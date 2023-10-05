<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('plenary_resolution', function (Blueprint $table) {
            $table->id();
            $table->timestamps();

            $table->integer('plenary_id');
            $table->integer('resolution_id');
            $table->boolean('is_first_reading')->nullable();


        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('plenary_resolution');
    }
};
