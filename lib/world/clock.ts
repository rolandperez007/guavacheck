import { WORLD } from "./constants";
import { WorldClock } from "./types";

export function getWorldClock(): WorldClock {

    const now = new Date();

    const hour = now.getHours();

    const minute = now.getMinutes();

    let phase:WorldClock["phase"]="night";

    if(hour>=WORLD.DAY_START && hour<8){

        phase="dawn";

    }else if(hour<13){

        phase="morning";

    }else if(hour<18){

        phase="afternoon";

    }else if(hour<20){

        phase="sunset";

    }else{

        phase="night";

    }

    return{

        hour,

        minute,

        timezone:Intl.DateTimeFormat().resolvedOptions().timeZone,

        phase,

        isDay:phase!=="night"

    }

}