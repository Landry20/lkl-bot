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
        Schema::create('fundamental_analyses', function (Blueprint $blueprint) {
            $blueprint->id();
            $blueprint->string('category'); // macro, geo, micro, discours
            $blueprint->string('symbol')->nullable();
            $blueprint->string('bias')->default('neutre');
            $blueprint->integer('confidence')->default(50);
            $blueprint->text('content');
            $blueprint->json('details')->nullable();
            $blueprint->string('impact_level')->default('medium'); // low, medium, high
            $blueprint->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('fundamental_analyses');
    }
};
