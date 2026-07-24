import {registry} from "./registry";

export function publish(message:any){

registry.broadcast(message);

}