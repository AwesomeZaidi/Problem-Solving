import React, { Component } from 'react';
import '../../styles/home.scss';

class List extends Component {
    constructor(props) {
        super(props);
        
        this.state = {
            numberSelected: 0,
            animals: ['dog', 'cat', 'bad apple']
        }
    }

    componentDidMount = () => {
        //  {dog: false, cat: false, apple: true}
        let newAnimals = {}
        this.state.animals.forEach((animal, _) => {
            console.log('animal');
            newAnimals[animal] = false
        })
        console.log('newAnimals:', newAnimals);
        
        this.setState = ({
            animals: newAnimals
        })
    }

    updateDict = (e, animal) => {
        console.log('animal:', animal);
        
        console.log('here');
        
        let newAnimals = this.state.animals;
        console.log('updateDict newAnimals:', this.state.animals);
        
        newAnimals[animal] = !this.state.animals[animal];
        // console.log('newAnimals:', newAnimals);
        
        this.setState = ({
            animals: newAnimals
        });
        this.props.updateCount(e.target.checked);
    }

    render() {
        console.log('this.state.animals:', this.state.animals);
        
        return (
            <div>
                <ul className='list'>
                    {this.state.animals.map((animal, index) => {
                        return (
                            <div key={index}>
                                <label>{animal}</label>
                                <input onClick={(e) => this.updateDict(e, animal)} type='checkbox' value={animal}></input>
                            </div>
                        )
                    })
                    }
                </ul>
            </div>
        );
    }
}

export default List;

// map creates new array, for each modifies the original array!
