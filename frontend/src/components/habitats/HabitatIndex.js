import React from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'


class HabitatIndex extends React.Component {
  constructor(){
    super()

    this.state = {
      habitats: null
    }
  }

  componentDidMount() {
    axios.get('/api/habitats')
      .then(res => this.setState({ habitats: res.data }))
      .catch(err => console.log(err))
  }
  
  render() {
    console.log(this.state)
    const { habitats } = this.state
    if (!habitats) return null
    return (
      <div className="habitat-index">

        <div className="habitat-index-banner"></div>

        <div className="habitat-index-content-container">
          <div className="habitat-index-heading">
            <h1>Habitats</h1>
          </div>
          <div  className="habitat-index-card-container">
            <div className="habitat-index-card-row">
              {habitats.map(habitat =>
                <Link to={`/habitats/${habitat.id}`} key={habitat.id} className="habitat-index-card">{habitat.name}</Link>
              )}
            </div>
            <div className="habitat-index-card-row">
              {habitats.map(habitat =>
                <Link to={`/habitats/${habitat.id}`} key={habitat.id} className="habitat-index-card">{habitat.name}</Link>
              )}
            </div>
            <div className="habitat-index-card-row">
              {habitats.map(habitat =>
                <Link to={`/habitats/${habitat.id}`} key={habitat.id} className="habitat-index-card">{habitat.name}</Link>
              )}
            </div>
            <div className="habitat-index-card-row">
              {habitats.map(habitat =>
                <Link to={`/habitats/${habitat.id}`} key={habitat.id} className="habitat-index-card">{habitat.name}</Link>
              )}
            </div>
            <div className="habitat-index-card-row">
              {habitats.map(habitat =>
                <Link to={`/habitats/${habitat.id}`} key={habitat.id} className="habitat-index-card">{habitat.name}</Link>
              )}
            </div>
          </div>
        </div>

      </div>
    )
  }
}

export default HabitatIndex

// habitat show page
{/* <div>
        <h1>Habitat Show Page</h1>
        <div className="habitat-show-bkg-top"></div>
        <div className="habitat-show-bkg-bottom"></div>
      </div> */}