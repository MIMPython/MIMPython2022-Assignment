from unittest import result


A = """
    Python was designed to be easy to understand and fun to use (its name came 
    from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, 
    and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python 
    a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, 
    gand it has replaced Java as the most popular introductory language at Top U.S. Universities.
    """
# a)    
print ("Python" in A )       # True
print ("contains" in A)      # False
print ("experience" in A)    # True
print ("difficult" in A)     # False

# b)
print (A.count("Python"))    # 5

# c)
print (len(A.split(" ")))    # 102

# d)
result = ""
B = A.split(".")
for i in range(len(B)):
    if i == 0:
        result += B[i].upper() + "."
    else:
        result += B[i] + "."
print (result)      # PYTHON WAS DESIGNED TO BE EASY TO UNDERSTAND AND FUN TO USE (ITS NAME CAME
                    # FROM MONTY PYTHON SO A LOT OF ITS BEGINNER TUTORIALS REFERENCE IT). Fun...
