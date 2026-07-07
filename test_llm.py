from config import Settings
from modules.llm_client import LLMClient

settings = Settings()

client = LLMClient(settings)

response = client.generate(
    "Respond ONLY with the word OK."
)

print(response)