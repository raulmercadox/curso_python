s = "azcbobobegghakl"
word = "bob"
width = len(word)
count = 0
found = 0
len_s = len(s)
while count <= len_s - 3:
    part = s[count:count+3]
    if part == word:
        found += 1
    count += 1
print("Number of times bob occurs is:", found)