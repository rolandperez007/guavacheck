\# Module Mapping



> The official mapping between Guava architecture, ACOS, Austin OS, and the production codebase.



\---



\# Purpose



Every business capability belongs to exactly one primary module.



Austin orchestrates modules.



Modules own business logic.



No business logic should exist inside controllers or UI components.



\---



\# Architectural Principle



```

Workflow



↓



Business Module



↓



Service



↓



Engine



↓



API



↓



Events



↓



Database



↓



Frontend

```



Every layer has one clear owner.



\---



\# Root Architecture



```

app/



├── api/

├── auth/

├── austin/

├── billing/

├── community/

├── commerce/

├── construction/

├── contractors/

├── cost/

├── digital\_twin/

├── documents/

├── events/

├── geo/

├── government/

├── identity/

├── institutions/

├── investor/

├── jobs/

├── knowledge/

├── localization/

├── maintenance/

├── maps/

├── marketplace/

├── messaging/

├── mortgage/

├── notifications/

├── passport/

├── payments/

├── permissions/

├── projects/

├── property/

├── registry/

├── reports/

├── search/

├── security/

├── storage/

├── survey/

├── users/

├── verification/

├── vision/

├── world/

└── workflow/

```



\---



\# Austin



Directory



```

app/austin/

```



Responsibilities



Intent Detection



Planning



Reasoning



Delegation



Conversation



Knowledge



Memory



Runtime



Engine Orchestration



Austin owns cognition.



Austin owns no property business rules.



\---



\# Property



```

app/property/

```



Responsibilities



Property Records



Metadata



Ownership Links



Basic Lifecycle



Property Creation



Property Updates



\---



\# Registry



```

app/registry/

```



Responsibilities



Property Registration



Land Registration



Submission Workflow



Registration Validation



\---



\# Verification



```

app/verification/

```



Responsibilities



Identity Verification



Ownership Verification



Document Verification



Evidence



Verification Scoring



\---



\# Passport



```

app/passport/

```



Responsibilities



Property Passport



Version History



Timeline



Audit



Property Intelligence



Passport Generation



\---



\# Construction



```

app/construction/

```



Responsibilities



Construction Projects



Scheduling



Milestones



Progress



Site Reports



Quality



Safety



\---



\# Cost



```

app/cost/

```



Responsibilities



Cost Estimation



BOQ



Material Pricing



Forecasting



Budgeting



Inflation



\---



\# Mortgage



```

app/mortgage/

```



Responsibilities



Loan Simulation



Mortgage Applications



Repayment



Affordability



Loan Monitoring



\---



\# Investor



```

app/investor/

```



Responsibilities



Portfolio



Investment Analysis



ROI



Market Evaluation



Investment Dashboard



\---



\# Digital Twin



```

app/digital\_twin/

```



Responsibilities



Twin Generation



Twin Synchronization



Versioning



Simulation



Maintenance History



\---



\# Vision



```

app/vision/

```



Responsibilities



3D Builder



Interior Design



Exterior Design



Rendering



Image Analysis



Floor Plans



\---



\# World



```

app/world/

```



Responsibilities



Spatial Intelligence



Infrastructure



Terrain



Environment



Neighbourhood



Planning



Geography



\---



\# Government



```

app/government/

```



Responsibilities



Planning



Permits



Land Registry



Government APIs



Environmental Records



Infrastructure



\---



\# Institutions



```

app/institutions/

```



Responsibilities



Banks



Insurance



Developers



Utilities



Third-party APIs



Institution Registry



\---



\# Marketplace



```

app/marketplace/

```



Responsibilities



Property Listings



Discovery



Search Results



Recommendations



Featured Properties



\---



\# Commerce



```

app/commerce/

```



Responsibilities



Furniture



Building Materials



Professionals



Home Services



Construction Marketplace



\---



\# Contractors



```

app/contractors/

```



Responsibilities



Architects



Engineers



Surveyors



Builders



Ratings



Professional Profiles



\---



\# Geo



```

app/geo/

```



Responsibilities



Coordinates



Reverse Geocoding



Distance



Routing



Location Utilities



\---



\# Maps



```

app/maps/

```



Responsibilities



Interactive Maps



Markers



Heatmaps



Spatial Visualization



\---



\# Knowledge



```

app/knowledge/

```



Responsibilities



Knowledge Graph



Semantic Search



Relationships



Austin Knowledge



\---



\# Search



```

app/search/

```



Responsibilities



Global Search



Indexing



Filtering



Ranking



Semantic Search



\---



\# Community



```

app/community/

```



Responsibilities



Communities



Posts



Comments



Property Discussions



Neighbourhood Updates



\---



\# Notifications



```

app/notifications/

```



Responsibilities



Push



SMS



Email



Alerts



Austin Notifications



\---



\# Messaging



```

app/messaging/

```



Responsibilities



Direct Messages



Austin Conversations



Institution Messaging



Support



\---



\# Reports



```

app/reports/

```



Responsibilities



PDF



Exports



Analytics



Executive Reports



Institution Reports



\---



\# Documents



```

app/documents/

```



Responsibilities



Upload



Storage



OCR



Versioning



Digital Signatures



\---



\# Workflow



```

app/workflow/

```



Responsibilities



Workflow State



Approvals



Transitions



Automation



Business Process Engine



\---



\# Events



```

app/events/

```



Responsibilities



Domain Events



Publishing



Subscriptions



Event Replay



Audit Integration



\---



\# Permissions



```

app/permissions/

```



Responsibilities



Authorization



Roles



Policies



Institution Access



Austin Access Rules



\---



\# Security



```

app/security/

```



Responsibilities



Encryption



Threat Detection



Secrets



Compliance



Audit Security



\---



\# Storage



```

app/storage/

```



Responsibilities



Object Storage



Images



Videos



Documents



Backups



\---



\# Jobs



```

app/jobs/

```



Responsibilities



Queues



Background Tasks



Scheduling



Workers



Automation



\---



\# Billing



```

app/billing/

```



Responsibilities



Subscriptions



Payments



Invoices



Credits



Usage Billing



\---



\# Guiding Rules



Every feature belongs to one module.



Modules communicate through APIs and events.



Austin coordinates modules.



Modules never bypass ownership boundaries.



Business rules remain inside their owning module.



\---



\# Ownership Matrix



| Capability | Owner |

|------------|-------|

| Registration | Registry |

| Verification | Verification |

| Passport | Passport |

| Construction | Construction |

| BOQ | Cost |

| Mortgage | Mortgage |

| Investment | Investor |

| Twin | Digital Twin |

| AI Rendering | Vision |

| Spatial Intelligence | World |

| Planning | Government |

| Banks | Institutions |

| Cognition | Austin |

| Search | Search |

| Marketplace | Marketplace |



\---



\# Guiding Statement



A clean architecture is one where every capability has exactly one owner, every owner exposes clear interfaces, and Austin coordinates the whole without violating module boundaries.



\---



\*\*Module Mapping\*\*



\*One capability. One owner. One place in the codebase.\*

