# Henry Roeser
# 16 SEP 2024
# Mad Lib


# Get some data from the user by using the input ( ) function



# noun = "house"
# verb = "sit"
# noun2 = "chair"
# verb2 = "lay"
# noun3 = "couch"

noun = input('Please enter a noun:')
verb = input('Please enter a verb:')
noun2 = input('Please enter another noun:')
verb2 = input('Please enter another verb:').upper()
noun3 = input('Please enter another noun:')


madlibs =  "Hey! Welcome to my " + noun.lower() + " You can " + verb + " on the " + noun2 + " You can also " + verb2 + " on the " + noun3 + "."

madlib = f"Hey! Welcome to my {noun.lower()} You can {verb.upper()} on the {noun2} You can also {verb2} on the {noun3}"


print(madlibs)



