"""
A string is a palindrome if it reads the same forward and backward. 
The words “mom,” “dad,” and “noon,” for instance, are all palindromes.
The problem is to write a program that prompts the user to enter a string
 and reports whether the string is a palindrome. 
 One solution is to check whether the first character in the string is
 the same as the last character. If so, check whether the second character is
 the same as the second-to-last character. 
This process continues until a mismatch is found or all the characters 
in the string are checked, except for the middle character if the string
 has an odd number of characters.
"""
##OR/AND

"""
Write a program to detect if a sentence is a pangram.
A pangram is a sentence or phrase that contains every letter of the alphabet
 at least once. Pangrams are often used for language and typing practice, 
 as they provide a way to ensure that each letter is used in a given context.
 An example of a pangram is the well-known sentence: "The quick brown fox jumps over a lazy dog."
"""
def get_msg():
  """
  Example function to build up a string and return it for a user-msg.
  """
  msg = \
  "\n\
  Check if a sentence is a Pangram?\
  \n\t Type 'ya'\
  \n\t (Press enter to stop)\
  \n"
  return msg

def is_pangram(given_text):
  pass          #write the code here

while( input( get_msg() ) != ""):
  typed = input("enter a sentence:\n") 	
  print("Is '",typed,"' a Pangram?:\n ", is_pangram(typed))