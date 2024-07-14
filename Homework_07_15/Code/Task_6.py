Sample_file = open("../Files/Sample_file_1.1.txt", "r")
Sample_data = Sample_file.read()
Sample_file.close()

Old_Word = input("Mazané slovo: ")
New_Word = input("Nové slovo: ")

print(Sample_data.replace(Old_Word, New_Word))
