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
        Schema::table('resolutions', function (Blueprint $table) {

            //acceptable statuses: null, approved, failed
            $table->string('status')->nullable();
            //AR-58 Replace is approved with less ambiguous column
//            $table->dropColumn('is_approved');
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::table('resolutions', function (Blueprint $table) {
            $table->dropColumn('status');
        });
    }
};
