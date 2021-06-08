# -*- coding: utf-8 -*-



import argparse

parser = argparse.ArgumentParser()

parser.add_argument("number_1", type=int, help="An integer")
parser.add_argument("number_2", type=int, help="Another integer")
parser.add_argument("--operation", choices=["div", "sub", "sum", "mult"])

parser.parse_args()


args = parser.parse_args()

print(args)

if args.operation == "div":
    result = args.number_1 / args.number_2 
elif args.operation == "sub":
    result = args.number_1 - args.number_2
elif args.operation == "sum":
    result = args.number_1 + args.number_2 
elif args.operation == "mult":
    result = args.number_1 * args.number_2

print(result)


