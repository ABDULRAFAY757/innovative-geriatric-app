import React from 'react';
import { useAuth } from '../context/AuthContext';
import { LayoutDashboard, Pill, Activity, ShoppingBag, LogOut, User } from 'lucide-react';
import { Link, useLocation } from 'react-router-dom';

const SidebarItem = ({ icon: Icon, label, to, active }) => (
    <Link to={to} className={`flex items-center space-x-3 px-4 py-3 rounded-xl transition-all ${active ? 'bg-blue-600 text-white shadow-lg shadow-blue-500/30' : 'text-slate-500 hover:bg-slate-100'}`}>
        <Icon size={20} />
        <span className="font-medium">{label}</span>
    </Link>
);

const Layout = ({ children }) => {
    const { user, logout } = useAuth();
    const location = useLocation();

    return (
        <div className="flex h-screen bg-slate-50">
            {/* Sidebar */}
            <aside className="w-64 bg-white border-r border-slate-200 p-6 flex flex-col hidden md:flex">
                <div className="flex items-center space-x-3 mb-10">
                    <div className="w-10 h-10 bg-blue-600 rounded-xl flex items-center justify-center text-white font-bold text-xl">IG</div>
                    <h1 className="font-bold text-slate-800 text-lg leading-tight">Innovative<br />Geriatrics</h1>
                </div>

                <nav className="flex-1 space-y-2">
                    <SidebarItem icon={LayoutDashboard} label="Dashboard" to="/" active={location.pathname === '/'} />
                    <SidebarItem icon={Pill} label="Medications" to="/medications" active={location.pathname === '/medications'} />
                    <SidebarItem icon={Activity} label="Vitals & Health" to="/vitals" active={location.pathname === '/vitals'} />
                    <SidebarItem icon={ShoppingBag} label="Marketplace" to="/marketplace" active={location.pathname === '/marketplace'} />
                </nav>

                <div className="pt-6 border-t border-slate-100">
                    <div className="flex items-center space-x-3 mb-4 px-2">
                        <div className="w-10 h-10 bg-slate-100 rounded-full flex items-center justify-center text-slate-500">
                            <User size={20} />
                        </div>
                        <div>
                            <p className="text-sm font-bold text-slate-700">{user?.name}</p>
                            <p className="text-xs text-slate-400 capitalize">{user?.role?.toLowerCase()}</p>
                        </div>
                    </div>
                    <button onClick={logout} className="flex items-center space-x-2 text-red-500 hover:bg-red-50 px-4 py-2 rounded-lg w-full transition-colors">
                        <LogOut size={18} />
                        <span>Sign Out</span>
                    </button>
                </div>
            </aside>

            {/* Main Content */}
            <main className="flex-1 overflow-y-auto p-4 md:p-8">
                {children}
            </main>
        </div>
    );
};

export default Layout;
