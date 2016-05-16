#!/usr/bin/python -tt

import sys

def main():
     if len(sys.argv) >= 2:
        name = sys.argv[1]
        a = len(sys.argv[1])
     else:
         name = 'world!'
         a = 0
#     print 'hello'   
     print 'hello', name, a 
     print 'Hi there!'
    
if __name__ == '__main__':
    main()

