\# Folder Structure



> Official production repository structure for Guava backend implementation.



\---



\# Purpose



This document defines the physical location of every backend component.



The goal:



\- Every feature has a home

\- Every file has ownership

\- Developers know where code belongs

\- Architecture maps directly to folders



\---



\# Root Structure



```

app/



├── api/

├── auth/

├── users/

├── identity/

├── permissions/

├── security/

│

├── austin/

│

├── property/

├── registry/

├── verification/

├── passport/

│

├── construction/

├── cost/

├── mortgage/

├── investor/

│

├── digital\_twin/

├── vision/

├── world/

├── geo/

├── maps/

│

├── marketplace/

├── commerce/

├── contractors/

│

├── institutions/

├── government/

│

├── community/

├── messaging/

├── notifications/

│

├── documents/

├── storage/

│

├── workflow/

├── events/

├── jobs/

│

├── billing/

├── payments/

│

├── database/

├── middleware/

├── config/

└── tests/

```



\---



\# Standard Module Structure



Every business module follows:



```

module/



├── api/

│

├── services/

│

├── engines/

│

├── repositories/

│

├── models/

│

├── schemas/

│

├── events/

│

├── providers/

│

├── exceptions/

│

└── tests/

```



\---



\# API Layer



Location:



```

app/api/

```



Contains:



```

routers



dependencies



middleware bindings

```



Example:



```

app/api/property.py

```



Only handles:



```

HTTP Request



↓



Service Call



↓



Response

```



\---



\# Service Layer



Example:



```

app/property/services/

```



Files:



```

property\_service.py



lifecycle\_service.py

```



Responsibilities:



\- workflows

\- orchestration

\- transactions



\---



\# Engine Layer



Example:



```

app/cost/engines/

```



Files:



```

cost\_engine.py



pricing\_engine.py



forecast\_engine.py

```



Responsibilities:



\- intelligence

\- calculations

\- AI operations



\---



\# Repository Layer



Example:



```

app/property/repositories/

```



Files:



```

interface.py



sql\_repository.py

```



Responsibilities:



Database communication.



\---



\# Model Layer



Example:



```

app/property/models/

```



Files:



```

property.py



feature.py



status.py

```



Contains:



SQLAlchemy models.



\---



\# Schema Layer



Example:



```

app/property/schemas/

```



Files:



```

property\_create.py



property\_response.py

```



Contains:



Pydantic models.



\---



\# Event Layer



Example:



```

app/property/events/

```



Files:



```

events.py



handlers.py

```



Contains:



Domain event definitions.



\---



\# Provider Layer



Example:



```

app/billing/providers/

```



Files:



```

stripe.py



paystack.py



flutterwave.py

```



External integrations only.



\---



\# Austin Structure



Special architecture:



```

app/austin/



├── api/



├── services/



├── engines/



│   ├── intent\_engine.py

│   ├── planning\_engine.py

│   ├── reasoning\_engine.py

│   └── memory\_engine.py

│

├── memory/



├── tools/



├── prompts/



├── repositories/



├── models/



└── events/

```



Austin is the intelligence layer.



\---



\# Database Structure



Location:



```

app/database/

```



Structure:



```

database/



├── session.py



├── base.py



├── migrations/



├── seeds/



└── connection.py

```



Responsibilities:



\- database connection

\- session lifecycle

\- migrations



\---



\# Configuration Structure



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



Contains:



\- environment variables

\- application configuration

\- logging setup



\---



\# Middleware Structure



Location:



```

app/middleware/

```



Files:



```

authentication.py



authorization.py



logging.py



rate\_limit.py

```



\---



\# Jobs Structure



Location:



```

app/jobs/

```



Structure:



```

jobs/



├── workers/



├── queues/



├── tasks/



└── scheduler.py

```



Responsibilities:



Background processing.



\---



\# Test Structure



Location:



```

app/tests/

```



Structure:



```

tests/



├── unit/



├── integration/



├── api/



├── security/



└── e2e/

```



\---



\# Documentation Structure



```

docs/



├── architecture/



├── implementation/



├── api/



├── product/



├── security/



└── operations/

```



\---



\# File Naming Rules



Python:



```

snake\_case.py

```



Classes:



```

PascalCase

```



Functions:



```

snake\_case()

```



Constants:



```

UPPER\_CASE

```



\---



\# Import Rules



Allowed:



```

API



↓



Service



↓



Engine



↓



Repository



↓



Model

```



Forbidden:



```

Model



↓



Service

```



```

Repository



↓



API

```



```

Austin



↓



Database

```



\---



\# Module Boundary Rules



A module owns:



```

models



services



engines



repositories



events



tests

```



A module exposes:



```

services



events



APIs

```



\---



\# Implementation Order



New features are built in this order:



```

1\. Documentation



2\. Database Model



3\. Repository



4\. Engine



5\. Service



6\. API



7\. Events



8\. Tests



9\. Frontend Integration

```



\---



\# Final Repository Rule



The folder structure is the physical expression of the architecture.



If code has no clear location:



The architecture is incomplete.



\---



\*\*Folder Structure\*\*



\*Every file has a home. Every module has a boundary.\*

