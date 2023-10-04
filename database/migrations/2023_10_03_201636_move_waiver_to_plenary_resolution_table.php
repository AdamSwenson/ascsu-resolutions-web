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
        Schema::table('plenary_resolution', function (Blueprint $table) {
            $table->boolean('is_waiver')->nullable();
        });

        Schema::table('resolutions', function (Blueprint $table) {
            $table->dropColumn('waiver');
        });

    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::table('plenary_resolutions_pivot', function (Blueprint $table) {
            $table->dropColumn('is_waiver');
        });

        Schema::table('resolutions', function (Blueprint $table) {
            $table->boolean('waiver')->nullable();
        });
    }
};
