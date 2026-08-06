import { NextResponse } from "next/server";
export async function POST(req: Request) {
  const { principal, annual_rate, years } = await req.json();
  const r = annual_rate / 100 / 12;
  const n = years * 12;
  const m = (principal * r * Math.pow(1 + r, n)) / (Math.pow(1 + r, n) - 1);
  return NextResponse.json({
    monthlyPayment: +m.toFixed(2),
    totalPayment: +(m * n).toFixed(2),
    totalInterest: +(m * n - principal).toFixed(2),
  });
}
