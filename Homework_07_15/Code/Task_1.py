Sample_1 = open("../Files/Sample_file_1.1.txt", "r")
Sample_2 = open("../Files/Sample_file_1.2.txt", "r")

Sample_data_1 = Sample_1.read()
Sample_data_2 = Sample_2.read()

Sample_1.close()
Sample_2.close()

Sample_1_lines = Sample_data_1.split("\n")
Sample_2_lines = Sample_data_2.split("\n")

Difference = []
for line in range(max(len(Sample_1_lines), len(Sample_2_lines))):
    if not Sample_1_lines[line] == Sample_2_lines[line]:
        #Diferrence = open("../Files/New file 1.txt", "w")
        Difference.append(Sample_1_lines[line])
        Difference.append(Sample_2_lines[line])

New_file = open("../Files/New_file_1.txt", "w")
New_file.writelines(line + "\n" for line in Difference)
New_file.close()