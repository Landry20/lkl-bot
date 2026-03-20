<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class SettingSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        \App\Models\Setting::updateOrCreate(['key' => 'bot_running'], [
            'value' => '0',
            'type' => 'boolean',
            'description' => 'Indique si le robot est actuellement en marche.'
        ]);

        \App\Models\Setting::updateOrCreate(['key' => 'work_days'], [
            'value' => json_encode([0, 1, 2, 3, 4]),
            'type' => 'json',
            'description' => 'Jours de la semaine travaillés (0=Lundi, 4=Vendredi).'
        ]);

        \App\Models\Setting::updateOrCreate(['key' => 'base_capital'], [
            'value' => '100',
            'type' => 'decimal',
            'description' => 'Capital de base pour le calcul des lots.'
        ]);
    }
}
