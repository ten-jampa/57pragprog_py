## Exercise 2: Counting the number of characters

"""
Create a program that prompts for an input string and 
displays output that shows the input string and the number of characters the string contains.P
"""

input_string = str(input("What is the input string? "))
while len(input_string) == 0:
    input_string = str(input("You must enter something into the program: "))
else:
    print(f"{input_string} has {len(input_string)} characters.")



"""Challenge:
• If theuserentersnothing,statethattheusermustenter something into the program.
• Implement this program using a graphical user interface and update the character counter every time a key is pressed.
If your language doesn’t have a particularly friendly GUI library, 
try doing this exercise with HTML and JavaScript instead.


"""

