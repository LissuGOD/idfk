
from flask import Flask, request

app = Flask(__name__)



mittaustieto = list()

@app.route("/", methods =["GET"])
def index():
    return f"mittaustieto:{mittaustieto[-1]}"

@app.route("/lisaa_tieto", methods=["POST"])
def lisaa_tieto():
    vastaanotettu_data = request.get_json(force=True)
    mittaustieto.append(vastaanotettu_data["mittaus"])

    return "200"


if __name__ == "__main__":
    app.run()