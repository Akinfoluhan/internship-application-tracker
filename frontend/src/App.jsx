import { useEffect, useState } from "react";

export default function App() {
  const [health, setHealth] = useState("loading...");

  useEffect(() => {
    const baseUrl = import.meta.env.VITE_API_BASE_URL;

    fetch(`${baseUrl}/health`)
      .then((res) => res.json())
      .then((data) => setHealth(data.status))
      .catch(() => setHealth("error"));
  }, []);

  return (
    <div style={{ padding: 24, fontFamily: "system-ui, Arial" }}>
      <h1>InternTrack</h1>
      <p>Frontend is running ✅</p>
      <p>
        Backend health: <strong>{health}</strong>
      </p>
    </div>
  );
}