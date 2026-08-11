# Playwright Python Testing Project

![API Tests](https://github.com/jeetshah07/Playwright_Python_Project/actions/workflows/tests.yml/badge.svg)

Automated test suite for [automationexercise.com](https://automationexercise.com), covering both UI testing (Page Object Model) and API testing, built with Playwright and Pytest. Includes CI/CD via GitHub Actions and reporting via pytest-html and Allure.

## Tech Stack

- **Python 3.12**
- **Playwright** (sync API) — browser automation and HTTP client
- **Pytest** — test runner
- **pytest-html** — HTML test reports
- **Allure** — interactive test reports
- **GitHub Actions** — CI/CD
## Setup

1. Clone the repository:
```bash
   git clone https://github.com/jeetshah07/Playwright_Python_Project.git
   cd Playwright_Python_Project
```

2. Create and activate a virtual environment:
```bash
   python -m venv venv
   venv\Scripts\activate
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
   playwright install
```

## Running Tests

Run everything (UI + API):
```bash
pytest -v
```

Run only API tests:
```bash
pytest api_tests -v
```

Run only UI tests:
```bash
pytest tests -v
```

## Reports

**HTML Report** — generated automatically at `reports/report.html` on every run (self-contained, viewable in any browser):
```bash
start reports\report.html
```

**Allure Report** — raw results generated at `allure-results/` on every run. View locally with:
```bash
allure serve allure-results
```

**Live Allure Report (CI)** — the latest report from the most recent GitHub Actions run is published here:
[https://jeetshah07.github.io/Playwright_Python_Project/](https://jeetshah07.github.io/Playwright_Python_Project/)

## CI/CD

Every push to `main` automatically triggers a GitHub Actions workflow that:
1. Installs dependencies in a clean environment
2. Runs the full API test suite
3. Publishes the HTML report and Allure results as artifacts
4. Publishes the Allure report to GitHub Pages

See `.github/workflows/tests.yml` for the full pipeline definition.

## Test Coverage

**API Tests (16 total):**
- Product listing and search (including parametrized search terms)
- Full account CRUD lifecycle (create, read, update, delete)
- Negative/edge cases — invalid login, missing parameters, wrong HTTP methods, duplicate account creation

**UI Tests:** Login, registration, logout, cart, subscription, and product browsing flows via Page Object Model.