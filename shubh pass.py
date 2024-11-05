import random
import string
print("password generator")
def s():
    a=input("Do you want to creat another password yes/no: ").lower()
    if(a=='yes'):
        main()
    elif (a=='no'):
        return
    else:
        print("invailed input")
        s()
        return
def main():
    try:
        length=int(input("Enter the password length up to 3  : "))
        if (3 >= length):
            print("invailed input")
            main()
        else:       
            lower=string.ascii_lowercase
            upper=string.ascii_uppercase
            digit=string.digits
            symbols=string.punctuation

            combine=lower+upper+digit+symbols 
            print(combine)  
            x =random.sample(combine,length)
            password="".join(x)
            print(password)
    except:
        print("invailed input")
        main()
    s()
main()
