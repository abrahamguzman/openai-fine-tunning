from openai import OpenAI
client = OpenAI()

# CAMBIAR POR EL MODELO DE FINE TUNNING (Puede ser otro modelo también)
modelo_fine_tunnig = "ft:gpt-3.5-turbo-0125:personal::9ImnMCrH" 
    
response = client.chat.completions.create(
  model=modelo_fine_tunnig,
  messages=[
    {
    "role": "user",
    "content": "Dime qué modelo de ai estoy usando ahora contigo"
    }],
  temperature=0,
  max_tokens=4095,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

# IMPRIME RESPUESTA
print(response.choices[0].message.content)

while True:
    # OBTENER MENSAJE DEL USUARIO
    user_message = input("Usuario: ")
    
    # OBTENER RESPUESTA DEL MODELO
    response = client.chat.completions.create(
      model=modelo_fine_tunnig,
      messages=[{
        "role": "user",
        "content": user_message
        }],
      temperature=0,
      max_tokens=4095,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    
    # IMPRIME RESPUESTA
    print(response.choices[0].message.content)