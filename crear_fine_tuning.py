# CONSEJO: Comentar/Descomentar bloque de código --> Alt + Shift + A

from openai import OpenAI 
from utils.print import print_job_info
client = OpenAI()


# PASO1: Subir archivo de entrenamiento
ruta_archivo_entrenamiento = "archivos-entrenamiento/entreno-v3.jsonl" # ¡ATENCIÓN! Cambiar por la ruta de tu archivo

archivo_entrenamiento = client.files.create(
  file=open(ruta_archivo_entrenamiento, "rb"),
  purpose="fine-tune"
)
print(f'Id de archivo cargado: {archivo_entrenamiento.id}')


# PASO2: Crear job/trabajo para fine-tuning
id_archivo_entrenamiento = archivo_entrenamiento.id # No es necesario cambiar

trabajo_subido = client.fine_tuning.jobs.create(
  training_file=id_archivo_entrenamiento, 
  model="gpt-3.5-turbo", # gpt-3.5-turbo
)
print(f"Trabajo subido correctamente: {trabajo_subido.id}")


# OPCIONAL: Verifica estado del job
ultimo_job = client.fine_tuning.jobs.list(limit=1)
print_job_info(ultimo_job.data[0])


# OPCIONAL: PRUEBA DE CHAT

""" completion = client.completions.create(
  model="ft:davinci-002:personal::9IQjSkAb",
  prompt="Que luego de efectuada la investigación preparatoria correspondiente, y al amparo de lo previsto en el Artículo 349° del Código Procesal Penal; procedo a formular ACUSACIÓN en contra de: KLIVER PÉREZ PAREDES, RUTH GUZMÁN LEÓN, LLISENIA PÉREZ PAREDES Y ERICH EDGAR FLORES HUAMÁN, en calidad de coautores de Actos de Promoción al tráfico ilícito de drogas, realizando actos de tráfico, acopio y transporte de droga agravado, ilícito previsto y sancionado en el primer párrafo del artículo 296 del Código Penal, concordante con el inc. 6) del art. 297 del C.P. en agravio del Estado Peruano, representado por el Procurador Público a cargo de los Asuntos Judiciales del Ministerio del Interior relativos al Tráfico Ilícito de Drogas. res:",
  max_tokens=4095,
)
print(completion.choices[0].text) """
