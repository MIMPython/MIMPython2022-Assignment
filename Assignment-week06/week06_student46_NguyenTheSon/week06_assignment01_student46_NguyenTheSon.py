import numpy as np
import random 
import time
# Bài 1:
# a)

def create_array_normal(rows, columns):
        random.seed(0)
        create_array = []
        for i in range(rows):
            create_array.append(random.sample(range(0, columns + rows), columns))
        return create_array

def sum_normal_columns(array):
        random.seed(0)
        sum_columns_array = []
        for col in range(len(array[0])):
            sum_column_array = 0
            for row in range(len(array)):
                sum_column_array += array[row][col]
            sum_columns_array.append(sum_column_array)
        return sum_columns_array

def sum_normal_rows(array):
        random.seed(0)
        sum_rows_array = []
        for row in range(len(array)):
            sum_row_array = 0
            for col in range(len(array[0])):
                sum_row_array += array[row][col]
            sum_rows_array.append(sum_row_array)
        return sum_rows_array

def create_array_by_numpy(rows, columns):
        np.random.seed(0)
        random_array = np.random.randint(0, rows + columns, (rows, columns))
        return random_array

def sum_columns_by_numpy(array):
        return np.sum(array, axis = 0)

def sum_rows_by_numpy(array):
        return np.sum(array, axis = 1)



if __name__ == "__main__":
    time_create_array_non_numpy = []
    time_of_sum_columns_non_numpy = []
    time_of_sum_rows_non_numpy = []

    time_create_array_by_numpy = []
    time_sum_columns_by_numpy= []
    time_sum_rows_by_numpy= []


    for row in range(500, 505):
        for col in range(500, 505):
            start_1 = time.time()
            creat_array = create_array_normal(row, col)
            end_1 = time.time()

            start_2 = time.time()
            sum_array_col = sum_normal_columns(creat_array)
            end_2 = time.time()

            start_3 = time.time()
            sum_array_rows = sum_normal_rows(creat_array)
            end_3 = time.time()

            start_4 = time.time()
            creat_array_by_numpy = create_array_by_numpy(row, col)
            end_4 = time.time()

            start_5 = time.time()
            sum_column_array_by_numpy = sum_columns_by_numpy(creat_array_by_numpy)
            end_5 = time.time()
            
            start_6 = time.time()
            sum_row_array_by_numpy = sum_rows_by_numpy(creat_array_by_numpy)
            end_6 = time.time()

            time_create_array_non_numpy.append(end_1 - start_1)
            time_of_sum_columns_non_numpy.append(end_2 - start_2)
            time_of_sum_rows_non_numpy.append(end_3 - start_3)

            time_create_array_by_numpy.append(end_4 - start_4)
            time_sum_columns_by_numpy.append(end_5 - start_5)
            time_sum_rows_by_numpy.append(end_6 - start_6)


    print('-' * 160)

    print("|{}".format("Time creat array by numpy"), "|{}".format("Time creat array non numpy"),\
        "|{}".format("Time sum columns by numpy"), "|{}".format("Time sum columns non numpy"),\
           "|{}".format("Time sum rows by numpy"), "|{}".format("Time sum rows non numpy"),"|")\

    print('-' * 160)
    for i in range(len(time_create_array_by_numpy)):
        print("|{: <25f}".format(time_create_array_by_numpy[i]), "|{: <26f}".format(time_create_array_non_numpy[i]),\
            "|{: <25f}".format(time_sum_columns_by_numpy[i]), "|{: <26f}".format(time_of_sum_columns_non_numpy[i]),\
            "|{: <22f}".format(time_sum_rows_by_numpy[i]), "|{: <23f}".format(time_of_sum_rows_non_numpy[i]),"|")

    print('-' * 160)


