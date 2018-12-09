import * as React from "react/cjs/react.development";
import './ZipCodeForm.css';

export default class ZipCodeForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {value: ''};
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(e) {
        const re = /^[0-9\b]+$/;

        // if value is not blank, then test the regex

        if (e.target.value === '' || re.test(e.target.value) && e.target.value.length < 6) {
            this.setState({value: e.target.value})
        }
    }

    handleSubmit(event) {
        console.log('Zip Code: ' + this.state.value);
        event.preventDefault();
    }

    render() {
        return (
            <div className='zip-code-form'>
                <form onSubmit={this.handleSubmit}>
                    <label>
                        <input type="text" value={this.state.value} onChange={this.handleChange} />
                        <input type="submit" value="Submit" className={'btn'}/>
                    </label>
                </form>
            </div>
        );
    }
}
