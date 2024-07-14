Sample_file = open("../Files/Sample_file_1.1.txt", "r")
Sample_data = Sample_file.read()
Sample_file.close()

New_data = ""
for i in Sample_data:
    if len(New_data) < Sample_data.rfind("\n"):
        New_data += i

New_file = open("../Files/New_file_3.txt", "w")
New_file.write(New_data)
New_file.close()
