# Goal is to convert lines of questions into ipynb form

# Open the input file in read mode
with open('input.txt', 'r') as file:
    # Read the contents of the file
    inputs = file.readlines()

# Loop through the inputs and print them with the expected output format
for i, input_text in enumerate(inputs):
    # Remove the newline character at the end of the input
    input_text = input_text.strip()
    
    # Print the input with the expected output format
    print(f"{i+1}. **{input_text}**<br>")
    print("")