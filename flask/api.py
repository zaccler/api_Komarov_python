from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello_world', methods=['GET'])
def func():
    data = {
        "1": "Hello World",
        "2": "Гудбай"
    }
    response = jsonify(data)
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response

@app.route('/route_name', methods=['GET'])
def sayHelloWorld():
    pass

users = {
    1: {
        "name": "Alex",
        "age": 25
    },
    2: {
        "name": "Vlad",
        "age": 19
    },
    3: {
        "name": "Max",
        "age": 18
    }
   
}

@app.route('/users/', methods=['GET'])
def returnUserInfo():
    user_id = request.args.get("id")
    if not user_id or not user_id.isdigit():
        return jsonify({"error": "Invalid ID"}), 400

    user_id = int(user_id)
    if user_id in users:
        return jsonify(users[user_id])
    else:
        return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
