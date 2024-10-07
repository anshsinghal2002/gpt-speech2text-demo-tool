from openai import OpenAI
import os
os.environ["OPENAI_API_KEY"] = secret_key 
client = OpenAI()