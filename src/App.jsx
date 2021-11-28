import React, { Component } from 'react'
import Search from "./components/Search"
import Bar from "./components/Bar"

export default class App extends Component {
  render() {
    return (
      <>
        <Search />
        <Bar />
      </>
    )
  }
}
