# Write your check_for_name function here:
def check_for_name(sentence, name):
    lowercase_sent = sentence.lower()
    name_sent = name.lower()
    if lowercase_sent.find(name_sent) != -1:
        return True
    return False
       
# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False