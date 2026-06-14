"use client";
import ROIChart from "@/components/investor/ROIChart";
import { useEffect, useState } from "react";
import ROIChart from "@/components/investor/ROIChart";

interface Deal {
  id: string;
  title: string;
  location: string;
  investmentScore: number;
  distressedScore: number;
  roi: number;
  recommendation: string;
}

export default function InvestorDashboard() {

  const [deals, setDeals] = useState<Deal[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {

    async function loadDeals() {

      try {

        const res = await fetch("/api/investor/deals");

        const data = await res.json();

        setDeals(data || []);

      } catch (err) {

        console.error(err);

      } finally {

        setLoading(false);

      }
    }

    loadDeals();

  }, []);

  return (

    <main className="p-6">

      <h1 className="text-3xl font-bold mb-6">
        Investor Dashboard
      </h1>

      <div className="grid md:grid-cols-4 gap-4 mb-8">

        <div className="border rounded-xl p-4">
          <h3>Total Deals</h3>
          <p className="text-2xl font-bold">
            {deals.length}
          </p>
        </div>

        <div className="border rounded-xl p-4">
          <h3>Hot Deals</h3>
          <p className="text-2xl font-bold">
            {
              deals.filter(
                d => d.recommendation === "BUY"
              ).length
            }
          </p>
        </div>

        <div className="border rounded-xl p-4">
          <h3>Average ROI</h3>
          <p className="text-2xl font-bold">
            {
              deals.length
                ? Math.round(
                    deals.reduce(
                      (a,b)=>a+b.roi,0
                    ) / deals.length
                  )
                : 0
            }%
          </p>
        </div>

        <div className="border rounded-xl p-4">
          <h3>Portfolio Score</h3>
          <p className="text-2xl font-bold">
            {
              deals.length
                ? Math.round(
                    deals.reduce(
                      (a,b)=>a+b.investmentScore,0
                    ) / deals.length
                  )
                : 0
            }
          </p>
        </div>

      </div>

      {loading ? (

        <p>Loading...</p>

      ) : (

        <div className="space-y-4">

          {deals.map(deal => (

            <div
              key={deal.id}
              className="border rounded-xl p-4"
            >

              <h2 className="font-bold text-xl">
                {deal.title}
              </h2>

              <p>{deal.location}</p>

              <div className="grid md:grid-cols-4 gap-4 mt-4">

                <div>
                  Investment Score
                  <br />
                  <strong>
                    {deal.investmentScore}
                  </strong>
                </div>

                <div>
                  Distressed Score
                  <br />
                  <strong>
                    {deal.distressedScore}
                  </strong>
                </div>

                <div>
                  ROI
                  <br />
                  <strong>
                    {deal.roi}%
                  </strong>
                </div>

                <div>
                  Recommendation
                  <br />
                  <strong>
                    {deal.recommendation}
                  </strong>
                </div>

              </div>

            </div>

          ))}

        </div>

      )}

    </main>
  );
}
<ROIChart data={deals} />