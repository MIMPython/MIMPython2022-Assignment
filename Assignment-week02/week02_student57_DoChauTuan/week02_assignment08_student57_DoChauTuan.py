# Bài tập 8. Viết chương trình in ra các hình sau
if __name__ == "__main__":
    # (1) Half Pyramid
    for i in range(6):
        print("*"*(i+1))
    """
    *
    **
    ***
    ****
    *****
    ******
    """
    # (2) Inverted Half Pyramid
    for i in range(6):
        print("*"*(6-i))
    """
    ******
    *****
    ****
    ***
    **
    *
    """
    # (3) Hollow Inverted Half Pyramid
    for i in range(6):
        row = "*"*(6-i)
        if i in [1, 2, 3]:
            row = row[0] + ' '*(6-i-2) + row[6-i-1]
        print(row)
    """
    ******
    *   *
    *  *
    * *
    **
    *
    """
    # (4) Full Pyramid
    for i in range(1, 7):
        s = " " * (6 - i)
        for j in range(i):
            s = s + " " + "*"
        print(s)
    """
        *
       * *
      * * *
     * * * *
    * * * * *
   * * * * * *
    """
    # (5) Inverted Full Pyramid
    for i in range(6):
        s = " " * i
        for j in range(6 - i):
            s = s + ' ' + '*'
        print(s)
    """
   * * * * * *
    * * * * *
     * * * *
      * * *
       * *
        *
    """
    # (6) Hollow Full Pyramid
    for i in range(1, 7):
        s = " "*(6-i)
        if i in [3, 4, 5]:
            s += " " + "*" + " "*(2*(i-2) + 1) + "*"
        else:
            for j in range(i):
                s = s+ " "+ "*"
        print(s)
    """
      *
     * *
    *   *
   *     *
  *       *
 * * * * * *
    """