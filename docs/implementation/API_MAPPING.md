\# API Mapping



> Official API ownership map between Guava frontend, backend modules, services, databases, and events.



\---



\# Purpose



This document defines:



\- API ownership

\- Endpoint responsibilities

\- Request flow

\- Response ownership

\- Service boundaries

\- Event publishing rules



The API layer is a gateway.



It does not contain business logic.



\---



\# API Architecture



```

Frontend



↓



API Gateway



↓



Module Router



↓



Service Layer



↓



Engine



↓



Database



↓



Domain Events



↓



Notifications / Austin

```



\---



\# API Principles



\## Controllers



Controllers only:



\- validate requests

\- authenticate users

\- call services

\- return responses





Controllers never:



\- calculate business rules

\- modify unrelated domains

\- access databases directly



\---



\# API Structure



```

app/api/



├── auth.py

├── users.py

├── properties.py

├── registry.py

├── verification.py

├── passport.py

├── construction.py

├── cost.py

├── mortgage.py

├── investor.py

├── vision.py

├── twin.py

├── marketplace.py

├── commerce.py

├── institutions.py

├── community.py

├── messaging.py

├── billing.py

└── austin.py

```



\---



\# Authentication API



Owner:



```

app/auth/

```



Base:



```

/api/auth

```



Endpoints:



```

POST   /register



POST   /login



POST   /logout



POST   /refresh



POST   /forgot-password

```



Responsibilities:



Account creation



Authentication



Sessions



Security



\---



\# User API



Owner:



```

app/users/

```



Base:



```

/api/users

```



Endpoints:



```

GET    /me



PATCH  /me



GET    /{user\_id}



GET    /preferences

```



\---



\# Austin API



Owner:



```

app/austin/

```



Base:



```

/api/austin

```



Endpoints:



```

POST /chat



POST /plan



POST /execute



GET  /memory



GET  /history

```



Flow:



```

User



↓



Austin



↓



Intent Detection



↓



Planning



↓



Module Delegation



↓



Response

```



Austin does not execute property rules.



\---



\# Property API



Owner:



```

app/property/

```



Base:



```

/api/properties

```



Endpoints:



```

POST   /



GET    /



GET    /{property\_id}



PATCH  /{property\_id}



DELETE /{property\_id}

```



Responsibilities:



Property lifecycle.



\---



\# Registry API



Owner:



```

app/registry/

```



Base:



```

/api/registry

```



Endpoints:



```

POST /submit



GET  /status/{property\_id}



POST /validate

```



\---



\# Verification API



Owner:



```

app/verification/

```



Base:



```

/api/verification

```



Endpoints:



```

POST /request



GET  /{verification\_id}



POST /review



GET  /score

```



\---



\# Passport API



Owner:



```

app/passport/

```



Base:



```

/api/passport

```



Endpoints:



```

POST /generate



GET  /{property\_id}



GET  /history/{property\_id}



GET  /timeline/{property\_id}

```



\---



\# Construction API



Owner:



```

app/construction/

```



Base:



```

/api/construction

```



Endpoints:



```

POST /projects



GET  /projects/{id}



POST /milestones



POST /reports



GET  /progress/{id}

```



\---



\# Cost API



Owner:



```

app/cost/

```



Base:



```

/api/cost

```



Endpoints:



```

POST /estimate



POST /boq



GET  /materials



GET  /forecast

```



Example:



```

Austin:



"Estimate this building"



↓



Cost API



↓



Cost Engine



↓



BOQ Generated

```



\---



\# Mortgage API



Owner:



```

app/mortgage/

```



Base:



```

/api/mortgage

```



Endpoints:



```

POST /simulate



GET  /products



POST /apply



GET  /status

```



\---



\# Investor API



Owner:



```

app/investor/

```



Base:



```

/api/investor

```



Endpoints:



```

GET  /portfolio



POST /analysis



GET  /roi



GET  /market

```



\---



\# Digital Twin API



Owner:



```

app/digital\_twin/

```



Base:



```

/api/twins

```



Endpoints:



```

POST /create



GET  /{id}



POST /simulate



GET  /history

```



\---



\# Vision API



Owner:



```

app/vision/

```



Base:



```

/api/vision

```



Endpoints:



```

POST /render



POST /interior



POST /exterior



POST /floorplan



POST /analyze

```



\---



\# World API



Owner:



```

app/world/

```



Base:



```

/api/world

```



Endpoints:



```

GET /location



GET /infrastructure



GET /environment



GET /planning

```



\---



\# Marketplace API



Owner:



```

app/marketplace/

```



Base:



```

/api/marketplace

```



Endpoints:



```

POST /listings



GET  /search



GET  /listing/{id}



POST /request

```



\---



\# Commerce API



Owner:



```

app/commerce/

```



Base:



```

/api/commerce

```



Endpoints:



```

GET  /vendors



GET  /products



POST /orders

```



\---



\# Contractor API



Owner:



```

app/contractors/

```



Base:



```

/api/contractors

```



Endpoints:



```

POST /profiles



GET  /search



GET  /ratings

```



\---



\# Institution API



Owner:



```

app/institutions/

```



Base:



```

/api/institutions

```



Endpoints:



```

GET  /



POST /connect



GET  /products



POST /simulate-offer

```



\---



\# Community API



Owner:



```

app/community/

```



Base:



```

/api/community

```



Endpoints:



```

GET  /communities



POST /posts



POST /comments



GET  /feed

```



\---



\# Messaging API



Owner:



```

app/messaging/

```



Base:



```

/api/messages

```



Endpoints:



```

POST /conversation



GET  /conversation/{id}



POST /send

```



\---



\# Billing API



Owner:



```

app/billing/

```



Base:



```

/api/billing

```



Endpoints:



```

POST /checkout



POST /webhook



GET  /subscription



GET  /credits

```



\---



\# Document API



Owner:



```

app/documents/

```



Base:



```

/api/documents

```



Endpoints:



```

POST /upload



GET  /{id}



POST /ocr



POST /sign

```



\---



\# Event Flow



Example:



Property Created



```

Property Service



↓



property.created



↓



Event Bus



↓



Austin



↓



Passport Generator



↓



Notification Service

```



\---



\# Frontend Mapping



\## Dashboard



Uses:



```

Austin API



Property API



Passport API



Investor API

```



\---



\## Property Page



Uses:



```

Property API



Vision API



Twin API



Marketplace API

```



\---



\## Investor Dashboard



Uses:



```

Investor API



Mortgage API



Cost API



World API

```



\---



\## Guava City



Uses:



```

World API



Marketplace API



Commerce API



Community API

```



\---



\# External Integration Boundary



External systems connect through:



```

app/institutions/

```



Examples:



Banks



Insurance



Government



Developers



Payment Providers



\---



\# API Ownership Matrix



| Capability | API Owner |

|-|-|

| AI Conversation | Austin |

| Property Data | Property |

| Legal Records | Registry |

| Trust | Verification |

| Intelligence | Passport |

| Building | Construction |

| Estimates | Cost |

| Finance | Mortgage |

| Investment | Investor |

| Rendering | Vision |

| Simulation | Digital Twin |

| Discovery | Marketplace |



\---



\# Final Rule



The API is a contract.



The frontend should never know internal business logic.



The backend should never depend on frontend structure.



Austin coordinates.



Modules execute.



\---



\*\*API Mapping\*\*



\*Every request has an owner. Every owner has a boundary.\*

