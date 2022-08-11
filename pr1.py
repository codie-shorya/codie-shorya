while True:
    print("Hi Welcome here ...")
    input_user_wish=input(print('''Here you can calculate numbers: 
        Type - to subtract 
        Type + to add 
        Type * to multiply 
        Type / to divide 
        Type exit to exit the  program: '''))

    number1=int(input("enter the number please:"))
    
    number2=int(input("enter the second number please:"))
    
    if number1==33 and number2==45:
        print("the answer is\n 77")
    elif number1==22 and number2==32:
        print("the answer is\n 4")
    elif number1==44 and number2==22:
        print("the answer is\n 2")
    else:
        if input_user_wish=='-':
            print("The answer is\n",number1-number2)
        elif input_user_wish=='/':
            print("The answer is\n",number1/number2)
        elif input_user_wish=='*':
            print("The answer is\n",number1*number2)
        elif input_user_wish=='+':
            print("The answer is\n",number1+number2)
        elif input_user_wish.lower()=="exit":
            print("Thank you for using our calculator.Have a good day ahead")
            exit()
        else:
            print("sorry,invalid choice.Kindly write the correct number along with its assignment....")
            

