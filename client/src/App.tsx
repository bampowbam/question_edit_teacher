import React, { Component, useEffect, useState } from 'react';
import './App.css';
import ApolloClient from 'apollo-boost';
import { responsePathAsArray } from 'graphql';
import { QuestionEdit } from './components/QuestionEdit';
import { Content, Layout } from 'react-mdl'
import { Route, RouteComponentProps, Router, Link, Switch } from 'react-router-dom';
import PageNotFound from './components/PageNotFound';
import {QuestionTable} from './components/QuestionTable';

function App() {

  const [questions, setQuestions] = useState()

  useEffect(() => {
    fetch('/get-question').then(response =>
      response.json().then(data => {
        console.log(data)
        setQuestions(data)
      })
    )
  }, [])

  console.log(questions)

  if (questions === undefined) {
    return (
      <div className="App">
      </div>
    );
  }
  if (questions !== undefined) {
    return (
        <div>
          <Layout>
            <Content>
              <div />
              <Switch>
                <Route path="/"
                  component={() => <QuestionTable rows={questions} />} exact />
                <Route path={"/Question/"} component={QuestionEdit} />
                <Route component={PageNotFound} />
              </Switch>
            </Content>
          </Layout>
        </div>
    )
  }
}

export default App;
