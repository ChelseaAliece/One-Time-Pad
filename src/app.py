import hashlib
import os, codecs, binascii, base64, Crypto
from Crypto.Cipher import AES
from Crypto import Random
from base64 import b64encode
import time
import numpy as np
from random_word import RandomWords
from random import choice




def targetGen():
    # Gets difficulty level from user input
    difficulty = input("Please enter a difficulty level: ")
    difficulty = int(difficulty)
    # Calculates number of 1's needed for target 
    ones = 256 - difficulty;
    #creates strings of 0's and 1's 
    firstHalf=np.zeros(difficulty)
    secondHalf=np.ones(ones)
    targetArr = np.concatenate((firstHalf, secondHalf))
    targetArr = targetArr.astype(int)
    targetArr = targetArr.astype(str).tolist()
    target = ''.join(targetArr) 
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')   
    print('Target: ' + target)   
    
    # writes target to target.txt file 
    target_file = open("./data/target.txt", "w")
    target_file.write(target)
    target_file.close()

def solutionGen():
   # starting time
   start = time.time()
    
    # Gets input & target from their respective files 
   message = open("./data/input.txt", "r")
   message = message.read()
   target = open("./data/target.txt", "r")
   target = target.read()
   
   # Incremental value / S
   s = 1
   
   # Concatenating the message and s value
   hashInput = message + str(s)

   # Creating SHA256 Hash and converting it to binary 
   hash = hashlib.sha256(hashInput.encode()).hexdigest()
   hash = (bin(int(hash, 16))[2:]).zfill(256)
   
   # Getting the solution
   while hash >= target:
        s += 1
        hashInput = message + str(s)
        hash = hashlib.sha256(hashInput.encode()).hexdigest()
        hash = (bin(int(hash, 16))[2:]).zfill(256)
   print('--------------------------------------------------------------------------------------------------------------------------------------')   
   print('Solution: ' + str(s))
   print('--------------------------------------------------------------------------------------------------------------------------------------')   
   solution_file = open("./data/solution.txt", "w")
   s = str(s)
   solution_file.write(s)
   solution_file.close()
   
   # end time
   end = time.time()
   print(f"Runtime of the program is {end - start}")

   return hash
    

def verification():
    # Gets input, solution, & target from their respective files 
    message = open("./data/input.txt", "r")
    message = message.read()
    target = open("./data/target.txt", "r")
    target = target.read()
    solution = open("./data/solution.txt", "r")
    solution = solution.read()
    
    # gets hash from solutionGen()
    hash = solutionGen()
    
    # Checks if hash <= target and return corresponding value if it is valud
    if hash <= target:
        print(1)
    else:
        print(0)
    
        
targetGen()
solutionGen()
verification()
