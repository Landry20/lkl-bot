import React from 'react';

export default function EconomicNews() {
    return (
        <div className="p-6">
            <h1 className="text-2xl font-bold mb-4">Annonces Économiques</h1>
            <div className="overflow-x-auto">
                <table className="min-w-full bg-white dark:bg-gray-800 rounded shadow">
                    <thead>
                        <tr>
                            <th className="p-3 text-left">Heure</th>
                            <th className="p-3 text-left">Devise</th>
                            <th className="p-3 text-left">Événement</th>
                            <th className="p-3 text-left">Impact</th>
                        </tr>
                    </thead>
                    <tbody>
                        {/* Rows placeholder */}
                        <tr>
                            <td className="p-3 text-center text-gray-500" colSpan={4}>Chargement du calendrier...</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    );
}
