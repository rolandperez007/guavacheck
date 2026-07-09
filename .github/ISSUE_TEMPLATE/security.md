# Security Policy

# guavacheck Security Policy

Version: 1.0

Status: Active

Owner: Guava Inc.

Classification: Repository Security

---

# Security First

Security is a foundational principle of guavacheck.

Protecting user trust, platform integrity and infrastructure reliability is considered a primary engineering responsibility.

Every contributor shares responsibility for maintaining the security of the platform.

---

# Supported Versions

The following versions receive security updates.

| Version | Supported |
|----------|-----------|
| Current Main Branch | ✅ Yes |
| Latest Production Release | ✅ Yes |
| Previous Major Release | ✅ Critical Fixes Only |
| Older Releases | ❌ No |

---

# Reporting a Vulnerability

Please **do not** create a public GitHub Issue for security vulnerabilities.

Instead, report vulnerabilities privately.

Security reports should include:

- Description of the issue
- Steps to reproduce
- Potential impact
- Affected components
- Proof of concept (if available)
- Suggested mitigation (optional)

---

# Contact

Security Team

Email:

security@guavacheck.com

Alternate Contact:

legal@guavacheck.com

---

# What to Expect

After receiving a report we will:

- Acknowledge receipt.
- Validate the issue.
- Assess severity.
- Develop a fix.
- Test the fix.
- Deploy the fix.
- Notify the reporter when appropriate.

We aim to acknowledge reports within **72 hours**.

---

# Responsible Disclosure

We encourage responsible disclosure.

Please:

- Give us reasonable time to investigate.
- Avoid public disclosure before a fix is available.
- Do not access or modify user data beyond what is necessary to demonstrate the issue.
- Do not disrupt production services.

---

# Out of Scope

The following generally do not qualify as security vulnerabilities:

- Typographical errors
- UI suggestions
- Feature requests
- Low-impact informational findings
- Vulnerabilities in unsupported versions

---

# Security Principles

guavacheck follows these principles:

- Least Privilege
- Defense in Depth
- Zero Trust Mindset
- Secure by Default
- Privacy by Design
- Encryption in Transit
- Encryption at Rest
- Continuous Monitoring
- Verified Backups
- Disaster Recovery Planning

---

# Infrastructure

Security protections include:

- Protected GitHub branches
- Code reviews
- Secret management
- Environment isolation
- Dependency monitoring
- Continuous Integration
- Automated testing
- Database backups
- Restore verification
- Audit logging

---

# Contributor Responsibilities

Contributors must never commit:

- Passwords
- API Keys
- Access Tokens
- Private Keys
- Database Credentials
- Production Secrets
- Customer Data
- Sensitive Configuration

Environment variables must be used for secrets.

---

# Artificial Intelligence

Austin™ must never expose:

- Internal secrets
- Credentials
- Tokens
- Private infrastructure
- Confidential customer information

Austin should always prioritize security over convenience.

---

# Legal Notice

Unauthorized attempts to compromise production infrastructure, access user data or interfere with platform operations may result in access restrictions and legal action where appropriate.

---

# Security Philosophy

Security is not a feature.

It is a continuous engineering discipline.

Every release should leave the platform more secure than the previous one.

---

© 2026 Guava Inc.

Intelligence with integrity.

Technology with purpose.

Trust above everything.