t=[-6,-3,-8,-4,9,5,18,9,12,11,14,15,5,8,6,4,18,19,20,23,21,22,16,13]
ora=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
media=round((sum(t)/24),2)
print("Temperatura medie=",media)
print("Maxim=",max(t))
print("Minim=",min(t))
ora_tmax=[]
ora_tmin=[]
for element in range (0,len(t)) :
    if t[element]==max(t) :
        ora_tmax.append(ora[element])
        print("Ora cu temperatura maxima:",ora_tmax)
    if t[element]==min(t) :
        ora_tmin.append(ora[element])    
        print("Ora cu temperatura minima:",ora_tmin)
        