infile = open("input.txt", "r")

line_count = 0
word_count = 0
char_count = 0

for line in infile:
    line_count += 1

    words = line.split()
    word_count += len(words)

    char_count += len(line)

infile.close()

print("Lines:", line_count)
print("Words:", word_count)
print("Characters:", char_count)