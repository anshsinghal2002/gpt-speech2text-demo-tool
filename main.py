from openai import OpenAI
import os
import json


def get_secret_key():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, 'CONFIG.json')
    try:
        # Open and read the config file
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)
        # Return the secret key
        return config.get('secret_key')
    except FileNotFoundError:
        print("Error: config.json file not found.")
        return None
    except json.JSONDecodeError:
        print("Error: config.json is not a valid JSON file.")
        return None
    except KeyError:
        print("Error: 'SecretKey' not found in config.json.")
        return None


def transcribe(audio_file_path,client):
  audio_file = open(audio_file_path, "rb")
  transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    # prompt = "" will improve accuracy if you can describe use case of audio input
    language="en",
    file=audio_file, 
    response_format="text"
  )
  return transcription

def generate_corrected_transcript(temperature, system_prompt, audio_file,client):
    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=temperature,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": transcribe(audio_file,client)
            }
        ]
    )
    return response.choices[0].message.content

def speech_prompt(client,audio_filepath = "gpt-test-file.m4a"):
    system_prompt = "You are a helpful assistant for the CFO of the company Uniqus. Your task is to generate a useful response to the transcribed text."
    speech_2_text_completion = generate_corrected_transcript(0, system_prompt, audio_filepath,client)
    return speech_2_text_completion


def main():
    os.environ["OPENAI_API_KEY"] = get_secret_key()
    client = OpenAI()
    speech_2_text_completion = speech_prompt(client,"gpt-test-file.m4a")
    print (speech_2_text_completion)



if __name__ == "__main__":
    main()