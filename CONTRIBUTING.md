# Contributing to Guava

Welcome to the Guava Platform.

This document defines the engineering standards for all contributors.

---

# Principles

Write readable code.

Prefer composition over duplication.

Keep engines independent.

Publish events instead of tightly coupling services.

Document major architectural changes.

---

# Branching Strategy

main

Production-ready code.

develop

Integration branch.

feature/<name>

New features.

bugfix/<name>

Bug fixes.

hotfix/<name>

Production fixes.

---

# Commit Messages

Examples

feat: add Twin Registry

fix: correct ownership validation

docs: update system architecture

refactor: simplify finance engine

test: add passport integration tests

---

# Pull Requests

Every PR must include:

Description

Screenshots (if UI)

Tests

Documentation updates

Migration notes (if required)

---

# Coding Standards

Use clear names.

Write modular code.

Keep functions focused.

Avoid duplicated logic.

Add comments only where necessary.

Prefer dependency injection.

---

# Testing

Unit Tests

Integration Tests

API Tests

Event Tests

Performance Tests

Security Tests

---

# Documentation

Major changes must update:

SYSTEM_ARCHITECTURE.md

ROADMAP.md

ENGINE specifications

API Guide

Database Guide

---

# Review Checklist

Architecture

Security

Performance

Documentation

Tests

Events

Backward compatibility

---

# Engineering Values

Build Once.

Reuse Everywhere.

Protect Trust.

Optimise Continuously.

Think Platform.

Think Long-Term.

Every commit should improve the platform.