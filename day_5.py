
def decode_morse(morse_code, type):
    morse_code_array = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '-----': '0',
    '.-.-.-': '.',
    '--..--': ',',
    '..--..': '?',
    '.----.': "'",
    '-.-.--': '!',
    '-..-.': '/',
    '-.--.': '(',
    '-.--.-': ')',
    '.-...': '&',
    '---...': ':',
    '-.-.-.': ';',
    '-...-': '=',
    '.-.-.': '+',
    '-....-': '-',
    '..--.-': '_',
    '.-..-.': '"',
    '...-..-': '$',
    '.--.-.': '@'
}
    

    if type == "decode":
        def get_word(morse):
            final_message = []
            for i in morse.split():
                for code, letter in morse_code_array.items():
                    if code == i:
                        final_message.append(letter)

            return "".join(final_message)
    
    
        final_message = []

        for i in morse_code.split("   ") :
            final_message.append(get_word(i))

        final_message = " ".join(final_message)

        return final_message.strip()
    
    elif type == "encode":
        final_message = []
        
        
        def get_word_code(word):
            
            final_word = []
            
            for i in word.upper():
                for code, letter in morse_code_array.items():
                    if i == letter:
                        final_word.append(code)
            return final_word
        
        
        for i in morse_code.split():
            final_message.append(" ".join(get_word_code(i)))
         
         
        the_message = "   ".join(final_message).strip()
         
        with open("my_codes", mode="a") as my_data:
            my_data.write(f"{morse_code.upper()}: {the_message}\n")
        return the_message
             
    
    
    
    
    
       
print(decode_morse("Fuck Samadzai and all the motherfucking teachers, except the good ones." ,"encode"))



# def decodeMorse(morseCode):
#     return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))