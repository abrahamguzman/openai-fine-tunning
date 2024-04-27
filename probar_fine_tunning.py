from openai import OpenAI
import json
client = OpenAI()

# ABRE JSON CON LOS MENSAJES DE CHAT
with open("mensajesparachat.json", "r", encoding='utf-8') as f:
    messages = json.load(f)

# CAMBIAR POR EL MODELO DE FINE TUNNING
modelo_fine_tunnig = "ft:gpt-3.5-turbo-0125:personal::9ISqvNP4"
    
response = client.chat.completions.create(
  model=modelo_fine_tunnig,
  messages=messages,
  temperature=0,
  max_tokens=4095,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

# IMPRIME RESPUESTA
print(response.choices[0].message.content)