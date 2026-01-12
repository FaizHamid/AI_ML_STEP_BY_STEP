# File Handling in Python
# File handling is a crucial aspect of programming that allows you to read from and write to files on your system.
# Python provides built-in functions and methods to handle files easily.
# The main file handling operations in Python include:
# 1. Opening a file - Using the open() function to open a file in different modes (read, write, append, etc.).
# 2. Reading from a file - Using methods like read(), readline(), and readlines() to read data from a file.
# 3. Writing to a file - Using methods like write() and writelines() to write data to a file.
# 4. Closing a file - Using the close() method to close a file after operations are complete.   

# Examples of File Handling in Python:

# 1. Opening and Closing a File
# Opening a file in write mode
file = open("example.txt", "w")
# Writing data to the file
file.write("Hello, World!\n")
file.write("This is a file handling example in Python.\n")
# Closing the file
file.close()    

# 2. Reading from a File
# Opening the file in read mode
file = open("example.txt", "r")
# Reading the entire content of the file
content = file.read()
print("File Content:\n", content)
# Closing the file
file.close()    

# 3. Appending to a File
# Opening the file in append mode
file = open("example.txt", "a")
# Appending data to the file
file.write("Appending a new line to the file.\n")
# Closing the file
file.close()    

# 4. Reading Line by Line
# Opening the file in read mode
file = open("example.txt", "r")
# Reading the file line by line
print("Reading Line by Line:")
for line in file:
    print(line.strip())
# Closing the file
file.close()    

# File Handling Modes Reference:
# 1. 'r' - Read mode (default mode, opens a file for reading)
# 2. 'w' - Write mode (opens a file for writing, creates a new file or truncates an existing file)
# 3. 'a' - Append mode (opens a file for appending, creates a new file if it doesn't exist)
# 4. 'b' - Binary mode (used for binary files like images, videos, etc.)
# 5. 't' - Text mode (default mode, used for text files)
# 6. 'x' - Exclusive creation (creates a new file, fails if the file already exists)   

# File Handling Methods Reference:
# open() - Opens a file and returns a file object
# read() - Reads the entire content of a file
# readline() - Reads a single line from a file
# readlines() - Reads all lines from a file and returns them as a list
# write() - Writes a string to a file
# writelines() - Writes a list of strings to a file
# close() - Closes the file
# File Handling Examples:

# Using 'with' statement for file handling (automatically closes the file)
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content using 'with' statement:\n", content)

# Writing multiple lines using writelines()
lines = ["First line.\n", "Second line.\n", "Third line.\n"]
with open("example2.txt", "w") as file:
    file.writelines(lines)

# Reading the newly created file
with open("example2.txt", "r") as file:
    print("Content of example2.txt:")
    for line in file:
        print(line.strip())

# End of File Handling in Python

# File Handling Types Reference:
# 1. Text File Handling - Involves reading and writing plain text files using text modes ('r', 'w', 'a', 't').
# 2. Binary File Handling - Involves reading and writing binary files (like images, videos) using binary modes ('rb', 'wb', 'ab').

# File Handling Types Examples:
# Text File Handling Example
with open("textfile.txt", "w") as file:
    file.write("This is a text file.\nIt contains plain text data.\n")
with open("textfile.txt", "r") as file:
    print("Text File Content:")
    print(file.read())
# Binary File Handling Example
# Writing binary data to a file
with open("binaryfile.bin", "wb") as file:
    file.write(b'\x00\xFF\x7A\x3C\x5D')
# Reading binary data from the file
with open("binaryfile.bin", "rb") as file:
    binary_content = file.read()
    print("Binary File Content:", binary_content)

# File Handling Methods Examples:
# Using readline() to read a file line by line
with open("example.txt", "r") as file:
    print("Reading using readline():")
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()
# Using readlines() to read all lines into a list
with open("example.txt", "r") as file:
    lines = file.readlines()
    print("Reading using readlines():")
    for line in lines:
        print(line.strip())

# File Handling Modes Examples:
# Writing to a file in write mode
with open("mode_example.txt", "w") as file:
    file.write("This file is opened in write mode.\n")
# Appending to the same file in append mode
with open("mode_example.txt", "a") as file:
    file.write("This line is appended in append mode.\n")
# Reading the file in read mode
with open("mode_example.txt", "r") as file:
    print("Content of mode_example.txt:")
    print(file.read())
# End of File Handling Modes Examples in Python 

# File Handling Methods Types Reference:
# 1. Basic File Operations - Methods like open(), close(), read(), write() for basic file handling.
# 2. Line-based File Operations - Methods like readline(), readlines() for reading files line by line.
# 3. Context Manager Operations - Using 'with' statement for automatic file handling.
# File Handling Methods Types Examples:
# Basic File Operations Example
file = open("basic_ops.txt", "w")
file.write("Basic file operations example.\n")
file.close()
with open("basic_ops.txt", "r") as file:
    print("Basic File Operations Content:")
    print(file.read())
# Line-based File Operations Example
with open("line_ops.txt", "w") as file:
    file.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])
with open("line_ops.txt", "r") as file:
    print("Line-based File Operations Content:")
    for line in file:
        print(line.strip())
# Context Manager Operations Example
with open("context_manager.txt", "w") as file:
    file.write("This file is handled using a context manager.\n")
with open("context_manager.txt", "r") as file:
    print("Context Manager File Content:")
    print(file.read())
# End of File Handling Methods Types Examples in Python 
# End of File Handling in Python    


#What happens if a file is opened in write mode (w) and the file already exists?
# Select the correct answer


# A. Data is appended to the file.

# B. An error is raised.

# C. The existing content is deleted and new data is written.

# D. The file is opened in read-only mode.

# Answer: C. The existing content is deleted and new data is written.
