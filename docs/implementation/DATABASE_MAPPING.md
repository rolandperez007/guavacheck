\# Database Mapping



> Official mapping between Guava architecture modules, domain entities, database tables, and ownership boundaries.



\---



\# Purpose



This document defines:



\- Database ownership

\- Primary entities

\- Table responsibilities

\- Relationships

\- Data boundaries

\- Future migration planning



The database follows the same principle as the application architecture:



```

Module



↓



Domain Model



↓



Database Tables



↓



Services



↓



APIs



↓



Events

```



\---



\# Database Principles



\## Ownership



Every table belongs to exactly one module.



A module owns:



\- Its tables

\- Its models

\- Its migrations

\- Its business rules



\---



\## Relationships



Modules communicate through:



\- Foreign keys where ownership is stable

\- Domain events where coupling should remain loose

\- API contracts for external systems



\---



\# Core Identity Domain



Owner:



```

app/identity/

```



Database:



```

users

profiles

organizations

roles

permissions

sessions

```



Responsibilities:



Users



Identity Records



Organizations



Access Control Subjects



\---



\# Authentication Domain



Owner:



```

app/auth/

```



Tables:



```

auth\_credentials



auth\_tokens



auth\_sessions



password\_resets



login\_history

```



Responsibilities:



Authentication lifecycle



JWT sessions



Security events



\---



\# Property Domain



Owner:



```

app/property/

```



Tables:



```

properties



property\_types



property\_features



property\_addresses



property\_status\_history

```



Responsibilities:



Core property identity.



Example:



```

Property

&#x20;|

&#x20;├── Address

&#x20;├── Type

&#x20;├── Features

&#x20;└── Status

```



\---



\# Registry Domain



Owner:



```

app/registry/

```



Tables:



```

property\_registrations



land\_records



title\_documents



registry\_submissions



registry\_history

```



Responsibilities:



Legal registration lifecycle.



\---



\# Verification Domain



Owner:



```

app/verification/

```



Tables:



```

verification\_requests



verification\_checks



verification\_documents



verification\_results



verification\_scores

```



Responsibilities:



Trust system.



\---



\# Passport Domain



Owner:



```

app/passport/

```



Tables:



```

property\_passports



passport\_versions



passport\_events



passport\_snapshots

```



Responsibilities:



Permanent property intelligence record.



\---



\# Construction Domain



Owner:



```

app/construction/

```



Tables:



```

construction\_projects



construction\_tasks



construction\_milestones



construction\_reports



construction\_progress



construction\_sites

```



Responsibilities:



Building lifecycle management.



\---



\# Cost Domain



Owner:



```

app/cost/

```



Tables:



```

cost\_estimates



bill\_of\_quantities



material\_prices



labour\_rates



cost\_forecasts



budget\_versions

```



Responsibilities:



Financial intelligence.



\---



\# Mortgage Domain



Owner:



```

app/mortgage/

```



Tables:



```

mortgage\_products



mortgage\_applications



loan\_simulations



repayment\_schedules



loan\_status\_history

```



Responsibilities:



Property financing.



\---



\# Investor Domain



Owner:



```

app/investor/

```



Tables:



```

investment\_profiles



investment\_portfolios



investment\_assets



roi\_analysis



market\_reports

```



Responsibilities:



Investment intelligence.



\---



\# Digital Twin Domain



Owner:



```

app/digital\_twin/

```



Tables:



```

digital\_twins



twin\_versions



twin\_components



simulation\_runs



maintenance\_records

```



Responsibilities:



Virtual representation of assets.



\---



\# Vision Domain



Owner:



```

app/vision/

```



Tables:



```

vision\_projects



renders



render\_versions



floor\_plans



design\_assets



image\_analysis\_results

```



Responsibilities:



AI design and visualization.



\---



\# World Domain



Owner:



```

app/world/

```



Tables:



```

locations



regions



terrain\_data



infrastructure\_nodes



environment\_records

```



Responsibilities:



Spatial intelligence.



\---



\# Government Domain



Owner:



```

app/government/

```



Tables:



```

government\_records



permits



planning\_applications



regulatory\_documents



authority\_connections

```



Responsibilities:



Government intelligence.



\---



\# Institutions Domain



Owner:



```

app/institutions/

```



Tables:



```

institutions



institution\_users



institution\_integrations



institution\_products



api\_connections

```



Responsibilities:



Banks, insurance, developers and partners.



\---



\# Marketplace Domain



Owner:



```

app/marketplace/

```



Tables:



```

listings



listing\_media



listing\_views



listing\_requests



listing\_status\_history

```



Responsibilities:



Property discovery.



\---



\# Commerce Domain



Owner:



```

app/commerce/

```



Tables:



```

vendors



products



services



orders



transactions

```



Responsibilities:



Guava City commerce ecosystem.



\---



\# Contractor Domain



Owner:



```

app/contractors/

```



Tables:



```

contractors



professional\_profiles



licenses



skills



ratings

```



Responsibilities:



Professional network.



\---



\# Geo Domain



Owner:



```

app/geo/

```



Tables:



```

coordinates



geocoding\_records



distance\_cache



routes

```



Responsibilities:



Location services.



\---



\# Maps Domain



Owner:



```

app/maps/

```



Tables:



```

map\_layers



map\_markers



spatial\_visualizations

```



Responsibilities:



Map presentation data.



\---



\# Knowledge Domain



Owner:



```

app/knowledge/

```



Tables:



```

knowledge\_nodes



knowledge\_edges



knowledge\_sources



knowledge\_embeddings

```



Responsibilities:



Austin knowledge graph.



\---



\# Search Domain



Owner:



```

app/search/

```



Tables:



```

search\_indexes



search\_documents



search\_queries



search\_history

```



Responsibilities:



Discovery engine.



\---



\# Community Domain



Owner:



```

app/community/

```



Tables:



```

communities



posts



comments



reactions



community\_members

```



Responsibilities:



Social layer.



\---



\# Messaging Domain



Owner:



```

app/messaging/

```



Tables:



```

conversations



messages



attachments



conversation\_participants

```



Responsibilities:



Communication.



\---



\# Notification Domain



Owner:



```

app/notifications/

```



Tables:



```

notifications



notification\_preferences



notification\_logs

```



Responsibilities:



Alerts.



\---



\# Document Domain



Owner:



```

app/documents/

```



Tables:



```

documents



document\_versions



document\_permissions



ocr\_results



signatures

```



Responsibilities:



Document intelligence.



\---



\# Workflow Domain



Owner:



```

app/workflow/

```



Tables:



```

workflows



workflow\_steps



workflow\_instances



workflow\_history

```



Responsibilities:



Automation engine.



\---



\# Event Domain



Owner:



```

app/events/

```



Tables:



```

events



event\_subscriptions



event\_logs



event\_replays

```



Responsibilities:



System communication.



\---



\# Billing Domain



Owner:



```

app/billing/

```



Tables:



```

subscriptions



payments



invoices



credits



usage\_records

```



Responsibilities:



Revenue engine.



\---



\# Storage Domain



Owner:



```

app/storage/

```



Tables:



```

files



media\_assets



storage\_objects

```



Responsibilities:



Digital assets.



\---



\# Job Domain



Owner:



```

app/jobs/

```



Tables:



```

jobs



job\_runs



scheduled\_tasks



worker\_logs

```



Responsibilities:



Background processing.



\---



\# Austin Domain



Owner:



```

app/austin/

```



Important:



Austin does NOT own business data.



Austin owns:



```

conversations



memories



plans



agent\_runs



reasoning\_logs

```



Austin references other domains.



Example:



Austin:



"Create a building estimate"



↓



Cost Engine:



"Generate BOQ"



\---



\# Master Relationships



```

User



&#x20;|

&#x20;+-- Properties



&#x20;|

&#x20;+-- Investments



&#x20;|

&#x20;+-- Conversations



&#x20;|

&#x20;+-- Payments





Property



&#x20;|

&#x20;+-- Passport



&#x20;|

&#x20;+-- Verification



&#x20;|

&#x20;+-- Construction



&#x20;|

&#x20;+-- Digital Twin



&#x20;|

&#x20;+-- Vision



&#x20;|

&#x20;+-- Marketplace Listing





Institution



&#x20;|

&#x20;+-- Products



&#x20;|

&#x20;+-- Integrations



&#x20;|

&#x20;+-- Users

```



\---



\# Database Ownership Matrix



| Domain | Primary Tables |

|---|---|

| Identity | users |

| Property | properties |

| Registry | registrations |

| Verification | checks |

| Passport | passports |

| Construction | projects |

| Cost | estimates |

| Mortgage | loans |

| Investor | portfolios |

| Twin | digital\_twins |

| Vision | renders |

| World | locations |

| Marketplace | listings |

| Commerce | vendors |

| Austin | conversations |



\---



\# Final Rule



The database is a reflection of the architecture.



If a table has unclear ownership, the architecture is incomplete.



If a feature has unclear data ownership, implementation must stop until ownership is defined.



\---



\*\*Database Mapping\*\*



\*One domain. One owner. One source of truth.\*

