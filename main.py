from flask import Flask, jsonify

app = Flask(__name__)


# new* - checking that the API is set up
@app.route('/')
def ping():
    return jsonify({
        'message': 'hi'
    })

if __name__ == '__main__':
    app.run(port = 5000, debug=True)