from os import path, makedirs

# Create the test_files directory if it doesn't already exist;

directory = 'C:\\Users\\slushy\\Desktop\\Python\\write.py\\test_files\\'

if not path.exists(directory):
    makedirs(directory)

# Create the original text file if it doesn't already exist;

filename = 'original.txt'

filepath = 'C:\\Users\\slushy\\Desktop\\Python\\write.py\\test_files\\'

full_filepath = 'C:\\Users\\slushy\\Desktop\\Python\\write.py\\test_files\\original.txt'

text = 'Copy this text from original.txt to 10 other text files.'

if filename not in filepath:
    file = open(full_filepath, 'w')

    file.write(text)

    file.close()

    print()
    print(f'File {filename} created and written successfully.')
    print()

elif filename in full_filepath:
    print()
    print(f'File {filename} already exists in the directory {filepath}.')
    print()

else:
    print()
    print('An error has occurred, please investigate and try again.')
    print()

# Copy the text from the original file and use it to create 10 new files,
# each with a different name;

#with open(full_filepath, 'w') as file:
#    file.write(text)

#print(f'File {} created and written successfully.')