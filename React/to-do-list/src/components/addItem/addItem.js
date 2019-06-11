// addItem.js

import React, { Component } from 'react';

// const MyInput = (props) => {
//     return (
//         <input
//             ref={props.inputRef} 
//             type='text'>
//         </input>
//     );
// }

// const FuncCustomComp = () => {
//     let inputRef = null;

//     const   onClick = () => {
//         inputRef.focus();
//     }
//     return (
//         <div>
//             <span>My Input</span>
//             <MyInput
//                 inputRef={(input) => {inputRef = input}} 
//             />
//             <input
//                 onClick={onClick}
//                 value='Submit'
//                 type='submit'>
//             </input>
//         </div>
//     )
// }

class AddItem extends Component {
    constructor(props) {
        super(props);

        this.state = {
            item: '',
            time: '',
            description: ''
        }
    }

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

    handleChange = (e) => {   
        this.setState({ [e.target.id]: e.target.value }); 
    }

    addItem = () => {
        console.log('formData from state:', this.state);
        // send state object to parent comp func to updates its state!
        this.props.updateList(this.state);
    } 

    render() {
        return (
            <div className='add_section'>
                
                {/* <div>
                    <FuncCustomComp/>
                </div> */}

                <label htmlFor='item'></label>
                <input
                    type='text'
                    placeholder='Enter item'
                    id='item'
                    name='item'
                    value={this.state.item}
                    onChange={this.handleChange}
                    onKeyUp={this.onKeyUp.bind(this, 'item')}
                    ref={(input) => {this.item = input; }}>
                </input>
                
                <label htmlFor='description'></label>
                <input
                    type='text'
                    placeholder='Enter description'
                    id='description'
                    name='description'
                    value={this.state.description}
                    onKeyUp={this.onKeyUp.bind(this, 'description')}
                    ref={(input) => {this.description = input; }}>
                </input>
                
                <label htmlFor='time'></label>
                <input
                    type='text'
                    placeholder='Enter time'
                    id='time'
                    name='time'
                    value={this.state.time}
                    onKeyUp={this.onKeyUp.bind(this, 'time')}
                    ref={(input) => {this.time = input; }}>
                </input>
                
                <label htmlFor='submit'>Add Item</label>
                <input
                    type='submit'
                    name='submit'
                    onClick={() => this.AddItem()}
                    ref={(input) => {this.submit = input}}>
                </input>
            </div>
        );
    }
}

export default AddItem;

// This comp needs to update its sibling components props.