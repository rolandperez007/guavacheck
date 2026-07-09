# Installation Guide

Version: 1.0

Status: Living Document

Owner: Guava Inc.

Classification: Developer Guide

---

# Purpose

This guide explains how to install, configure and run the guavacheck platform for local development.

By the end of this guide you should have:

- Frontend running
- Backend running
- Database connected
- Austin online
- Development environment ready

---

# System Requirements

Recommended:

Operating System

- Windows 11
- macOS
- Ubuntu 24.04 LTS

Memory

Minimum:

16 GB RAM

Recommended:

32 GB+

Storage

Minimum:

20 GB Free

Recommended:

100 GB SSD

Internet

Stable broadband connection.

---

# Required Software

Install:

Node.js (LTS)

Git

Python 3.12+

Visual Studio Code

Docker Desktop (Recommended)

---

# Verify Installation

Node

```bash
node -v
```

npm

```bash
npm -v
```

Git

```bash
git --version
```

Python

```bash
python --version
```

---

# Clone Repository

```bash
git clone https://github.com/rolandperez007/guavacheck.git
```

Enter project directory.

```bash
cd guavacheck
```

---

# Install Frontend Dependencies

```bash
npm install
```

This installs:

Next.js

React

TypeScript

Three.js

Supabase SDK

OpenAI SDK

Other project dependencies.

---

# Install Backend Dependencies

Navigate to the backend.

```bash
cd backend
```

Create virtual environment.

Windows

```bash
python -m venv .venv
```

Activate.

PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Install packages.

```bash
pip install -r requirements.txt
```

---

# Configure Environment

Copy:

```
.env.example
```

to

```
.env.local
```

Populate all required variables.

Do not commit secret values.

---

# Configure Supabase

Create a Supabase project.

Obtain:

- Project URL
- Anon Key
- Service Role Key

Populate the environment variables.

Run database migrations before starting the application.

---

# Start Frontend

Return to the project root.

```bash
npm run dev
```

Default URL

```
http://localhost:3000
```

---

# Start Backend

Navigate to the backend.

```bash
uvicorn main:app --reload
```

Default API

```
http://localhost:8000
```

---

# Austin Startup

Austin initializes after:

Configuration

↓

Authentication

↓

Database

↓

Storage

↓

Engine Registry

↓

Monitoring

↓

AI Provider

↓

Scheduler

↓

Platform Ready

Successful initialization reports:

```
Austin Online.
```

---

# Verify Installation

Open:

```
http://localhost:3000
```

Verify:

✓ Homepage loads

✓ Authentication works

✓ Austin available

✓ Database connected

✓ API responding

✓ Storage available

✓ Logs clean

---

# Troubleshooting

## npm install fails

Delete:

```
node_modules
```

Delete:

```
package-lock.json
```

Run:

```bash
npm install
```

---

## Frontend will not start

Verify:

Node version

Dependencies

Environment variables

Port availability

---

## Backend fails

Verify:

Python version

Virtual environment

Dependencies

Database connectivity

---

## Austin Offline

Check:

AI Provider

Environment variables

Backend

Engine Registry

Database

Logs

Austin should never silently fail.

---

# Updating Dependencies

Frontend

```bash
npm update
```

Backend

```bash
pip install -U -r requirements.txt
```

Review release notes before upgrading major dependencies.

---

# Best Practices

Keep dependencies current.

Commit frequently.

Document architectural changes.

Never commit secrets.

Run tests before pushing.

Keep Austin healthy.

---

# Engineering Principle

Every engineer should be able to reproduce the development environment from a clean machine using this guide alone.

---

© 2026 Guava Inc.

Intelligence with integrity.

Technology with purpose.

Trust above everything.