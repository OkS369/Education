morse = {'A': '.-',
         'B': '-...',
         'C': '-.-.',
         'D': '-..',
         'E': '.',
         'F': '..-.',
         'G': '--.',
         'H': '....',
         'I': '..',
         'J': '.---',
         'K': '-.-',
         'L': '.-..',
         'M': '--',
         'N': '-.',
         'O': '---',
         'P': '.--.',
         'Q': '--.-',
         'R': '.-.',
         'S': '...',
         'T': '-',
         'U': '..-',
         'V': '...-',
         'W': '.--',
         'X': '-..-',
         'Y': '-.--',
         'Z': '--..',
         
         'А': '.−',
         'Б': '−...',
         'В': '.−−',
         'Г': '−−.',
         'Д': '−..',
         'Е': '.',
         'Ё': '.',
         'Є': '..−..',
         'ж': '...−',
         'З': '−−..',
         'И': '−.−−',
         'І': '..',
         'Ї': '.−−−.',
         'Й': '.−−−',
         'К': '−.−',
         'Л': '.−..',
         'М': '−−',
         'Н': '−.',
         'О': '−−−',
         'П': '.−−.',
         'Р': '.−.',
         'С': '...',
         'Т': '−',
         'У': '..−',
         'Ф': '..−.',
         'Х': '....',
         'Ц': '−.−.',
         'Ч': '−−−.',
         'Ш': '−−−−',
         'Щ': '−−.−',
         'Ь': '--.--',
         'Ы': '-.--',
         'Э': '..-..',
         'Ь': '−..−',
         'Ю': '..−−',
         'Я': '.−.−',

         '1': '.----',
         '2': '..---',
         '3': '...--',
         '4': '....-',
         '5': '.....',
         '6': '-....',
         '7': '--...',
         '8': '---..',
         '9': '----.',

         '.': '......',
         ',': '.-.-.-',
         ':': '---...',
         ';': '-.-.-.',
         '(': '-.--.-',
         ')': '-.--.-',
         "'": '.----.',
         '"': '.-..-.',
         '-': '-....-',
         '/': '-..-.',
         '\'': '-..-.',
         '?': '..--..',
         '!': '--..--',
         ' ': '-...-',
         '@': '.--.-.',
         }
morse_l = morse = {
         'A': '.-',
         'B': '-...',
         'C': '-.-.',
         'D': '-..',
         'E': '.',
         'F': '..-.',
         'G': '--.',
         'H': '....',
         'I': '..',
         'J': '.---',
         'K': '-.-',
         'L': '.-..',
         'M': '--',
         'N': '-.',
         'O': '---',
         'P': '.--.',
         'Q': '--.-',
         'R': '.-.',
         'S': '...',
         'T': '-',
         'U': '..-',
         'V': '...-',
         'W': '.--',
         'X': '-..-',
         'Y': '-.--',
         'Z': '--..',

         '1': '.----',
         '2': '..---',
         '3': '...--',
         '4': '....-',
         '5': '.....',
         '6': '-....',
         '7': '--...',
         '8': '---..',
         '9': '----.',

         '.': '......',
         ',': '.-.-.-',
         ':': '---...',
         ';': '-.-.-.',
         '(': '-.--.-',
         ')': '-.--.-',
         "'": '.----.',
         '"': '.-..-.',
         '-': '-....-',
         '/': '-..-.',
         '\'': '-..-.',
         '?': '..--..',
         '!': '--..--',
         ' ': '-...-',
         '@': '.--.-.',
         }

morse_c = morse = {
         
         'А': '.−',
         'Б': '−...',
         'В': '.−−',
         'Г': '−−.',
         'Д': '−..',
         'Е': '.',
         'Ё': '.',
         'Є': '..−..',
         'ж': '...−',
         'З': '−−..',
         'И': '−.−−',
         'І': '..',
         'Ї': '.−−−.',
         'Й': '.−−−',
         'К': '−.−',
         'Л': '.−..',
         'М': '−−',
         'Н': '−.',
         'О': '−−−',
         'П': '.−−.',
         'Р': '.−.',
         'С': '...',
         'Т': '−',
         'У': '..−',
         'Ф': '..−.',
         'Х': '....',
         'Ц': '−.−.',
         'Ч': '−−−.',
         'Ш': '−−−−',
         'Щ': '−−.−',
         'Ь': '--.--',
         'Ы': '-.--',
         'Э': '..-..',
         'Ь': '−..−',
         'Ю': '..−−',
         'Я': '.−.−',

         '1': '.----',
         '2': '..---',
         '3': '...--',
         '4': '....-',
         '5': '.....',
         '6': '-....',
         '7': '--...',
         '8': '---..',
         '9': '----.',

         '.': '......',
         ',': '.-.-.-',
         ':': '---...',
         ';': '-.-.-.',
         '(': '-.--.-',
         ')': '-.--.-',
         "'": '.----.',
         '"': '.-..-.',
         '-': '-....-',
         '/': '-..-.',
         '\'': '-..-.',
         '?': '..--..',
         '!': '--..--',
         ' ': '-...-',
         '@': '.--.-.',
         }

m_c, m_s = [], []
for i in morse_l.keys():
    m_s += i
    m_c.append(morse_l[i])
print(m_s)   
print(m_c)
morse = dict(zip(m_s,m_c))
demorse = dict(zip(m_c,m_s))
print(morse)   
print(demorse)
