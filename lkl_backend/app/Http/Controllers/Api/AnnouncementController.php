<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class AnnouncementController extends Controller
{
    /**
     * Récupère les annonces pour l'utilisateur connecté
     * Filtre par date (prochaines en premier)
     */
    public function index(Request $request)
    {
        // $user = $request->user();
        
        $announcements = DB::table('announcements')
            // ->where('user_id', $user->id)
            ->where('date', '>=', now()->format('Y-m-d')) // Seulement les annonces futures
            ->orderBy('date', 'asc')
            ->orderBy('time', 'asc')
            ->get();
        
        return response()->json([
            'status' => 'success',
            'data' => $announcements
        ]);
    }
    
    /**
     * Crée une nouvelle annonce (appelé par le bot Python)
     */
    public function store(Request $request)
    {
        $validated = $request->validate([
            'user_id' => 'required|exists:users,id',
            'date' => 'required|date',
            'time' => 'nullable|string',
            'currency' => 'required|string|max:10',
            'event' => 'required|string',
            'impact' => 'required|in:HIGH,MEDIUM,LOW',
            'source' => 'nullable|string',
            'url' => 'nullable|url'
        ]);
        
        $announcement = DB::table('announcements')->insertGetId([
            'user_id' => $validated['user_id'],
            'date' => $validated['date'],
            'time' => $validated['time'] ?? null,
            'currency' => $validated['currency'],
            'event' => $validated['event'],
            'impact' => $validated['impact'],
            'source' => $validated['source'] ?? null,
            'url' => $validated['url'] ?? null,
            'created_at' => now(),
            'updated_at' => now()
        ]);
        
        return response()->json([
            'status' => 'success',
            'message' => 'Annonce créée',
            'id' => $announcement
        ], 201);
    }
}
