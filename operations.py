from cmath import e
from cal import add,sub,mul,div
import argparse

parser = argparse.ArgumentParser()

try:
    parser.add_argument('-o', '--operation',
    help='operation to perform',
    choices=['add', 'sub', 'mul', 'div'],
    required=True)
    
    parser.add_argument('-n1', '--number1', help='number1', 
    type=int)
    parser.add_argument('-n2', '--number2', help='number2', 
    type=int)

    args = parser.parse_args()

    if args.operation == 'add':
        print(add(args.number1, args.number2))
    elif args.operation == 'sub':
        print(sub(args.number1, args.number2))
    elif args.operation == 'mul':
        print(mul(args.number1, args.number2))
    elif args.operation == 'div':
        print(div(args.number1, args.number2))  
        
except Exception as e:
    print(e)      