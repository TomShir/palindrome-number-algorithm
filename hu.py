import time
import random 
from colorama import Fore 
def method_name(name):
    print(f'Using method {name}')
    
while True:
    try:
        integer=int(input('integer:'))
        strinteger=str(integer)
        check_if_palindrome_msg='Alogrithm checking if number is a palindrome number or not...'
        def check_if_palindrome():
            method_name(name=1)
            time.sleep(0.5)
            print(f'{check_if_palindrome_msg}')
            time.sleep(0.5)
            if strinteger==strinteger[::-1]:
                global is_palindrome 
                is_palindrome='passed number is a palindrome number'
                print(f'{is_palindrome}')
            else:
                global is_not_palindrome 
                is_not_palindrome='Passed number is not a palindrome number'
                print(f'{is_not_palindrome}')
                
        def check_if_palindrome_2():
            method_name(name=2)
            time.sleep(0.5)
            print(f'{check_if_palindrome_msg}')
            numerical_seq=[]
            for ch in strinteger:
                numerical_seq.append(ch)
            else:
                numerical_seq.reverse()
                if ''.join(numerical_seq)==strinteger:
                     is_palindrome='passed number is a palindrome number'
                     time.sleep(0.5)
                     print(f'{is_palindrome}')
                else:
                     is_not_palindrome='passed number is not a palindrome number'
                     time.sleep(0.5)
                     print(f'{is_not_palindrome}')
                    
        check_palindrome_functions=[check_if_palindrome,check_if_palindrome_2]
        random.choice(check_palindrome_functions)()
    except ValueError:
        def error_msg(txt):
            for ch in txt:
                time.sleep(0.1)
                print(f'{Fore.RED}{ch}',flush=True,end='')
            else:
                reset_to_default_color=Fore.RESET 
                print(f'{reset_to_default_color}')
                
        error_msg(txt='Error, not a numeric value')