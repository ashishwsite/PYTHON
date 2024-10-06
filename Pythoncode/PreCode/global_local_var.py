glo=9
def fun():
    glo=10
    print(glo)
# agar function ke anadr var ko cll karega to  pahle local ko search karega baad me global ko dekrga    
print("value of glo varible in fun")    
fun()
print("value of glo varible in outside the fun")  
print(glo)    