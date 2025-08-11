"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, send_from_directory
from flask_migrate import Migrate
from flask_swagger import swagger
from api.utils import APIException, generate_sitemap
from api.models import db
from api.routes import api
from api.admin import setup_admin
from api.commands import setup_commands

from flask_cors import CORS

# importa la instancia de SQLAlchemy y tus modelos
from api.models import db  # asegúrate de NO recrear db en models.py
# importa tu Blueprint principal (ajusta el nombre si es distinto)
from api.routes import api as api_bp
# registra comandos CLI (insert-test-data, etc.)
from api.commands import setup_commands

# from models import Person

ENV = "development" if os.getenv("FLASK_DEBUG") == "1" else "production"
static_file_dir = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), '../dist/')
app = Flask(__name__)
app.url_map.strict_slashes = False

# database condiguration
db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace(
        "postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db, compare_type=True)
db.init_app(app)

#################


def create_app():
    app = Flask(__name__)

    # ---- Config ----
    # Usa .env / variables de entorno; cae en SQLite para dev
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL", "sqlite:///dev.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False

    # ---- Extensiones ----
    db.init_app(app)
    Migrate(app, db)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # ---- Rutas / Blueprints ----
    app.register_blueprint(api_bp, url_prefix="/api")

    # ---- Comandos CLI ----
    setup_commands(app)

    # ---- Rutas de salud (opcional) ----
    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

    return app


# Opción para ejecutar directamente: `python -m flask --app src.app:create_app run`
if __name__ == "__main__":
    # Útil si quieres ejecutar sin Pipenv scripts
    app = create_app()
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 3001)), debug=True)
