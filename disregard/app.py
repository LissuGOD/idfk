
from flask import Flask, request, render_template, Response, stream_with_context
import json
import threading

app = Flask(__name__)



mittaustieto = list()
uusi_mittaus = None
condition = threading.Condition()

@app.route("/", methods =["GET"])
def index():
    return f"mittaustieto:{mittaustieto[-1]}"

@app.route("/lisaa_tieto", methods=["POST"])
def lisaa_tieto():
    vastaanotettu_data = request.get_json(force=True)
    mittaustieto.append(vastaanotettu_data["mittaus"])

    return "200"

@app.route("/stream")
def stream():
    def event_stream():
        while True:
            with condition:
                condition.wait()
                data = uusi:mittaus

            viesti = {
                "mittaus": data
            }           
            yield f"data: {json.dumps(viesti)}\n\n"

    return Response(
        stream_with_context(event_stream()),
        mimetype="text/event-stream",
        headers=(
            "Cache-Control", "no-cache",
            "connection", "keep-alive",
        )
    )

if __name__ == "__main__":
    app.run()