"""
a.
While loop:
- It checks the conditions first. If the conditions is satysfied, then do the statements. If not, the loop exits.
- It can run no time or some times.
Do-while loop:
- The conditions are checked after the first run. If the condition is satysfied, continue the statements. If not, the loop exits.
- It can run at least once or more.
b.
Under circumstances, while loop and do-while loop still can be equivalent converted to each other.
Example:

int x = 1;
do {
    printf(x);
    x = x + 1;
}
while (x <= 5);

equivalent to

x = 1
while x <= 5:
    print(x)
    x += 1

But when the conditions are not satysfied in the beginning, the do-while loop & while loop can not be converted.
Example:

int x = 1;
do {
    print(x);
    x = x + 1;
}
while (x < 0);

is not equivalent to

x = 1
while x < 0:
    print(x)
    x += 1
"""
