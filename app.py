import datetime
import pam
from flask import (
    Flask, 
    jsonify, 
    request,
)
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt_identity,
    jwt_required,
    get_jwt,
)


class config:
    SECRET_KEY = 'some-secret-key'
    JWT_SECRET_KEY = 'some-secret-key'
    JWT_ERROR_MESSAGE_KEY = 'error'
    JWT_IDENTITY_CLAIM = 'user'
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(hours=2)
    DEBUG = True


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)
    app.jwt = JWTManager(app)

    @app.route('/login', methods=['POST'])
    def login():
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        if pam.authenticate(username, password):
            access_token = create_access_token(identity=username, fresh=True)
            app.logger.info(f"return access token {access_token} for user {username}")
            return jsonify(token=access_token)
        return jsonify({'error': 'bad username or password'}), 401

    @app.route('/inspect')
    @jwt_required()
    def inspect():
        payload = get_jwt()
        app.logger.info(f"return token payload {payload}")
        return jsonify(payload), 200

    @app.route('/user', methods=['GET'])
    @jwt_required()
    def user():
        username = get_jwt_identity()
        app.logger.info(f"return user {username}")
        return jsonify(username=username), 200        

    return app



if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=3000)
