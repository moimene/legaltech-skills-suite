import {
    Scale,
    Search,
    Building2,
    Calculator,
    Users,
    ShieldCheck,
    LayoutGrid
} from 'lucide-react';

const areas = [
    { id: 'all', label: 'Todas', icon: LayoutGrid },
    { id: 'litigios', label: 'Litigios', icon: Scale },
    { id: 'forensia', label: 'Forensia', icon: Search },
    { id: 'corporativo', label: 'Corporativo', icon: Building2 },
    { id: 'fiscal', label: 'Fiscal', icon: Calculator },
    { id: 'laboral', label: 'Laboral', icon: Users },
    { id: 'compliance', label: 'Compliance', icon: ShieldCheck }
];

export default function AreaFilter({ activeFilter, onFilterChange }) {
    return (
        <div
            style={{
                display: 'flex',
                flexWrap: 'wrap',
                gap: 'var(--g-space-2)',
                justifyContent: 'center',
                padding: 'var(--g-space-6) 0'
            }}
        >
            {areas.map(area => {
                const Icon = area.icon;
                const isActive = activeFilter === area.id;

                return (
                    <button
                        key={area.id}
                        onClick={() => onFilterChange(area.id)}
                        className={`btn-filter ${isActive ? 'active' : ''}`}
                        style={{
                            display: 'flex',
                            alignItems: 'center',
                            gap: 'var(--g-space-2)',
                            cursor: 'pointer'
                        }}
                    >
                        <Icon size={14} />
                        <span>{area.label}</span>
                    </button>
                );
            })}
        </div>
    );
}
