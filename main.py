text = input()
results = []

f = open('words.txt', 'r')
lines = f.readlines()

for word in lines:
    sortedword = sorted(word.lower())
    
    del(sortedword[0])
    print(word)
    if sorted(text.lower()) == sortedword:
        results.append(word.replace("\n", ""))

print(results)
print("Done")
