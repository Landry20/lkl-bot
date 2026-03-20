<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class FundamentalAnalysis extends Model
{
    use HasFactory;

    protected $fillable = [
        'category',
        'symbol',
        'bias',
        'confidence',
        'content',
        'details',
        'impact_level'
    ];

    protected $casts = [
        'details' => 'array',
        'confidence' => 'integer'
    ];
}
