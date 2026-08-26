# Write a program to fill a letter template given below with name and date:
# letter = ''' 
#       Dear <|Name|>,
#       You are selected!
#       <|Date|>
#          '''

Name = input("Enter your name: ")
Day = int(input("Enter Date: "))
Month = int(input("Enter a month from 0 to 12: "))
Year = int(input("Enter Year: "))

letter = (f'''
        Dear <|{Name}|>,
        You are selected!
        <|{Day} - {Month} - {Year}|>
        ''')

print(letter)