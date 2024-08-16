from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/change', methods=['POST'])
def change(dollar):
    # finding the number of coins
    dollar = request.json['dollar']
    dollar = int(dollar)
    coins = [25, 10, 5, 1]
    change = []
    for coin in coins:
        while dollar >= coin:
            change.append(coin)
            dollar -= coin
    return jsonify({'change': change})


@app.route('/', methods=['GET'])
def hello():
    return "Hello World! I can make changes at route : /change"

if __name__ == '__main__':
    app.run(debug=True)
