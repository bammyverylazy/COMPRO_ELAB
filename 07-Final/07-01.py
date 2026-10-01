# 12 Sort elements in a list
user = input("Enter list of tuple: ").split()
lst_input = []

for i in user:
    blank = ()
    for x in i:
        blank = blank +(int(x),)
    lst_input.append(blank)

print(f"Input list: {lst_input}")
lst_output = sorted(lst_input, key = lambda x : x[-1])
print(f"Output list: {lst_output}")

# 13 Count the number of unique sublists
num = eval(input("Input: "))
num_dict ={}

for x in num:
    x = str(x)
    num_dict[x] = num_dict.get(x, 0) + 1
num_dictt = dict(sorted(num_dict.items(), key = lambda x: x[1] , reverse = True))
#print(num_dictt)
for k , v in num_dictt.items():
    print(f"{k}: {v}")


# 14 Count consecutive objects // not finished
user = eval(input("Enter a list of objects: "))

def countConsec(lst):
    if len(lst) == 0:
        return "Nothing to do."
    dictt_shell = []
    visited = set()
    for x in lst:
        if x in visited:
            continue
        dictt_shell.append((x, lst.count(x)))
        visited.add(x)
    return dictt_shell
        
output = countConsec(user)
outputt = sorted(output, key= lambda x: x[-1] , reverse = True)
print(outputt[0][0])
print(outputt[0][1])

# 15 Find top K occurrences in a text
dictt = {}
print("Parse a long paragraph (or text) below, following an ENTER as needed:")
while True:
    user = input()
    if user == "":
        k = int(input("Top K rank: "))
        break
    userr = user.split()
    for c in userr:
        dictt[c] = dictt.get(c, 0)+1
    
dictt_sorted = sorted(dictt.items(), key = lambda x : x[1] , reverse = True)[:k]


