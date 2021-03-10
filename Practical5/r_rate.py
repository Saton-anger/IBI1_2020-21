n=84
r=1.2
add=n
for i in range(1,6):
#calculate the new students who are infected
    add=add*r
#calculate the total students
    n=n+add
print("the r rate is:",r,"  number of infected individuals after 5 rounds of infectionn:",n)

