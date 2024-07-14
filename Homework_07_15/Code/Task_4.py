Sample_file = open("../Files/Sample_file_1.1.txt", "r")
Sample_data = Sample_file.read()
Sample_file.close()

Sample_lines = Sample_data.split("\n")

line_length = 0
for line in Sample_lines:
    if len(line) > line_length:
        line_length = len(line)
print(line_length)