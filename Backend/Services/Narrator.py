import json
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
def storytelling(player_action = None):
    coterie = ""

    def read_file(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    def write_file(path, content):
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    BASE_DIR = os.path.dirname(__file__)
    lore = read_file(os.path.join(BASE_DIR, "Story", "LoreSheet.txt"))
    prompt  = read_file(os.path.join(BASE_DIR, "prompt.txt"))
    journey = read_file(os.path.join(BASE_DIR, "player_journey.txt"))
    member = read_file(os.path.join(BASE_DIR, "Member.txt"))

    
    coterie = f"{lore}\n\n{prompt}"

    if player_action:
        coterie += f"\n\nPLAYER ACTION:\n{player_action}\n"

    

    recent_history = "".join(journey[-3000:])

    coterie += member
    coterie += recent_history

    payload = {
    "model": "openai/gpt-5.1",
    "messages": [
        {"role": "system", "content": coterie}
    ],
    "response_format": {
        "type": "json_schema",
        "json_schema": {
            "name": "two_sections_output",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "Story": {"type": "string"},
                    "Character Sheet": {"type": "string"}
                },
                "required": ["Story", "Character Sheet"],
                "additionalProperties": False
                }
            }
        }
    }

    def clean_text(text: str) -> str:
        lines = text.splitlines()
        cleaned = [line.strip() for line in lines if line.strip() != ""]
        return "\n".join(cleaned)

    api_response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json=payload
    )

    api_json = api_response.json()

    content = api_json["choices"][0]["message"]["content"]


    journey = json.loads(content)

    journey["Story"] = clean_text(journey["Story"])
    journey["Character Sheet"] = clean_text(journey["Character Sheet"])


    write_file(os.path.join(BASE_DIR, "player_journey.txt"), journey["Story"] + "\n\n")
    write_file(os.path.join(BASE_DIR, "Member.txt"), journey["Character Sheet"] + "\n")

    return journey["Story"]