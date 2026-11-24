from flask import Flask, render_template, request

app = Flask(__name__)


# Route "/" menerima GET (buka halaman) dan POST (kirim form)
@app.route("/", methods=["GET", "POST"])
def index():
    pesan = ""

    if request.method == "POST":
        # Ambil parameter dari TextField (name="nama") lewat method POST
        nama = request.form.get("nama", "").strip()

        if nama:
            pesan = f"Halo, {nama}! Data berhasil dikirim lewat method POST."
        else:
            pesan = "Nama tidak boleh kosong."

    return render_template("index.html", pesan=pesan)


if __name__ == "__main__":
    app.run(debug=True)
