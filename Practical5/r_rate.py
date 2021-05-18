n=84
r=1.2
add=n
# The	rate	of	reproduction	of	a	virus,	e.g.	COVID-19,	can	be	quantified	using	the	‘r’	number	which
# is	the	average	number	of	individuals	infected	by	each	individual	with	the	virus.	An	r	rate	of	1.2
# means	that	each	infected	individual	will	on	average	infect	1.2	individuals.
for i in range(1,6):
# calculate the new students who are infected
    add=add*r
# calculate the total students
    n=n+add
print("the r rate is:",r,"  number of infected individuals after 5 rounds of infectionn:",n)
