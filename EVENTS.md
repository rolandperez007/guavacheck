# Guava Platform Events

Version: 1.0

---

# Purpose

Guava uses an Event-Driven Architecture (EDA).

Engines communicate by publishing and subscribing to events rather than calling each other directly.

This reduces coupling, improves scalability, and allows every engine to react independently.

---

# Event Categories

## Property Events

PropertyCreated

PropertyUpdated

PropertyVerified

PropertyArchived

PropertyDeleted

PropertyViewed

PropertyListed

PropertyDelisted

---

## Property Passport Events

PassportCreated

PassportUpdated

PassportVerified

PassportTransferred

PassportArchived

---

## Twin Studio Events

TwinCreated

TwinUpdated

TwinVersionCreated

TwinModelUploaded

TwinAssetAdded

TwinInspectionAdded

TwinComponentUpdated

TwinSnapshotGenerated

TwinRendered

---

## Construction Events

ConstructionStarted

MilestoneCreated

MilestoneCompleted

InspectionScheduled

InspectionPassed

InspectionFailed

ConstructionCompleted

---

## Commerce Events

SupplierRegistered

SupplierVerified

ProductPublished

ProductPurchased

ServiceBooked

InstallationCompleted

WarrantyRegistered

---

## Finance Events

LoanRequested

LoanApproved

LoanRejected

MortgageCreated

InsuranceIssued

EscrowCreated

EscrowReleased

PaymentCompleted

RefundIssued

---

## Trust Exchange Events

OwnershipVerificationStarted

OwnershipVerified

OwnershipTransferred

AgreementSigned

LegalReviewStarted

ClosingCompleted

CertificateIssued

---

## Distress Events

SellerRegistered

SellerVerified

DistressListingCreated

BuyerRequestSubmitted

BuyerApproved

OfferSubmitted

OfferAccepted

OfferRejected

LegalProcessStarted

TransactionCompleted

---

## Investor Events

PortfolioCreated

PropertyAddedToPortfolio

ValuationUpdated

ROIUpdated

ForecastGenerated

MarketAlertGenerated

---

## Austin Events

AustinWorkflowStarted

AustinRecommendationGenerated

AustinAlertGenerated

AustinTaskCreated

AustinWorkflowCompleted

---

# Event Rules

Every event must contain

Event ID

Timestamp

Property ID

Passport ID (if available)

User ID

Originating Engine

Correlation ID

Payload

---

No engine should assume another engine has completed work until it receives the corresponding event.