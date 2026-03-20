<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\Trade;
use App\Events\TradeUpdated;
use Illuminate\Http\Request;

class TradeController extends Controller
{
    public function index(Request $request)
    {
        $query = Trade::query();

        if ($request->has('period')) {
            switch ($request->period) {
                case 'today':
                    $query->whereDate('created_at', now()->today());
                    break;
                case 'week':
                    $query->whereBetween('created_at', [now()->startOfWeek(), now()->endOfWeek()]);
                    break;
                case 'month':
                    $query->whereMonth('created_at', now()->month)
                          ->whereYear('created_at', now()->year);
                    break;
            }
        }

        return $query->latest()->paginate(50);
    }

    public function store(Request $request)
    {
        $data = $request->validate([
            'user_id' => 'required|exists:users,id',
            'symbol' => 'required',
            'type' => 'required',
            'entry_price' => 'required|numeric',
            'sl' => 'required|numeric',
            'tp' => 'required|numeric',
            'lot' => 'required|numeric',
            'reason' => 'nullable|string',
            'status' => 'nullable|string',
            'mt5_order_id' => 'nullable|string'
        ]);

        $trade = Trade::create($data);
        broadcast(new TradeUpdated($trade));
        return $trade;
    }

    public function show(Trade $trade)
    {
        return $trade;
    }

    public function update(Request $request, Trade $trade)
    {
        $data = $request->validate([
            'status' => 'sometimes|string',
            'pnl' => 'sometimes|numeric',
            'sl' => 'sometimes|numeric',
            'tp' => 'sometimes|numeric',
        ]);

        $trade->update($data);
        broadcast(new TradeUpdated($trade));
        return $trade;
    }
}
