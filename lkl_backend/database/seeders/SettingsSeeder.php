<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;

class SettingsSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $settings = [
            [
                'key' => 'bot_running',
                'value' => '1',
                'type' => 'boolean',
                'description' => 'Active ou désactive le robot de trading',
                'created_at' => now(),
                'updated_at' => now(),
            ],
            [
                'key' => 'risk_percent',
                'value' => '1.0',
                'type' => 'decimal',
                'description' => 'Pourcentage de risque par trade',
                'created_at' => now(),
                'updated_at' => now(),
            ],
        ];

        foreach ($settings as $setting) {
            DB::table('settings')->updateOrInsert(
                ['key' => $setting['key']],
                $setting
            );
        }
    }
}
