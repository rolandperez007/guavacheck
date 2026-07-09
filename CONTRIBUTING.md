# CONTRIBUTING.md

# Contributing to guavacheck

Welcome to the guavacheck project.

Thank you for your interest in helping build one of the world's most ambitious property and infrastructure intelligence platforms.

This document explains how contributions should be made to ensure the platform remains secure, maintainable and consistent.

---

# Before You Begin

Please read the following documents before making significant changes:

README.md

AUSTIN.md

GUAVA_DOCTRINE.md

UI_BIBLE.md

ARCHITECTURE.md

ENGINES.md

API.md

CODE_OF_CONDUCT.md

These documents define the philosophy and standards of the platform.

---

# Guiding Principle

Every contribution should improve at least one of the following:

Trust

Performance

Reliability

Security

Maintainability

Scalability

Developer Experience

User Experience

If a contribution improves none of these, reconsider it.

---

# Development Workflow

1.

Fork or clone the repository.

2.

Create a new feature branch.

Example:

feature/property-search

bugfix/auth-refresh

docs/austin-update

refactor/engineering-engine

3.

Keep commits focused.

Avoid unrelated changes in the same commit.

4.

Open a Pull Request.

5.

Respond to review feedback professionally.

---

# Branch Naming

Examples

feature/user-verification

feature/austin-memory

feature/engineering-engine

bugfix/login-loop

bugfix/api-timeout

docs/readme-update

docs/ui-bible

refactor/property-engine

hotfix/payment-service

---

# Commit Messages

Use clear commit messages.

Examples

feat: add engineering estimation engine

fix: resolve authentication refresh bug

docs: update Austin doctrine

refactor: simplify property routing

perf: optimize map rendering

security: improve token validation

test: add verification engine tests

Avoid messages like:

update

changes

fix stuff

misc

done

---

# Pull Requests

A Pull Request should explain:

What changed

Why it changed

How it was tested

Any known limitations

Screenshots if UI changed

Documentation updates if required

---

# Code Style

Code should be:

Readable

Consistent

Modular

Well named

Documented where necessary

Avoid unnecessary complexity.

Simple solutions usually scale better.

---

# Documentation

Every significant feature should include documentation.

Documentation should be updated when:

Architecture changes

New APIs are introduced

Austin behavior changes

Engine responsibilities change

Security procedures change

Documentation is part of the product.

---

# Austin

Austin is the central intelligence.

Contributors should avoid embedding business logic inside Austin.

Austin should:

Understand intent

Select engines

Coordinate engines

Explain results

Monitor operations

Business logic belongs inside engines.

---

# Engine Development

Each engine should:

Have a single responsibility.

Remain independently testable.

Expose clean interfaces.

Avoid unnecessary dependencies.

Register through Austin.

Every new engine should include:

Documentation

Configuration

Tests

Health checks

Logging

Version information

---

# Security

Never commit:

Passwords

Secrets

Private keys

Tokens

Database credentials

Certificates

Environment files

Sensitive customer data

Use environment variables.

Review security implications before submitting code.

---

# Testing

Before submitting changes:

Run linting.

Run unit tests.

Run integration tests.

Verify affected workflows.

Confirm documentation remains accurate.

Production stability is more important than development speed.

---

# Performance

Avoid introducing:

Unnecessary database queries

Large bundle sizes

Blocking operations

Memory leaks

Duplicate calculations

Performance should improve over time.

---

# User Experience

Every interface should remain:

Simple

Accessible

Responsive

Predictable

Professional

Complex engineering should remain behind the interface.

---

# Reviews

Code reviews exist to improve quality.

Review feedback should:

Remain respectful

Explain reasoning

Suggest improvements

Focus on code

Not individuals

The objective is a better platform.

---

# Version Control

Never rewrite published history without team approval.

Avoid force pushes to protected branches.

Keep history understandable.

Future engineers should understand why changes were made.

---

# Issues

When reporting an issue include:

Description

Expected behaviour

Actual behaviour

Steps to reproduce

Logs if available

Screenshots when useful

Platform information

---

# Feature Requests

Feature requests should explain:

Problem

Proposed solution

Alternatives considered

Expected user value

Architectural impact

Features should solve real problems.

---

# Philosophy

We build for decades.

Not for demonstrations.

Not for temporary trends.

Every contribution should move guavacheck closer to becoming the world's most trusted operating intelligence for property and infrastructure.

---

# Thank You

Every contribution strengthens the platform.

Every improvement helps future users.

Every engineer helps shape the future of guavacheck.

We appreciate your professionalism, curiosity and commitment.

---

© 2026 Guava Inc.

Intelligence with integrity.

Technology with purpose.

Trust above everything.