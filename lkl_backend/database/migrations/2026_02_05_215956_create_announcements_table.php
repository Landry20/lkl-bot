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
        Schema::create('announcements', function (Blueprint $table) {
            $table->id();
            $table->foreignId('user_id')->constrained()->onDelete('cascade');
            $table->date('date'); // Date de l'événement
            $table->string('time')->nullable(); // Heure de l'événement (ex: "14:30")
            $table->string('currency', 10); // USD, EUR, GBP, GOLD, GLOBAL
            $table->text('event'); // Description de l'événement
            $table->enum('impact', ['HIGH', 'MEDIUM', 'LOW'])->default('MEDIUM');
            $table->string('source')->nullable(); // Source de l'info (ex: "Reuters")
            $table->text('url')->nullable(); // Lien vers l'article
            $table->timestamps();
            
            // Index pour requêtes rapides
            $table->index(['user_id', 'date']);
            $table->index('impact');
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('announcements');
    }
};
