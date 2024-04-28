from openai import OpenAI
from utils.funciones import formatear_txt_a_lista, save_to_jsonl

# Instanciamos la classe OpenAI (Práctica recomendada)
client = OpenAI()

# PASO1: PREPARAR DATA

""" 
  Cargamos dialogos de burro
"""
with open('dialogos_burro.txt', 'r', encoding="utf-8") as f:
    text = [line for line in f]

""" 
  Formateamos de txt a lista
"""
system_message = 'Eres un Burro muy parlanchín y muy ingenioso en tus respuestas. \
Usa los símbolos [ y ] para señalar que realizas alguna acción. \
Por ejemplo, para señalar que extiendes la mano: \
Hola, como estás? [extiendo la mano].'

dataset = []

ejemplo = []
for line in text:
  if line == '-\n':
    ejemplo_formateado = formatear_txt_a_lista(lista_mensajes=ejemplo,
                                            system_message=system_message)

    dataset.append(ejemplo_formateado)
    ejemplo = []
    continue

  ejemplo.append(line)
  
""" 
  Formateamos de lista a jsonl
"""

save_to_jsonl(dataset, 'dialogos_burro_train_full.jsonl')


# PASO 2 -> CARGAR ARCHIVO A OPENAI
train_full_response_file = client.files.create(
    file=open('dialogos_burro_train_full.jsonl','rb'),
    purpose='fine-tune'
)

print(f'Id de archivo cargado: {train_full_response_file.id}')


# PASO 3 -> CREAR FINE TUNNING JOB
response = client.fine_tuning.jobs.create(
  training_file=train_full_response_file.id,
  model="gpt-3.5-turbo",
  suffix='burro-shrek-v2',
  hyperparameters={'n_epochs':4}
  )

print(f"ID de fine job cargado: {response.id}")
