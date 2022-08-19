# Bai 7
# The answer is Yes
"""
In a 1990 article published in Journal of Recreational Mathematics, Michael Keith
of Pennsylvania, USA, showed how the palindromic squares can be classified into
the trivial squares, four infinite families of squares, plus the sporadics which
are not known to belong to any well defined family.
The simplest palindromic squares are the trivial squares, in which the squares
consist of only one digit. These are 0, 1, 4 and 9 (the squares of 0, 1, 2 and 3).

The "binary root" family of palindromic squares all have palindromic roots with an even number of digits. The digits of the roots are either 0 or 1, with no more than eight 1s appearing in the root. The root can therefore be expressed as 1[x][x]'1, where [x] is a string of zero or more of the digits 0 and 1 (with the 1 digit occuring no more than three times in the string), and [x]' is the string [x] with all the digits in reverse order. The total number of such possible roots with D digits (D must be even) is calculated by the formula (D^3 - 6N^2 + 32N)/48. The simplest examples of these palindromic squares include: 11^2 = 121, 1001^2 = 1002001, 1111^2 = 1234321, 100001^2 = 10000200001, 101101^2 = 10221412201, 110011^2 = 12102420121, 111111^2 = 12345654321, and so on.

The "ternary root" family are palindromic squares whose roots do not contain any digits greater than 2. The roots all palindromes with have an odd number of digits greater than 1. The roots are of the form 1[x]y[x]'1, where [x] and [x]' are defined as for the binary root family, and y is either 0, 1 or 2. If y = 2 then the string [x] has at most one 1, otherwise if y < 2 then [x] has at most three 1s. The total number of possible roots with D digits (D must be odd) which generate ternary root palindromic squares is expressed by the formula (N^3 - 9N^2 + 59N - 51)/24. The simplest examples of the palindromic squares of this family include: 101^2 = 10201, 111^2 = 12321, 121^2 = 14641, 10001^2 = 100020001, 10101^2 = 102030201, 10201^2 = 104060401, and so on.

The third family is known as the "even root" family, in which the roots are even numbers. The roots are of the form 2[0]2 (when the number of digits is even), or 2[0]x[0]2 (when the number of digits is odd). Here the expression [0] is a string of zero or more 0s, and x is either 0 or 1. If the root consists of D digits, only one palindromic square can result when D is even, and two when D is odd. The first few members of this family include: 22^2 = 484, 202^2 = 40804, 212^2 = 44944, 2002^2 = 4008004, 20002^2 = 400080004, 20102^2 = 404090404, etc.

The most interesting family recognised by Keith are the "asymmetric root" family. Their roots are always non-palindromic with at least seven digits, and an odd number of digits in those roots. In this family the root is of the form 1(x)0[9]9[0]1(x)'1, where (x) represents a string of at least one of the digits 0 and 1, while [0] and [9] are strings of zero or more 0s and 9s respectively. The string (x)' is the same as (x) but with the order of digits reversed. A very difficult problem (apparently still unsolved) is finding an exact formula for calculating the number of possible roots with D digits of this family which result in palindromic squares. The first few members of this family include: 1109111^2 = 1230127210321, 110091011^2 = 1212003070300121, 111091111^2 = 12341234943214321, and so on. The sequence of the number of palindromic squares of this family with roots of 7, 9, 11, 13, 15,... digits begins: 1, 2, 5, 6, 9, 10, 10, 15, 15, 16, 18, 24, 18, 26,...

The remaining palindromic squares are all of the sporadic type, and do not fit into any of the above families. The first fifty of these (the palindromic squares of 31 or fewer digits) can be extracted from a table published in a 1991 article by J. Keith R. Barnett in Journal of Recreational Mathematics. The article was actually sent to JRM in January 1986, only to be accidentally mislaid by the editor for several years!

These sporadics are listed along with 17 more I computed, covering the entire range exhaustively out to forty digits (there are no sporadics with exactly forty digits). I do not know whether this list has been completely confirmed independently by anyone else. Incidentally, the smallest possible pandigital palindromic square (a palindromic square containing all ten digits) is now known to be the square of 10101010101010101 or 102030405060708090807060504030201. If an equipandigital palindromic square (a palindromic square in which each of the ten digits occur equally often) exists, it must have at least 60 digits. I provide here a table of all 67 possible sporadic palindromic squares less than 10^40.
"""
# Reference
"""
G. J. Simmons, "Palindromic Powers," Journal of Recreational Mathematics, 3:2, pp 93-98, April 1970. 
G. J. Simmons, "On Palindromic Squares of Non-Palindromic Numbers," Journal of Recreational Mathematics, 5:1, pp 11-19, January 1972. 
R. Ondrejka, "A Palindrome (151) of Palindromic Squares," Journal of Recreational Mathematics, 20:1, pp 68-71, 1988. 
M. Keith, "Classification and Enumeration of Palindromic Squares," Journal of Recreational Mathematics, 22:2, pp 124-132, 1990. 
C. Ashbacher, "More on Palindromic Squares," Journal of Recreational Mathematics, 22:2, pp 133-135, 1990.
J. K. R. Barnett, "Tables of Square Palindromes in Bases 2 and 10," Journal of Recreational Mathematics, 23:1, pp 13-18, 1991.
"""