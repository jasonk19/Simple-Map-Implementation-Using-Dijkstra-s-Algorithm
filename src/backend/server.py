from flask import Flask, jsonify, request, make_response
from backend.lib.convert import convert
from backend.lib.node import Node
from backend.lib.dijkstra import Dijkstra

app = Flask(__name__)
app.debug = True

@app.route("/data", methods = ['POST'])
def post_data():
  if request.method == 'POST':
    file = request.form.get('file')
    source = request.form.get('source')
    destination = request.form.get('destination')

    data = {}
    collection = convert(file)
    src_node = Node(source)
    dest_node = Node(destination)
    solver = Dijkstra(collection, src_node, dest_node)

    result, total_cost = solver.solveDuaArah()

    data["connections"] = file.replace(" ", "").split("\n")
    data["result"] = result
    data["total_cost"] = total_cost

    response = make_response(
      data,
      200
    )

    return response
