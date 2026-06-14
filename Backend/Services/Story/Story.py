import json
import requests
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


def makeStory(coterie = None):
    BASE_DIR = Path(__file__).resolve().parent
    MATERIALS_DIR = BASE_DIR / "Materials"
    coterie = ""

    for book in MATERIALS_DIR.glob("*.txt"):
        with open(book, "r", encoding="utf-8") as prompt:
            coterie += "\n\n///////////\n\n" + prompt.read()
            prompt.close()


    try:
        api_response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "model": "anthropic/claude-4.7-opus",
                "messages": [{"role": "system", "content": f"{coterie}"}],
                "reasoning": {"enabled": True}
            })
        )

        api_json = api_response.json()
        assistant_msg = api_json['choices'][0]['message']['content']

        def clean_text(text: str) -> str:
            lines = text.splitlines()
            cleaned = [line.strip() for line in lines if line.strip() != ""]
            return "\n".join(cleaned)

        if assistant_msg:
            story = clean_text(assistant_msg)
            with open("LoreSheet.txt", "w", encoding="utf-8") as lore:
                lore.write(story + "\n\n")
            
    except Exception as e:
        print(f"Error: {e}")
        return None



        
