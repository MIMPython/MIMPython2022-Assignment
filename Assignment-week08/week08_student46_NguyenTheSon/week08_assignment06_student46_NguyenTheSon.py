# BÀi 6:
def longest_collatz_sequence(number_check = 1000000):
    list_collatz_sequence_number_check = []
    for number in range(1, number_check + 1):
        list_collatz_sequence = [number]
        while number != 1 :
            if number % 2 == 0:
                number //= 2
            else:
                number = number * 3 + 1
            
            if len(list_collatz_sequence_number_check) != 0:
                for index in range(len(list_collatz_sequence_number_check)):
                    if number in list_collatz_sequence_number_check[index]:
                        index_number = list_collatz_sequence_number_check[index].index(number)
                        for i in list_collatz_sequence_number_check[index][index_number:]:
                            list_collatz_sequence.append(i)
                        list_collatz_sequence_number_check.append(list_collatz_sequence)
                        break
            
                    
            list_collatz_sequence.append(number)    # thêm số 1 vào dãy 
        if len(list_collatz_sequence_number_check) < number:
            list_collatz_sequence_number_check.append(list_collatz_sequence)
    return list_collatz_sequence_number_check