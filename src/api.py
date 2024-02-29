import flask
from po2.src.logic import Logic

app = flask.Flask(__name__)
logic = Logic()


@app.route('/users', methods=['GET', 'POST'])
def get_users():
    if flask.request.method == 'GET':
        return logic.get_users(), 200
    elif flask.request.method == 'POST':
        data = flask.request.json
        if not data:
            return {"error": "Nie podano danych"}, 400
        if not logic.validate_user(data):
            return {"error": "Nie znaleziono użytkownika"}, 400
        logic.add_user(data)
        return {}, 201


@app.route('/users/<int:user_id>', methods=['GET', 'PATCH', 'DELETE'])
def get_user(user_id):
    if flask.request.method == 'GET':
        user = logic.get_user(user_id)
        if not user:
            return {"error": "User not found"}, 404
        return user, 200
    elif flask.request.method == 'PATCH':
        data = flask.request.json
        if not data:
            return {"error": "Nie podano danych"}, 400
        if not logic.validate_user(data):
            return {"error": "Błąd walidacji"}, 400
        return logic.update_user(user_id, data), 200
    elif flask.request.method == 'DELETE':
        if not logic.delete_user(user_id):
            return {"error": "Nie znaleziono użytkownika"}, 404
        return {}, 200


if __name__ == '__main__':
    app.run()
