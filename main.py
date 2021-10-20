from flask import Flask, render_template
from flask_socketio import SocketIO
from code_morse_decode import CodeMorseDecode

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def sessions():
    return render_template('session.html')

@socketio.on('code morse decode')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    code_morse_decode = CodeMorseDecode()
    translated_code = code_morse_decode.decode(json)
    if translated_code:
        socketio.emit('code morse decoded', {'message': translated_code})

if __name__ == '__main__':
    socketio.run(app, debug=True)
