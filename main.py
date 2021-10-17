text = input()
results = []

f = open('words.txt', 'r')
lines = f.readlines()

for word in lines:
    sortedword = sorted(word)
    del(sortedword[0])
    print(word)
    if sorted(text) == sortedword:
        results.append(word.replace("\n", ""))

print(results)
print("Done")