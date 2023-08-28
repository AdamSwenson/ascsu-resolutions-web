<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration {
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('plenaries', function (Blueprint $table) {
            $table->id();

            $table->text('second_reading_folder_id')->nullable();
            $table->text('feedback_folder_id')->nullable();
            $table->text('plenary_folder_id')->nullable();
            $table->text('first_reading_folder_id')->nullable();
            $table->date('thursday_date');

            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('plenaries');
    }
};
