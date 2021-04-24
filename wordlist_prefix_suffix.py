# getting input for prefix and suffix for list
pre = input("Enter prefix for every word in list  :  ")
suf = input("Enter suffix for every word in list  :  ")
lst = []

n = 99999999999
# iterating till the range and getting list of words.
for i in range(0, n):
    ele = input("Enter word list 1 by 1 or copy all and paste   (Or you want to submit list then type Y) : ")
    if ele == "Y":
        break
    else:
        result = pre + ele + suf
        lst.append(result)  # adding the element
print(lst)

# save in file or not
file=input("Enter file name to save wordlist in .txt format (OR Don't want to save then type N)  :  ")
if file != "N":
    with open(file+".txt", 'w') as output:
        for row in lst:
            output.write(str(row) + '\n')
    print("Go to "+file+".txt and see the wordlist generated........")
print("Done !!!")

