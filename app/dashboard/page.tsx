import HeroCard from "@/components/dashboard/cards/HeroCard";
import MissionControl from "@/components/dashboard/mission/MissionControl";
import IntelligenceWall from "@/components/dashboard/intelligence/IntelligenceWall";
import OpportunityFeed from "@/components/dashboard/ai/OpportunityFeed";
import AustinPanel from "@/components/dashboard/ai/AustinPanel";
import MarketPulse from "@/components/dashboard/market/MarketPulse";
import PortfolioSummary from "@/components/dashboard/portfolio/PortfolioSummary";
import ActivityFeed from "@/components/dashboard/activity/ActivityFeed";
import DashboardShell from "@/components/dashboard/common/DashboardShell";

export default function DashboardPage() {

return(

<DashboardShell>

<div className="space-y-8">

<HeroCard/>

<div className="grid gap-8 xl:grid-cols-3">

<div className="xl:col-span-2">

<MissionControl/>

</div>

<AustinPanel/>

</div>

<IntelligenceWall/>

<div className="grid gap-8 xl:grid-cols-2">

<MarketPulse/>

<OpportunityFeed/>

</div>

<div className="grid gap-8 xl:grid-cols-2">

<ActivityFeed/>

<PortfolioSummary/>

</div>

</div>

</DashboardShell>

)

}