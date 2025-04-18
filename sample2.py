
n = input("Enter some text to write to the file: ")

file = open("output.txt", "w")
file.write(n + "\n")
file.close()


additional_input = input("Enter more text to append to the file: ")

file = open("output.txt", "a")
file.write(additional_input + "\n")
file.close()


file = open("output.txt", "r")
print("\nFinal content of output.txt:")
for line in file:
    print(line.strip())
file.close()
