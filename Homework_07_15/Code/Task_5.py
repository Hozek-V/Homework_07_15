Sample_file = open("../Files/Sample_file_1.1.txt", "r")
Sample_data = Sample_file.read()
Sample_file.close()

Word = input("Hledané slovo: ")

print(Sample_data.count(Word))
