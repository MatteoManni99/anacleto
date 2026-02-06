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
system_prompt = "Sei un animale parlante, un gufo, che svolge la funzione di assistente personale. Ti chiami Anacleto. Rispondi alle domande in modo scorbutico e divertente. Continua la conversazione con l'utente"
messages = [
    {"role": "anacleto", "content": system_prompt}
]

# Prima domanda
messages.append({"role": "user", "content": "Ciao, come ti chiami?"})
risposta1 = chat_with_tinyllama(messages)
print("Bot:", risposta1)

# Aggiungi risposta del bot alla cronologia
messages.append({"role": "anacleto", "content": risposta1})

# Seconda domanda (il bot ricorda il contesto)
messages.append({"role": "user", "content": "Cosa sei?"})
risposta2 = chat_with_tinyllama(messages)
print("Bot:", risposta2)