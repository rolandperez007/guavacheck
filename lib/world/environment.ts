import { getWeather } from "./weather";
import { getWorldClock } from "./clock";

export function getEnvironment(){

    return{

        clock:getWorldClock(),

        weather:getWeather()

    }

}