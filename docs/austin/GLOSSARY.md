\# Glossary



> Canonical terminology for Austin OS.



\---



\# Overview



This glossary defines the standard terminology used throughout the Austin OS architecture.



Every contributor should use these definitions consistently to avoid ambiguity across documentation, implementation, and discussions.



\---



\# A



\## ACOS



Austin Cognitive Operating System.



The core cognitive platform that provides reasoning, memory, world knowledge, engine orchestration, agent coordination, and execution services.



\---



\## Agent



An autonomous software component that performs specialized reasoning or tasks on behalf of Austin.



Agents collaborate through the Runtime and are coordinated by the Reasoning System.



\---



\## API Gateway



The official public interface into Austin OS.



All external applications communicate with Austin exclusively through the API Gateway.



\---



\## Application



A software product built on top of Austin OS.



Applications own their business logic while Austin provides cognitive capabilities.



Example:



\- guavacheck



\---



\# C



\## Context



The collection of information describing the current execution environment.



Examples include:



\- Active session

\- User objective

\- Current workflow

\- Conversation state



\---



\## Cognitive Memory



Knowledge retained by Austin to support reasoning and future execution.



\---



\# E



\## Engine



A modular execution component responsible for a specific domain capability.



Examples include:



\- Property Engine

\- Finance Engine

\- Vision Engine

\- Verification Engine



\---



\## Engine Registry



The catalog of all available execution engines.



\---



\## Engine Router



The component responsible for selecting the appropriate engine for a given intent.



\---



\## Execution Pipeline



The ordered sequence of steps that transforms an incoming request into a completed response.



\---



\# G



\## guavacheck



The flagship application built on Austin OS.



It demonstrates Austin's cognitive capabilities within the global property intelligence domain.



\---



\# I



\## Intent



Austin's structured understanding of what the user wants to achieve.



Intent is produced by the Intent Normalizer.



\---



\## Intent Normalizer



The component responsible for converting natural language into structured intent.



\---



\# K



\## Kernel



The foundational layer of Austin OS.



It provides the platform services upon which all higher-level capabilities are built.



\---



\# M



\## Memory System



The subsystem responsible for storing and retrieving cognitive information.



It supports both short-term and long-term memory.



\---



\# O



\## Observability



The collection of logging, metrics, tracing, diagnostics, and monitoring capabilities that provide operational visibility into Austin OS.



\---



\# P



\## Planner



The reasoning component responsible for transforming intent into executable plans.



\---



\## Plugin



An independently deployable extension that adds capabilities to Austin OS without modifying the kernel.



\---



\## Plugin Manager



The runtime service responsible for discovering, validating, loading, and managing plugins.



\---



\# R



\## Reasoning



The cognitive process of analyzing goals, context, constraints, and available knowledge to produce execution plans.



\---



\## Runtime



The operational layer responsible for coordinating execution across Austin OS.



\---



\# S



\## Scheduler



A runtime component responsible for coordinating the execution of asynchronous or scheduled work.



\---



\## Security Model



The collection of identity, authorization, audit, and protection mechanisms that secure Austin OS.



\---



\## Session



The active execution context for a user or application interaction.



\---



\# T



\## Tenant



An isolated organizational environment within a multi-tenant deployment.



\---



\# W



\## Workflow



A structured sequence of cognitive or operational tasks executed by Austin.



\---



\## World OS



Austin's structured representation of the physical world.



World OS models countries, administrative divisions, languages, currencies, time zones, legal structures, and other real-world entities.



\---



\# Design Philosophy



Terminology should remain:



\- Precise

\- Stable

\- Consistent

\- Unambiguous



When introducing new concepts, contributors should extend this glossary to preserve a shared understanding across the platform.



\---



\*\*Glossary\*\*



\*A shared vocabulary for building and evolving Austin OS.\*



