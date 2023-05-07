# Program to compute the electricity bill for household:
n=int(input("Enter the units of electricity consumed in a month ="))
Bill=0
part1=min(100,n) #per unit 4.5rs in part1
part2=min(100,n-part1)  #per unit 6rs in part2
part3=min(100,n-part1-part2)  #per unit 10rs in part3
part4=n-part1-part2-part3    #per unit 20rs in part4

#METHOD:-1
L=[part1*4.5,part2*6,part3*10,part4*20]

for i in L:
    Bill=Bill+i
print(Bill)

#METHOD:-2
L=[part1,part2,part3,part4]
M=[4.5,6,10,20] #all per unit rates corresponding to the parts
for i in range(len(L)):
    Bill=Bill+L[i]*M[i]
print(Bill)

