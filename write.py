# The path.exists() method is used to check whether a filepath exists in OS,
# and the makedirs() method is used to create directories;
from os import path, makedirs

# This is the directory where we will be storing our original file and its
# copies, we assign it to a descriptive variable for efficiency;
directory = 'C:\\Users\\slushy\\Desktop\\Python\\write.py\\test_files\\'

# Checks the filepath to see if the directory exists; if it does NOT exist...
if not path.exists(directory):
    
    # then create it;
    makedirs(directory)

# Create the name for the original text file and assign it to the variable, 
# this is the file we will copy from to create the ten duplicate
# (besides the names) files;
orig_file = 'original.txt'

# We need to use the full filepath for the path.exists() method below;
# the double backslashes are used to insert literal backslashes since this
# script was written for Windows;
orig_full_path = 'C:\\Users\\slushy\\Desktop\\Python\\write.py\\test_files\\original.txt'

# We will use this variable to write the string to our original.txt file;
text = 'Copy this text from original.txt to 10 other text files.'

# If the full filepath of original.txt does NOT exist...
if not path.exists(orig_full_path):
    
    # then create (open) original.txt at the filepath in write mode;
    file = open(orig_full_path, 'w')

    # Then write the text (string) to it;
    file.write(text)

    file.close()

    print()
    print(f'{orig_file} was created and written successfully.')
    print()

# Else if original.txt already exists at that filepath...
elif path.exists(orig_full_path):
    print()
    # simply print out this message and don't do anything else;
    print(f'File {orig_file} already exists in the directory {directory}.')
    print()


else:
    print()
    print('An error has occurred, please investigate and try again.')
    print()

# Copy the text from the original file and use it to create 10 new files,
# each with a different name;

# Open original.txt at its full filepath in read mode under the variable name,
# orig_file; using 'with open' ensures the file gets closed automatically 
# after exiting the 'with' block without having to explicitly use close();
with open(orig_full_path, 'r') as orig_file:
    
    # Read the contents of the file and assign the contents to the variable,
    # content;
    content = orig_file.read()

# Since we are trying to create ten duplicate files (aside from the name),
# we set up a loop that will begin at 1 and end at 10 (the 11 is exclusive);
for i in range(1, 11):

    # Every loop, we create a new file that contains the same text as
    # original.txt, and we add the current value of i in the filename;
    # then we assign the full filepath of the new file to the variable;
    new_full_path = (f'{directory}copy_file{i}.txt')
    
    # Check whether the new file already exists at its full filepath;
    # if it does NOT exist...
    if not path.exists(new_full_path):
        
        # open (create) new file at its full filepath in write mode;
        # again, using 'with open' ensures the file is closed automatically
        # after exiting the 'with' block;
        with open(new_full_path, 'w') as new_file:
            
            # Write the content (contents of original.txt) to it;
            new_file.write(content)
            #new_file.close()

            print(f'copy_file{i} was created and written successfully.')
    
    # Else if new file already exists at its full filepath... 
    elif path.exists(new_full_path):
        
        # just print out this message, don't do anything else;
        print(f'copy_file{i} already exists in {directory}.')

print()