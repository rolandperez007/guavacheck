-- ==========================================================
-- GUAVACHECK DATABASE SCHEMA
-- ==========================================================

create extension if not exists pgcrypto;

-- ==========================================================
-- PROPERTY ENGINEERING SNAPSHOTS
-- ==========================================================

create table if not exists property_engineering_snapshots (

    id uuid primary key default gen_random_uuid(),

    property_id uuid not null references properties(id) on delete cascade,

    simulation_version text not null default 'v1',

    location_snapshot jsonb not null,

    engineering_snapshot jsonb,

    design_snapshot jsonb,

    cost_snapshot jsonb,

    blueprint_snapshot jsonb,

    metadata jsonb default '{}'::jsonb,

    created_at timestamptz not null default now(),

    updated_at timestamptz not null default now()

);