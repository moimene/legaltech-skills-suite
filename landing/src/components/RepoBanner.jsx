import { Github, Star, ExternalLink } from 'lucide-react';

const REPO_URL = 'https://github.com/moimene/legaltech-skills-suite';

export default function RepoBanner() {
    return (
        <a
            href={REPO_URL}
            target="_blank"
            rel="noopener noreferrer"
            style={{
                display: 'block',
                background: 'linear-gradient(135deg, var(--g-brand-3308) 0%, var(--g-sec-700) 100%)',
                color: '#ffffff',
                padding: 'var(--g-space-4) var(--g-space-6)',
                textDecoration: 'none',
                transition: 'all 200ms ease'
            }}
            onMouseOver={(e) => {
                e.currentTarget.style.background = 'linear-gradient(135deg, var(--g-sec-700) 0%, var(--g-brand-bright) 100%)';
            }}
            onMouseOut={(e) => {
                e.currentTarget.style.background = 'linear-gradient(135deg, var(--g-brand-3308) 0%, var(--g-sec-700) 100%)';
            }}
        >
            <div
                className="container"
                style={{
                    display: 'flex',
                    justifyContent: 'center',
                    alignItems: 'center',
                    gap: 'var(--g-space-4)',
                    flexWrap: 'wrap'
                }}
            >
                <div style={{ display: 'flex', alignItems: 'center', gap: 'var(--g-space-3)' }}>
                    <Github size={24} />
                    <span style={{ fontWeight: 600, fontSize: '1rem' }}>
                        ⭐ Explora el código en GitHub
                    </span>
                </div>

                <div
                    style={{
                        display: 'flex',
                        alignItems: 'center',
                        gap: 'var(--g-space-2)',
                        backgroundColor: 'rgba(255,255,255,0.15)',
                        padding: 'var(--g-space-2) var(--g-space-3)',
                        borderRadius: 'var(--g-radius-full)',
                        fontSize: '0.875rem'
                    }}
                >
                    <Star size={14} fill="#ffffff" />
                    <span>Star</span>
                    <ExternalLink size={14} />
                </div>
            </div>
        </a>
    );
}
