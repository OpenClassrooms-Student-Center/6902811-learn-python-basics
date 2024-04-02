# String Error
print('Hello, world!') # String was not closed by "'"
      
# Indentation Error
if True:
    print('Ahoy, matey!') # Put 4 four spaces before the print
      
# Syntax Error
if True: # ":" is missing
    print('Greetings, Earthlings!')

# Logic Error
animal = 'Lion'
if animal == 'Lion': # Put "Lion" instead of "Lino"
    print('Meat')
elif animal == 'Zebra':
    print('Grass')
else:
    print('Water')