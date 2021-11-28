import React, { Component } from 'react'

export default class Bar extends Component {
  render() {
    const { bar } = this.props
    return <div dangerouslySetInnerHTML={{ __html: bar }} />
  }
}
