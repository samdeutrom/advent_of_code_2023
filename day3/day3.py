input_file = open("input")

lines = input_file.readlines()

for i in range(0,len(lines)):
    for j in range(0, len(lines[i])):
        if (not (lines[i][j].isdigit() or lines[i][j] == '.' or lines[i][j] == '\n')):
            print(lines[i][j])
