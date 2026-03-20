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
        Schema::table('users', function (Blueprint $table) {
            $table->decimal('mt5_balance', 15, 2)->default(0);
            $table->decimal('mt5_equity', 15, 2)->default(0);
            $table->decimal('mt5_today_profit', 15, 2)->default(0); // Profit journalier réel
            $table->integer('mt5_active_deals')->default(0); // Nombre de positions ouvertes
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::table('users', function (Blueprint $table) {
            $table->dropColumn(['mt5_balance', 'mt5_equity', 'mt5_today_profit', 'mt5_active_deals']);
        });
    }
};
