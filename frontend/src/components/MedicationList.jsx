import React from 'react';
import { Check, Clock, AlertCircle } from 'lucide-react';

const MedicationList = ({ role }) => {
    // Mock Data
    const meds = [
        { id: 1, name: 'Aspirin', dose: '100mg', time: '08:00 AM', status: 'taken' },
        { id: 2, name: 'Metformin', dose: '500mg', time: '01:00 PM', status: 'pending' },
        { id: 3, name: 'Lisinopril', dose: '10mg', time: '08:00 PM', status: 'pending' },
    ];

    return (
        <div className="glass-card p-6">
            <h3 className="text-lg font-bold text-slate-800 mb-4 flex items-center justify-between">
                Today's Medications
                {role === 'FAMILY' && <span className="text-xs bg-blue-100 text-blue-600 px-2 py-1 rounded-full">Viewing as Family</span>}
            </h3>
            <div className="space-y-3">
                {meds.map((med) => (
                    <div key={med.id} className="flex items-center justify-between p-3 bg-slate-50 rounded-xl border border-slate-100 group hover:border-blue-200 transition-all">
                        <div className="flex items-center space-x-3">
                            <div className={`w-10 h-10 rounded-full flex items-center justify-center ${med.status === 'taken' ? 'bg-green-100 text-green-600' : 'bg-amber-100 text-amber-600'}`}>
                                {med.status === 'taken' ? <Check size={20} /> : <Clock size={20} />}
                            </div>
                            <div>
                                <p className="font-bold text-slate-800">{med.name}</p>
                                <p className="text-xs text-slate-500">{med.dose} • {med.time}</p>
                            </div>
                        </div>
                        {role === 'PATIENT' && med.status !== 'taken' && (
                            <button className="text-sm bg-blue-600 text-white px-3 py-1.5 rounded-lg active:scale-95 transition-all">
                                Take
                            </button>
                        )}
                        {role === 'FAMILY' && med.status !== 'taken' && (
                            <span className="text-xs text-amber-500 font-medium flex items-center bg-amber-50 px-2 py-1 rounded">
                                <AlertCircle size={12} className="mr-1" /> Not Taken
                            </span>
                        )}
                    </div>
                ))}
            </div>
        </div>
    );
};

export default MedicationList;
