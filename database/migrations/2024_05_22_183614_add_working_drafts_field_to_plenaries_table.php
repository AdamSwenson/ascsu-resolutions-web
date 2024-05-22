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
        Schema::table('plenaries', function (Blueprint $table) {
            $table->text('working_drafts_folder_id')->nullable();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::table('plenaries', function (Blueprint $table) {
            $table->dropColumn('working_drafts_folder_id');
        });
    }
};
