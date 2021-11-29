import React, { Component } from 'react'

export default class Bar extends Component {
  render() {
    const { bar, isFirst, isLoading, err } = this.props
    return (
      <div>
        {
          isFirst ? "" :
            isLoading ? <h2>Loading......</h2> :
              err ? <h2>{err}</h2> :
                <div dangerouslySetInnerHTML={{ __html: bar }} />
        }
      </div>
    )
  }
}
