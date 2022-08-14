import math
import datetime
MAX_PRICE = 58.59
DATE = datetime.datetime(2022,8,7,0,0,0,0)
def real_price(price):
    day_num = math.log(MAX_PRICE/price, 1.07)
    day_out = DATE + datetime.timedelta(days = day_num)
    return day_out
    
    
def after_point_price(price):
    string_price = str(price).split('.')
    string_price_out = ''
    for i in range(2):
        string_price_out += string_price[i]
    for i in range(len(string_price_out), 2):
        string_price_out += '0'
    price_out = float(string_price_out)
    day_num = math.log(MAX_PRICE/price, 1.07)
    day_out = DATE + datetime.timedelta(days = day_num)
    return day_out
    
    
if __name__ == '__main__':
    price_a = 7.24
    price_b = 32.40
    print(real_price(price_a)) # 2022-09-06 21:42:11.082155
    print(after_point_price(price_b)) # 2022-08-15 18:08:21.141008
