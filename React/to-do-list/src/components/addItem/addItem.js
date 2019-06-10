// addItem.js

import React, { Component } from 'react';

class AddItem extends Component {
    onKeyUp = (target, e) => {
        if (e.keyCode === 13) {
            switch(target) {
                case 'item':
                    this.description.focus();
                    break;
                case 'description':
                    this.time.focus();
                    break;
                case 'time':
                    this.submit.focus();
                    break;
                default:
                    this.item.focus();
            }
        }
    }
    render() {
        return (
            <div className='add_section'>
                
                <label for='item'></label>
                <input
                    type='text'
                    placeholder='Enter item'
                    name='item'
                    onKeyUp={this.onKeyUp.bind(this, 'item')}
                    ref={(input) => {this.item = input; }}
                >
                </input>
                
                <label for='description'></label>
                <input
                    type='text'
                    placeholder='Enter description'
                    name='description'
                    onKeyUp={this.onKeyUp.bind(this, 'description')}
                    ref={(input) => {this.description = input; }}
                >
                </input>
                
                <label for='time'></label>
                <input
                    type='text'
                    placeholder='Enter time'
                    name='time'
                    onKeyUp={this.onKeyUp.bind(this, 'time')}
                    ref={(input) => {this.time = input; }}
                >
                </input>
                
                <label for='submit'>Add Item</label>
                <input
                    type='submit'
                    name='submit'
                    // onClick={() => this.AddItem()}
                    ref={(input) => {this.submit = input}}
                >
                </input>
            </div>
        );
    }
}

export default AddItem;

// This comp needs to update its sibling components props.