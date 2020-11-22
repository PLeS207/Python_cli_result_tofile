import argparse


parser = argparse.ArgumentParser(description="Simple Calculation")

parser.add_argument('A', type=float, help='First number')
parser.add_argument('B', type=float, help='Second number')

parser.add_argument('-m', '--multiply', '--mul', action="store_true", help='multiply')
parser.add_argument('-d', '--division', '--div', action="store_true", help='division')
parser.add_argument('-s', '--subtraction', '--sub', action="store_true", help='subtraction')
parser.add_argument('-a', '--addiction', '--add', action="store_true", help='addiction')
parser.add_argument('-o', '--file', nargs='+', help='output to file')
parser.add_argument('--append', nargs='?', default='w', const='a', help='append result to file')


args = parser.parse_args()

if args.multiply:
    ans = args.A * args.B

elif args.division:
    if args.B == 0:
        raise ValueError('Division by zero!!')
    ans = args.A / args.B

elif args.subtraction:
    ans = args.A - args.B

elif args.addiction:
    ans = args.A + args.B

else:
    ans = args.A + args.B

if args.file:
        f = open(args.file[0], args.append)
        f.write('Result = ' + str(ans) + '\n')
        f.close()
else:
    print(ans)




