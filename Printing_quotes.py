## Exercise 3: Printing Quotes

quote_str = str(input("What is the quote? "))
quoter = str(input("Who said it? "))
#print(f'{quoter} says, "{quote_str}".') This is string interpolation

print(quoter + ' says, "'+ quote_str + '." ')
