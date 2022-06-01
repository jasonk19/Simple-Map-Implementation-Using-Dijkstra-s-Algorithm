import "./App.css"
import React, { useState, createRef } from 'react'
import axios from 'axios'
import Graph from 'react-graph-vis'
import { v4 as uuidv4 } from "uuid"
import { cloneDeep } from "lodash"

const init_graph = {
  nodes: [
    { id: 1, label: 'Empty'},
    { id: 2, label: 'Node'},
  ],
  edges: [
    { from: 1, to: 2 },
  ]
}

function App() {
  const [graphData, setGraphData] = useState(init_graph)
  const options = {
    layout: {
      hierarchical: false
    },
    edges: {
      color: "#000000"
    },
    height: "470px"
  };
  const [data, setData] = useState({
    file: '',
    option: '',
    source: '',
    destination: ''
  })
  const [result, setResult] = useState({})

  const inputFile = createRef()

  const handleFileChange = (e) => {
    setData({
      ...data,
      file: ''
    })
    const reader = new FileReader()
    reader.onload = (e) => {
      const text = e.target.result;
      setData({
        ...data,
        file: text
      })
    }
    reader.readAsText(inputFile.current.files[0])
  }

  const handlePointChange = (e) => {
    const value = e.target.value;
    setData({
      ...data,
      [e.target.name]: value.toUpperCase()
    })
  }

  const handleCheck = async (e) => {
    e.preventDefault()
    data.option = 'check'
    console.log(data)
    await axios.post("http://localhost:5000/data", data).then(res => {
      console.log(res.data)
      setResult(res.data)
      const new_graph = {
        nodes: res.data.nodes.map(node => ({
          id: node,
          label: node,
          color: "#add8e6"
        })),
        edges: res.data.connections.map(connection => ({
          from: connection[0],
          to: connection[1],
          label: connection[2]
        }))
      }
      setGraphData(new_graph)
    })
  }
  const handleSolve = async (e) => {
    e.preventDefault()
    data.option = 'solve'
    await axios.post("http://localhost:5000/data", data).then(res => {
      console.log(res.data)
      setResult(res.data)
      let updateGraph = cloneDeep(graphData)
      for (let i = 0; i < res.data.path.length; i++) {
        for (let j = 0; j < updateGraph.nodes.length; j++) {
          if (res.data.path[i] === updateGraph.nodes[j].id) {
            updateGraph.nodes[j].color = "#ffcccb"
          }
        }
        for (let k = 0; k < updateGraph.edges.length; k++) {
          if ((res.data.path[i] === updateGraph.edges[k].from && res.data.path[i+1] === updateGraph.edges[k].to) || (res.data.path[i] === updateGraph.edges[k].to && res.data.path[i+1] === updateGraph.edges[k].from)) {
            updateGraph.edges[k].color = "red"
          }
        }
      }
      setGraphData(updateGraph)
    })
  }
  return (
    <div className="App">
      <h1>Simple Map Pathfinder</h1>
      <h3>Dijkstra's Algorithm</h3>
      <div className="container">
        <div className="input">
          <form>
            <div className="main-input">
              <label>Input File</label>
              <input type="file" ref={inputFile} onChange={handleFileChange}></input>
              <label>Pick starting point</label>
              <input type="text" name="source" value={data.source} onChange={handlePointChange} placeholder="Starting point" />
              <label>Pick destination point</label>
              <input type="text" name="destination" value={data.destination} onChange={handlePointChange} placeholder="Destination point" />
              <button className="check" onClick={handleCheck}>Check</button>
              <button className="solve" onClick={handleSolve}>Solve</button>
            </div>
              <div className="info">
                <p>Total Cost: {result.total_cost}</p>
                <p>Total Iteration: {result.iteration}</p>
                <p>Execution Time: {result.exec_time} seconds</p>
                <p>Steps:</p>
                <p>{result.steps}</p>
              </div>
          </form>
        </div>
        <div className="result">
          <div className="graph">
          </div>
          <div className="cost">
            <Graph key={uuidv4} graph={graphData} options={options} />
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
