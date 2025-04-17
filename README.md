# Proyecto Urban Grocers (Pruebas API)

Este proyecto contiene pruebas automatizadas para verificar el comportamiento del endpoint de creación de kits en una API. Se utiliza `pytest` para reazliar pruebas y `requests` para hacer solicitudes HTTP.

## Estrucutura del proyecto

- configuration.py: Contiene las URLs y rutas de la API 
- data.py: Contiene los cuerpos de las solicitudes y headers.
- sender_stand_request.py: Funciones para enviar solicitudes HTTP.
- create_kit_name_kit_test.py: Archivo principal de pruebas.
- .gitignore: Archivos que Git debe ignorar

## Requisitos

Necesitas tener instalados los paquetes pytest para poder ejecutar las pruebas y request para reazlizar solicitudes HTTP.

## Como ejecutar las pruebas

Desde la terminal, estando en la carpeta del proyecto:
pytest create_kit_name_kit_test.py

## Lista de comprobación de pruebas

Nº	Descripción	Entrada	Resultado esperado (ER)

1	Nombre con 1 carácter	"name": "a"	201, el nombre coincide

2	Nombre con 511 caracteres	"name": "a"*511	201, el nombre coincide

3	Nombre vacío	"name": ""	400

4	Nombre con 512 caracteres	"name": "a"*512	400

5	Caracteres especiales permitidos	"name": "№%@,\"\\""	201, el nombre coincide

6	Nombre con espacios	"name": " A Aaa "	201, el nombre coincide

7	Nombre numérico	"name": "123"	201, el nombre coincide

8	Falta el parámetro "name"	{}	400

9	"name" como tipo numérico (no str)	"name": 123	400

## Resumen de pruebas realizadas

============================= test session starts =============================
collecting ... collected 9 items

create_kit_name_kit_test.py::test_kit_name_1_char PASSED                 [ 11%]201
{'name': 'a', 'user': {'id': 2, 'firstName': 'Andrea', 'phone': '+11234567890', 'address': '123 Elm Street, Hilltop', 'email': '', 'comment': '', 'authToken': '1a003cc8-6557-42d6-b638-717275891469'}, 'productsList': None, 'id': 7, 'productsCount': 0}

create_kit_name_kit_test.py::test_kit_name_511_chars PASSED              [ 22%]201
{'name': 'AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC', 'user': {'id': 3, 'firstName': 'Andrea', 'phone': '+11234567890', 'address': '123 Elm Street, Hilltop', 'email': '', 'comment': '', 'authToken': 'e91c0c4a-d98a-4faf-aab8-da6eabe41f45'}, 'productsList': None, 'id': 8, 'productsCount': 0}

create_kit_name_kit_test.py::test_kit_name_empty FAILED                  [ 33%]
create_kit_name_kit_test.py:56 (test_kit_name_empty)
201 != 400

Expected :400
Actual   :201
<Click to see difference>

def test_kit_name_empty():
>       negative_assert_code_400 (get_kit_body(""))

create_kit_name_kit_test.py:58:

create_kit_name_kit_test.py::test_kit_name_512_chars FAILED              [ 44%]
create_kit_name_kit_test.py:60 (test_kit_name_512_chars)
201 != 400

Expected :400
Actual   :201
<Click to see difference>

def test_kit_name_512_chars():
>       negative_assert_code_400(get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"))

create_kit_name_kit_test.py:62:

create_kit_name_kit_test.py::test_kit_name_special_chars PASSED          [ 55%]201
{'name': '"№%@",', 'user': {'id': 6, 'firstName': 'Andrea', 'phone': '+11234567890', 'address': '123 Elm Street, Hilltop', 'email': '', 'comment': '', 'authToken': '0d12746b-ebde-4157-9db8-c7cad88bbeb4'}, 'productsList': None, 'id': 11, 'productsCount': 0}

create_kit_name_kit_test.py::test_kit_name_with_spaces PASSED            [ 66%]201
{'name': ' A Aaa ', 'user': {'id': 7, 'firstName': 'Andrea', 'phone': '+11234567890', 'address': '123 Elm Street, Hilltop', 'email': '', 'comment': '', 'authToken': 'be111f5b-a2ff-43ab-8712-ba2b2521a6e6'}, 'productsList': None, 'id': 12, 'productsCount': 0}

create_kit_name_kit_test.py::test_kit_name_numbers PASSED                [ 77%]201
{'name': '123', 'user': {'id': 8, 'firstName': 'Andrea', 'phone': '+11234567890', 'address': '123 Elm Street, Hilltop', 'email': '', 'comment': '', 'authToken': '57fff4dd-d00d-4b0d-831b-3c5d7e904e98'}, 'productsList': None, 'id': 13, 'productsCount': 0}

create_kit_name_kit_test.py::test_kit_name_lost_chart FAILED             [ 88%]
create_kit_name_kit_test.py:76 (test_kit_name_lost_chart)
500 != 400

Expected :400
Actual   :500
<Click to see difference>

def test_kit_name_lost_chart():
        bearer = get_new_user_token()
        response = sender_stand_request.post_new_client_kit ({}, bearer)
>       assert response.status_code == 400
E       assert 500 == 400
E        +  where 500 = <Response [500]>.status_code

create_kit_name_kit_test.py:80: AssertionError

create_kit_name_kit_test.py::test_kit_name_different_chart FAILED        [100%]
create_kit_name_kit_test.py:82 (test_kit_name_different_chart)
201 != 400

Expected :400
Actual   :201
<Click to see difference>

def test_kit_name_different_chart():
>       negative_assert_code_400(get_kit_body(123))

create_kit_name_kit_test.py:84:


========================= 4 failed, 5 passed in 7.96s =========================

## Notas

- El token de autorización (Bearer) se genera automáticamente al crear un usuario.
- Las funciones que manejan solicitudes están en sender_stand_request.py.

## Autor

- Ricardo Gómora, cohort QA26- 7.mo sprint
- 16/04/2025

