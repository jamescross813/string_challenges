# Write your add_exclamation function here:
def add_exclamation(string):
    i=0
    phrase = string
    while i <= 20:
        if i>len(string):
            phrase = phrase +"!"
        i+=1
    return phrase
# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn