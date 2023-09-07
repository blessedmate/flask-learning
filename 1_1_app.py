from flask import Flask, jsonify, request


app = Flask(__name__)
app.debug = True


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/super_simple")
def super_simple():
    return jsonify(message="Hello from the Planetary API")


@app.route("/not_found")
def not_found():
    return jsonify(message="That resource was not found"), 404


@app.route("/parameters")
def parameters():
    name = request.args.get("name")
    age = int(request.args.get("age"))
    if age < 18:
        return jsonify(message="Not old enough"), 401
    else:
        return jsonify(message=f"Welcome {name}")


if __name__ == "__main__":
    app.run()
