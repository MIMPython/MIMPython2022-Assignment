import datetime, math


print("Enter initial date:")
day = int(input("dd:"))
month = int(input("mm:"))
year = int(input("yyyy:"))
initialDate = datetime.date(year, month, day)
initialPrice = float(input("Enter initial price:\n"))
wishingPrice = float(input("Enter wishing price:\n"))
rate = float(input("Enter rate:\n"))
wishingPriceDate = initialDate + datetime.timedelta(
    days=math.ceil(math.log(wishingPrice / initialPrice, rate))
)
print(
    "The earliest date for stock price to reach the wishing price:\n",
    wishingPriceDate.strftime("%d, %b, %Y"),
)
"""
Because of asking for the earliest date for stock price to reach 58.69,
the rate should be maximum in every day(?).
Result:
    - Initial date: 7/8/2022
    - Initial price: 7.24 or 7240
    - Wishing price: 58.69 or 58690
    - Rate: 1.07
    >>>7/9/2022"""
