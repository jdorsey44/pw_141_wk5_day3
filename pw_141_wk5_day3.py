from flask import Flask
from flask_smorest import Api

app = Flask(__name__)
api = Api(app)
from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)

class PostSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    author = fields.Nested(UserSchema, only=('id', 'username'), required=True)
from flask.views import MethodView
from flask_smorest import Blueprint

user_bp = Blueprint('users', 'users', url_prefix='/users')
post_bp = Blueprint('posts', 'posts', url_prefix='/posts')

@user_bp.route('/')
class Users(MethodView):
    @user_bp.response(200, UserSchema(many=True))
    def get(self):
        # Implement logic to get all users
        pass

    @user_bp.arguments(UserSchema)
    @user_bp.response(201, UserSchema)
    def post(self, new_user):
        # Implement logic to create a new user
        pass

@post_bp.route('/')
class Posts(MethodView):
    @post_bp.response(200, PostSchema(many=True))
    def get(self):
        # Implement logic to get all posts
        pass

    @post_bp.arguments(PostSchema)
    @post_bp.response(201, PostSchema)
    def post(self, new_post):
        # Implement logic to create a new post
        pass

api.register_blueprint(user_bp)
api.register_blueprint(post_bp)    