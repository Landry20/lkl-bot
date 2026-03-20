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
        Schema::create('analyses', function (Blueprint $table) {
            $table->id();
            $table->string('symbol');
            $table->string('timeframe');
            $table->string('trend')->nullable();
            $table->string('smma_50_pos')->nullable();
            $table->string('fibo_zone')->nullable();
            $table->boolean('confluence')->default(false);
            $table->string('candle_pattern')->nullable();
            $table->integer('confirmation_count')->default(0);
            $table->string('status')->default('pending');
            $table->text('details')->nullable();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('analyses');
    }
};
