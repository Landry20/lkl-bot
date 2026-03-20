<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\User;
use App\Models\Mt5Account;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Facades\Validator;

class AuthController extends Controller
{
    public function register(Request $request)
    {
        if ($request->hasHeader('Accept-Language')) {
            app()->setLocale($request->header('Accept-Language'));
        }

        $validator = Validator::make($request->all(), [
            'name' => 'required|string|max:255',
            'email' => 'required|string|max:255|unique:users',
            'password' => 'required|string|min:8|confirmed',
            'phone' => 'nullable|string',
            'id_type' => 'nullable|string',
            'id_country' => 'nullable|string',
            'id_number' => 'nullable|string',
            'dob' => 'nullable|date',
        ]);

        if ($validator->fails()) {
            return response()->json($validator->errors(), 422);
        }

        $user = User::create([
            'name' => $request->name,
            'email' => $request->email,
            'password' => Hash::make($request->password),
            'phone' => $request->phone,
            'id_type' => $request->id_type,
            'id_country' => $request->id_country,
            'id_number' => $request->id_number,
            'dob' => $request->dob,
        ]);

        $token = $user->createToken('auth_token')->plainTextToken;

        return response()->json([
            'access_token' => $token,
            'token_type' => 'Bearer',
            'user' => $user,
        ]);
    }

    public function login(Request $request)
    {
        if ($request->hasHeader('Accept-Language')) {
            app()->setLocale($request->header('Accept-Language'));
        }

        $user = User::where('email', $request->email)->first();

        if (!$user || !Hash::check($request->password, $user->password)) {
            return response()->json([
                'message' => __('auth.failed')
            ], 401);
        }

        $token = $user->createToken('auth_token')->plainTextToken;

        return response()->json([
            'access_token' => $token,
            'token_type' => 'Bearer',
            'user' => $user,
        ]);
    }

    public function updateMt5(Request $request)
    {
        $user = $request->user();
        $fields = $request->only([
            'mt5_login',
            'mt5_password',
            'mt5_server',
            'mt5_broker',
            'mt5_name'
        ]);
        
        $user->update($fields);

        // Sauvegarder ou mettre à jour dans l'historique
        Mt5Account::updateOrCreate(
            ['user_id' => $user->id, 'login' => $fields['mt5_login']],
            [
                'password' => $fields['mt5_password'],
                'server' => $fields['mt5_server'],
                'broker' => $fields['mt5_broker'] ?? null,
                'name' => $fields['mt5_name'] ?? null,
            ]
        );

        return response()->json(['message' => 'MT5 settings updated', 'user' => $user]);
    }

    public function updateTradingSettings(Request $request)
    {
        $user = $request->user();
        $validated = $request->validate([
            'trading_authorized' => 'sometimes|boolean',
            'bot_language' => 'sometimes|string|in:fr,en'
        ]);

        $user->update($validated);

        return response()->json([
            'status' => 'success',
            'message' => 'Trading settings updated',
            'user' => $user
        ]);
    }

    public function getMt5Accounts(Request $request)
    {
        return $request->user()->mt5Accounts()->latest()->get();
    }
}
