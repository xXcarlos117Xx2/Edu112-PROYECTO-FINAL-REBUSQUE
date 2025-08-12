# # src/api/commands.py
# import click
# from flask.cli import with_appcontext
# from api.models import db, User, ClientProfile, Category, WorkerProfile, ServiceRequest

# # Profesiones (categorías)
# PROFESIONES = [
#     ("Carpintero",   "carpintero"),
#     ("Fontanero",    "fontanero"),
#     ("Electricista", "electricista"),
#     ("Cristalero",   "cristalero"),
# ]

# @click.command("insert-test-data")
# @with_appcontext
# def insert_test_data():
#     # 1) Profesiones (categorías)
#     for name, slug in PROFESIONES:
#         if not Category.query.filter_by(slug=slug).first():
#             db.session.add(Category(name=name, slug=slug))
#     db.session.commit()

#     # 2) Cliente 
#     cliente = User.query.filter_by(email="cliente@example.com").first()
#     if not cliente:
#         cliente = User(email="cliente@example.com", password="secret", is_active=True)
#         db.session.add(cliente); db.session.flush()
#         db.session.add(ClientProfile(user_id=cliente.id))
#         db.session.commit()

#     # 3) Trabajadores (uno por profesión)
#     trabajadores = [
#         ("Juan Carpintero",  "Madrid",    "carpintero"),
#         ("Ana Fontanera",    "Barcelona", "fontanero"),
#         ("Luis Electricista","Valencia",  "electricista"),
#         ("Marta Cristalera", "Sevilla",   "cristalero"),
#     ]
#     for full_name, city, slug in trabajadores:
#         email = f"{slug}@demo.local"
#         if not User.query.filter_by(email=email).first():
#             u = User(email=email, password="secret", is_active=True)
#             db.session.add(u); db.session.flush()
#             db.session.add(WorkerProfile(user_id=u.id, full_name=full_name, city=city))
#     db.session.commit()

#     # 4) Solicitudes de ejemplo (vinculadas a profesiones)
#     cp = ClientProfile.query.filter_by(user_id=cliente.id).first()
#     ejemplos = [
#         ("Montar estantería de pino", "carpintero"),
#         ("Arreglo de fuga en fregadero", "fontanero"),
#     ]
#     for title, slug in ejemplos:
#         cat = Category.query.filter_by(slug=slug).first()
#         if cat and not ServiceRequest.query.filter_by(title=title).first():
#             db.session.add(ServiceRequest(
#                 title=title, client_id=cp.id, category_id=cat.id, status="new"
#             ))
#     db.session.commit()

#     click.echo("✅ Datos de prueba insertados: profesiones, cliente, 4 trabajadores y solicitudes.")

# # Probar rápido
# # GET /api/categories → debe listar las 4 profesiones.

# # GET /api/workers?city=Madrid → devuelve “Juan Carpintero” (y así con otras ciudades).

# # GET /api/service-requests → verás las solicitudes de ejemplo.