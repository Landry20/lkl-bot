<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\Api\NotificationController;
use App\Http\Controllers\Api\BotController;
use App\Http\Controllers\Api\AnnouncementController;
use App\Http\Controllers\Api\AuthController;
use App\Http\Controllers\Api\BrokerController;
use App\Http\Controllers\Api\AnalysisController;
use App\Http\Controllers\Api\TradeController;
use App\Http\Controllers\Api\SettingController;
use App\Http\Controllers\Api\ChatController;
use App\Http\Controllers\Api\FundamentalAnalysisController;

use Illuminate\Support\Facades\Broadcast;

Route::get('brokers/search', [BrokerController::class, 'search']);
Route::get('bot/users', [BotController::class, 'getMt5Users']);
Route::post('bot/sync', [BotController::class, 'syncStats']);
Route::post('announcements', [AnnouncementController::class, 'store']);
Route::post('register', [AuthController::class, 'register']);
Route::post('login', [AuthController::class, 'login']);

// Broadcasting authentication for private channels
Broadcast::routes(['middleware' => ['auth:sanctum']]);

Route::middleware('auth:sanctum')->group(function () {
    Route::post('user/mt5', [AuthController::class, 'updateMt5']);
    Route::post('user/trading-settings', [AuthController::class, 'updateTradingSettings']);
    Route::get('user', function (Request $request) {
        return $request->user();
    });
    Route::get('mt5-accounts', [AuthController::class, 'getMt5Accounts']);

    // Notifications
    Route::get('notifications', [NotificationController::class, 'index']);
    Route::get('notifications/unread-count', [NotificationController::class, 'unreadCount']);
    Route::post('notifications/read-all', [NotificationController::class, 'markAllAsRead']);
    Route::post('notifications/{id}/read', [NotificationController::class, 'markAsRead']);
    
    // Announcements
    Route::get('announcements', [AnnouncementController::class, 'index']);

    // Chats
    Route::get('chats', [ChatController::class, 'index']);
    Route::post('chats', [ChatController::class, 'store']);

    // Fundamental Analyses (Specialized menus)
    Route::get('fundamental-analyses', [FundamentalAnalysisController::class, 'index']);
    Route::get('fundamental-analyses/latest', [FundamentalAnalysisController::class, 'latest']);
});

Route::post('bot/response', [ChatController::class, 'botResponse']);
Route::post('bot/fundamental', [FundamentalAnalysisController::class, 'store']);

Route::post('notifications', [NotificationController::class, 'store']);

Route::apiResource('analyses', AnalysisController::class);
Route::apiResource('trades', TradeController::class);
Route::post('analyses/check', [AnalysisController::class, 'check']);

Route::get('settings', [SettingController::class, 'index']);
Route::get('settings/raw', [SettingController::class, 'getSettings']);
Route::post('settings', [SettingController::class, 'update']);





