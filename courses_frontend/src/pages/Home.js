import React from 'react';
import { Button } from '@material-ui/core';

const Home = () => {
  const handleClick = () => {
    fetch('http://127.0.0.1:8080/auth/users/', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      }
    }).then((res) => {
      if (res.status === 200) {
        console.log(res.json());
      }
      else return Promise.reject(res);
    }).catch((err) => {
      return Promise.reject(err);
    });
  }

  return (
    <div>
      <Button onClick={handleClick}>Test</Button>
    </div>
  )
};

export default Home;