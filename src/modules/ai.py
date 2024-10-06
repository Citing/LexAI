from openai import OpenAI
from modules.config import Config

OpenAIAgent = OpenAI(api_key=Config.OPENAI_API_KEY)

def chat(prompts):
    responses = OpenAIAgent.chat.completions.create(
        model="gpt-4o-mini",
        messages=prompts,
    )
    response = responses.choices[0].message.content
    return response

def embedding(text):
    responses = OpenAIAgent.embeddings.create(
        model="text-embedding-3-small",
        input=text,
        encoding_format="float"
    )
    embedding = responses.data[0].embedding
    return embedding