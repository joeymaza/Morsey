


MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    ' ': ' '  # Space
}


def morse_translate(message):
    output = ""
    for char in message.upper():
        if char in MORSE_CODE_DICT:
            output += (MORSE_CODE_DICT[char] + " ")
        else:
            return KeyError
    return output.strip()


def morse_decode(morse_message):
    output = ""
    message_text = morse_message.split(' ')
    for message in message_text:
        if message in MORSE_CODE_DICT.values():
            for char, morse_code in MORSE_CODE_DICT.items():
                if morse_code == message:
                    output += char
                    break
        output += " "
    return output.strip()


message_to_encode = input('Type a message or word to encode to Morse: ')
print(morse_translate(message_to_encode))
morse_code_decode = morse_translate(message_to_encode)
print(morse_decode(morse_code_decode))
