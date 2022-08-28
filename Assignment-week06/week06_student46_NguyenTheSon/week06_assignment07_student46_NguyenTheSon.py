# Bài 7:
import numpy as np

def  product_four_numbers_direction_up(array):
    list_product_numbers = []
    for row in range(len(array) - 3):
        for column in range(len(array[0])):
            product_numbers = 1
            for i in range(4):
                product_numbers *= array[row + i][column]
            list_product_numbers.append(product_numbers)
    return np.max(np.array(list_product_numbers))

def product_four_numbers_direction_right(array):
    list_product_numbers = []
    for row in range(len(array)):
        for column in range(len(array[0]) - 3):
            product_numbers = 1
            for i in range(4):
                product_numbers *= array[row][column + i]
            list_product_numbers.append(product_numbers)
    return np.max(np.array(list_product_numbers))

def product_four_numbers_direction_diagonally_1(array):
    list_product_numbers = []
    for row in range(len(array) - 3):
        for column in range(len(array[0]) - 3):
            product_numbers = 1
            for i in range(4):
                product_numbers *= array[row + i][column + i]
            list_product_numbers.append(product_numbers)
    return np.max(np.array(list_product_numbers))

def product_four_numbers_direction_diagonally_2(array):
    list_product_numbers = []
    for row in range(len(array) - 1, 2, - 1):
        for column in range(len(array[0]) - 1, 2, - 1):
            product_numbers = 1
            for i in range(4):
                product_numbers *= array[row - i][column - i]
            list_product_numbers.append(product_numbers)
    return np.max(np.array(list_product_numbers))

with open("additionalFolder/data_for_assignment07.txt", 'r') as f:
    all_lines = f.read().split()
    all_lines = np.array(all_lines, dtype = int).reshape(20,20)

protduct_1 = product_four_numbers_direction_up(all_lines)
protduct_2 = product_four_numbers_direction_right(all_lines)
protduct_3 = product_four_numbers_direction_diagonally_1(all_lines)
protduct_4 = product_four_numbers_direction_diagonally_2(all_lines)

max(protduct_1, protduct_2, protduct_3, protduct_4) #51267216