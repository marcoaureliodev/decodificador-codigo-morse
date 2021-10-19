from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cesarsecretkey2021#'
socketio = SocketIO(app)


@app.route('/')
def sessions():
    return render_template('session.html')


def messageReceived(methods=['GET', 'POST']):
    pass


@socketio.on('code morse decode')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    morse = Morse()
    codigo = morse.decode(json['message'])
    socketio.emit('code morse decoded', {'message':codigo}, callback=messageReceived)


class Morse(object):
    def __init__(self):
        self.morse_code = {
            'A': '.-', 'B': '-...',
            'C': '-.-.', 'D': '-..',
            'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....',
            'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.',
            'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-',
            'U': '..-', 'V': '...-',
            'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..',
            '0': '-----', '1': '.----',
            '2': '..---', '3': '...--',
            '4': '....-', '5': '.....',
            '6': '-....', '7': '--...',
            '8': '---..', '9': '----.'
        }

    def decode(self, morsecodeencode):
        codemorsedecodedstring = ''
        for codeMorse in morsecodeencode.split(' '):
            for codeMorseValueDecoded, codeMorseValue in self.morse_code.items():
                if codeMorse == codeMorseValue:
                    codemorsedecodedstring += codeMorseValueDecoded
                    break
        return codemorsedecodedstring


if __name__ == '__main__':
    socketio.run(app, debug=True)
