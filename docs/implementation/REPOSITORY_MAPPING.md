\# Repository Mapping



> Official persistence architecture defining the relationship between services, repositories, ORM models, and databases.



\---



\# Purpose



Repositories provide the database abstraction layer for every Guava module.



They ensure:



\- Business logic remains database independent

\- Database access has clear ownership

\- Testing is easier

\- Data migrations remain controlled

\- Modules maintain boundaries



\---



\# Persistence Architecture



```

Service



↓



Repository Interface



↓



Repository Implementation



↓



SQLAlchemy Model



↓



PostgreSQL



↓



Supabase

```



\---



\# Core Principle



Services never directly access:



\- SQLAlchemy sessions

\- Database queries

\- Tables



Incorrect:



```

PropertyService



↓



SELECT \* FROM properties

```



Correct:



```

PropertyService



↓



PropertyRepository



↓



Database

```



\---



\# Repository Responsibilities



Repositories handle:



\- Create

\- Read

\- Update

\- Delete

\- Filtering

\- Persistence queries

\- Database transactions



Repositories do NOT handle:



\- Business decisions

\- AI reasoning

\- Validation rules

\- External APIs



\---



\# Repository Structure



Every module follows:



```

module/



├── models/

│

├── repositories/

│   ├── interface.py

│   └── sql\_repository.py

│

├── services/

│

└── schemas/

```



\---



\# Base Repository Pattern



Example:



```

BaseRepository



Methods:



create()



get()



list()



update()



delete()

```



Every repository extends this pattern.



\---



\# Property Repository



Location:



```

app/property/repositories/

```



Interface:



```

PropertyRepository

```



Implementation:



```

SQLPropertyRepository

```



Models:



```

PropertyModel

PropertyFeatureModel

PropertyStatusModel

```



Tables:



```

properties



property\_features



property\_status\_history

```



\---



\# Registry Repository



Location:



```

app/registry/repositories/

```



Repository:



```

RegistryRepository

```



Implementation:



```

SQLRegistryRepository

```



Models:



```

RegistrationModel



LandRecordModel



TitleDocumentModel

```



\---



\# Verification Repository



Repository:



```

VerificationRepository

```



Models:



```

VerificationRequestModel



VerificationResultModel



EvidenceModel

```



\---



\# Passport Repository



Repository:



```

PassportRepository

```



Models:



```

PropertyPassportModel



PassportVersionModel



PassportSnapshotModel

```



\---



\# Construction Repository



Repository:



```

ConstructionRepository

```



Models:



```

ConstructionProjectModel



MilestoneModel



ProgressReportModel

```



\---



\# Cost Repository



Repository:



```

CostRepository

```



Models:



```

CostEstimateModel



BOQModel



MaterialPriceModel

```



\---



\# Mortgage Repository



Repository:



```

MortgageRepository

```



Models:



```

MortgageProductModel



LoanApplicationModel



RepaymentModel

```



\---



\# Investor Repository



Repository:



```

InvestorRepository

```



Models:



```

PortfolioModel



InvestmentModel



ROIAnalysisModel

```



\---



\# Vision Repository



Repository:



```

VisionRepository

```



Models:



```

VisionProjectModel



RenderModel



FloorPlanModel

```



\---



\# Digital Twin Repository



Repository:



```

TwinRepository

```



Models:



```

DigitalTwinModel



TwinVersionModel



SimulationModel

```



\---



\# World Repository



Repository:



```

WorldRepository

```



Models:



```

LocationModel



InfrastructureModel



TerrainModel

```



\---



\# Marketplace Repository



Repository:



```

MarketplaceRepository

```



Models:



```

ListingModel



ListingMediaModel



RequestModel

```



\---



\# Commerce Repository



Repository:



```

CommerceRepository

```



Models:



```

VendorModel



ProductModel



OrderModel

```



\---



\# Institution Repository



Repository:



```

InstitutionRepository

```



Models:



```

InstitutionModel



IntegrationModel



OfferModel

```



\---



\# Community Repository



Repository:



```

CommunityRepository

```



Models:



```

CommunityModel



PostModel



CommentModel

```



\---



\# Messaging Repository



Repository:



```

MessagingRepository

```



Models:



```

ConversationModel



MessageModel

```



\---



\# Billing Repository



Repository:



```

BillingRepository

```



Models:



```

PaymentModel



SubscriptionModel



InvoiceModel



CreditModel

```



\---



\# Austin Repository



Important:



Austin does not store business data.



Austin stores cognition data.



Repository:



```

AustinRepository

```



Models:



```

ConversationModel



MemoryModel



AgentRunModel



PlanModel

```



\---



\# Repository Injection



Services receive repositories through dependency injection.



Example:



```

PropertyService



(

&#x20;PropertyRepository

)



↓



create\_property()



↓



repository.save()

```



\---



\# Database Session Ownership



Database session:



```

app/database/

```



Responsibilities:



\- Connection management

\- Transactions

\- Session lifecycle



Example:



```

Database Session



↓



Repository



↓



Model

```



\---



\# SQLAlchemy Rules



Models represent:



\- Tables

\- Relationships

\- Constraints



Models do not contain:



\- Workflows

\- AI logic

\- External calls



\---



\# Migration Ownership



Every module owns its migrations.



Example:



```

migrations/



property/



001\_create\_properties.sql



002\_add\_features.sql

```



\---



\# Testing Strategy



Repository tests verify:



```

Repository



↓



Database



↓



Expected Result

```



Example:



```

Create Property



↓



Save



↓



Retrieve



↓



Compare

```



\---



\# Future Scaling



Development:



```

SQLAlchemy



↓



PostgreSQL

```



Production options:



```

PostgreSQL Cluster



Read Replicas



Caching Layer



Event Streaming

```



\---



\# Final Backend Boundary



```

API



receives requests





Service



controls workflows





Engine



performs intelligence





Repository



controls persistence





Database



stores truth





Events



connect the ecosystem





Austin



coordinates intelligence

```



\---



\*\*Repository Mapping\*\*



\*Data access is controlled. Business logic remains clean.\*

