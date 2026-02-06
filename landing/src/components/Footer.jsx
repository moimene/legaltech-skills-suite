import { Github, ExternalLink } from 'lucide-react';

export default function Footer() {
    return (
        <footer
            style={{
                backgroundColor: 'var(--g-brand-3308)',
                color: '#ffffff',
                padding: 'var(--g-space-8) 0',
                marginTop: 'var(--g-space-8)'
            }}
        >
            <div className="container">
                <div
                    style={{
                        display: 'flex',
                        justifyContent: 'space-between',
                        alignItems: 'center',
                        flexWrap: 'wrap',
                        gap: 'var(--g-space-4)'
                    }}
                >
                    <div>
                        <h4 style={{ fontSize: '1.125rem', fontWeight: 600, marginBottom: 'var(--g-space-2)', color: '#ffffff' }}>
                            LegalTech Skills Suite
                        </h4>
                        <p style={{ fontSize: '0.875rem', opacity: 0.8 }}>
                            Análisis legal seguro en entornos TEE
                        </p>
                    </div>

                    <div style={{ display: 'flex', gap: 'var(--g-space-4)' }}>
                        <a
                            href="https://github.com/moimene/legaltech-skills-suite"
                            target="_blank"
                            rel="noopener noreferrer"
                            style={{
                                display: 'flex',
                                alignItems: 'center',
                                gap: 'var(--g-space-2)',
                                color: '#ffffff',
                                opacity: 0.8,
                                transition: 'opacity 150ms ease'
                            }}
                            onMouseOver={(e) => e.currentTarget.style.opacity = 1}
                            onMouseOut={(e) => e.currentTarget.style.opacity = 0.8}
                        >
                            <Github size={20} />
                            <span style={{ fontSize: '0.875rem' }}>GitHub</span>
                            <ExternalLink size={14} />
                        </a>
                    </div>
                </div>

                <div
                    style={{
                        borderTop: '1px solid rgba(255, 255, 255, 0.1)',
                        marginTop: 'var(--g-space-6)',
                        paddingTop: 'var(--g-space-6)',
                        textAlign: 'center',
                        fontSize: '0.75rem',
                        opacity: 0.6
                    }}
                >
                    MIT License © 2026 — Diseñado para entornos LegalTech de alta seguridad
                </div>
            </div>
        </footer>
    );
}
