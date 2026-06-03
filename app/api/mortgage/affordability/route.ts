import { NextResponse } from 'next/server'
export async function POST(req: Request) {
const { income, debts, rate = 30 } = await req.json()
const disposable = income - debts
const maxMonthly = disposable * (rate / 100)
const estimatedLoan = maxMonthly * 12 * 20
return NextResponse.json({
maxMonthlyPayment: +maxMonthly.toFixed(2),
estimatedLoan: +estimatedLoan.toFixed(2)
})
}