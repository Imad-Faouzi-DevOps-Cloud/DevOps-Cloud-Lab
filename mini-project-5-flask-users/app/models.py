from flask_sqlalchemy import SQLAlchemy

# This creates an instance of SQLAlchemy to be used across the app
db = SQLAlchemy()

# This is our User model — it maps to a 'users' table in PostgreSQL
class User(db.Model):
    __tablename__ = 'users'  # Optional: set the table name explicitly

    id = db.Column(db.Integer, primary_key=True)  # Auto-incrementing ID
    name = db.Column(db.String(100), nullable=False)  # Name column (required)

    def __repr__(self):
        return f"<User {self.name}>"

