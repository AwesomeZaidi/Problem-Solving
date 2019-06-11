import React, { Component } from 'react';
import List from '../list';
import '../../styles/home.scss';

class Selector extends Component {
    constructor(props) {
        super(props);

        this.state = {
            show: false,
            selected: 0,
        }
    }

    show = () => {
        this.setState({
            show: !this.state.show
        })
    }

    updateCount = (updateValue) => {
        if (updateValue) {
            this.setState({
                selected: this.state.selected + 1
            })
        } else {
            this.setState({
                selected: this.state.selected - 1
            })
        }
    }



    render() {
        return (
            <div>
                <div onClick={() => this.show()} className='selector'>{this.state.selected} Selected</div>
                { this.state.show ? <List updateCount={this.updateCount}/> : null }
            </div>
        );
    }
}

export default Selector;

// Uppercase letter in classname differentites from jsx elements.