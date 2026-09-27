# 🎙️ Voice-Activated Data Query to SQL (Voice-to-SQL)

An enterprise-grade, speech-driven database analyst powered by Google Gemini and SQLite.  
Convert natural spoken language into accurate SQL queries and get immediate local analytical results.

---

## 📌 How It Works

1. **Microphone Capture:** SpeechRecognition calibrates for ambient noise and listens to your natural voice prompt.
2. **Audio-to-Text:** Transcribes spoken query into raw text.
3. **Gemini Query Generation:** Gemini processes the text via custom system instructions, generating case-insensitive SQLite queries using `LIKE` wildcards.
4. **Local Execution:** Executes against `company_data.db` and outputs the result in your terminal.

---

## ✨ Key Highlights

- **Hands-Free Querying:** Voice-driven interface calibrated for background ambient noise.
- **Fuzzy & Partial Match Resilience:** Employs SQL `LIKE '%keyword%'` wildcards to handle misheard words or imperfect voice transcriptions seamlessly.
- **Python 3.14 Ready:** Overcomes upstream PyAudio compatibility limitations using a drop-in `pyaudiowpatch` patch.
- **Zero Hallucination Routing:** Uses strict system instructions to guarantee valid SQLite `SELECT` syntax without conversational markdown fluff.
- **Secure Credentials:** Isolates API keys and database binaries from version control using custom `.gitignore` rules.

---

## 📂 Repository Layout

- `setup_db.py` — Seeds the initial enterprise sales database.
- `voice_agent.py` — Core voice listener, Gemini engine, and SQL executor.
- `.gitignore` — Shields `.env`, Python bytecode, and SQLite databases.
- `README.md` — Project documentation and setup guide.

---

