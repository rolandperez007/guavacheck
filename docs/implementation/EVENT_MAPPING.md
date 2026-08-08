\# Event Mapping



> Official event architecture defining communication between Guava modules, Austin OS, and external systems.



\---



\# Purpose



Events are the communication layer of Guava.



They allow:



\- Loose coupling

\- Real-time reactions

\- Workflow automation

\- Austin awareness

\- Audit history

\- Scalable integrations



\---



\# Event Architecture



```

Module



↓



Domain Event



↓



Event Bus



↓



Subscribers



↓



Actions

```



\---



\# Core Principle



Modules do not call each other directly.



Incorrect:



```

Construction Service



↓



Passport Service

```



Correct:



```

Construction Service



↓



construction.completed



↓



Event Bus



↓



Passport Service

```



\---



\# Event Structure



Every event contains:



```

Event



{



id,



type,



timestamp,



source,



actor,



payload,



metadata



}

```



\---



\# Event Ownership



Every module owns the events it creates.



Example:



Property owns:



```

property.created

property.updated

property.deleted

```



Construction does not create property events.



\---



\# Property Events



Owner:



```

app/property/

```



Events:



```

property.created



property.updated



property.status\_changed



property.archived

```



Subscribers:



```

Passport



Search



Marketplace



Austin



Notifications

```



\---



\# Registry Events



Owner:



```

app/registry/

```



Events:



```

registry.submitted



registry.validated



registry.approved



registry.rejected

```



Subscribers:



```

Verification



Passport



Notifications



Austin

```



\---



\# Verification Events



Owner:



```

app/verification/

```



Events:



```

verification.started



verification.completed



verification.failed



verification.score\_generated

```



Subscribers:



```

Passport



Property



Trust Engine



Austin

```



\---



\# Passport Events



Owner:



```

app/passport/

```



Events:



```

passport.created



passport.updated



passport.version\_created

```



Subscribers:



```

Search



Investor



Marketplace



Austin

```



\---



\# Construction Events



Owner:



```

app/construction/

```



Events:



```

construction.started



construction.progress\_updated



construction.completed



construction.delayed

```



Subscribers:



```

Passport



Cost



Investor



Notifications



Austin

```



\---



\# Cost Events



Owner:



```

app/cost/

```



Events:



```

estimate.created



boq.generated



cost.updated



budget.exceeded

```



Subscribers:



```

Construction



Investor



Mortgage



Austin

```



\---



\# Mortgage Events



Owner:



```

app/mortgage/

```



Events:



```

mortgage.simulated



application.created



loan.approved



loan.rejected

```



Subscribers:



```

Investor



Property



Notifications

```



\---



\# Investor Events



Owner:



```

app/investor/

```



Events:



```

portfolio.created



investment.created



roi.calculated



market\_alert.created

```



Subscribers:



```

Austin



Notifications



Reports

```



\---



\# Vision Events



Owner:



```

app/vision/

```



Events:



```

render.started



render.completed



design.generated



floorplan.created

```



Subscribers:



```

Digital Twin



Property



Marketplace



Austin

```



\---



\# Digital Twin Events



Owner:



```

app/digital\_twin/

```



Events:



```

twin.created



twin.updated



simulation.completed



maintenance.updated

```



Subscribers:



```

Passport



Construction



Austin

```



\---



\# Marketplace Events



Owner:



```

app/marketplace/

```



Events:



```

listing.created



listing.updated



listing.viewed



property.requested

```



Subscribers:



```

Property



Austin



Messaging



Analytics

```



\---



\# Commerce Events



Owner:



```

app/commerce/

```



Events:



```

vendor.registered



product.created



order.created



order.completed

```



Subscribers:



```

Billing



Notifications



Austin

```



\---



\# Institution Events



Owner:



```

app/institutions/

```



Events:



```

institution.connected



offer.created



offer.updated



integration.failed

```



Subscribers:



```

Austin



Mortgage



Investor

```



\---



\# Community Events



Owner:



```

app/community/

```



Events:



```

community.created



post.created



comment.created



discussion.started

```



Subscribers:



```

Notifications



Austin

```



\---



\# Billing Events



Owner:



```

app/billing/

```



Events:



```

payment.created



payment.completed



subscription.started



subscription.cancelled



credits.updated

```



Subscribers:



```

Austin



Notifications



Analytics

```



\---



\# Austin Events



Owner:



```

app/austin/

```



Events:



```

conversation.started



intent.detected



plan.created



action.completed



memory.updated

```



Subscribers:



```

Knowledge



Analytics



Audit

```



\---



\# System Events



Owner:



```

app/events/

```



Events:



```

system.started



system.error



system.health\_changed



integration.failed

```



\---



\# Event Bus Architecture



Development:



```

FastAPI



\+



Redis Queue



\+



Event Dispatcher

```



Production:



```

Services



↓



Message Broker



↓



Consumers



↓



Workers

```



Possible future:



```

Kafka



RabbitMQ



AWS EventBridge

```



\---



\# Austin OS Event Intelligence



Austin listens to selected events.



Example:



```

construction.completed



↓



Austin receives event



↓



Updates property understanding



↓



Updates memory



↓



Suggests next action

```



Austin observes.



Modules execute.



\---



\# Event Storage



Owner:



```

app/events/

```



Tables:



```

events



event\_logs



event\_subscriptions



event\_replays

```



Purpose:



\- Audit

\- Debugging

\- Replay

\- Compliance



\---



\# Event Rules



Events should be:



\- Immutable

\- Timestamped

\- Traceable

\- Replayable



Events should not:



\- Contain business logic

\- Modify databases directly

\- Replace services



\---



\# Example Complete Workflow



\## New Property Purchase



```

User



↓



Property Created



↓



property.created



↓



Verification Started



↓



verification.completed



↓



Passport Generated



↓



passport.created



↓



Marketplace Listing Created



↓



listing.created



↓



Austin Updates Knowledge



↓



Notification Sent

```



\---



\# Final Rule



Events are the nervous system.



Modules are organs.



Austin is the intelligence observing and coordinating the system.



\---



\*\*Event Mapping\*\*



\*Everything communicates. Nothing becomes tangled.\*

