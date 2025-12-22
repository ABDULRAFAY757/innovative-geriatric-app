import React from 'react';
import { useAuth } from '../context/AuthContext';
import MedicationList from '../components/MedicationList';
import { Heart, Activity, Brain, AlertTriangle } from 'lucide-react';

const StatCard = ({ icon: Icon, label, value, color, trend }) => (
    <div className="glass-card p-5 flex items-start justify-between">
        <div>
            <p className="text-slate-400 text-sm font-medium mb-1">{label}</p>
            <h4 className="text-2xl font-bold text-slate-800">{value}</h4>
            {trend && <p className="text-xs text-slate-400 mt-1">{trend}</p>}
        </div>
        <div className={`p-3 rounded-xl ${color}`}>
            <Icon size={24} className="text-white" />
        </div>
    </div>
);

const Dashboard = () => {
    const { user } = useAuth();

    return (
        <div className="max-w-6xl mx-auto space-y-6">
            <header className="mb-8">
                <h2 className="text-3xl font-bold text-slate-800">
                    Good Morning, {user.name.split(' ')[0]}
                </h2>
                <p className="text-slate-500">Here is your daily health summary</p>
            </header>

            {/* Stats Row */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                <StatCard icon={Heart} label="Heart Rate" value="72 bpm" color="bg-rose-500 shadow-rose-500/30" trend="Normal" />
                <StatCard icon={Activity} label="Blood Pressure" value="120/80" color="bg-cyan-500 shadow-cyan-500/30" trend="+2% from yesterday" />
                <StatCard icon={Brain} label="Cognitive Score" value="85/100" color="bg-indigo-500 shadow-indigo-500/30" trend="Stable" />
                <StadCard icon={AlertTriangle} label="Risk Level" value="Low" color="bg-green-500 shadow-green-500/30" trend="No recent falls" />
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                {/* Left Column */}
                <div className="lg:col-span-2 space-y-6">
                    <MedicationList role={user.role} />

                    {/* Recent Activity / Alert Section (Family View primarily) */}
                    <div className="glass-card p-6">
                        <h3 className="text-lg font-bold text-slate-800 mb-4">Recent Activity</h3>
                        <ul className="space-y-4 border-l-2 border-slate-100 ml-2 pl-4">
                            <li className="relative">
                                <div className="absolute -left-[21px] top-1 w-3 h-3 rounded-full bg-green-500 border-2 border-white"></div>
                                <p className="text-sm font-bold text-slate-700">Vitals Recorded</p>
                                <p className="text-xs text-slate-400">10:00 AM • Automated Check</p>
                            </li>
                            <li className="relative">
                                <div className="absolute -left-[21px] top-1 w-3 h-3 rounded-full bg-blue-500 border-2 border-white"></div>
                                <p className="text-sm font-bold text-slate-700">Aspirin Taken</p>
                                <p className="text-xs text-slate-400">08:05 AM • Patient Logged</p>
                            </li>
                        </ul>
                    </div>
                </div>

                {/* Right Column */}
                <div className="space-y-6">
                    <div className="glass-card p-6 bg-gradient-to-br from-blue-600 to-blue-700 text-white">
                        <h3 className="font-bold text-lg mb-2">Need Equipment?</h3>
                        <p className="text-blue-100 text-sm mb-4">Request wheelchairs, monitors, and more from our marketplace.</p>
                        <button className="w-full bg-white text-blue-600 font-bold py-2 rounded-lg hover:bg-blue-50 transition-colors">
                            Visit Marketplace
                        </button>
                    </div>

                    <div className="glass-card p-6 border-red-100">
                        <h3 className="font-bold text-lg text-red-600 mb-2 flex items-center">
                            <AlertTriangle size={20} className="mr-2" />
                            Fall Detection
                        </h3>
                        <p className="text-slate-500 text-sm mb-4">Simulate a fall alert for testing purposes.</p>
                        <button className="w-full bg-red-50 text-red-600 border border-red-200 font-bold py-2 rounded-lg hover:bg-red-100 transition-colors">
                            Simulate Alert
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
};

// Fix typo in StatCard usage
const StadCard = StatCard;

export default Dashboard;
