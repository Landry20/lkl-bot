<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Trade extends Model
{
    protected $fillable = [
        'user_id',
        'symbol',
        'type',
        'entry_price',
        'sl',
        'tp',
        'lot',
        'reason',
        'status',
        'pnl',
        'mt5_order_id'
    ];
}
