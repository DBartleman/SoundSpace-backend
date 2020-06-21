from app import app
from app.routes.user import User
from flask import jsonify, request
from functools import wraps
import jwt

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return {'message': 'valid token not found in request.headers'}
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(id=data['id']).first()
        except:
            return {'message': 'token is invalid'}, 401
        return f(current_user=current_user, *args, **kwargs)
    return decorator
