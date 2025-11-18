# Write text to file
text = input("Enter text to write to the file: ")
with open("output.txt", "w") as fh:
    fh.write(text + "\n")
print("Data successfully written to output.txt.\n")

# Append additional text
text2 = input("Enter additional text to append: ")
with open("output.txt", "a") as fh:
    fh.write(text2 + "\n")
print("Data successfully appended.\n")

# Read and display final content
try:
    with open("output.txt", "r") as fh:
        print("Final content of output.txt:")
        print(fh.read())
except FileNotFoundError:
    print("Error: The file 'output.txt' was not found.")
