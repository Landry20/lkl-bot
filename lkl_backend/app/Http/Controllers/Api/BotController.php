<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\User;
use Illuminate\Http\Request;

class BotController extends Controller
{
    /**
     * Retourne la liste des utilisateurs ayant configuré MT5.
     */
    public function getMt5Users(Request $request)
    {
        // On pourrait ajouter une vérification de token BOT_SECRET_TOKEN ici pour plus de sécurité
        $users = User::whereNotNull('mt5_login')
                     ->whereNotNull('mt5_password')
                     ->whereNotNull('mt5_server')
                     ->get(['id', 'name', 'mt5_login', 'mt5_password', 'mt5_server', 'mt5_broker']);

        return response()->json([
            'status' => 'success',
            'data' => $users
        ]);
    }

    /**
     * Reçoit les statistiques en temps réel depuis le Bot MT5.
     */
    public function syncStats(Request $request)
    {
        $request->validate([
            'user_id' => 'required|exists:users,id',
            'mt5_name' => 'nullable|string',
            'balance' => 'required|numeric',
            'equity' => 'required|numeric',
            'today_profit' => 'required|numeric',
            'active_deals' => 'required|numeric',
        ]);

        $user = User::find($request->user_id);
        $user->update([
            'mt5_name' => $request->mt5_name ?? $user->mt5_name,
            'mt5_balance' => $request->balance,
            'mt5_equity' => $request->equity,
            'mt5_today_profit' => $request->today_profit,
            'mt5_active_deals' => $request->active_deals,
        ]);

        // Diffusion en temps réel
        broadcast(new \App\Events\StatsUpdated($user->id, [
            'balance' => $request->balance,
            'equity' => $request->equity,
            'today_profit' => $request->today_profit,
            'active_deals' => $request->active_deals,
            'mt5_name' => $request->mt5_name ?? $user->mt5_name,
        ]))->toOthers();

        return response()->json(['status' => 'success']);
    }
}
