Sample_file = open("../Files/Sample_file_1.1.txt", "r")
Sample_data = Sample_file.read()
Sample_file.close()

# number of characters
num_char = len(Sample_data)
print(num_char)

# number of lines
num_line = Sample_data.count("\n")+1
print(num_line)

# number of vowels
vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
num_vow = 0
for vowel in vowels:
    num_vow += Sample_data.count(vowel)
print(num_vow)

# number of consonants
consonants = (list("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"))
num_con = 0
for consonant in consonants:
    num_con += Sample_data.count(consonant)
print(num_con)

# number of digits
num_dig = 0
for i in Sample_data:
    if i.isdigit():
        num_dig += 1
print(num_dig)

New_data = (f"{num_char}\n{num_line}\n{num_vow}\n{num_con}\n{num_dig}")
New_file = open("../Files/New_file_2.txt", "w")
New_file.write(New_data)
New_file.close()
