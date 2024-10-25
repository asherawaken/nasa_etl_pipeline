# NASA ETL Project

This project extracts data from NASA APIs, transforms it, and loads it into a PostgreSQL database hosted on AWS RDS. The project also includes a FastAPI microservice to access NASA data.

## Setup

1. Clone the repository.
2. Set up environment variables for the database and API key in `config/settings.py`.
3. Install dependencies:
   ```bash
   pip install fastapi requests boto3 python-dotenv
4. Deploy infrastructure:
cd infrastructure
terraform init
terraform apply
5. Run the FastAPI application:
uvicorn app.main:app --reload