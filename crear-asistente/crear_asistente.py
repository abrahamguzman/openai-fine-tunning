from openai import OpenAI
client = OpenAI()
 
assistant = client.beta.assistants.create(
  name="Fragmentador de texto",
  instructions="Eres un lingüista especialista en idioma español, y debes ayudar a fragmentar texto en frases lo más cortas posibles añadiéndoles un salte de línea. Cada frase debe incluir, de forma explícita o tácita según el contexto, sujeto, verbo y predicado. Asegúrate de que cada una exprese solo una idea y no confíes en la puntuación original, pues podría no ser correcta. No olvides sintentizar el texto y numerar las frases, fragméntalas lo más posible manteniendo la idea de cada uno de los fragmentos.",
  model="gpt-4-turbo",
  tools=[{"type": "file_search"}],
)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content="Fragmenta lo siguiente con saltos de línea y numeralos: El Ministerio Público, presenta como hecho que se atribuye a los acusados, Llisenia Pérez Paredes y Ruth Guzmán León, ser presuntos coautores del delito contra la Salud Publica en la modalidad de Promoción y Favorecimiento al Tráfico Ilícito de Drogas agravado, por cuanto que, Que, en horas de la mañana del día 26 de Agosto del 2015 el personal policial del DEPANDRO Tacna salieron de su base con la finalidad de realizar acciones de orientación de esfuerzo de búsqueda de TID OEBI. Siendo ello así es así como al promediar las 10:54 horas observaron el tránsito del vehículo de placa de rodaje ZlA-387 marça HYUNDAI STAREX color negro, conducido por la persona conocida como FITO, quien por información confidencial se dedicaría al TID."
)

run = client.beta.threads.runs.create_and_poll(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Fragmenta el texto"
)

if run.status == 'completed': 
  messages = client.beta.threads.messages.list(
    thread_id=thread.id
  )
  print(messages.data[0].content[0].text.value)
else:
  print(run.status)