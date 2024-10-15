from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diary', methods=['GET'])
def show_diary():
    sample_receive = request.args.get('sample_give')
    print(sample_receive)
    return jsonify({'msg': 'GET request complete!'})

@app.route('/diary', methods=['POST'])
def save_diary():
    titleReceive = request.form['title']
    content_receive = request.form["desc"]

    if not titleReceive or not content_receive:
        return jsonify({'msg': 'Title and description are required!'}), 400
    print(titleReceive)
    print(content_receive)
    return jsonify({'msg': 'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)