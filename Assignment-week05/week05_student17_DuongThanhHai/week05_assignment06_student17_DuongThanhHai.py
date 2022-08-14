
import argparse

parser = argparse.ArgumentParser(description='File Name')
parser.add_argument('-w', '--week', type = int)
parser.add_argument('-a', '--assignment', type = int)
parser.add_argument('-n', '--name', type = str)

args = parser.parse_args()

w = args.week
a = args.assignment
n = args.name

print ('week' + "%02d" % w + '_' + 'assignment' + '%02d' % a + '_' + n + '.py')

    

