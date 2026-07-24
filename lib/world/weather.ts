import { WeatherState } from "./types";

export function getWeather():WeatherState{

    return{

        condition:"clear",

        temperature:27,

        humidity:72,

        windSpeed:6

    }

}