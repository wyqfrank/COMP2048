from collections import Counter
import string
import json 

def caesar_decoder(encoded_message: string):
    # with open('dictionary.json', 'r') as word_set:
    #     data = json.load(word_set)
    
    # with open('firstnames_m.json', 'r') as word_set:
    #     firstnames_m = json.load(word_set)
    
    # with open('firstnames_f.json', 'r') as word_set:
    #     firstnames_f = json.load(word_set)

    # with open('surnames.json', 'r') as word_set:
    #     surnames = json.load(word_set)

    frequency_letters = ["e","t", "a", "o", "i", "n", "s", "h", "r", "d", "l", "c", "u", "m", "w", "f", "g", "y", "p", "b", "v", "k", "j", "x", "q", "z"]
    letters = string.ascii_letters
    totalLetters = 26

    #find max letter
    maxFreq = -1
    letter_counts = Counter(encoded_message)
    maxLetter = None
    for letter, freq in letter_counts.items(): 
        # print(letter, ":", freq) 
        if letter != " " and freq > maxFreq:
            maxFreq = freq
            maxLetter = letter
    # print("Max Ocurring Letter:", maxLetter)
   
    for char in frequency_letters:
        shift = letters.index(maxLetter) - letters.index(char)
        keys = {} #use dictionary for letter mapping
        invkeys = {} #use dictionary for inverse letter mapping, you could use inverse search from original dict
        for index, letter in enumerate(letters):
            # cypher setup
            if index < totalLetters: #lowercase
                keys[letter] = letters[(index + shift) % totalLetters] 
                invkeys[letters[(index + shift) % totalLetters]] = letters[index]
            else: #uppercase
                keys[letter] = letters[((index + shift) % totalLetters) + totalLetters]
                invkeys[letters[((index + shift) % totalLetters) + totalLetters]] = letter

        decryptedMessage = []
        for letter in encoded_message:
            if letter == ' ': #spaces
                decryptedMessage.append(letter)
            else:
                decryptedMessage.append(invkeys[letter])
        # print("Decrypted Message:", ''.join(decryptedMessage))
        decrypted = ''.join(decryptedMessage)
        
        check = input(f"is this the message (Y/N)? \n{decrypted}\n")

        if check == "Y":
            return decrypted
        

        # from_dictionary = []
        # for word in decrypted.split(" "):
        #     if word.lower() in data:
        #         from_dictionary.append(word)
        #     elif word in firstnames_m:
        #         from_dictionary.append(word)
        #     elif word in firstnames_f:
        #         from_dictionary.append(word)
        #     elif word in surnames:
        #          from_dictionary.append(word)

        # if from_dictionary == decrypted.split(" "):
        #     print(decrypted)

        # print(from_dictionary)
        # print(decrypted.split(" "))
        # break
    # for i in range(25):
    #     pass 
    # pass # can try every shift 0-25 to see if the messsage is decoded

message = "K wkx k zvkx k mkxkv Zkxkwk"       
print(caesar_decoder(encoded_message=message))