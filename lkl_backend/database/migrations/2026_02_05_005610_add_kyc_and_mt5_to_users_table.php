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
            $table->string('phone')->nullable();
            $table->string('id_type')->nullable(); // passeport, carte d'identité, etc.
            $table->string('id_country')->nullable();
            $table->string('id_number')->nullable();
            $table->date('dob')->nullable();
            
            // Paramètres MT5
            $table->string('mt5_login')->nullable();
            $table->string('mt5_password')->nullable();
            $table->string('mt5_server')->nullable();
            $table->string('mt5_broker')->nullable();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::table('users', function (Blueprint $table) {
            //
        });
    }
};
