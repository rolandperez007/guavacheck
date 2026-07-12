-- ==========================================================
-- GUAVACHECK FUNCTIONS
-- ==========================================================

create or replace function update_timestamp()
returns trigger
language plpgsql
as
$$
begin
    NEW.updated_at = now();
    return NEW;
end;
$$;

alter table property_engineering_snapshots
add column if not exists updated_at timestamp default now();

drop trigger if exists trg_property_engineering_snapshots_updated_at
on property_engineering_snapshots;

create trigger trg_property_engineering_snapshots_updated_at
before update
on property_engineering_snapshots
for each row
execute function update_timestamp();