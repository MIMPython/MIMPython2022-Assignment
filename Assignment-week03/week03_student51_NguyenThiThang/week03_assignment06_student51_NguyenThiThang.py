#a
def UCLN(a,b):
    while a !=b:
        if (a>b):
            a=a-b
        else:
            b=b-a
    return a
#b
if __name__=='__main__':
    print("Nhap so N")
    n= int (input())
    count=0
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if (UCLN(i,j)==1):
                count=count+1
    soCap=n*(n-1)/2
    P=(count/soCap) *100
print("Xac suat la:",P,"%")