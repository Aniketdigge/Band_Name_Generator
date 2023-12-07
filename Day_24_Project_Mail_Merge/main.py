#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

"""
 starting_letter = open("Input\Letters\starting_letter.txt", mode="r")
invited_names = open("Input\\Names\invited_names.txt", mode="r")

st_let = starting_letter.readlines(100)
inv_nm = invited_names.readlines(100)
content = st_let[0]

for i in range(len(inv_nm)): 
    name = inv_nm[i]
    content_s = content.strip()
    final_c = content_s.replace("name", name)
    print(final_c)
    for j in range(len(st_let)):
        print(st_let[j])
    

#print(st_let[0])
print(inv_nm)

starting_letter.close()
invited_names.close()"""

PLACEHOLDER = "[name]"

with open("Input\\Names\invited_names.txt") as names_file:
    names = names_file.readlines()

with open("Input\Letters\starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"Output\ReadyToSend\letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)