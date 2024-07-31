#Exercise 4: Mad Lib

"""
Mad libs are a simple game where you create a story tem- plate with blanks for words. 
You, or another player, then construct a list of words and place them into the story, 
creating an often silly or funny story as a result.
Create a simple mad-lib program that prompts for a noun, a verb, an adverb, 
and an adjective and injects those into a story that you create.
"""

noun = str(input("Enter a noun: "))
verb = str(input("Enter a verb: "))
adjec = str(input("Enter an adjective: "))
adverb = str(input("Enter an adverb: "))

print(f"A {noun} {adverb} {verb}s with anger! That's {adjec}!")