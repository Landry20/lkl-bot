<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\Analysis;
use App\Events\AnalysisCreated;
use Illuminate\Http\Request;

class AnalysisController extends Controller
{
    public function index()
    {
        return Analysis::latest()->paginate(20);
    }

    public function store(Request $request)
    {
        $data = $request->validate([
            'symbol' => 'required',
            'timeframe' => 'required',
            'trend' => 'nullable',
            'smma_50_pos' => 'nullable',
            'fibo_zone' => 'nullable',
            'confluence' => 'boolean',
            'candle_pattern' => 'nullable',
            'status' => 'nullable',
            'status' => 'nullable',
            'details' => 'nullable',
            'image_url' => 'nullable|string'
        ]);

        $analysis = Analysis::create($data);
        broadcast(new AnalysisCreated($analysis));
        return $analysis;
    }

    public function check(Request $request)
    {
        $request->validate([
            'user_id' => 'required|exists:users,id',
            'symbol' => 'required',
            'trend' => 'required',
            'action' => 'required',
            'image_url' => 'nullable|string'
        ]);

        $userId = $request->user_id;
        $symbol = $request->symbol;
        $trend = $request->trend;
        $action = $request->action;

        if ($action === 'none') {
            Analysis::where('user_id', $userId)
                ->where('symbol', $symbol)
                ->where('status', 'pending')
                ->update(['status' => 'invalid']);
            return response()->json(['confirmed' => false, 'count' => 0]);
        }

        // 1. GLOBAL ANTI-SPAM / ANTI-DUPLICATE CHECK
        // If ANY analysis exists for this symbol in the last 4 hours, ignore it.
        $recentAnalysis = Analysis::where('symbol', $symbol)
            ->where('created_at', '>=', now()->subHours(4))
            ->first();

        if ($recentAnalysis) {
             // Already exists recently, do not create new one.
             return response()->json(['confirmed' => false, 'count' => 0, 'reason' => 'duplicate']);
        }

        $analysis = Analysis::where('user_id', $userId)
            ->where('symbol', $symbol)
            ->where('status', 'pending')
            ->where('trend', $trend)
            ->latest()
            ->first();

        if (!$analysis) {
            $analysis = Analysis::create([
                'user_id' => $userId,
                'symbol' => $symbol,
                'timeframe' => $request->timeframe,
                'trend' => $trend,
                'action' => $action,
                'fibo_zone' => $request->fibo_zone,
                'smma_50_pos' => $request->smma_50_pos,
                'status' => 'pending',
                'confirmation_count' => 1,
                'details' => $request->details,
                'image_url' => $request->image_url
            ]);
            return response()->json(['confirmed' => false, 'count' => 1]);
        }

        if ($analysis->updated_at->diffInMinutes(now()) >= 1) {
            $analysis->increment('confirmation_count');
            
            if ($analysis->confirmation_count >= 2) {
                $analysis->update(['status' => 'valid']);
                broadcast(new AnalysisCreated($analysis));
                return response()->json(['confirmed' => true, 'count' => $analysis->confirmation_count]);
            }
        }

        return response()->json(['confirmed' => false, 'count' => $analysis->confirmation_count]);
    }
}
