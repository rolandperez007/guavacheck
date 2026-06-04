export async function runAustin(query: string, user_id?: string) {
  const res = await fetch("http://127.0.0.1:8000/austin/execute", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      query,
      user_id
    })
  });

  return await res.json();
}