// home.js

import React, { Component } from 'react';
import PropTypes from 'prop-types';
import List from '../../components/list';
import AddItem from '../../components/addItem';


const Home = () => {
    return (
        <>
            <AddItem/>
            <List/>
        </>
    )
}

export default Home;
