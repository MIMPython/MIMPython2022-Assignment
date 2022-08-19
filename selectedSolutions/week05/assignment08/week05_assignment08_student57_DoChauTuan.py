# Bai 8

# vnm to eng
# Before begining the exercise we need to install and import "unidecode" library
# Do this to install: !pip install unidecode
# Reference: https://pypi.org/project/Unidecode/
from unidecode import unidecode

print(unidecode("Việt Nam Đất Nước Con Người")) # Viet Nam Dat Nuoc Con Nguoi
print(unidecode("Welcome to Vietnam !"))  # Welcome to Vietnam !
print(unidecode("VIỆT NAM ĐẤT NƯỚC CON NGƯỜI")) # VIET NAM DAT NUOC CON NGUOI

# eng to vnm
# Before begining the exercise we need to install and import "bogo" library
# Do this to install: !pip install bogo
# Reference: https://github.com/BoGoEngine/bogo-python
import bogo

print(bogo.process_sequence('Nawm ddieeuf Bacs Hoof dayj!')) # Năm điều Bác Hồ dạy!
print(bogo.process_sequence('Yeeu toor quoocs, yeeu ddoongf baof')) # Yêu tổ quốc, yêu đồng bào
print(bogo.process_sequence('Hocj taapj toots, lao ddoongj toots')) # Học tập tốt, lao động tốt
print(bogo.process_sequence('DDoanf keets toots, kyr luaatj toots'))  # Đoàn kết tốt, kỷ luật tốt
print(bogo.process_sequence('Giwx ginf veej sinh thaatj toots'))  # Giữ gìn vệ sinh thật tốt
print(bogo.process_sequence('Khieem toons thaatj thaf dungx camr ...')) # Khiêm tốn thật thà dũng cảm ...