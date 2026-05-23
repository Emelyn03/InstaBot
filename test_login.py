from instagrapi import Client

cl = Client()

usuario = "usuario"
password = "password"

try:

    cl.login(
        usuario,
        password
    )

    print(
        "LOGIN EXITOSO"
    )

except Exception as e:

    print(
        "ERROR:",
        e
    )