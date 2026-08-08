\# Service Mapping



> Official internal execution map between APIs, services, engines, repositories, and databases.



\---



\# Purpose



This document defines how backend execution flows through Guava.



The objective:



\- Thin API controllers

\- Clear service ownership

\- Intelligent engines

\- Isolated database access

\- Testable business logic



\---



\# Backend Execution Pattern



Every feature follows:



```

API Router



↓



Service



↓



Engine



↓



Repository



↓



Database



↓



Domain Event

```



\---



\# Layer Responsibilities



\---



\# API Layer



Location:



```

app/api/

```



Responsibilities:



\- HTTP handling

\- Authentication checks

\- Request validation

\- Response formatting



The API layer does NOT:



\- Calculate business rules

\- Access database directly

\- Call external providers directly



\---



\# Service Layer



Location:



Inside each module.



Example:



```

app/property/services/

```



Responsibilities:



\- Business workflows

\- Combining engines

\- Coordinating repositories

\- Transaction boundaries



Example:



```

PropertyService.create\_property()



↓



Validate data



↓



Save property



↓



Generate event



↓



Notify Austin

```



\---



\# Engine Layer



Location:



Inside each module.



Example:



```

app/cost/engines/

```



Responsibilities:



\- Intelligence

\- Calculations

\- Algorithms

\- AI workflows

\- Domain reasoning



Examples:



```

Cost Engine



Vision Engine



Mortgage Engine



Investor Engine



Austin Engine

```



\---



\# Repository Layer



Location:



Inside each module.



Example:



```

app/property/repositories/

```



Responsibilities:



\- Database queries

\- Persistence

\- Data retrieval



Repositories never contain business rules.



\---



\# Property Module



Location:



```

app/property/

```



Structure:



```

property/



├── api/

├── services/

├── engines/

├── repositories/

├── models/

├── schemas/

└── events/

```



Services:



```

PropertyService

PropertyLifecycleService

```



Engines:



```

PropertyValidationEngine

PropertyClassificationEngine

```



Repositories:



```

PropertyRepository

```



Database:



```

properties

property\_features

property\_status\_history

```



\---



\# Registry Module



Location:



```

app/registry/

```



Services:



```

RegistrationService

SubmissionService

ValidationService

```



Engines:



```

RegistryValidationEngine

ComplianceEngine

```



Repositories:



```

RegistryRepository

```



\---



\# Verification Module



Location:



```

app/verification/

```



Services:



```

VerificationService

EvidenceService

ScoringService

```



Engines:



```

IdentityVerificationEngine

TrustScoreEngine

FraudDetectionEngine

```



Repositories:



```

VerificationRepository

```



\---



\# Passport Module



Location:



```

app/passport/

```



Services:



```

PassportService

TimelineService

SnapshotService

```



Engines:



```

PassportGenerationEngine

IntelligenceEngine

```



Repositories:



```

PassportRepository

```



\---



\# Construction Module



Location:



```

app/construction/

```



Services:



```

ConstructionService

ProgressService

ReportingService

```



Engines:



```

ScheduleEngine

QualityEngine

SafetyEngine

```



Repositories:



```

ConstructionRepository

```



\---



\# Cost Module



Location:



```

app/cost/

```



Services:



```

CostService

BOQService

ForecastService

```



Engines:



```

CostEstimationEngine

PricingEngine

InflationEngine

```



Repositories:



```

CostRepository

```



\---



\# Mortgage Module



Location:



```

app/mortgage/

```



Services:



```

MortgageService

LoanApplicationService

RepaymentService

```



Engines:



```

AffordabilityEngine

InterestEngine

RiskEngine

```



Repositories:



```

MortgageRepository

```



\---



\# Investor Module



Location:



```

app/investor/

```



Services:



```

InvestmentService

PortfolioService

AnalysisService

```



Engines:



```

ROIEngine

MarketAnalysisEngine

RiskAnalysisEngine

```



Repositories:



```

InvestorRepository

```



\---



\# Vision Module



Location:



```

app/vision/

```



Services:



```

VisionService

RenderService

DesignService

```



Engines:



```

InteriorEngine

ExteriorEngine

FloorPlanEngine

RenderingEngine

ImageAnalysisEngine

```



Repositories:



```

VisionRepository

```



\---



\# Digital Twin Module



Location:



```

app/digital\_twin/

```



Services:



```

TwinService

SimulationService

SyncService

```



Engines:



```

TwinGenerationEngine

SimulationEngine

SynchronizationEngine

```



Repositories:



```

TwinRepository

```



\---



\# World Module



Location:



```

app/world/

```



Services:



```

WorldService

SpatialService

InfrastructureService

```



Engines:



```

TerrainEngine

SpatialEngine

PlanningEngine

```



Repositories:



```

WorldRepository

```



\---



\# Marketplace Module



Location:



```

app/marketplace/

```



Services:



```

ListingService

DiscoveryService

RecommendationService

```



Engines:



```

MatchingEngine

RankingEngine

RecommendationEngine

```



Repositories:



```

MarketplaceRepository

```



\---



\# Commerce Module



Location:



```

app/commerce/

```



Services:



```

VendorService

ProductService

OrderService

```



Engines:



```

CommerceRecommendationEngine

PricingEngine

```



Repositories:



```

CommerceRepository

```



\---



\# Institution Module



Location:



```

app/institutions/

```



Services:



```

InstitutionService

IntegrationService

OfferSimulationService

```



Engines:



```

BankOfferEngine

InsuranceEngine

PartnerMatchingEngine

```



Repositories:



```

InstitutionRepository

```



\---



\# Austin Module



Location:



```

app/austin/

```



Austin follows:



```

Conversation



↓



Intent Engine



↓



Planning Engine



↓



Decision Engine



↓



Module Executor



↓



Response Generator

```



Services:



```

AustinService

ConversationService

MemoryService

ExecutionService

```



Engines:



```

IntentEngine

ReasoningEngine

PlanningEngine

MemoryEngine

```



Repositories:



```

AustinRepository

```



Austin never replaces modules.



Austin activates modules.



\---



\# Billing Module



Location:



```

app/billing/

```



Services:



```

BillingService

SubscriptionService

CreditService

```



Engines:



```

PricingEngine

UsageEngine

RevenueEngine

```



Repositories:



```

BillingRepository

```



\---



\# Cross Module Communication



Preferred:



```

Module A



↓



Event Bus



↓



Module B

```



Example:



```

Construction Completed



↓



construction.completed



↓



Passport Service



↓



Update Property Passport

```



\---



\# External Provider Rule



External services never connect directly to modules.



Correct:



```

Module



↓



Provider Adapter



↓



External Service

```



Example:



```

Billing



↓



Stripe Provider



↓



Stripe API

```



\---



\# Testing Ownership



Every module owns:



```

tests/



├── unit/

├── integration/

└── e2e/

```



Test order:



```

Engine Tests



↓



Service Tests



↓



API Tests



↓



Full Workflow Tests

```



\---



\# Final Backend Rule



Routers receive.



Services coordinate.



Engines think.



Repositories persist.



Events connect.



Austin orchestrates.



\---



\*\*Service Mapping\*\*



\*Clear execution paths create scalable systems.\*

