import json


class CodeMorseDecode(object):
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
            '8': '---..', '9': '----.',
            ' ': '/'
        }


    def decode(self, morse_code_encode):
        if self.validate_message(morse_code_encode):
            code_morse_decoded_string = ''
            for code_morse in morse_code_encode['message'].split(' '):
                for code_morse_value_decoded, code_morse_value in self.morse_code.items():
                    if code_morse == code_morse_value:
                        code_morse_decoded_string += code_morse_value_decoded
                        break
                else:
                    code_morse_decoded_string += code_morse
            return code_morse_decoded_string


    def validate_message(self, json_message):
        if 'message' in json_message:
            return True
        return False