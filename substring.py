# Write your substring_between_letters function here:
def substring_between_letters(word, sub1, sub2):
   start_point = word.find(sub1)
   end_point = word.find(sub2)
   
# Uncomment these function calls to test your function:
#print(substring_between_letters("apple", "p", "e"))
# should print "pl"
#print(substring_between_letters("apple", "p", "c"))
# should print "apple"