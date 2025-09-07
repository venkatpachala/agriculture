'use client';
import React, { useState } from 'react';

export default function QueryPage() {
  const [text, setText] = useState('');
  const [answer, setAnswer] = useState<string | null>(null);

  const submit = async () => {
    const res = await fetch((process.env.NEXT_PUBLIC_API_URL || '') + '/api/v1/query', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text, language: 'te' })
    });
    const data = await res.json();
    setAnswer(data.answer_te);
  };

  return (
    <main className="p-4">
      <h1 className="text-lg font-semibold">Ask</h1>
      <textarea
        aria-label="Question"
        value={text}
        onChange={e => setText(e.target.value)}
        className="border p-2 w-full"
      />
      <button onClick={submit} className="mt-2 px-4 py-2 bg-green-600 text-white">
        Submit
      </button>
      {answer && <p className="mt-4">{answer}</p>}
    </main>
  );
}
