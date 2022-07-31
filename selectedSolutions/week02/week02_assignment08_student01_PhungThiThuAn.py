def draw_half_pyramid(size):
    for row in range(1, size+1):
        print('*' * row)

draw_half_pyramid(6)
# *
# **
# ***
# ****
# *****
# ******

def draw_inverted_half_pyramid(size):
    for row in range(size, 0, -1):
        print('*' * row)

draw_inverted_half_pyramid(6)
# ******
# *****
# ****
# ***
# **
# *

def draw_hollow_inverted_half_pyramid(size):
    print('*' * size)
    for row in range(size-1, 1, -1):
        print('*' + ' ' * (row-2) + '*')
    print('*')
    
draw_hollow_inverted_half_pyramid(6)
# ******
# *   *
# *  *
# * *
# **
# *

def draw_full_pyramid(size):
    for row in range(1, size+1):
        space = (size - row) * ' '
        print(space + '* ' * row)

draw_full_pyramid(6)
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# * * * * * *

def draw_inverted_full_pyramid(size):
    for row in range(size, 0, -1):
        space = (size - row) * ' '
        print(space + '* ' * row)

draw_inverted_full_pyramid(6)
# * * * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *

def draw_hollow_full_pyramid(size):
    print(' ' * (size-1) + '*')
    for row in range(2, size):
        space_out = (size - row) * ' '
        space_in = (row-2) * 2 * ' '
        print(space_out + '* ' + space_in + '*')
    print('* ' * size)

draw_hollow_full_pyramid(6)
#      *
#     * *
#    *   *
#   *     *
#  *       *
# * * * * * *