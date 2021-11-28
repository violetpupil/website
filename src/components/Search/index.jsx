import React, { Component } from 'react'

export default class Search extends Component {
  inputRef = React.createRef()

  search = async () => {
    const res = await fetch(`/popular?q=${this.inputRef.current.value}`)
    this.props.updateAppState({ bar: await res.text() })
  }

  render() {
    return (
      <div>
        <input ref={this.inputRef} type="text"></input>
        <button onClick={this.search} >search</button>
      </div>
    )
  }
}
