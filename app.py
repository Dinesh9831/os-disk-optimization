from flask import Flask, render_template, request, jsonify

from disk_algo import fcfs, sstf, scan, cscan, look, clook

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    result = None

    if request.method == "POST":


        requests_input = request.form["requests"]
        requests = list(map(int, requests_input.split(",")))

        head = int(request.form["head"])
        disk_size = int(request.form["disk_size"])

        algorithm = request.form["algorithm"]
        direction = request.form["direction"]


        if algorithm == "FCFS":

            seek, sequence = fcfs(requests, head)

        elif algorithm == "SSTF":

            seek, sequence = sstf(requests, head)

        elif algorithm == "SCAN":

            seek, sequence = scan(requests, head, disk_size, direction)

        elif algorithm == "CSCAN":

            seek, sequence = cscan(requests, head, disk_size)

        elif algorithm == "LOOK":

            seek, sequence = look(requests, head, direction)

        elif algorithm == "CLOOK":

            seek, sequence = clook(requests, head)

        else:

            seek = 0
            sequence = []

        avg_seek = round(seek / len(requests), 2)

        starvation_count = 0
        starved_items = []
        starvation_risk = "None"

        if algorithm == "SSTF":
            services = {}
            for idx, step in enumerate(sequence[1:], 1):
                if step in requests and step not in services:
                    services[step] = idx
            
            for i, req in enumerate(requests):
                serviced_idx = services.get(req, 0)
                if serviced_idx - (i + 1) > len(requests) // 2:
                    starvation_count += 1
                    starved_items.append(req)
                    
            if starvation_count > 0:
                starvation_risk = "High"
            else:
                starvation_risk = "Low"
        elif algorithm in ["FCFS", "SCAN", "CSCAN", "LOOK", "CLOOK"]:
            starvation_risk = "None"

        result = {
            "seek": seek,
            "avg_seek": avg_seek,
            "sequence": sequence,
            "starvation_risk": starvation_risk,
            "starved_items": starved_items
        }

        if request.headers.get("Accept") == "application/json":
            return jsonify({
                "result": result
            })

    return render_template(
        "index.html",
        result=result
    )


if __name__ == "__main__":

    app.run(debug=True)
