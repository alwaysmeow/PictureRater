from flask import Flask, render_template, request, Response
import os
import csv

app = Flask(__name__)

@app.route('/<id>')
def mainPage(id):
    return render_template("index.html", id=id)

@app.route('/mark', methods=["POST"])
def setMark():
    data = request.get_json()
    mark = data["mark"]
    id = data["id"]

    with open("markup.csv", 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        data = list(csvreader)
    
    for row in data:
        if row[0] == f"{id}.jpeg":
            row[1] = mark
            break
    
    with open("markup.csv", 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(data)

    return Response(status=200)

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)