from flask import Flask, jsonify

app = Flask(__name__)
def alkuluku(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

@app.route('/alkuluku/<int:numero>', methods=['GET'])
def alkuluku_check(numero):
    result = {
        "numero": numero,
        "on_alkuluku": alkuluku(numero)
    }
    return jsonify(result)
if __name__ == '__main__':
    app.run(debug=True, port=3000)