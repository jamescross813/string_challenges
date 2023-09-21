# Write your substring_between_letters function here:
def substring_between_letters(word, sub1, sub2):
   start_point = word.find(sub1)
   end_point = word.find(sub2)
   if start_point > -1 and end_point > -1:
    return(word[start_point+1:end_point])
   return word
# Uncomment these function calls to test your function:
#print(substring_between_letters("apple", "p", "e"))
# should print "pl"
#print(substring_between_letters("apple", "p", "c"))
# should print "apple"