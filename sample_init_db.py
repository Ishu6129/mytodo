from sample_app import app, db

with app.app_context():
    db.create_all()
