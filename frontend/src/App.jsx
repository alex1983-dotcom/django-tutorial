import { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch("http://localhost:8000/blog/api/test/")
      .then((res) => res.json())
      .then((data) => setMessage(data.message));
  }, []);

  return (
    <div>
      <h1>React + Django</h1>
      <p>Сообщение от Django: <strong>{message}</strong></p>
    </div>
  );
}

export default App;