import json
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
coterie = ""
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
books = [os.path.join(BASE_DIR, "LorePrompt.txt"), 
         os.path.join(BASE_DIR, "20thAnni-world.txt"), 
         os.path.join(BASE_DIR, "Disciplines.txt"), 
         os.path.join(BASE_DIR, "KindredSociety.txt"), 
         os.path.join(BASE_DIR, "Setting.txt")]


for book in books:
    prompt =  open(book, "r", encoding="utf-8");
    coterie += "/////////// \n \n \n" + prompt.read()
    prompt.close()


def makeStory(coterie):
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

        return assistant_msg
    except Exception as e:
        print("Error" + e)
        return None

story = makeStory(coterie)

def clean_text(text: str) -> str:
    lines = text.splitlines()
    cleaned = [line.strip() for line in lines if line.strip() != ""]
    return "\n".join(cleaned)

if story:
    story = clean_text(story)
    lore_path = os.path.join(BASE_DIR, "LoreSheet.txt")
    with open(lore_path, "w", encoding="utf-8") as lore:
        lore.write(story + "\n\n")
        