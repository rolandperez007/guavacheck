-- =========================
-- EXTENSIONS
-- =========================
create extension if not exists pgcrypto;

-- =========================
-- USERS
-- =========================
create table if not exists users (
    id uuid primary key default gen_random_uuid(),
    email text unique,
    full_name text,
    phone text,
    country text,
    city text,
    preferred_currency text default 'USD',
    preferred_language text default 'en',
    timezone text,
    created_at timestamp default now(),
    updated_at timestamp default now()
);

-- =========================
-- CONVERSATIONS
-- =========================
create table if not exists conversations (
    id uuid primary key default gen_random_uuid(),
    user_id uuid references users(id) on delete cascade,
    title text,
    created_at timestamp default now(),
    updated_at timestamp default now()
);

-- =========================
-- MESSAGES
-- =========================
create table if not exists messages (
    id uuid primary key default gen_random_uuid(),
    conversation_id uuid references conversations(id) on delete cascade,
    role text check (role in ('user', 'assistant', 'system')),
    content text,
    created_at timestamp default now()
);

-- =========================
-- EXCHANGE RATES
-- =========================
create table if not exists exchange_rates (
    id uuid primary key default gen_random_uuid(),
    base_currency text default 'USD',
    currency text,
    rate_to_usd numeric,
    source text,
    fetched_at timestamp default now()
);

-- =========================
-- BUDGETS
-- =========================
create table if not exists budgets (
    id uuid primary key default gen_random_uuid(),
    user_id uuid references users(id) on delete cascade,
    original_amount numeric,
    original_currency text,
    normalized_amount numeric,
    normalized_currency text default 'USD',
    exchange_rate numeric,
    created_at timestamp default now()
);

-- =========================
-- PROPERTIES
-- =========================
create table if not exists properties (
    id uuid primary key default gen_random_uuid(),
    user_id uuid references users(id) on delete cascade,

    title text,
    description text,

    property_type text,
    bedrooms int,
    bathrooms int,

    price numeric,
    currency text,
    normalized_price numeric,

    country text,
    state text,
    city text,
    address text,

    latitude double precision,
    longitude double precision,

    status text default 'active',

    created_at timestamp default now(),
    updated_at timestamp default now()
);