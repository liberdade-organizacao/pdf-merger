from os import remove
from io import BytesIO

from flask import (
    Flask,
    request,
    send_file,
)
from flask_cors import CORS

from app.utils import randomword
from merger import merge_pdf


app = Flask(__name__)
CORS(app)


@app.route("/merge", methods=["POST"])
def merge():
    request_id = randomword(10)
    result = "oops"

    # saving request files locally
    local_files = []
    for key, fileStorage in request.files.items():
        temporary_file_name = f"./{request_id}-{key}.pdf"
        with open(temporary_file_name, "wb") as fp:
            fp.write(fileStorage.stream.read())
        local_files.append(temporary_file_name)

    # merge files and load result
    output_file = f"./{request_id}-outlet.pdf"
    merge_pdf(local_files, output_file)
    with open(output_file, "rb") as fp:
        result = fp.read()

    # deleting temporary files
    for fn in [output_file, *local_files]:
        remove(fn)

    return send_file(
        BytesIO(result),
        mimetype='application/pdf',
        as_attachment=True,
        attachment_filename=f"{request_id}.pdf",
    )
