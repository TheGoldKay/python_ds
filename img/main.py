import os
from openai import OpenAI
from dotenv import load_dotenv
import webbrowser

load_dotenv()

client = OpenAI()

PROMPT2 = "Dracula little daughter"

response = client.images.generate(
    model="dall-e-3",
    prompt=PROMPT2,
)
webbrowser.open(response.data[0].url)
print(response.data[0].url)
