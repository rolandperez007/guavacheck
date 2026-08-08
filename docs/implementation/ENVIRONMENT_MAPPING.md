\# Environment Mapping



> Official infrastructure and deployment architecture defining development, staging, and production environments for Guava.



\---



\# Purpose



This document defines:



\- Where Guava runs

\- How environments communicate

\- Infrastructure ownership

\- Configuration boundaries

\- Deployment workflow



\---



\# Environment Philosophy



Guava uses separate environments.



```

Development



↓



Staging



↓



Production

```



Each environment has:



\- Separate databases

\- Separate secrets

\- Separate storage

\- Separate integrations



\---



\# Environment Overview



```

Developer Machine



↓



Development Environment



↓



Staging Environment



↓



Production Environment

```



\---



\# Development Environment



Purpose:



Local feature development.



Used by:



\- Developers

\- AI engineering

\- Testing



\---



\# Development Stack



```

Frontend



Next.js



↓



Backend



FastAPI



↓



Database



PostgreSQL



↓



Cache



Redis



↓



Workers



RQ / Background Jobs

```



\---



\# Local Repository



Example:



```

guavacheck-clean/

```



Structure:



```

app/



docs/



tests/



scripts/



requirements.txt



.env

```



\---



\# Local Services



Developer runs:



Backend:



```

uvicorn app.main:app --reload

```



Frontend:



```

npm run dev

```



Database:



```

PostgreSQL / Supabase Development

```



Workers:



```

Redis Worker

```



\---



\# Development Database



Purpose:



Feature development.



Contains:



\- Test users

\- Sample properties

\- Mock institutions

\- Synthetic documents



Never contains:



\- Real customer information

\- Real financial records



\---



\# Staging Environment



Purpose:



Production simulation.



Used for:



\- Integration testing

\- Client demonstrations

\- Final validation



\---



\# Staging Architecture



```

Frontend



↓



Vercel Preview



↓



FastAPI Backend



↓



Staging Database



↓



Redis Workers



↓



External Sandbox APIs

```



\---



\# Staging Integrations



Use:



```

Stripe Test Mode



Payment Sandbox



Government Sandbox APIs



Institution Test APIs

```



\---



\# Production Environment



Purpose:



Live Guava platform.



\---



\# Production Architecture



```

Users



↓



Frontend Application



↓



API Layer



↓



Backend Services



↓



Database



↓



Event System



↓



Workers



↓



External Providers

```



\---



\# Frontend Infrastructure



Technology:



```

Next.js



React



Vercel Deployment

```



Responsibilities:



\- User interface

\- Dashboards

\- Austin interface

\- Property visualization



\---



\# Backend Infrastructure



Technology:



```

FastAPI



Python



Uvicorn



Workers

```



Responsibilities:



\- Business logic

\- APIs

\- AI orchestration

\- Integrations



\---



\# Database Infrastructure



Technology:



```

PostgreSQL



Supabase

```



Responsibilities:



\- Persistent data

\- Relationships

\- Transactions



\---



\# Cache Infrastructure



Technology:



```

Redis

```



Responsibilities:



\- Sessions

\- Queues

\- Temporary data

\- Performance optimization



\---



\# Worker Infrastructure



Technology:



```

RQ Workers

```



Responsibilities:



Background tasks:



```

AI rendering



Reports



Notifications



Document processing



Event handling

```



\---



\# Storage Infrastructure



Purpose:



Digital assets.



Stores:



```

Images



Videos



Documents



3D Models



Reports

```



\---



\# Environment Variables



Never commit:



```

.env

```



Contains:



```

DATABASE\_URL



SECRET\_KEY



JWT\_SECRET



OPENAI\_API\_KEY



STRIPE\_SECRET\_KEY



PAYSTACK\_SECRET



REDIS\_URL

```



\---



\# Configuration Ownership



Location:



```

app/config/

```



Files:



```

settings.py



environment.py



logging.py

```



\---



\# Deployment Pipeline



```

Developer



↓



Git Commit



↓



Pull Request



↓



Automated Tests



↓



Staging Deployment



↓



Validation



↓



Production Deployment

```



\---



\# CI/CD Requirements



Every deployment runs:



```

Linting



Unit Tests



Integration Tests



Security Checks



Build Verification

```



\---



\# Monitoring



Production monitoring covers:



\## Application



```

Errors



Latency



Availability

```



\---



\## Database



```

Connections



Queries



Performance

```



\---



\## Infrastructure



```

CPU



Memory



Storage



Workers

```



\---



\# Logging Architecture



Every service produces:



```

Application Logs



Security Logs



Audit Logs



Event Logs

```



\---



\# Backup Strategy



Protected:



```

Database



Documents



Media



Configuration

```



\---



\# Disaster Recovery



Future capability:



```

Database Restore



Storage Recovery



Service Restart



Event Replay

```



\---



\# Scaling Strategy



Initial:



```

Single Backend Instance



Managed Database



Worker Queue

```



Future:



```

Multiple Services



Database Replicas



Distributed Workers



Event Streaming

```



\---



\# External Service Boundary



All external providers connect through:



```

Provider Adapter

```



Examples:



```

Stripe Adapter



Paystack Adapter



AI Provider Adapter



Maps Provider Adapter

```



\---



\# Security Boundary



Production secrets:



```

Secret Manager



Environment Variables



Encrypted Storage

```



Never:



```

Frontend



↓



Secret Credentials

```



\---



\# Final Infrastructure Rule



Development creates.



Staging validates.



Production serves.



Each environment has a clear purpose.



\---



\*\*Environment Mapping\*\*



\*Reliable systems are built on reliable environments.\*

