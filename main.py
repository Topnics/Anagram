# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
   
# convert both the strings into lowercase
    word = word.lower()
    anagram = anagram.lower()

# check if length is same
    if(len(word) == len(anagram)):

        if(sorted(word) == sorted(anagram)):
        
            print ("True")
        else:
            print ("False")
    else:
        print("False") 

    return True
word = (input("Type in the word: "))
anagram = (input("Type in the anagram you want to check: "))

find_anagram(word, anagram)
   

