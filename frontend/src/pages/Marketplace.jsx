import React from 'react';

const Marketplace = () => {
    const items = [
        { id: 1, name: 'Wheelchair', desc: 'Lightweight manual wheelchair', status: 'Available' },
        { id: 2, name: 'Blood Pressure Monitor', desc: 'Digital arm monitor', status: 'Requested' },
        { id: 3, name: 'Walking Cane', desc: 'Adjustable height', status: 'Available' },
    ];

    return (
        <div className="max-w-4xl mx-auto">
            <h2 className="text-3xl font-bold text-slate-800 mb-6">Equipment Marketplace</h2>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {items.map((item) => (
                    <div key={item.id} className="glass-card p-5 flex flex-col h-full">
                        <div className="h-40 bg-slate-100 rounded-xl mb-4 flex items-center justify-center text-slate-400">
                            Image Placeholder
                        </div>
                        <h3 className="font-bold text-lg text-slate-800">{item.name}</h3>
                        <p className="text-slate-500 text-sm flex-1 mb-4">{item.desc}</p>
                        <div className="flex items-center justify-between mt-auto">
                            <span className={`text-xs px-2 py-1 rounded-full font-bold ${item.status === 'Available' ? 'bg-green-100 text-green-600' : 'bg-amber-100 text-amber-600'}`}>
                                {item.status}
                            </span>
                            <button disabled={item.status !== 'Available'} className="text-sm bg-blue-600 text-white px-3 py-1.5 rounded-lg disabled:opacity-50">
                                Request
                            </button>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Marketplace;
