import React, { Component } from 'react'
import Search from "./components/Search"
import Bar from "./components/Bar"

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
      <>
        <Search updateAppState={this.updateAppState} />
        <Bar {...this.state} />
      </>
    )
  }
}
