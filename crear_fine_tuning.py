# CONSEJO: Comentar/Descomentar bloque de código --> Alt + Shift + A

from openai import OpenAI
from pprint import pprint 
client = OpenAI()


# PASO1: Subir archivo de entrenamiento
""" client.files.create(
  file=open("acusacionfinal-gpt3.jsonl", "rb"),
  purpose="fine-tune"
) """


# PASO2: Crear job/trabajo para fine-tuning
""" client.fine_tuning.jobs.create(
  training_file="file-baMWKF9mgLfl6KG9BVzq39rC", 
  model="gpt-3.5-turbo" # gpt-3.5-turbo
) """

# OPCIONAL: Ver estado de trabajos
pprint(client.fine_tuning.jobs.list(limit=1))
id_job = "ftjob-JHexJxf1vmkU5ql84a2UOfb1"
#pprint(client.fine_tuning.jobs.retrieve(id_job))


# OPCIONAL: PRUEBA DE CHAT

""" completion = client.completions.create(
  model="ft:davinci-002:personal::9IQjSkAb",
  prompt="Que luego de efectuada la investigación preparatoria correspondiente, y al amparo de lo previsto en el Artículo 349° del Código Procesal Penal; procedo a formular ACUSACIÓN en contra de: KLIVER PÉREZ PAREDES, RUTH GUZMÁN LEÓN, LLISENIA PÉREZ PAREDES Y ERICH EDGAR FLORES HUAMÁN, en calidad de coautores de Actos de Promoción al tráfico ilícito de drogas, realizando actos de tráfico, acopio y transporte de droga agravado, ilícito previsto y sancionado en el primer párrafo del artículo 296 del Código Penal, concordante con el inc. 6) del art. 297 del C.P. en agravio del Estado Peruano, representado por el Procurador Público a cargo de los Asuntos Judiciales del Ministerio del Interior relativos al Tráfico Ilícito de Drogas. res:",
  max_tokens=4095,
)
print(completion.choices[0].text) """
