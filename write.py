from os import path, makedirs

# Create the test_files directory if it doesn't already exist;

directory = 'C:\\Users\\slushy\\Desktop\\Python\\write.py\\test_files\\'

if not path.exists(directory):
    makedirs(directory)

# Create the original text file if it doesn't already exist;

filename = 'original.txt'

filepath = 'C:\\Users\\slushy\\Desktop\\Python\\write.py\\test_files\\'

orig_full_path = 'C:\\Users\\slushy\\Desktop\\Python\\write.py\\test_files\\original.txt'

text = 'Copy this text from original.txt to 10 other text files.'

if not path.exists(orig_full_path):
    file = open(orig_full_path, 'w')

    file.write(text)

    file.close()

    print()
    print(f'{filename} was created and written successfully.')
    print()

elif path.exists(orig_full_path):
    print()
    print(f'File {filename} already exists in the directory {filepath}.')
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
    new_full_path = (f'{filepath}copy_file{i}.txt')
    
    if not path.exists(new_full_path):
        with open(new_full_path, 'w') as new_file:
            new_file.write(content)
            new_file.close()

            print(f'copy_file{i} was created and written successfully.')

    elif path.exists(new_full_path):
        print(f'copy_file{i} already exists in {filepath}.')

orig_file.close()