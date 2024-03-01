import flask

from po2.src import structure
from po2.src.logic import Logic

app = flask.Flask(__name__)
logic = Logic()


def validate_user(user):
    try:
        structure.User(**user)
        return True
    except structure.pydantic.ValidationError:
        return False
@app.route('/users', methods=['GET'])
def get_users():
    return logic.get_users(), 200

@app.route('/users', methods=['POST'])
def add_user():
    data = flask.request.json
    if not data:
        return {"error": "Nie podano danych"}, 400
    if not validate_user(data):
        return {"error": "Nie znaleziono użytkownika"}, 400
    logic.add_user(data)
    return {}, 201

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = logic.get_user(user_id)
    if not user:
        return {"error": "User not found"}, 404
    return user, 200

@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    data = flask.request.json
    if not data:
        return {"error": "Nie podano danych"}, 400
    if not validate_user(data):
        return {"error": "Błąd walidacji"}, 400
    return logic.update_user(user_id, data), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if not logic.delete_user(user_id):
        return {"error": "Nie znaleziono użytkownika"}, 404
    return {}, 200


if __name__ == '__main__':
    app.run()