import requests

def chat_with_tinyllama(prompts):
    url = "http://localhost:11434/api/chat"
    
    payload = {
        "model": "gemma:2b",
        "messages": prompts,
        "stream": False
    }
    
    response = requests.post(url, json=payload)
    
    return response.json()['message']['content']

# System prompt to set the context
system_prompt = "Sei un animale parlante, un gufo, il tuo nome è Anacleto. Rispondi alle domande in modo conciso, scontroso e divertente"
messages = [
    {"role": "system", "content": system_prompt}  # Changed "anacleto" to "system"
]

# First question
messages.append({"role": "user", "content": "Come ti chiami?"})
risposta1 = chat_with_tinyllama(messages)
print("Bot:", risposta1)

# Add bot's response to conversation history
messages.append({"role": "assistant", "content": risposta1})  # Changed "anacleto" to "assistant"

# Second question (bot remembers context)
messages.append({"role": "user", "content": "Cosa sei?"})
risposta2 = chat_with_tinyllama(messages)
print("Bot:", risposta2)

# Add bot's response
messages.append({"role": "assistant", "content": risposta2})

# Third question to test context memory
messages.append({"role": "user", "content": "Tell me a joke about being an owl"})
risposta3 = chat_with_tinyllama(messages)
print("Bot:", risposta3)