import { NextResponse } from 'next/server'
import { createClient } from '@supabase/supabase-js'
const supabase = createClient(
process.env.NEXT_PUBLIC_SUPABASE_URL!,
process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
)
export async function GET(req: Request) {
const { searchParams } = new URL(req.url)
const city = searchParams.get('city')
const min = searchParams.get('min')
const max = searchParams.get('max')
let query = supabase.from('properties').select('*')
if (city) query = query.eq('city', city)
if (min) query = query.gte('price', Number(min))
if (max) query = query.lte('price', Number(max))
const { data, error } = await query
if (error) {
return NextResponse.json({ error: error.message }, { status: 500 })
}
return NextResponse.json({ data })
}






