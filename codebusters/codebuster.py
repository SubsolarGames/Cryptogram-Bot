# IMPORTS
from wordfreq import word_frequency
import random
import math


# STATIC variables
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
LETTER_FREQ = {
    "E": 0.1210,
    "T": 0.0894,
    "A": 0.0855,
    "O": 0.0747,
    "I": 0.0733,
    "N": 0.0717,
    "S": 0.0673,
    "R": 0.0633,
    "H": 0.0496,
    "L": 0.0421,
    "D": 0.0382,
    "C": 0.0334,
    "U": 0.0273,
    "M": 0.0251,
    "F": 0.0240,
    "P": 0.0214,
    "G": 0.0187,
    "W": 0.0168,
    "Y": 0.0166,
    "B": 0.0148,
    "V": 0.0105,
    "K": 0.0054,
    "X": 0.0023,
    "J": 0.0016,
    "Q": 0.0012,
    "Z": 0.0009
}

# MAIN variables
quotes = []


# FUNCTIONS
def line_to_text(line):
    line = line.replace('"text": ', '')
    line = line.replace('"quoteText": ', '')
    line = line.replace('\\"', "π")
    line = line.replace('"', "")
    line = line[:-1]
    
    return line.lower()


def line_to_length(line):
    line = line.replace('"length": ', '')
    line = line.replace(",", "")
    
    return int(line)


def strip_word(word):
    word = word.replace(",", '')
    word = word.replace(":", '')
    word = word.replace(".", '')
    word = word.replace("!", '')
    word = word.replace("?", '')
    word = word.replace(";", '')
    word = word.replace('"', '')
    word = word.replace(",", '')
    word = word.replace("π", '')
    
    return word


def get_frequence_of_words(line):
    acc = 0
    leng = 0
    for word in line.split(" "):
        word = strip_word(word)
    
        
        if word != "":
            acc += word_frequency(word, "en")
            leng += 1
            
    return acc / leng


def get_avg_word_length(line):
    acc = 0
    leng = 0
    for word in line.split(" "):
        word = strip_word(word)
        
        if word != "":
            acc += len(word)
            leng += 1
    
    return acc / leng


def get_ones(line):
    acc = 0
    for word in line.split(" "):
        word = strip_word(word)
        
        if len(word) == 1:
            acc += 1
    
    return acc


def get_dev_letter_freq(line):

    freq_map = {}
    for letter in line:
        if letter in ALPHABET:
            if letter in freq_map:
                freq_map[letter] += 1
            else:
                freq_map[letter] = 1
    
    acc = 0
    leng = 0         
    for letter in ALPHABET:
        if letter in freq_map.keys():
            leng += 1
            acc += abs(LETTER_FREQ[letter.upper()] - freq_map[letter])
    
    return acc / leng


def get_length(line):
    acc = 0
    for word in line.split(" "):
        word = strip_word(word)
        
        if word != "":
            acc += len(word)
    
    return acc 


def get_difficulty(freq_of_words, avg_word_length, dev_letter_freq, length, ones):
    weight_avg_word_length = 0.1
    weight_dev_letter_freq = 0.3
    weight_freq_of_words = 100
    weight_of_length = 0.005
    weight_of_ones = 0
    negative_weight = 10
    positive_weight = 1
    
    growth_function = lambda x: math.log((x**2) + 1)

    negative = (growth_function(avg_word_length * weight_avg_word_length)) + (growth_function(dev_letter_freq * weight_dev_letter_freq))
    positive = (growth_function(freq_of_words * weight_freq_of_words)) + (growth_function(length * weight_of_length))
    
    return math.sqrt((negative * negative_weight) / (positive * positive_weight)) * 1


def new_solve(cryptogram):
    solve = {}
    for i in ALPHABET:
        solve[i] = "_"
    other_string = ""
    solve_string = ""
    for char in cryptogram[0]:
        if char in ALPHABET:
            solve_string += solve[char]
            
        else:
            solve_string += char
        other_string += " "
        
    solve_string += "\n"
    return [solve, solve_string, [], [], other_string] 


def update_solve(solve, cryptogram):
    solve_string = ""
    other_string = ""
    new_letters =[]
    for char in cryptogram[0]:
        if char in ALPHABET:
            if char not in solve[3] and solve[0][char] != "_":
                new_letters.append(char)
                other_string += "|"
                solve_string += solve[0][char]
            else:
                other_string += " "
                solve_string += solve[0][char]
        else:
            other_string += " "
            solve_string += char
            
    solve_string += "\n"

    return [solve[0], solve_string, new_letters, solve[3]+new_letters, other_string]


def quote_to_code(full_quote):
    quote = full_quote['text']
    key = {}
    prev = []
    
    unused = list(ALPHABET)
    for i in ALPHABET:
        letter = random.choice(unused)
        if len(unused) == 1 and i == letter:
            correct_index = 0
            while unused[0] == prev[correct_index]:
                correct_index += 1
            key[i] = key[prev[correct_index]]
            key[prev[correct_index]] = letter
        else:
                
            while letter == i:
                letter = random.choice(unused)

            key[i] = letter
        
        unused.remove(letter)
        prev.append(i)
        
    for i in key:
        quote = quote.replace(i, key[i].upper())
    quote = quote.replace("π", '"')
    
    return [quote.lower(), dict(map(reversed, key.items())), full_quote]


def check_win(cryptogram, solve):
    done_i = []
    for i in cryptogram[0]:
        if i not in done_i and i in ALPHABET:
            if cryptogram[1][i] != solve[0][i]:
                return False
            done_i.append(i)
        
    return True


def code_to_text(code):
    return code[0].upper()+'\n'


def get_freq(cryptogram):
    freq = {}
    for i in ALPHABET:
        freq[i] = cryptogram[0].count(i)
    
    return freq
        

def disp_freq(freq):
    txt_dict = {}
    counter = 0
    for i in freq:
        if freq[i] != 0:
            spacing = ""
            for j in range(3-len(str(freq[i]))):
                spacing += " "
                
            if counter in txt_dict:
                txt_dict[counter] += f"    `**`{i.upper()}`**`: {freq[i]}" + spacing
            else:
                txt_dict[counter] = f"`**`{i.upper()}`**`: {freq[i]}" + spacing
            
            counter += 1
            
            if counter == 5:
                counter = 0
    
    txt = ""
    for i in txt_dict:
        txt += txt_dict[i] + "\n"
        
    return txt


def disp(puzzle, solved, time):
    done = 0
    not_done = 0
    for char in solved[1]:
        
        if char in ALPHABET or char == "_":
            if char == "_":
                not_done += 1
            else:
                done += 1
    
    complete = int((done / (not_done+done)) * 100)
            
    return f"`Time: `**`{round(time,2)}`**`        Completion: `**`{complete}%`**`        Difficulty: `**`{round(puzzle[2]['difficulty']-1, 2)}`**`\n\n{code_to_text(puzzle)}{solved[4]}\n{solved[1].upper()}\n{disp_freq(get_freq(puzzle))}`"


def get_quotes_of_diff(diff_min, diff_max):
    return list(filter(lambda x: round(x['difficulty']) in range(diff_min, diff_max), quotes))

    
def read_txt(f):
    global quotes
    
    for line in f:
        current = {}
        line = line.replace("\n", '')

        if '"text"' in line or '"quoteText"' in line:
            line = line_to_text(line)
            
            current['text'] = line
            current['length'] = get_length(line)
            
            if current['length'] in range(50, 150):
                current['freq of words'] = get_frequence_of_words(line)
                current['avg word length'] = get_avg_word_length(line)
                current['dev letter freq'] = get_dev_letter_freq(line)
                current['ones'] = get_ones(line)
                
                current['difficulty'] = get_difficulty(current['freq of words'], current['avg word length'], current['dev letter freq'], current['length'], current['ones'])

                quotes.append(current)
  

def main():

    f = open("codebusters/quotes.txt", "r")
    read_txt(f)
    f = open("codebusters/quotes2.txt", "r")
    read_txt(f)


main()