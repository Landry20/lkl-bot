<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\Setting;
use App\Events\StatsUpdated;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Http;

class SettingController extends Controller
{
    public function index()
    {
        return Setting::all()->pluck('value', 'key');
    }

    public function update(Request $request)
    {
        $data = $request->all();
        foreach ($data as $key => $value) {
            $setting = Setting::where('key', $key)->first();
            if ($setting) {
                if ($setting->type === 'json' && !is_string($value)) {
                    $value = json_encode($value);
                }
                $setting->update(['value' => $value]);
            }
        }

        // Emit WebSocket event for real-time sync
        if (Auth::check() && isset($data['bot_running'])) {
            event(new StatsUpdated(Auth::id(), [
                'bot_running' => $data['bot_running'],
                'updated_at' => now()->toIso8601String()
            ]));

            // Synchroniser avec le backend Python
            try {
                $pythonEndpoint = $data['bot_running'] === '1' 
                    ? 'http://localhost:8001/api/robot/activate'
                    : 'http://localhost:8001/api/robot/deactivate';
                
                Http::timeout(3)->post($pythonEndpoint, [
                    'user_id' => Auth::id(),
                    'timestamp' => now()->toIso8601String()
                ]);
            } catch (\Exception $e) {
                // Log l'erreur mais ne bloque pas la requête
                \Log::warning('Erreur synchronisation Python: ' . $e->getMessage());
            }
        }

        return response()->json(['status' => 'success']);
    }

    public function getSettings()
    {
        return Setting::all();
    }
}
