import sender_stand_request
import data

# esta función cambia los valores en el parámetro "name"
def get_kit_body(name):
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos del diccionario de origen
    current_body = data.kit_body.copy()
    # Se cambia el valor del parámetro name
    current_body["name"] = name
    # Se devuelve un nuevo diccionario con el valor name requerido
    return current_body

#Recibe token
def get_new_user_token():
    user_response = sender_stand_request.post_new_user(data.user_body)
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""
    return user_response.json()["authToken"]

# Función de prueba positiva
def positive_assert(kit_body):
    # El cuerpo de la solicitud actualizada se guarda en la variable bearer
    bearer = get_new_user_token()
    # El resultado de la solicitud para crear un/a nuevo/a usuario/a se guarda en la variable user_response
    user_response = sender_stand_request.post_new_client_kit(kit_body, bearer)
    #Imprime el estado del codigo recibido
    print(user_response.status_code)
    #imprime el kit de respuesta
    print(user_response.json())

# Comprueba si el código de estado es 201
    assert user_response.status_code == 201
    # Comprueba que el campo name del kit son iguales y que se a guradado el valor
    assert user_response.json()["name"] == kit_body["name"]

# Función de prueba negativa
def negative_assert_code_400 (kit_body):
    # El cuerpo de la solicitud actualizada se guarda en la variable bearer
    bearer = get_new_user_token()
    # Comprueba si la variable "response" almacena el resultado de la solicitud.
    response = sender_stand_request.post_new_client_kit(kit_body, bearer)

    # Comprueba si la respuesta contiene el código 400.
    assert response.status_code == 400
    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400.
    assert response.json()["code"] == 400

# 1 El número permitido de caracteres (1)
def test_kit_name_1_char():
    positive_assert(get_kit_body("a"))

#2 El número permitido de caracteres (511)
def test_kit_name_511_chars():
    positive_assert(get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"))

#3 El número de caracteres es menor que la cantidad permitida (0):
def test_kit_name_empty():
    negative_assert_code_400 (get_kit_body(""))

#4 El número de caracteres es mayor que la cantidad permitida (512)
def test_kit_name_512_chars():
    negative_assert_code_400(get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"))

#5 Se permiten caracteres especiales
def test_kit_name_special_chars():
    positive_assert(get_kit_body("\"№%@\","))

#6 Se permiten espacios
def test_kit_name_with_spaces():
    positive_assert(get_kit_body(" A Aaa " ))

#7 Se permiten números
def test_kit_name_numbers():
    positive_assert(get_kit_body("123"))

#8 El parámetro no se pasa en la solicitud
def test_kit_name_lost_chart():
    bearer = get_new_user_token()
    response = sender_stand_request.post_new_client_kit ({}, bearer)
    assert response.status_code == 400

#9 Se ha pasado un tipo de parámetro diferente (número)
def test_kit_name_different_chart():
    negative_assert_code_400(get_kit_body(123))





