#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        

placeholder = "[name]"
#using the readlines() method to return the names into a list     
with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()
    print(names)

#another method or way to read files.   
#with open("./Input/Names/invited_names.txt") as name_file:
#with open("./Input/Letters/starting-letter.docx") as file:
    
with open(r"C:\Users\WK. BRANDON\Desktop\100 days of python\INTERMEDIATE LEVEL FROM DAY15-TO-DAY40\day-24-files\Input\Letters\starting_letter.docx") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(placeholder, stripped_name)
        print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as completed_letter:
            completed_letter.write(new_letter)
            
