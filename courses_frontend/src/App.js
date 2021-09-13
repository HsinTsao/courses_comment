import Appbar from './components/Appbar';
// packages
import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  // Link,
} from 'react-router-dom';
import clsx from 'clsx';
import { makeStyles } from '@material-ui/core/styles';
import Home from './pages/Home';

const drawerWidth = 240;

const useStyles = makeStyles((theme) => ({
  drawerHeader: {
    display: 'flex',
    alignItems: 'center',
    padding: theme.spacing(0, 1),
    ...theme.mixins.toolbar,
    justifyContent: 'flex-end',
  },
  content: {
    flexGrow: 1,
    padding: theme.spacing(1),
    transition: theme.transitions.create('margin', {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
    marginLeft: 0,
  },
  contentShift: {
    transition: theme.transitions.create('margin', {
      easing: theme.transitions.easing.easeOut,
      duration: theme.transitions.duration.enteringScreen,
    }),
    marginLeft: drawerWidth,
  },
}))

function App() {
  const classes = useStyles();
  const [open, setOpen] = React.useState(false);

  const handleDrawerOpen = () => {
    setOpen(true);
  };

  const handleDrawerClose = () => {
    setOpen(false);
  };

  return (
    <div>
      <Router>
        <Appbar open={open} handleDrawerOpen={handleDrawerOpen} handleDrawerClose={handleDrawerClose}/>
        <main
        className={clsx(classes.content, {
          [classes.contentShift]: open,
        })}
      >
        <div className={classes.drawerHeader} />
        {/* <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/login">Login</Link>
          </li>
          <li>
            <Link to="/register">Register</Link>
          </li>
        </ul> */}
        <Switch>
            <Route exact path='/' component={Home}>
            </Route>
            <Route path='/login'>
              <h1>Login</h1>
            </Route>
            <Route path='/register'>
              <h1>Register</h1>
            </Route>
            <Route path='/about'>
              <h1>About</h1>
            </Route>
          </Switch>
      </main>
      </Router>
    </div>
  );
}

export default App;
