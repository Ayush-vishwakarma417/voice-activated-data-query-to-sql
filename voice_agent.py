
import os
import sqlite3
import sys

# 1. Drop-in patch for PyAudio on Python 3.14
import pyaudiowpatch

sys.modules["pyaudio"] = pyaudiowpatch

# 2. Imports for audio, environment, and Gemini API
from dotenv import load_dotenv
from google import genai
from google.genai import types  # <--- Added types here
import speech_recognition as sr

# Load your Gemini API key from .env
load_dotenv()
ai_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def listen_and_generate_sql():
  r = sr.Recognizer()

  # Capture microphone audio
  with sr.Microphone() as source:
    print("Adjusting for ambient noise... Please wait.")
    r.adjust_for_ambient_noise(source, duration=1)
    print("Listening... Ask your data question!")
    audio = r.listen(source, timeout=5, phrase_time_limit=10)

  try:
    # Transcribe speech to text
    print("Transcribing audio...")
    user_text = r.recognize_google(audio, language="en-US")
    print(f"You asked: '{user_text}'")

    system_instruction = """You are an enterprise database router. 
The user will ask a natural language question about sales data. 
You must output ONLY a valid SQLite SELECT query based on a table named 'sales'.
The 'sales' table has columns: id, product_name, revenue, sale_date.
Always use the LIKE operator with % wildcards (e.g., LIKE '%keyword%') for product names so partial voice transcriptions will still match.
Do not output markdown, explanations, or code blocks. Just the raw SQL string."""

    # Generate SQL with AFC disabled to silence the warning
    print("Generating SQL via Gemini...")
    response = ai_client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=user_text,
        config=types.GenerateContentConfig(  # <--- Updated config block here
            system_instruction=system_instruction,
            automatic_function_calling=types.AutomaticFunctionCallingConfig(
                disable=True
            ),
        ),
    )

    sql_query = response.text.strip()
    print(f"\nGenerated SQL Query:\n{sql_query}")

    # Connect to SQLite and execute the query
    print("\nExecuting query on local database...")
    with sqlite3.connect("company_data.db") as conn:
      cursor = conn.cursor()
      cursor.execute(sql_query)
      results = cursor.fetchall()

      print("\n--- Database Results ---")
      if results:
        for row in results:
          print(row)
      else:
        print("No matching records found.")

    return results

  except sr.UnknownValueError:
    print("Error: Could not understand the audio.")
  except sr.RequestError as e:
    print(f"Error: Could not request results; {e}")
  except Exception as ex:
    print(f"An unexpected error occurred: {ex}")


if __name__ == "__main__":
  listen_and_generate_sql()