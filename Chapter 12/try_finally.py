def main():

    try:
        a = int(input("Enter value of a: "))
        print(a)

    except Exception as e:
        print(e)

    finally:
        print("I am inside finally")

main()