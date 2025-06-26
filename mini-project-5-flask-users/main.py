import os
import psycopg2
from app import create_app

# Create the Flask app
app = create_app()

@app.route('/')
def hello():
    return 'Hello, DevOps World!'

if __name__ == '__main__':
    # Use the Cloud Run-assigned port
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# OPTIONAL: Direct connection to Cloud SQL (if you're not using SQLAlchemy)
# Usually handled inside your app with SQLAlchemy if configured via DATABASE_URL
if os.environ.get("GAE_ENV", "").startswith("standard") or os.environ.get("K_SERVICE"):
    try:
        conn = psycopg2.connect(
            host="/cloudsql/devops-lab-464007:us-central1:flask-db-instance",
            dbname="flaskdb",
            user="flaskuser",
            password="FlaskStrongPassword123"
        )
        print("Connected to Cloud SQL.")
    except Exception as e:
        print("Failed to connect to Cloud SQL:", e)
