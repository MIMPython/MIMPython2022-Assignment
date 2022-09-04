def returnAverage(list):
    try :
        size = int(input("Enter size of list: "))
        assert size != 0
        for turn in range(0, size):
            try:
                listNumber = float(input("Enter number " + str(turn + 1) + " of list: "))
                list.append((listNumber))
            except ValueError: #catch input error
                print('element must be float')
        print(sum(list) / len(list))
    except AssertionError:
        print('len must differnt from zero')
    except ValueError:
        print('size must be int')
     
#run program
list = []
returnAverage(list)