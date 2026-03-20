import React from 'react';

export default function Analyses() {
    return (
        <div className="p-6">
            <h1 className="text-2xl font-bold mb-4">Analyses</h1>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                    <h2 className="text-xl font-semibold mb-2">Analyse IA</h2>
                    <div className="h-48 bg-gray-100 dark:bg-gray-700 rounded"></div>
                </div>
                <div>
                    <h2 className="text-xl font-semibold mb-2">Analyse Utilisateur</h2>
                    <div className="h-48 bg-gray-100 dark:bg-gray-700 rounded"></div>
                </div>
            </div>
        </div>
    );
}
