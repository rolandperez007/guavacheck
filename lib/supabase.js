import { createClient } from '@supabase/supabase-js'

const supabaseUrl = 'https://gxrslgddffdslvmemtqa.supabase.co'
const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imd4cnNsZ2RkZmZkc2x2bWVtdHFhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQ5ODUwMTEsImV4cCI6MjA5MDU2MTAxMX0.hJ4w6e5TgkkkF3QuRcGpIwG0cyMMCj1xImzJ-J-Bz2M'

export const supabase = createClient(
  supabaseUrl,
  supabaseKey
)