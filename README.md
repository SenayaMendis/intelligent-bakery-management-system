# Intelligent Bakery Management System

A centralized web-based system proposed to manage bakery operations across multiple branches. It aims to go beyond basic operational management by analysing business data and providing intelligent recommendations.

> **Project status:** Initial setup / under development. Features and technologies described here represent the proposed project scope and may be refined during implementation.

## Project Goals

- Improve coordination and operational efficiency across multiple bakery branches.
- Support inventory, procurement, production, ordering, and delivery decisions.
- Reduce unnecessary purchasing and food wastage.
- Use forecasting, machine learning, and AI-assisted insights to support managers.

## Main Modules

1. **Product and Recipe Management**
2. **Intelligent Inventory and Procurement Management**
3. **Intelligent Production Planning and Demand Forecasting**
4. **Intelligent Online Ordering and Order Management**
5. **Intelligent Delivery and Logistics Management**
6. **AI-Powered Customer Support and Business Intelligence**

## Key Intelligent Features

- **Smart Stock Transfers:** Recommend a suitable supplying branch using stock availability and upcoming requirements.
- **Predictive Procurement:** Recommend purchasing quantities and suitable suppliers.
- **Smart Production:** Forecast demand and recommend production quantities.
- **Intelligent Order Assignment:** Check stock, ingredients, and production capacity before recommending a branch.
- **Smart Discounts:** Recommend discounts for products nearing expiry to help reduce wastage.
- **Automated Branch Monitoring:** Provide business insights and highlight operational issues.
- **AI-Powered Business Assistant:** Explain information retrieved from the system and answer administrative questions.

## Proposed Technology Stack

| Area | Technology |
|---|---|
| Frontend | React.js |
| Backend API | Node.js, Express.js |
| Database | PostgreSQL |
| Machine-learning service | Python, FastAPI |
| Forecasting and data analysis | Pandas, Scikit-learn; Prophet may be evaluated for sales forecasting |
| Maps and branch assignment | Google Maps Platform: Geocoding API and Distance Matrix API |
| AI business assistant | Gemini API or OpenAI API (to be finalized) |
| Version control | Git and GitHub |

## Proposed Repository Structure

```text
intelligent-bakery-management-system/
├── frontend/                 # React user interface
├── backend/                  # Node.js and Express REST API
├── ml-service/               # Python and FastAPI services
├── database/                 # SQL scripts, migrations, and seed data
├── docs/                     # Project documentation and diagrams
├── .gitignore
└── README.md
```

## Prerequisites

Install Git, Node.js LTS (includes npm), Python 3.11 or compatible newer version, PostgreSQL, and an IDE such as Visual Studio Code.

Check the installations:

```bash
git --version
node --version
npm --version
python --version
psql --version
```

On Windows, you can also check Python with `py --version`.

## Initial Setup

### 1. Clone the repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd intelligent-bakery-management-system
```

Create an empty GitHub repository first if you have not already done so.

### 2. Create the project folders

Run from the repository root:

```bash
mkdir frontend backend ml-service database docs
```

### 3. Set up the React frontend

```bash
cd frontend
npm create vite@latest . -- --template react
npm install
npm run dev
```

Open the local URL shown in the terminal. Stop the server with `Ctrl + C`.

### 4. Set up the Node.js and Express backend

Open a new terminal at the repository root:

```bash
cd backend
npm init -y
npm install express cors dotenv pg
npm install --save-dev nodemon
```

Create `backend/server.js`:

```javascript
const express = require("express");
const cors = require("cors");
require("dotenv").config();

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());

app.get("/api/health", (req, res) => {
  res.json({ message: "Bakery Management API is running" });
});

app.listen(PORT, () => {
  console.log(`Backend server running on port ${PORT}`);
});
```

In `backend/package.json`, set the scripts to:

```json
"scripts": {
  "start": "node server.js",
  "dev": "nodemon server.js"
}
```

Start the backend:

```bash
npm run dev
```

Test it at `http://localhost:5000/api/health`.

### 5. Create the PostgreSQL database

Using pgAdmin or the PostgreSQL command line, create:

```sql
CREATE DATABASE intelligent_bakery_db;
```

Create `backend/.env`:

```env
PORT=5000
DATABASE_URL=postgresql://YOUR_USERNAME:YOUR_PASSWORD@localhost:5432/intelligent_bakery_db
```

Replace the placeholders with your local PostgreSQL credentials.

> Never commit `.env` files, passwords, or API keys. Use an `.env.example` file with placeholders when documenting required variables.

### 6. Set up the Python machine-learning service

From the repository root:

```bash
cd ml-service
py -m venv .venv
```

Activate on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

On Windows Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

Install the initial packages:

```bash
pip install fastapi uvicorn pandas scikit-learn
```

Create `ml-service/main.py`:

```python
from fastapi import FastAPI

app = FastAPI(title="Bakery ML Service")

@app.get("/health")
def health_check():
    return {"message": "Bakery ML service is running"}
```

Run the service:

```bash
python -m uvicorn main:app --reload --port 8000
```

Open `http://localhost:8000/docs` to view the FastAPI documentation.

Save installed dependencies:

```bash
pip freeze > requirements.txt
```

### 7. Add a root `.gitignore`

Create `.gitignore` in the repository root:

```gitignore
# Node dependencies
node_modules/

# Secrets and environment files
.env
.env.*
!.env.example

# Python
.venv/
__pycache__/
*.py[cod]

# Build output
dist/
build/

# Logs
*.log
npm-debug.log*

# IDE and operating system files
.vscode/
.idea/
.DS_Store
Thumbs.db
```

### 8. Commit and push the initial setup

Run from the repository root:

```bash
git add .
git commit -m "chore: initialize project structure and services"
git branch -M main
git push -u origin main
```

If you created the GitHub repository with an initial README or other files, you may need to pull and reconcile those changes before pushing.

## Running the Services

Run each service in a separate terminal:

| Service | Folder | Command | Local address |
|---|---|---|---|
| React frontend | `frontend/` | `npm run dev` | Vite URL shown in terminal |
| Express backend | `backend/` | `npm run dev` | `http://localhost:5000` |
| FastAPI ML service | `ml-service/` | `python -m uvicorn main:app --reload --port 8000` | `http://localhost:8000` |

PostgreSQL must also be running.

## Development Notes

- The React frontend communicates with the Node.js backend through API endpoints.
- The Node.js backend handles business rules and database access.
- The Node.js backend calls FastAPI when a machine-learning prediction or analysis is needed.
- Store external API keys in environment variables; never commit them.
- Use realistic sample data for development and testing. Do not upload private customer or business data.
- Add authentication, role-based access control, database migrations, validation, automated tests, and deployment configuration as development progresses.

## License

A license has not been selected yet. Add one only after deciding how the project may be used and shared.
