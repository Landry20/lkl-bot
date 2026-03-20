<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Analysis extends Model
{
    protected $fillable = [
        'user_id',
        'symbol',
        'timeframe',
        'action', // Added
        'trend',
        'smma_50_pos',
        'fibo_zone',
        'confluence',
        'candle_pattern',
        'confirmation_count',
        'status',
        'details'
    ];
}
