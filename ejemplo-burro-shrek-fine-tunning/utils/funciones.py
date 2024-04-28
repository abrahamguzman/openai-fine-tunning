import json

def formatear_txt_a_lista(lista_mensajes, system_message=None):
    messages = []

    # Incluir primero el mensaje de sistema
    if system_message:
        messages.append({
            "role": "system",
            "content": system_message
        })

    # Iterar por la lista de mensajes
    for mensaje in lista_mensajes:
        # Separar los mensajes por los dos puntos y el espacio
        partes = mensaje.split(': ', maxsplit=1)

        #Controlar si alguna línea no cumple el patrón
        if len(partes) < 2:
            continue

        # Identificar el rol y content
        role = partes[0].strip()
        content = partes[1].strip()

        # Formatear el mensaje
        message = {
            "role": role,
            "content": content
        }

        #Agregar el mensaje a la lista
        messages.append(message)

    # Crear diccionario final
    dict_final = {
        "messages": messages
    }

    return dict_final

def save_to_jsonl(dataset, file_path):
    with open(file_path, 'w') as file:
        for ejemplo in dataset:
            json_line = json.dumps(ejemplo, ensure_ascii=False)
            file.write(json_line + '\n')