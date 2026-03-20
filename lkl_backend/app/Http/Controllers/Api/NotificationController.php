<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Str;
use App\Events\NotificationSent;

class NotificationController extends Controller
{


    public function store(Request $request)
    {
        $request->validate([
            'user_id' => 'required|exists:users,id',
            'type' => 'required|string',
            'message' => 'required|string',
        ]);

        $id = Str::uuid()->toString();
        
        // Manual insertion for performance and flexibility
        $notifData = [
            'id' => $id,
            'user_id' => $request->user_id,
            'type' => $request->type,
            'message' => $request->message,
            'url' => $request->url, // Nouveau champ URL
            'created_at' => now()->toIso8601String()
        ];

        // Manual insertion
        DB::table('notifications')->insert([
            'id' => $id,
            'type' => 'manual',
            'notifiable_type' => 'App\Models\User',
            'notifiable_id' => $request->user_id,
            'data' => json_encode($notifData),
            'created_at' => now(),
            'updated_at' => now(),
        ]);

        // Broadcast live
        event(new NotificationSent($notifData));

        return response()->json(['id' => $id, 'status' => 'success'], 201);
    }

    public function index(Request $request)
    {
        // Return ALL notifications for debugging/visibility
        $notifications = \Illuminate\Support\Facades\DB::table('notifications')
            ->orderBy('created_at', 'desc')
            ->take(50)
            ->get();

        // Decode data manually since we are using query builder
        return $notifications->map(function ($n) {
            $n->data = json_decode($n->data);
            return $n;
        });
    }

    public function markAsRead(Request $request, $id)
    {
        $notification = $request->user()->notifications()->findOrFail($id);
        $notification->markAsRead(); // Standard method

        return response()->json(['status' => 'success']);
    }

    public function markAllAsRead(Request $request)
    {
        $request->user()->unreadNotifications->markAsRead();
        return response()->json(['status' => 'success']);
    }

    public function unreadCount(Request $request)
    {
        return response()->json([
            'count' => $request->user()->unreadNotifications()->count()
        ]);
    }
}
