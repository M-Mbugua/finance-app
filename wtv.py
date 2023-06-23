with open("wordlist.txt", "r") as f:
    names = [line.strip() for line in f.readlines()]

names.sort()

with open("wordlist.txt", "w") as f:
    for name in names:
        f.write(name + "\n")
