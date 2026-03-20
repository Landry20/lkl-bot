import React from 'react';

export default function Markets() {
    return (
        <div className="p-6">
            <h1 className="text-2xl font-bold mb-4">Marchés</h1>
            <div className="mb-8">
                <h2 className="text-xl font-semibold mb-2">Forex Majeurs</h2>
                {/* Forex Charts Placeholder */}
                <div className="h-64 bg-gray-100 dark:bg-gray-700 rounded flex items-center justify-center">
                    Graphiques Forex
                </div>
            </div>

            <div>
                <h2 className="text-xl font-semibold mb-2">Métaux (Or & Argent)</h2>
                {/* Metals Charts Placeholder */}
                <div className="h-64 bg-gray-100 dark:bg-gray-700 rounded flex items-center justify-center">
                    Graphiques Métaux
                </div>
            </div>
        </div>
    );
}
