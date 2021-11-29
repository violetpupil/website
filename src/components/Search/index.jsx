import React, { Component } from 'react'

export default class Search extends Component {
  inputRef = React.createRef()

  search = async () => {
    const keyword = this.inputRef.current.value
    this.props.updateAppState({ isFirst: false, isLoading: true })

    let res
    let text
    try {
      res = await fetch(`/popular?q=${keyword}`)
      text = await res.text()
    } catch (e) {
      this.props.updateAppState({ isLoading: false, bar: "", err: e.message })
      return
    }

    if (res.ok === false)
      this.props.updateAppState({ isLoading: false, bar: "", err: `${res.status} ${res.statusText} ${text}` })
    else
      this.props.updateAppState({ isLoading: false, bar: text, err: "" })
  }

  render() {
    return (
      <div>
        <input ref={this.inputRef} type="text" />
        <button onClick={this.search} >search</button>
      </div>
    )
  }
}
