import argparse
import math

parser = argparse.ArgumentParser()


parser.add_argument("square", type=int,
                    help="display a square of a given number")
                    
parser.add_argument("-v", "--verbosity", action="count",
                    help="increase output verbosity")

parser.add_argument("-s", "--sqrt", action="store_false",
                    help="get square root")

parser.add_argument('-o', '--file', nargs='+', help='output to file')
parser.add_argument('--append', nargs='?', default='w', const='a', help='append result to file')

args = parser.parse_args()


if args.sqrt:
    answer = args.square**2
    mod = 'square'
    mod2 = f"{args.square}^2 = {answer}"
else:
    answer = math.sqrt(args.square)
    mod = 'square root'
    mod2 = f"sqrt({args.square}) = {answer}"


if args.file:
    f = open(args.file[0], args.append)
    result = f.write
else:
    result = print

if args.verbosity == 2:
    result(f"the {mod} of {args.square} equals {answer}" + '\n')
elif args.verbosity == 1:
    result(mod2 + '\n')
else:
    result(answer + '\n')
# if args.file:
#         f = open(args.file[0], args.append)
#         if args.verbosity == 2:
#             f.write(f"the {mod} of {args.square} equals {answer}" + '\n')
#         elif args.verbosity == 1:
#             f.write(f"{mod2}" + '\n')
#         else:
#             f.write(f"{answer}" + '\n')
#         f.close()
#
# else:
#     if args.verbosity == 2:
#         print(f"the {mod} of {args.square} equals {answer}")
#     elif args.verbosity == 1:
#         print(mod2)
#     else:
#         print(answer)

