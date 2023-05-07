# To count the vowels in the given string
string="i want to become a data scientist"
vowels=['a','e','i','o','u']
count=0
#METHOD:-1
print(len(string))
for i in string:
    if i in vowels:
        count=count+1
print(count)

#METHOD:-2
for i in string:
    if i=='a':
        count=count+1
    elif i=='e':
        count=count+1
    elif i=='i':
        count=count+1
    elif i=='o':
        count=count+1
    elif i=='u':
        count=count+1
print(count)