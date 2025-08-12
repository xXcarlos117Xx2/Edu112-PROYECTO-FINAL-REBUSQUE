from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_migrate import Migrate

db = SQLAlchemy()  


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)

    def serialize(self):
        return {"id": self.id, "email": self.email}

class ClientProfile(db.Model):
    __tablename__ = "client_profiles"
    id = db.Column(db.Integer, primary_key=True)

class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)


class ServiceRequest(db.Model):  # solicitud de servicio
    __tablename__ = "service_requests"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(140), nullable=False)
    status = db.Column(db.String(20), nullable=False, default="new")
    client_id = db.Column(db.Integer, db.ForeignKey("client_profiles.id"), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "client_id": self.client_id,
            "category_id": self.category_id,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }

class WorkerProfile(db.Model):
    __tablename__ = "worker_profiles"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, unique=True)
    full_name = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(120), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "full_name": self.full_name,
            "city": self.city
        }