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
        Schema::create('committee_resolution', function (Blueprint $table) {
            $table->id();
            $table->integer('committee_id');
            $table->integer('resolution_id');
            $table->boolean('is_sponsor')->nullable();
            $table->boolean('is_cosponsor')->nullable();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('committee_resolution');
    }
};
