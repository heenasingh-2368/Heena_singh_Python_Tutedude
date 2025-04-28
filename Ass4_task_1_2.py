
user_input = input("Enter some text to write into the file: ")


with open('output.txt', 'w') as file:
    file.write(user_input + '\n')

print("Data written to output.txt.")


additional_input = input("Enter additional text to append to the file: ")


with open('output.txt', 'a') as file:
    file.write(additional_input + '\n')

print("Additional data appended to output.txt.")


print("\nFinal content of 'output.txt':")
with open('output.txt', 'r') as file:
    content = file.read()
    print(content)
