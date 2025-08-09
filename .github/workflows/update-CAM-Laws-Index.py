name: Auto-Update Laws Index

on:
  push:
    paths:
      - "Governance/Laws/**"
      - ".github/workflows/update-CAM-Laws-Index.yml"
      - "Scripts/update-CAM-Laws-Index.py"
  pull_request:
    paths:
      - "Governance/Laws/**"

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write  # required for committing changes
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Run laws index updater
        run: |
          python -m pip install --upgrade pip
          python Scripts/update-CAM-Laws-Index.py

      - name: Commit changes (if any)
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "[AUTO][Laws] Updated CAM-Laws-Index.md (sorted, summaries)"
          file_pattern: Governance/Laws/CAM-Laws-Index.md
