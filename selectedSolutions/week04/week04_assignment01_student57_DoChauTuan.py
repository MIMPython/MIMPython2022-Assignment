# bai 1
# them tieu chi dua vao do dai cua list on trong truong hop 2 list on co cung tong

def sort_a_list(a):
  return sorted(a, key=lambda x: (sum(x), len(x)))

print(sort_a_list([[1,2], [3,0,4], [1, 1], [2], [4,5]]) # [[2], [1, 1], [1, 2], [3, 0, 4], [4, 5]]
