<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;

class BrokerController extends Controller
{
    // Liste simulée de brokers populaires
    private $popularBrokers = [
        ['name' => 'Deriv', 'logo' => '/brokers/deriv.png', 'servers' => ['Deriv-Demo', 'Deriv-Server', 'Deriv-Server-02']],
        ['name' => 'FTMO', 'logo' => '/brokers/ftmo.png', 'servers' => ['FTMO-Demo', 'FTMO-Server', 'FTMO-Server-2']],
        ['name' => 'MetaQuotes', 'logo' => '/brokers/metaquotes.png', 'servers' => ['MetaQuotes-Demo']],
        ['name' => 'IC Markets', 'logo' => '/brokers/icmarkets.png', 'servers' => ['ICMarkets-Demo', 'ICMarkets-Live01', 'ICMarkets-SC-Live12']],
        ['name' => 'Pepperstone', 'logo' => '/brokers/pepperstone.png', 'servers' => ['Pepperstone-Demo', 'Pepperstone-Live01']],
        ['name' => 'FBS', 'logo' => '/brokers/fbs.png', 'servers' => ['FBS-Real', 'FBS-Demo']],
        ['name' => 'Exness', 'logo' => '/brokers/exness.png', 'servers' => ['Exness-Real1', 'Exness-Trial']],
        ['name' => 'XTB', 'logo' => '/brokers/xtb.png', 'servers' => ['XTrade-Real', 'XTrade-Demo']],
        ['name' => 'Admiral Markets', 'logo' => '/brokers/admiral.png', 'servers' => ['AdmiralMarkets-Live1', 'AdmiralMarkets-Demo']],
        ['name' => 'JustMarkets', 'logo' => '/brokers/justmarkets.png', 'servers' => ['JustMarkets-Live', 'JustMarkets-Demo']],
        ['name' => 'Tickmill', 'logo' => '/brokers/tickmill.png', 'servers' => ['Tickmill-Live', 'Tickmill-Demo']],
    ];

    public function search(Request $request)
    {
        $query = strtolower($request->query('q', ''));
        if (empty($query)) {
            return response()->json($this->popularBrokers);
        }

        $filtered = array_filter($this->popularBrokers, function ($broker) use ($query) {
            return str_contains(strtolower($broker['name']), $query);
        });

        return response()->json(array_values($filtered));
    }
}
