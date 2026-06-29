import { SupportLevel } from "./types";

export const SupportNames: Record<SupportLevel,string>={

    [SupportLevel.NONE]:"None",

    [SupportLevel.GLOBAL_AI]:"Global AI",

    [SupportLevel.BASIC]:"Basic",

    [SupportLevel.DEVELOPING]:"Developing",

    [SupportLevel.GROWING]:"Growing",

    [SupportLevel.ADVANCED]:"Advanced",

    [SupportLevel.VERIFIED]:"Verified",

    [SupportLevel.ENTERPRISE]:"Enterprise",

    [SupportLevel.NATIONAL]:"National",

    [SupportLevel.PREMIUM]:"Premium",

    [SupportLevel.COMPLETE]:"Complete"

};