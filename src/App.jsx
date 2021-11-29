import React, { Component } from 'react'
import Bar from "./components/Bar"
import Search from "./components/Search"
import "./App.css"

export default class App extends Component {
  state = {
    bar: "",
    isFirst: true,
    isLoading: false,
    err: ""
  }

  updateAppState = state => this.setState(state)

  render() {
    return (
      <div id="app">
        <Search updateAppState={this.updateAppState} />
        <Bar {...this.state} />
      </div>
    )
  }
}
