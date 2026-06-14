import { NextResponse } from "next/server";

export async function GET() {

  const deals = [

    {
      id: "1",
      title: "Luxury Villa",
      location: "Dubai",
      investmentScore: 92,
      distressedScore: 88,
      roi: 14,
      recommendation: "BUY"
    },

    {
      id: "2",
      title: "Residential Block",
      location: "London",
      investmentScore: 74,
      distressedScore: 61,
      roi: 9,
      recommendation: "REVIEW"
    }

  ];

  return NextResponse.json(deals);
}