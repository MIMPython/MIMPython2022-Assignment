from concurrent.futures import process
import time
startTime = time.time()
max = 0
for number in range(2, 1000001):
    count = 1
    while number > 1:
        if number % 2 == 0:
            number = number/2
            count += 1
        else:
            number = 3 * number + 1
            count += 1
    if count >= max:
            max = count
endTime = time.time()
processingTime = endTime - startTime

print('the number of numbers of longest set of collatz sequence is: ' + str(max))
print('processing time: ' + str(processingTime))
        