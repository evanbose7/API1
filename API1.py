from flask import Flask ,request, jsonify


app = Flask(__name__) # for creating flask application#

@app.route('/')
def home():
    return 'Home'
@app.route('/Evan')
def evan():
    return 'Evan'

if __name__ == '__main__': #for initializing flask application#
    app.run(debug=True)
    

