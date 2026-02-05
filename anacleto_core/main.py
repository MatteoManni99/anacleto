import requests
import json

def chat_with_tinyllama(prompts):
    url = "http://localhost:11434/api/chat"
    
    payload = {
        "model": "tinyllama",
        "messages": prompts,
        "stream": False
    }
    
    response = requests.post(url, json=payload)
    
    return response.json()['message']['content']

#Prompt iniziale per impostare il contesto della conversazione
system_prompt = "Sei un assistente utile che risponde in italiano."
messages = [
    {"role": "system", "content": system_prompt}
]

# Prima domanda
messages.append({"role": "user", "content": "Ciao, come stai?"})
risposta1 = chat_with_tinyllama(messages)
print("Bot:", risposta1)

# Aggiungi risposta del bot alla cronologia
messages.append({"role": "assistant", "content": risposta1})

# Seconda domanda (il bot ricorda il contesto)
messages.append({"role": "user", "content": "Mi racconti una barzelletta?"})
risposta2 = chat_with_tinyllama(messages)
print("Bot:", risposta2)