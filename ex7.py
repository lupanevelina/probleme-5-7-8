zi=["Luni","Marti","Miercuri","Joi","Vineri","Sambata","Duminica"]
venit=[200,350,400,360,180,480,280]
print("Venitul saptamanal=",sum(venit))
media=round((sum(venit)/7),2)
print("Media venitului zilnic=",media)
maxv=max(venit)
minv=min(venit)
ziua_maxv=[]
ziua_minv=[]
for element in range(0,len(zi)):
    if venit[element]==maxv :
        ziua_maxv.append(zi[element])
        print("Cel mai mare venit:",ziua_maxv)
    if venit[element]==minv :
        ziua_minv.append(zi[element]) 
        print("Cel mai mic venit:",ziua_minv)  
