import { useState, useMemo } from 'react';
import Hero from './components/Hero';
import AreaFilter from './components/AreaFilter';
import SkillCard from './components/SkillCard';
import Footer from './components/Footer';
import skills from './data/skills.json';
import './index.css';

export default function App() {
  const [activeFilter, setActiveFilter] = useState('all');

  const filteredSkills = useMemo(() => {
    if (activeFilter === 'all') return skills;
    return skills.filter(skill => skill.area === activeFilter);
  }, [activeFilter]);

  const areaCounts = useMemo(() => {
    const counts = {};
    skills.forEach(skill => {
      counts[skill.area] = (counts[skill.area] || 0) + 1;
    });
    return counts;
  }, []);

  return (
    <div className="app">
      <Hero skillCount={skills.length} />

      <main className="container">
        <section style={{ textAlign: 'center', padding: 'var(--g-space-8) 0 0' }}>
          <h2 style={{ marginBottom: 'var(--g-space-2)' }}>
            Catálogo de Skills
          </h2>
          <p style={{ fontSize: '1rem', color: 'var(--g-text-secondary)', marginBottom: 0 }}>
            Filtra por área legal para explorar las capacidades disponibles
          </p>
        </section>

        <AreaFilter
          activeFilter={activeFilter}
          onFilterChange={setActiveFilter}
        />

        <div style={{ marginBottom: 'var(--g-space-4)', textAlign: 'center' }}>
          <span
            style={{
              fontSize: '0.875rem',
              color: 'var(--g-text-secondary)',
              backgroundColor: 'var(--g-surface-subtle)',
              padding: 'var(--g-space-2) var(--g-space-4)',
              borderRadius: 'var(--g-radius-full)'
            }}
          >
            Mostrando {filteredSkills.length} de {skills.length} skills
          </span>
        </div>

        <div
          className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3"
          style={{ paddingBottom: 'var(--g-space-8)' }}
        >
          {filteredSkills.map((skill, index) => (
            <SkillCard
              key={skill.id}
              skill={skill}
              index={index}
            />
          ))}
        </div>

        {/* Statistics Section */}
        <section
          style={{
            backgroundColor: 'var(--g-surface-subtle)',
            borderRadius: 'var(--g-radius-lg)',
            padding: 'var(--g-space-8)',
            marginBottom: 'var(--g-space-8)'
          }}
        >
          <h3 style={{ textAlign: 'center', marginBottom: 'var(--g-space-6)' }}>
            Distribución por Área
          </h3>
          <div
            style={{
              display: 'grid',
              gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))',
              gap: 'var(--g-space-4)'
            }}
          >
            {Object.entries(areaCounts).map(([area, count]) => (
              <div
                key={area}
                style={{
                  textAlign: 'center',
                  padding: 'var(--g-space-4)',
                  backgroundColor: 'var(--g-surface-card)',
                  borderRadius: 'var(--g-radius-md)',
                  border: '1px solid var(--g-border-subtle)'
                }}
              >
                <div
                  style={{
                    fontSize: '1.5rem',
                    fontWeight: 700,
                    color: `var(--area-${area})`
                  }}
                >
                  {count}
                </div>
                <div
                  style={{
                    fontSize: '0.75rem',
                    textTransform: 'capitalize',
                    color: 'var(--g-text-secondary)'
                  }}
                >
                  {area}
                </div>
              </div>
            ))}
          </div>
        </section>
      </main>

      <Footer />
    </div>
  );
}
