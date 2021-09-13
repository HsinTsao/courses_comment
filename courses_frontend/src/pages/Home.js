import React from 'react';

// packages
import { makeStyles } from '@material-ui/core/styles';
import 
{ Typography,
  Paper,
  Grid,
  Card,
  CardActionArea,
  CardContent,
  CardActions,
  IconButton,
  Badge,
}from '@material-ui/core';

// icon
import ChatIcon from '@material-ui/icons/Chat';
import ThumbsUpDownIcon from '@material-ui/icons/ThumbsUpDown';

import { Link } from 'react-router-dom';

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
    margin: theme.spacing(2),
    minHeight: '85vh',
  },
  topPaper: {
    margin: theme.spacing(0, 0, 2),
    padding: theme.spacing(2),
  },
  paper: {
    padding: theme.spacing(2),
    display: 'inline-block',
    minWidth: '97.5%',
    // textAlign: 'center',
    // height: '100%'
  },
  card: {
    margin: theme.spacing(1, 2),
    minWidth: '30%',
    display: 'inline-block',
  }
}));

// test data for courese
const courses = [
  {
    name: 'COMP9021',
    intro: 'Principle of Program Learning',
    comment: 4,
    thumbs: 11
  },
  {
    name: 'COMP9333',
    intro: 'Principle of Program Learning',
    comment: 5,
    thumbs: 5
  },
  {
    name: 'COMP9044',
    intro: 'Principle of Program Learning',
    comment: 8,
    thumbs: 6
  },
  {
    name: 'COMP9444',
    intro: 'Principle of Program Learning',
    comment: 0,
    thumbs: -2
  },
]

const Home = () => {
  const classes = useStyles();
  
  return (
    <div className={classes.root}>
      <Grid container>
        <Grid item xs={12}>
          <Paper className={classes.topPaper} elevation={2}>
            <Typography variant='h4'>CSE Postgraduate Coursework</Typography>
            <Link to='/about'>About</Link>
          </Paper>
          <Paper className={classes.paper} elevation={2}>
            {/* todo: 
                1- card should be written as a component
                2- paper height need to be set
            */}
            {courses.map((course, idx) => (
              <Card className={classes.card} key={idx} variant='outlined'>
                <CardActionArea>
                  <CardContent>
                    <Typography variant="h6">{course.name}</Typography>
                    <Typography variant="body2" color='textSecondary'>{course.intro}</Typography>
                  </CardContent>
                </CardActionArea>
                <CardActions>
                <IconButton aria-label="show 4 new mails">
                  <Badge badgeContent={course.comment} color="secondary">
                    <ChatIcon fontSize='small' />
                  </Badge>
                </IconButton>
                <IconButton aria-label="show 11 new notifications">
                  <Badge badgeContent={course.thumbs} color="secondary">
                    <ThumbsUpDownIcon fontSize='small' />
                  </Badge>
                </IconButton>
                </CardActions>
              </Card>
            ))}
          </Paper>
        </Grid>
      </Grid>
    </div>
  )
};

export default Home;