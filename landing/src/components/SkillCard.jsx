import {
    Scale,
    Search,
    Building2,
    Calculator,
    Users,
    ShieldCheck,
    ArrowRight
} from 'lucide-react';

const areaIcons = {
    litigios: Scale,
    forensia: Search,
    corporativo: Building2,
    fiscal: Calculator,
    laboral: Users,
    compliance: ShieldCheck
};

const areaLabels = {
    litigios: 'Litigios',
    forensia: 'Forensia',
    corporativo: 'Corporativo',
    fiscal: 'Fiscal',
    laboral: 'Laboral',
    compliance: 'Compliance'
};

export default function SkillCard({ skill, index }) {
    const Icon = areaIcons[skill.area] || Scale;

    return (
        <article
            className="card animate-fadeInUp"
            style={{
                animationDelay: `${index * 50}ms`,
                display: 'flex',
                flexDirection: 'column',
                height: '100%'
            }}
        >
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 'var(--g-space-4)' }}>
                <div
                    style={{
                        width: '40px',
                        height: '40px',
                        borderRadius: 'var(--g-radius-md)',
                        backgroundColor: `var(--area-${skill.area})`,
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center'
                    }}
                >
                    <Icon size={20} color="#ffffff" strokeWidth={1.5} />
                </div>
                <span className={`badge badge-${skill.area}`}>
                    {areaLabels[skill.area]}
                </span>
            </div>

            <h3
                style={{
                    fontSize: '1.125rem',
                    fontWeight: 600,
                    marginBottom: 'var(--g-space-2)',
                    color: 'var(--g-text-primary)'
                }}
            >
                {skill.name}
            </h3>

            <p
                style={{
                    fontSize: '0.875rem',
                    color: 'var(--g-text-secondary)',
                    marginBottom: 'var(--g-space-4)',
                    flex: 1
                }}
            >
                {skill.description}
            </p>

            <div
                style={{
                    padding: 'var(--g-space-3)',
                    backgroundColor: 'var(--g-surface-subtle)',
                    borderRadius: 'var(--g-radius-sm)',
                    marginTop: 'auto'
                }}
            >
                <div style={{ display: 'flex', alignItems: 'center', gap: 'var(--g-space-2)' }}>
                    <ArrowRight size={14} color="var(--g-text-secondary)" />
                    <code
                        style={{
                            fontSize: '0.75rem',
                            color: 'var(--g-text-secondary)',
                            fontFamily: 'monospace'
                        }}
                    >
                        {skill.topology}
                    </code>
                </div>
            </div>
        </article>
    );
}
