x=[1,2,3,4,5]
y=x
suma1=x[0]+x[1]+x[2]
print("Suma primelor 3 comp ale x=",suma1)
print('y=',y)
print("Suma tuturor comp y=",sum(y))
produsul=1
for element in range(0,len(x)):
    produsul=produsul*x[element]
print("Produsul=",produsul)    
print("Valoare abs=",abs(y[3]))
print("Suma primelor comp=",x[0]+y[0])