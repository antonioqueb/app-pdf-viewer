from io import BytesIO
from flask import Flask, send_file, make_response, render_template

app = Flask(__name__)

@app.route('/')
def view_cv():
    cv_path = '/cv/cv.pdf'

    with open(cv_path, 'rb') as cv_file:
        # Leer el archivo PDF en memoria
        cv_content = cv_file.read()
        # Crear un objeto BytesIO
        cv_stream = BytesIO(cv_content)
        # Crear una respuesta con el archivo PDF
        response = make_response(cv_stream.getvalue())
        # Establecer el tipo de contenido a 'application/pdf'
        response.headers.set('Content-Type', 'application/pdf')
        # Establecer el encabezado para mostrar el PDF en el navegador
        response.headers.set('Content-Disposition', 'inline', filename='cv/cv.pdf')
        return response


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=7000)
