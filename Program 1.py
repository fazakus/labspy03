a=100000000
for s in range(1,9):
    if(s>=1 and s<=2):
        b=a*0
        print("Laba bulan ke-",s,":",b)

    if(s>=3 and s<=4):
        c=a*0.01
        print("Laba bulan ke-",s,":",c)

    if(s>=5 and s<=7):
        d=a*0.05
        print("Laba bulan ke-",s,":",d)

    if(s==8):
        e=a*(0.03)
        print("Laba bulan ke-",s,":",e)

total=b+b+c+c+d+d+d+e
print("total : ",total)