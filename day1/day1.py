
word_to_digit = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6, 
    "seven": 7,
    "eight": 8,
    "nine": 9
}

input_file = open('input', 'r')
lines = input_file.readlines()

first_digit_found = 0
count = 0

for line in lines:
    # Iterate over the line using indexes
    for start_index in range(0, len(line)):
        # Check if character is a digit
        if (line[start_index].isdigit()):
            # Check if its the first digit
            if (first_digit_found):
                # First digit already found
                last_digit = int(line[start_index])
            else:
                # First digit not found
                first_digit = int(line[start_index])
                last_digit = int(line[start_index])
                first_digit_found = 1

        else:
            word = ""
            # See if number is written as a word
            for current_index in range(start_index, len(line)):

                # Check if word is a number written out
                if (word in word_to_digit):
                    # Check if its the first digit
                    if (first_digit_found):
                        # First digit already found
                        last_digit = word_to_digit[word]
                    else:
                    # First digit not found
                        first_digit = word_to_digit[word]
                        last_digit = word_to_digit[word]
                        first_digit_found = 1

                    break
                else:
                    # Expand word
                    word += line[current_index]

    first_digit_found = 0
    count = count + (first_digit * 10) + last_digit
        
print(count)

            
        




    






        
