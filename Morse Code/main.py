# First I will need a dictionary that saves morse code alphabets

morse_code = {
    # Letters
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",

    # Numbers
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",

    # Punctuation
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "_": "..--.-",
    '"': ".-..-.",
    "$": "...-..-",
    "@": ".--.-."
}

reverse_morse = {value: key for key, value in morse_code.items()}

def text_to_morse(text):
    translated = []
    for letter in text.upper():
        if letter == " ":
            translated.append("/")
        elif letter in morse_code:
            translated.append(morse_code[letter])
        else:
            translated.append("?")
    return " ".join(translated)

def morse_to_text(morse):
    translated = []
    for word in morse.split(" / "):
        letters = word.split()

        for letter in letters:
            if letter in reverse_morse:
                translated.append(reverse_morse[letter])
            else:
                translated.append("?")

        translated.append(" ")

    return "".join(translated).strip()

running = True

while running:
    print("""
    Morse Translator
    -------------------
    [E2M] English → Morse
    [M2E] Morse → English
    [Q]   Quit
    """)
    question = input("Choose: ").upper()
    if question == "E2M":
        text_input = input("Please enter the English word or sentence here: ")
        result = text_to_morse(text_input)
        print(result)

    elif question == "M2E":
        text_input = input("Please enter the morse code here: ")
        result2 = morse_to_text(text_input)
        print(result2)
    elif question == "Q":
        running = False
    else:
        print("Invalid option. Please choose E2M, M2E, or Q.")