import AustinOrb from '../components/austin-orb/AustinOrb';
import useAustinDemo from '../hooks/useAustinDemo';

export default function Home() {
  const { state } = useAustinDemo();

  return (
    <main style={{
      height: '100vh',
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      background: '#0b0f14'
    }}>
      <AustinOrb state={state} />
    </main>
  );
}