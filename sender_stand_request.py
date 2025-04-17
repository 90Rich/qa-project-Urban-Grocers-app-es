import configuration
import requests
import data

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH) # inserta la dirección URL completa

# Funcion para crear usuario
def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa sin /
                         json=user_body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

#Función para crear un nuevo kit de producto por Bearer auth_Token
def post_new_client_kit(kit_body,auth_token):
    headers_with_auth_token = data.headers.copy()
    headers_with_auth_token["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH, # inserta la dirección URL completa
                         json=kit_body,  # inserta el cuerpo de solicitud
                         headers=headers_with_auth_token)  # inserta los encabezados



respons = post_new_user(data.user_body)
print(respons.status_code)
print(respons.json())