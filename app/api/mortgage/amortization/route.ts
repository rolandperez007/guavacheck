import { NextResponse } from 'next/server'
export async function POST(req: Request) {
const { principal, annual_rate, years } = await req.json()
const r = annual_rate / 100 / 12
const n = years * 12
let balance = principal
const schedule = []
const payment = (principal * r * Math.pow(1 + r, n)) /
(Math.pow(1 + r, n) - 1)
for (let i = 1; i <= n; i++) {
const interest = balance * r
const principalPaid = payment - interest
balance -= principalPaid
schedule.push({
month: i,
payment: +payment.toFixed(2),
principal: +principalPaid.toFixed(2),
interest: +interest.toFixed(2),
balance: +Math.max(balance, 0).toFixed(2)
})
}