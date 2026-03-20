<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\FundamentalAnalysis;
use Illuminate\Http\Request;

class FundamentalAnalysisController extends Controller
{
    public function index(Request $request)
    {
        $query = FundamentalAnalysis::query();

        if ($request->has('category')) {
            $query->where('category', $request->category);
        }

        if ($request->has('symbol')) {
            $query->where('symbol', $request->symbol);
        }

        return response()->json([
            'status' => 'success',
            'data' => $query->latest()->paginate(20)
        ]);
    }

    public function store(Request $request)
    {
        $validated = $request->validate([
            'category' => 'required|string',
            'symbol' => 'nullable|string',
            'bias' => 'required|string',
            'confidence' => 'required|integer',
            'content' => 'required|string',
            'details' => 'nullable|array',
            'impact_level' => 'nullable|string|in:high,medium,low'
        ]);
        $validated['impact_level'] = $validated['impact_level'] ?? 'medium';

        $analysis = FundamentalAnalysis::create($validated);

        // TODO: Broadcast event for real-time UI update

        return response()->json([
            'status' => 'success',
            'data' => $analysis
        ]);
    }

    public function latest()
    {
        $categories = ['macro', 'geo', 'micro', 'discours'];
        $latest = [];

        foreach ($categories as $cat) {
            $latest[$cat] = FundamentalAnalysis::where('category', $cat)->latest()->first();
        }

        return response()->json([
            'status' => 'success',
            'data' => $latest
        ]);
    }
}
