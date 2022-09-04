def listAverage(data: list):
    try:
        assert len(data) != 0
        avr = sum(data) / len(data)
        if avr % 1 == 0:
            return int(avr)
        return avr
    except AssertionError:
        print("Empty List!")
        return
        

print(listAverage([]))