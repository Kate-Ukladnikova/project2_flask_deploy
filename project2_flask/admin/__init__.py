from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from project2_flask.models import User, Post
from project2_flask import db
from project2_flask import create_app

app = create_app()

admin = Admin(app)
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
