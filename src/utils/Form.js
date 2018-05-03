import React, {Component} from 'react';


const getConfigView=(struct, state, callback)=>{
    return Object.keys(struct).filter((e)=>{
        return struct[e].options;
    }).map((property, index)=>{
        var c=struct[property];
        var options = Object.keys(c.options).map((e)=>{ return { value: c.options[e].name, key: e}});
        var value = state[property];
        var children = [];
        const Input = c.input;
        if (value){
            if (typeof value === "string"){
                var select = c.options[value];
                if (select){
                    if (select.config){
                        children = getConfigView(select.config, state, callback)
                    }
                } else {
                    console.error(value + ' value not found in '+JSON.stringify(c.options));
                }
            } else {
                console.warn('Type \'' + typeof value + '\' value not implemented')
            }
        }
        return <Input key={index} name={c.name} placeholder={c.placeholder} options={options} value={value} callback={(value)=>callback(property, value)} children={children}/>
    })
}

class Form extends Component{
    constructor(props){
        super(props);
        this.state = props.options || {};
        this.changeProperty = this.changeProperty.bind(this);
    }

    changeProperty(property, value){
        let change= {[property]:value};
        if (this.props.onChange){
            const state = Object.assign(this.state, change)
            this.props.onChange(state);
        }
        this.setState(change);
        
    }

    render(){
        return (
            <div className="row">
                {getConfigView(this.props.config, this.state, this.changeProperty)}
            </div>
        )
    }
}

export default Form;