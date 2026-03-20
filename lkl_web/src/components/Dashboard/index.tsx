import React from 'react';

export default function Dashboard() {
    return (
        <div className="p-6">
            <h1 className="text-2xl font-bold mb-4">Dashboard</h1>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {/* Status Robot */}
                <div className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow">
                    <h2 className="text-xl font-semibold mb-2">État du Robot</h2>
                    <div className="flex items-center space-x-4">
                        <button className="bg-green-500 text-white px-4 py-2 rounded">Activer</button>
                        <button className="bg-red-500 text-white px-4 py-2 rounded">Désactiver</button>
                    </div>
                </div>

                {/* Market Summary */}
                <div className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow">
                    <h2 className="text-xl font-semibold mb-2">Résumé Marché</h2>
                    <p>Risk: <span className="font-bold">Neutral</span></p>
                </div>
            </div>
        </div>
    );
}
