<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\Chat;
use App\Events\MessageSent;
use Illuminate\Http\Request;

class ChatController extends Controller
{
    public function index(Request $request)
    {
        $chats = Chat::where('user_id', $request->user()->id)
            ->latest()
            ->paginate(50);
            
        return response()->json([
            'status' => 'success',
            'data' => $chats
        ]);
    }

    public function store(Request $request)
    {
        $validated = $request->validate([
            'message' => 'required|string',
            'type' => 'nullable|string'
        ]);

        $chat = Chat::create([
            'user_id' => $request->user()->id,
            'message' => $validated['message'],
            'sender' => 'user',
            'type' => $validated['type'] ?? 'text'
        ]);

        broadcast(new MessageSent($chat))->toOthers();

        return response()->json([
            'status' => 'success',
            'data' => $chat
        ]);
    }

    /**
     * Utilisé par le bot Python pour répondre
     */
    public function botResponse(Request $request)
    {
        $validated = $request->validate([
            'user_id' => 'required|exists:users,id',
            'message' => 'required|string',
            'type' => 'nullable|string'
        ]);

        $chat = Chat::create([
            'user_id' => $validated['user_id'],
            'message' => $validated['message'],
            'sender' => 'bot',
            'type' => $validated['type'] ?? 'text'
        ]);

        broadcast(new MessageSent($chat));

        return response()->json([
            'status' => 'success',
            'data' => $chat
        ]);
    }
}
