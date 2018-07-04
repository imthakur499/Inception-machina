try:
    a= 562
    b= 786


    a = b/0
    #f = open("abc.txt")

    for line in f:
        print(line)

except FileNotFoundError as e:
    print(e.filename)

except Exception as e:

    print(e)

except ZeroDivisionError as e:
    print(e)

#except ZeroDivisionError:
   # print("   Natalie   ")


