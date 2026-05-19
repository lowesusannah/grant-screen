# Grant Screen API & CI/CD Pipeline

A Python-based microservice designed to streamline the grant-making process by automatically identifying proposals that require manual due diligence based on a financial threshold. 

This project serves as a DevOps portfolio piece demonstrating automated unit testing, code linting, and containerization using a GitHub Actions Continuous Integration (CI) pipeline.

## Features

- **Automated Grant Screening:** Uses a FastAPI backend to instantly validate grant applications and flag requests over a set threshold (e.g., $50,000) for manual audit.
- **Continuous Integration:** A multi-job GitHub Actions workflow that automatically lints code, runs unit tests, and verifies Docker container builds on every push or pull request.
- **Containerized Architecture:** Fully Dockerized to ensure consistent deployment environments across local development and cloud infrastructure.

## Tech Stack

- **Language:** Python 3.10
- **Framework:** FastAPI & Pydantic
- **Testing:** Pytest & HTTPX
- **DevOps & CI/CD:** GitHub Actions, Docker, Flake8

---

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Docker (optional, for containerized running)

### Local Installation & Testing

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/lowesusannah/grant-screen.git](https://github.com/lowesusannah/grant-screen.git)
   cd grant-screen
   ```
2. **Install dependencies:**
  ```bash
pip  install fastapi uvicorn pytest httpx flake8
```
3. **Run the test suite locally:**
   ```bash
   pytest
   ```
4. **Spin up the API locally:**
   ```bash
   uvicorn main:app --reload
   ```
Once running, you can view the interactive API documentation at
```http://127.0.org:8000/docs```

##Docker Deployment
To build and run the application as an isolated container:

1. **Build the Docker image:**
   ```Bash
   docker build -t grant-screen-api .
   ```
2. **Run the Container**
   ```bash
   docker run -p 8000:8000 grant-screen-api




## CI/CD Pipeline Architecture
The automated workflow inside ```.github/workflows/ci.yml``` triggers on all branch pushes and pull requests. It runs two parallel stages to enforce code quality and delivery stability:

1. **Lint & Test Job:**
   - Sets up a Python environment.
   - Runs flake8 to catch syntax errors or style deviations.
   - Executes pytest against test_main.py to ensure the core validation logic passes.
2. **Container Build Verification Job:**
 - Depends on the Lint & Test job passing successfully.
 - Sets up Docker Buildx.
 - Tests the Dockerfile build sequence to ensure the application safely packages without errors.
   

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## AI Disclosure

Google Gemini and GitHub Copilot were invovled in brainstorming, drafting code frameworks, and writing documentation for this project. Final decisions were made by a human.

## Support

For support, please open an issue in the repository.
