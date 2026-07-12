-- ==========================================================
-- ROW LEVEL SECURITY
-- ==========================================================

alter table property_engineering_snapshots
enable row level security;

create policy "Authenticated users can read engineering snapshots"

on property_engineering_snapshots

for select

to authenticated

using (true);

create policy "Authenticated users can insert engineering snapshots"

on property_engineering_snapshots

for insert

to authenticated

with check (true);

create policy "Authenticated users can update engineering snapshots"

on property_engineering_snapshots

for update

to authenticated

using (true);