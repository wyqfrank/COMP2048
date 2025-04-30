# -*- coding: utf-8 -*-
"""
Create and test an Enigma machine encryption and decoding machine

This code is based on the implementation of the Enigma machine in Python 
called pyEnigma by Christophe Goessen (initial author) and Cédric Bonhomme
https://github.com/cedricbonhomme/pyEnigma

Created on Tue Feb  5 12:17:02 2019

@author: uqscha22
"""
import string
import enigma
import rotor
import time 

letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
capitalLetters = letters[-26:]
# print(capitalLetters)

ShakesHorribleMessage = "Xm xti ca idjmq Ecokta Rkhoxuu! Kdiu gm xex oft uz yjwenv qik parwc hs emrvm sfzu qnwfg. Gvgt vz vih rlt ly cnvpym xtq sgfvk jp jatrl irzru oubjo odp uso nsty jm gfp lkwrx pliv ojfo rl rylm isn aueuom! Gdwm Qopjmw!"
crib = "Hail Shakes!"

##Break the code via brute force search
#INSERT CODE HERE

def decrypted_key(message: string) -> string:
    start = time.time()
    counter = 0
    for char1 in capitalLetters:
        for char2 in capitalLetters:
            for char3 in capitalLetters:
                attempt = char1 + char2 + char3
                engine = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                    rotor.ROTOR_II, rotor.ROTOR_III, key=attempt,
                                    plugs="AA BB CC DD EE")
                decrypted_message = engine.encipher(ShakesHorribleMessage)
                last_two_words = " ".join(decrypted_message.split(" ")[-2:])
                counter +=1

                if crib in last_two_words:
                    print(f"no. attempts: {counter}")
                    print(f"Key: {attempt}")
                    
                    end = time.time()
                    print(f"execution time: {end - start}s")
                    return attempt
                
    
# decrypted_key(ShakesHorribleMessage)

#Print the Decoded message

engine = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                   rotor.ROTOR_II, rotor.ROTOR_III, key=decrypted_key(ShakesHorribleMessage),
                                   plugs="AA BB CC DD EE")
print(engine.encipher(ShakesHorribleMessage))


# section 2 part e 
# with 3 rotors:
# 5 * 4 * 3 = 60
# 26 * 26 * 26 = 17576
# total: 1736
# ~10.806 seconds

# with 5 rotors, plugboard
# 5 * 4 * 3 * 2 * 1 = 120
# 26 * 26 * 26 * 26 * 26 = 11881376
# 26! / (16! * 5! * 2^5) = 5.01958957*10^{9} (16! because we of 5 pairs for plugs)
# total: 5.03147107*10^{9}
# 2898312.826 times more total possible outcomes 
# approx. 31319168.4 seconds (2898312.826 * 10.806)

