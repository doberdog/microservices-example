import * as React from "react/cjs/react.development";
import './ZipCodeForm.css';

export default class ZipCodeForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {value: ''};
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    static isValidZipCode(e)  {
        const re = /^[0-9\b]+$/;
        return (e.target.value === '' || re.test(e.target.value))
            && e.target.value.length < 6
    }

    handleChange(e) {
        if (ZipCodeForm.isValidZipCode(e)) {
            this.setState({value: e.target.value})
        }
    }

    state = {
        response: '',
        post: '',
        responseToPost: '',
    };

    componentDidMount() {
        this.callApi()
            .then(res => this.setState({ response: res.express }))
            .catch(err => console.log(err));
    }

    callApi = async () => {
        const response = await fetch('/api/hello');
        const body = await response.json();
        if (response.status !== 200) throw Error(body.message);
        return body;
    };

    handleSubmit = async e => {
        console.log(this.state);
        e.preventDefault();
        const response = await fetch('/api/weather/', {  // add zip code as req param
            method: 'GET',
        });
        const body = await response.text();
        this.setState({ responseToPost: body });
    };

    render() {
        return (
            <div className='zip-code-form'>
                <label>
                    <input type="text" value={this.state.value} onChange={this.handleChange} />
                    <div className={'btn'} onClick={this.handleSubmit}>Submit</div>
                </label>
            </div>
        );
    }
}
