version: 2

updates:

  # ==========================================================
  # Node.js / Next.js
  # ==========================================================
  - package-ecosystem: "npm"

    directory: "/"

    schedule:
      interval: "weekly"

    open-pull-requests-limit: 10

    labels:
      - dependencies
      - security

    commit-message:
      prefix: "deps"

    reviewers:
      - rolandperez007

    assignees:
      - rolandperez007

  # ==========================================================
  # GitHub Actions
  # ==========================================================
  - package-ecosystem: "github-actions"

    directory: "/"

    schedule:
      interval: "weekly"

    labels:
      - github-actions

    commit-message:
      prefix: "ci"

    reviewers:
      - rolandperez007