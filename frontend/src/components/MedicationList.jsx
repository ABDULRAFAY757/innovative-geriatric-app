import { medicationService } from '../services/api';
import { useAuth } from '../context/AuthContext';

const MedicationList = ({ role }) => {
    const { user } = useAuth();
    const [meds, setMeds] = React.useState([]);
    const [loading, setLoading] = React.useState(true);

    const fetchMeds = async () => {
        if (!user?.patientId) return;
        try {
            const response = await medicationService.getMedications(user.patientId);
            setMeds(response.data);
        } catch (error) {
            console.error("Failed to fetch medications", error);
        } finally {
            setLoading(false);
        }
    };

    React.useEffect(() => {
        fetchMeds();
    }, []);

    const handleTake = async (medId) => {
        try {
            await medicationService.logMedication({
                medication_id: medId,
                status: 'TAKEN'
            });
            fetchMeds(); // Refresh list
        } catch (error) {
            console.error("Failed to log medication", error);
        }
    };

    if (loading) return <div className="glass-card p-6 animate-pulse">Loading medications...</div>;

    return (
        <div className="glass-card p-6">
            <h3 className="text-lg font-bold text-slate-800 mb-4 flex items-center justify-between">
                Today's Medications
                {role === 'FAMILY' && <span className="text-xs bg-blue-100 text-blue-600 px-2 py-1 rounded-full">Viewing as Family</span>}
            </h3>
            <div className="space-y-3">
                {meds.length === 0 && <p className="text-slate-500 text-center py-4">No medications scheduled.</p>}
                {meds.map((med) => (
                    <div key={med.id} className="flex items-center justify-between p-3 bg-slate-50 rounded-xl border border-slate-100 group hover:border-blue-200 transition-all">
                        <div className="flex items-center space-x-3">
                            <div className={`w-10 h-10 rounded-full flex items-center justify-center ${med.status === 'taken' ? 'bg-green-100 text-green-600' : 'bg-amber-100 text-amber-600'}`}>
                                {med.status === 'taken' ? <Check size={20} /> : <Clock size={20} />}
                            </div>
                            <div>
                                <p className="font-bold text-slate-800">{med.name}</p>
                                <p className="text-xs text-slate-500">{med.dosage} • {med.frequency}</p>
                                <p className="text-[10px] text-slate-400 font-medium italic">{med.instructions}</p>
                            </div>
                        </div>
                        {role === 'PATIENT' && med.status !== 'taken' && (
                            <button
                                onClick={() => handleTake(med.id)}
                                className="text-sm bg-blue-600 text-white px-3 py-1.5 rounded-lg active:scale-95 transition-all"
                            >
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
