import React from 'react';
import {Switch, Route} from 'react-router-dom';
import { QuestionEdit } from './components/QuestionEdit';
import { QuestionTable } from './components/QuestionTable';


const Routes = () => {
   return <Switch>
        <Route exact path="/" component={QuestionTable} />
        <Route exact path="/Question/" component={QuestionEdit} />
    </Switch>
}

export default Routes;