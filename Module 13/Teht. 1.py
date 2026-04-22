from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/alkuluku/<int:luku>')
def alkuluku(luku):
    if luku <= 1:
        return jsonify({"Number": luku, "isPrime": False})

    for i in range(2, int(luku**0.5) + 1):
        if luku % i == 0:
            return jsonify({"Number": luku, "isPrime": False})

    return jsonify({"Number": luku, "isPrime": True})


app.run(host='127.0.0.1', port=3000, use_reloader=True)