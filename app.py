from flask import Flask, render_template, request
from zipfile import ZipFile, BadZipFile
from io import BytesIO

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    file_names = []
    error = None

    if request.method == 'POST':
        uploaded_file = request.files.get('zip_file')

        if not uploaded_file or uploaded_file.filename == '':
            error = 'Please choose a ZIP file to upload.'
        else:
            try:
                with ZipFile(BytesIO(uploaded_file.read())) as zip_file:
                    file_names = zip_file.namelist()
            except BadZipFile:
                error = 'The uploaded file is not a valid ZIP archive.'

    return render_template('index.html', file_names=file_names, error=error)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
