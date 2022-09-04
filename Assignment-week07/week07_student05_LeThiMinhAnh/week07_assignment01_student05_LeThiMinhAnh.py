def meanOfList(lst):
    try:
        result = sum(lst)/len(lst)
        print("The mean of the list of numbers is:", result)
    except ZeroDivisionError:
        print("This is an empty list")
    except Exception:
        print("List contains only numbers")


lst1 = []
meanOfList(lst1)  # This is an empty list
lst2 = ["a", "b", "c", 4, 5]
meanOfList(lst2)  # List contains only numbers
lst3 = [12, 56, 34]
meanOfList(lst3)  # The mean of the list of numbers is: 34.0
