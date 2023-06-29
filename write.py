from os import path, makedirs

# This is the directory where we will be storing our original file and its
# copies, we assign it to a descriptive variable for efficiency;
directory = 'C:\\Users\\slushy\\Desktop\\Python\\write.py\\test_files\\'

# Checks the filepath to see if the directory exists; if it does NOT exist...
if not path.exists(directory):
    # then create it;
    makedirs(directory)

# Create the original text file if it doesn't already exist, this is the one
# we will copy from to create the ten duplicate (besides their names) files;
orig_file = 'original.txt'

#filepath = 'C:\\Users\\slushy\\Desktop\\Python\\write.py\\test_files\\'

orig_full_path = 'C:\\Users\\slushy\\Desktop\\Python\\write.py\\test_files\\original.txt'

text = 'Copy this text from original.txt to 10 other text files.'

if not path.exists(orig_full_path):
    file = open(orig_full_path, 'w')

    file.write(text)

    file.close()

    print()
    print(f'{orig_file} was created and written successfully.')
    print()

elif path.exists(orig_full_path):
    print()
    print(f'File {orig_file} already exists in the directory {directory}.')
    print()

else:
    print()
    print('An error has occurred, please investigate and try again.')
    print()

# Copy the text from the original file and use it to create 10 new files,
# each with a different name;

with open(orig_full_path, 'r') as orig_file:
    content = orig_file.read()

for i in range(1, 11):
    new_full_path = (f'{directory}copy_file{i}.txt')
    
    if not path.exists(new_full_path):
        with open(new_full_path, 'w') as new_file:
            new_file.write(content)
            new_file.close()

            print(f'copy_file{i} was created and written successfully.')

    elif path.exists(new_full_path):
        print(f'copy_file{i} already exists in {directory}.')

orig_file.close()