print( "running tester.py...")

import my_import
print(f"inside tester.py: __name__ is: {__name__}")

if __name__ == '__main__':
    print("Tester.py's __name__ block running...")
    print("this is the file we kicked off the program with...")