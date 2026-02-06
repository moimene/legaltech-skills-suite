import { Shield, Lock, Database, Cpu } from 'lucide-react';

export default function Hero({ skillCount }) {
  return (
    <header 
      className="hero"
      style={{ 
        backgroundColor: '#004438',
        color: '#ffffff',
        padding: 'var(--g-space-8) 0',
        minHeight: '400px',
        display: 'flex',
        alignItems: 'center'
      }}
    >
      <div className="container">
        <div style={{ display: 'flex', alignItems: 'center', gap: 'var(--g-space-4)', marginBottom: 'var(--g-space-4)' }}>
          <Shield size={48} strokeWidth={1.5} />
          <span 
            style={{ 
              backgroundColor: 'var(--g-brand-bright)',
              padding: '4px 12px',
              borderRadius: 'var(--g-radius-full)',
              fontSize: '0.75rem',
              fontWeight: 600,
              textTransform: 'uppercase',
              letterSpacing: '0.05em'
            }}
          >
            TEE Secure Enclave
          </span>
        </div>
        
        <h1 
          style={{ 
            fontSize: '3rem', 
            fontWeight: 700, 
            marginBottom: 'var(--g-space-4)',
            lineHeight: 1.1
          }}
        >
          LegalTech Skills Suite
        </h1>
        
        <p 
          style={{ 
            fontSize: '1.25rem', 
            opacity: 0.9, 
            maxWidth: '600px',
            marginBottom: 'var(--g-space-6)',
            lineHeight: 1.6
          }}
        >
          {skillCount} skills especializadas para análisis legal en entornos de ejecución confiable (TEE).
          Procesamiento local, sin exposición de datos sensibles.
        </p>
        
        <div style={{ display: 'flex', gap: 'var(--g-space-6)', flexWrap: 'wrap' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 'var(--g-space-2)', opacity: 0.8 }}>
            <Lock size={18} />
            <span style={{ fontSize: '0.875rem' }}>Sin acceso a red</span>
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 'var(--g-space-2)', opacity: 0.8 }}>
            <Database size={18} />
            <span style={{ fontSize: '0.875rem' }}>Solo lectura de inputs</span>
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 'var(--g-space-2)', opacity: 0.8 }}>
            <Cpu size={18} />
            <span style={{ fontSize: '0.875rem' }}>Datos en RAM únicamente</span>
          </div>
        </div>
      </div>
    </header>
  );
}
