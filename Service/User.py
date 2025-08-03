from models.user import User, db
from werkzeug.security import generate_password_hash, check_password_hash

def get_all_users():
    return [{'id': u.id, 'name': u.name, 'email': u.email} for u in User.query.all()]

def get_user_by_id(user_id):
    user = User.query.get(user_id)
    return {'id': user.id, 'name': user.name, 'email': user.email} if user else None

def create_user(data):
    if not all(k in data for k in ('name','email','password')): return None
    hashed = generate_password_hash(data['password'])
    new_user = User(name=data['name'], email=data['email'], password=hashed)
    db.session.add(new_user)
    db.session.commit()
    return {'id': new_user.id, 'name': new_user.name, 'email': new_user.email}

def update_user(user_id, data):
    user = User.query.get(user_id)
    if not user: return None
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    if 'password' in data:
        user.password = generate_password_hash(data['password'])
    db.session.commit()
    return {'id': user.id, 'name': user.name, 'email': user.email}

def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    return False

def search_user_by_name(name):
    return [{'id': u.id, 'name': u.name, 'email': u.email} for u in User.query.filter(User.name.like(f'%{name}%')).all()]

def login_user(data):
    user = User.query.filter_by(email=data['email']).first()
    return user and check_password_hash(user.password, data['password'])
  
