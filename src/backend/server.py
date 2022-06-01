from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from backend.lib.convert import convert, getNodes
from backend.lib.node import Node
from backend.lib.dijkstra import Dijkstra

app = Flask(__name__)
CORS(app)
# app.debug = True


@app.route("/data", methods = ['POST'])
def post_data():
  if request.method == 'POST':
    input_data = request.get_json(silent=True)
    file = input_data.get('file')
    option = input_data.get('option')
    source = input_data.get('source')
    destination = input_data.get('destination')
    
    data = {}

    if option.lower() == "check":
      data["nodes"] = getNodes(file)
      data["connections"] = file.replace(" ", "").split("\n")
    else:
      collection = convert(file)
      src_node = Node(source)
      dest_node = Node(destination)
      solver = Dijkstra(collection, src_node, dest_node)

      result, total_cost, iteration, exec_time, steps = solver.solveBerarah()

      data["nodes"] = getNodes(file)
      data["connections"] = file.replace(" ", "").split("\n")
      data["path"] = result
      data["total_cost"] = total_cost
      data["iteration"] = iteration
      data["exec_time"] = exec_time
      data["steps"] = steps

    response = make_response(
      data,
      200
    )
    return response
