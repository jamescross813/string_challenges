# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
    start1 = word1[0]
    start2 = word2[0]
    rest1 = word1[1:len(word1)]
    rest2 = word2[1:len(word2)]
    

# Uncomment these function calls to test your function:
make_spoonerism("Codecademy", "Learn")
# print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
#print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
#print(make_spoonerism("a", "b"))
# should print b a