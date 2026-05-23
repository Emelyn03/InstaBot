from flask import (
    Flask,
    render_template,
    request
)

from instagram_bot import (
    cargar_sesion,
    dar_like,
    comentar
)

app = Flask(__name__)

# Intentar login
login_correcto = cargar_sesion()


@app.route(
    "/",
    methods=["GET", "POST"]
)
def inicio():

    mensaje = ""

    if not login_correcto:

        mensaje = (
            "Instagram no inició sesión."
        )

        return render_template(
            "index.html",
            mensaje=mensaje
        )

    if request.method == "POST":

        url = request.form["url"]

        accion = request.form["accion"]

        if accion == "like":

            mensaje = dar_like(url)

        elif accion == "comentario":

            texto = request.form["comentario"]

            if texto.strip() == "":

                mensaje = (
                    "Debes escribir un comentario"
                )

            else:

                mensaje = comentar(
                    url,
                    texto
                )

    return render_template(
        "index.html",
        mensaje=mensaje
    )


if __name__ == "__main__":

    app.run(debug=True)