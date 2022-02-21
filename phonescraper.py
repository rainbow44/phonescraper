
import re
import pyperclip
phoneNumRegex = re.compile(r'''`
(\+)?            
(\()?            # optional parentheses
(380)            # country code
(\s)?            #optional spacebar
(\))?            # optional parentheses
(\d\d)(\d)?      # operator code with an optional number
(\))?            # optional parentheses
(\s)?            #optional spacebar
(\d\d)           #
(\s)?            #optional spacebar
(\d)             #
(\s)?            #optional spacebar
(\d\d)           #
(\s)?            #optional spacebar
(\d\d)           # rest of the number 

''', re.VERBOSE)
text1 = '+380961776845, 380964847994, +(380 665)4567878'
text = pyperclip.paste()
extractedPhones = phoneNumRegex.findall(text1)
phonesList = [] 
for number in extractedPhones:
    phones = ''
    for group in number:

        phones += ''.join(group)
    phonesList.append(phones)
    
        
for phonenumber in range(len((phonesList))):
    print(phonesList[phonenumber], end='\n')


    
#use join to print out the whole number
#print out the groups separately
