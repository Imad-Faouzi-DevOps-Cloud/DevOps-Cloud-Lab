# main.py
import psycopg2
from app import create_app  # Import the factory function

# Create the Flask app instance using the factory
app = create_app()

# Define a simple root route for health check or welcome message
@app.route('/')
def hello():
    return 'Hello, DevOps World!'  # Simple response to verify the server is running

# Run the Flask development server if this file is executed directly
if __name__ == '__main__':
    # host='0.0.0.0' allows access from outside the container or machine
    # debug=True enables hot reload and debug info in dev environment
    app.run(host='0.0.0.0', port=8080, debug=True)

conn = psycopg2.connect(
    host="/cloudsql/devops-lab-464007:us-central1:flask-db-instance",
    dbname="flaskdb",
    user="flaskuser",
    password="FlaskStrongPassword123"
)
