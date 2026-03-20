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
        Schema::create('trades', function (Blueprint $table) {
            $table->id();
            $table->string('symbol');
            $table->string('type');
            $table->decimal('entry_price', 15, 5);
            $table->decimal('sl', 15, 5);
            $table->decimal('tp', 15, 5);
            $table->decimal('lot', 10, 2);
            $table->text('reason')->nullable();
            $table->string('status')->default('open');
            $table->decimal('pnl', 15, 2)->nullable();
            $table->string('mt5_order_id')->nullable();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('trades');
    }
};
