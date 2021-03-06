import * as React from 'react'
import * as ReactDOM from 'react-dom'
import { Route, BrowserRouter } from 'react-router-dom'
import styled from 'styled-components'

import { Home } from './home'
import { Results } from './results'
import kLogoPath from './logo.png'

const Logo = styled.img`
    height: 1em;
    margin-right: 8px;
`

const NoUnderline = styled.a`
    text-decoration: none;
`

const App = () => {
    return <React.Fragment>
        <NoUnderline href="/">
            <h1>
                <Logo src={kLogoPath} />
                Cheat Sheet
            </h1>
        </NoUnderline>
        <BrowserRouter>
            <div>
                <Route exact path="/" render={() => <Home />} />
                <Route path="/search/:user/:repo" render={({ match }) => <Results repo={match.params.user + "/" + match.params.repo} />} />
            </div>
        </BrowserRouter>
    </React.Fragment>
}

window.addEventListener('load', () => {
    ReactDOM.render(<App />, document.getElementById("main"));
});