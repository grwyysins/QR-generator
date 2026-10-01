
from flask import Flask, render_template, request
import qrcode
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    qr_filename = None

    if request.method == "POST":
        data = request.form["data"]

        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4
        )

        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(
            fill_color="black",
            back_color="white"
        )

        qr_filename = "qr_code.png"
        img.save(os.path.join(app.static_folder, qr_filename))

    return render_template(
        "index.html",
        qr_filename=qr_filename
    )


if __name__ == "__main__":
    app.run(debug=True)