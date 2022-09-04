def sumList(a):
    try:
        return sum(a)/len(a)
    except ZeroDivisionError:
        print("Empty List")
    finally:
        print("done")

if __name__=='__main__':
    list1=[]
    print(sumList(list1))
    list2=[1,2,3]
    print(sumList(list2))
