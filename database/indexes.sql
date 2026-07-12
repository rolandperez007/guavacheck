-- ==========================================================
-- INDEXES
-- ==========================================================

create index if not exists idx_engineering_property
on property_engineering_snapshots(property_id);

create index if not exists idx_engineering_created_at
on property_engineering_snapshots(created_at desc);

create index if not exists idx_engineering_version
on property_engineering_snapshots(simulation_version);