# Write your every_other_letter function here:
def every_other_letter(sentence):
    count = 0
    new_str=""
    while count < len(sentence):
        if count%2==0:
            new_str = new_str + sentence[count]
        count= count+1
    return new_str
# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 