# This is for learning purpose only........
# This tool help you to generate wordlist as a valid credentials after certain regular interval of wordlist
# simply have to log in to their own account every few attempts to prevent this limit from ever being reached.

print("This is for learning purpose only........ \n This tool help you to generate wordlist as a valid credentials after certain regular interval of wordlist \n ")
# valid credential for brute force to generate wordlist
uname = input("Enter valid word for username or password  :  ")
lst = []

# number of elemetns as input
y = int(input("Enter number of words you want to enter :  "))

# number of place where correct credential want
t = int(input("Enter number where repeted " + uname + ". e.g recurrcivly every 2 place from the list :  "))
x = 1

num = y+(y/t)
n = int(num)
# iterating till the range
for i in range(0, n):

    if x == t:
        lst.insert(i, uname)
        x =1

    else:
        ele = input("Enter word list 1 by 1 or copy all and paste : ")
        lst.append(ele)  # adding the element
        x= x + 1
print(lst)
# save in file
with open("file.txt", 'w') as output:
    for row in lst:
        output.write(str(row) + '\n')
print("go to file.txt and see the wordlist generated........")