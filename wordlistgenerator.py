# This is for learning purpose only........
# This tool help you to generate wordlist as a valid credentials after certain regular interval of wordlist
# simply have to log in to their own account every few attempts to prevent this limit from ever being reached.
# Do not enter wrong values (there is no input validations for input) this tool is in development process
print("This is for learning purpose only........ \n ")
print("This tool help you to generate wordlist as a valid credentials after certain regular interval of wordlist \n ")
print("Do not enter wrong values (there is no input validations) this tool is in development process")
# valid credential for brute force to generate wordlist
uname = input("Enter valid word for username or password  :  ")
lst = []

# number of place where correct credential want
t = int(input("Enter number where repeted " + uname + ". e.g recurrcivly every 2 place from the list :  "))
x = 1

n = 99999999999
# iterating till the range
for i in range(0, n):

    if x == t:
        lst.insert(i, uname)
        x = 1

    else:
        ele = input("Enter word list 1 by 1 or copy all and paste   (Or you want to submit list then type y) : ")
        if ele == "y":
            break
        lst.append(ele)  # adding the element
        x = x + 1
print(lst)
# save in file
with open("file.txt", 'w') as output:
    for row in lst:
        output.write(str(row) + '\n')
print("Go to file.txt and see the wordlist generated........")
