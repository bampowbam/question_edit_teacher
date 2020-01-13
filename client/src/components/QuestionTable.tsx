import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import PropTypes from "prop-types";
import {Navigation} from 'react-mdl'
import { Switch, Route, Link } from 'react-router-dom'
import { QuestionEdit } from './QuestionEdit';

const useStyles = makeStyles({
  table: {
    minWidth: 650,
  },
});

interface Props {
  rows: Array<{
    id: number;
    library: string;
    reviewed: string;
    title: string;
    type: string;
    visibility: string;
  }>;
}

function createQuestionRoute(id: any) {
  return (
    <div>
      <Switch>
        <Route path={`/question/` + id} component={QuestionEdit} />
      </Switch>
    </div>
  )
}

export function QuestionTable({ rows }: Props) {
  return (
    <Paper>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>Id</TableCell>
            <TableCell>Reviewed</TableCell>
            <TableCell>Title</TableCell>
            <TableCell>Library</TableCell>
            <TableCell>Visibility</TableCell>
            <TableCell>Type</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map(row => (
            <TableRow key={row.id}>
              <TableCell>{row.id}</TableCell>
              <TableCell>{row.reviewed}</TableCell>
              <TableCell>
              {createQuestionRoute(row.id)}
              <Navigation>
                <Link to={`/question/` + row.id}>
                  {row.title}
                </Link>
              </Navigation>
              </TableCell>
              <TableCell>{row.library}</TableCell>
              <TableCell>{row.visibility}</TableCell>
              <TableCell>{row.type}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </Paper>
  );
}

