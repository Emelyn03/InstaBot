from instagrapi import Client
import os

cl = Client()

# Hace el comportamiento más humano
cl.delay_range = [1, 3]

USERNAME = "TU_USUARIO"
PASSWORD = "TU_PASSWORD"


def login():

    try:

        cl.login(
            USERNAME,
            PASSWORD
        )

        cl.dump_settings(
            "session.json"
        )

        print(
            "Sesión iniciada correctamente"
        )

        return True

    except Exception as e:

        print(
            "Error login:",
            e
        )

        return False


def cargar_sesion():

    if os.path.exists(
        "session.json"
    ):

        try:

            cl.load_settings(
                "session.json"
            )

            cl.login(
                USERNAME,
                PASSWORD
            )

            print(
                "Sesión cargada"
            )

            return True

        except:

            print(
                "Sesión inválida"
            )

            return login()

    else:

        return login()


def dar_like(url_post):

    try:

        media_pk = cl.media_pk_from_url(
            url_post
        )

        cl.media_like(
            media_pk
        )

        return (
            "Like realizado correctamente"
        )

    except Exception as e:

        return str(e)


def comentar(url_post, texto):

    try:

        media_pk = cl.media_pk_from_url(
            url_post
        )

        cl.media_comment(
            media_pk,
            texto
        )

        return (
            "Comentario enviado"
        )

    except Exception as e:

        return str(e)