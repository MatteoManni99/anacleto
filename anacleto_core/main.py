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
system_prompt = "You are a talking animal, an owl, who acts as a personal assistant. Your name is Anacleto. Answer questions in a grumpy and funny way. Continue the conversation with the user"
messages = [
    {"role": "anacleto", "content": system_prompt}
]

# Prima domanda
messages.append({"role": "user", "content": "whats your name?"})
risposta1 = chat_with_tinyllama(messages)
print("Bot:", risposta1)

# Aggiungi risposta del bot alla cronologia
messages.append({"role": "anacleto", "content": risposta1})

# Seconda domanda (il bot ricorda il contesto)
messages.append({"role": "user", "content": "What are you?"})
risposta2 = chat_with_tinyllama(messages)
print("Bot:", risposta2)