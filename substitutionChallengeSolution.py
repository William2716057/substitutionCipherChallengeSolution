import string
from collections import Counter

#Frequency dictionary
frequency_dict = {
    'a': 8.08, 
    'b': 1.67, 
    'c': 3.18, 
    'd': 3.99, 
    'e': 12.56, 
    'f': 2.17, 
    'g': 1.80, 
    'h': 5.27, 
    'i': 7.24, 
    'j': 0.14, 
    'k': 0.63, 
    'l': 4.04, 
    'm': 2.60, 
    'n': 7.38, 
    'o': 7.47, 
    'p': 1.91, 
    'q': 0.09, 
    'r': 6.42, 
    's': 6.59, 
    't': 9.15, 
    'u': 2.79, 
    'v': 1.00, 
    'w': 1.89, 
    'x': 0.21, 
    'y': 1.65, 
    'z': 0.07
}
#calculate letter frequency distributions in input messages
def frequency_analysis(text):

    text = ''.join(filter(str.isalpha, text)).lower()
    #get total count
    letter_count = Counter(text)
    total_letters = sum(letter_count.values())
    #formula for calculating frequencies
    letter_frequencies = {letter: (count / total_letters) * 100 for letter, count in letter_count.items()}

    sorted_frequencies = sorted(letter_frequencies.items(), key=lambda x: x[1], reverse=True)

    return sorted_frequencies

#test against most common letters 
def find_shift(frequencies):
    most_frequent_letter = frequencies[0][0]  

    most_frequent_letter_frequency = frequencies[0][1] 
    #if statement to deal with irregular edge case
    if most_frequent_letter_frequency > 15:  
        target_letter = 'o'
    else:
        target_letter = 'e'
    shift = (ord(most_frequent_letter) - ord(target_letter)) % 26
    
    return shift
#calculate shift number
def decode_message(message, shift):
    decoded_message = []
    #perform for upper and lower case
    for char in message:
        if char.isalpha():
            if char.islower():
                decoded_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            elif char.isupper():
                decoded_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decoded_message.append(decoded_char)
        else:
 
            decoded_message.append(char)

    return ''.join(decoded_message)
#main function with inputs and function calls
def main():
    encoded_message = input()
    frequencies = frequency_analysis(encoded_message)
    shift = find_shift(frequencies)
    decoded_message = decode_message(encoded_message, shift)
    #print result 
    print(decoded_message)

if __name__ == "__main__":
    main()