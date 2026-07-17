# Intent Engine

**Version:** 1.0.0

**Status:** Living Document

---

# Purpose

The Intent Engine is responsible for understanding what the user is trying to achieve.

Rather than reacting to individual words, the engine identifies objectives, constraints and expected outcomes.

Intent recognition is the foundation of every Austin interaction.

---

# Responsibilities

The Intent Engine shall:

- Identify user goals.
- Detect ambiguity.
- Understand conversational context.
- Recognize follow-up questions.
- Classify request types.
- Extract structured information.
- Determine confidence levels.

---

# Supported Intent Categories

Austin currently recognizes multiple categories of intent.

Examples include:

- Buy Property
- Sell Property
- Rent Property
- Estimate Construction Cost
- Generate Building Design
- Renovate Existing Building
- Analyze Investment
- Compare Properties
- Verify Documents
- Research Locations
- Ask General Questions
- Enterprise Planning

Additional intent categories should be introduced without affecting existing classifications.

---

# Inputs

The engine accepts:

- Natural language
- Structured JSON
- Images
- Documents
- Voice transcripts
- Platform events

---

# Outputs

The engine produces:

- Intent classification
- Confidence score
- Extracted entities
- Missing information
- Recommended next actions

---

# Design Principles

Intent detection should prioritize understanding over assumption.

When uncertainty exists, Austin should request clarification rather than making unsupported assumptions.

---

# Future Evolution

Future versions may support:

- Multi-intent conversations.
- Predictive intent.
- Collaborative intent recognition.
- Emotional context awareness.