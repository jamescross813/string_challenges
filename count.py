letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(input_word):
    count = 0
    for let in letters:
        if input_word.find(let) !=-1:
            count +=1

            
# Uncomment these function calls to test your function:
#print(unique_english_letters("mississippi"))
# should print 4
#print(unique_english_letters("Apple"))
# should print 4