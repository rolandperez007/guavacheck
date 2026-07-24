import {DomainModule} from "../types";

export class PropertyModule implements DomainModule{

initialize(){

console.log("Property Engine Ready");

}

destroy(){}

handle(message:any){

console.log("Property Event",message);

}

}