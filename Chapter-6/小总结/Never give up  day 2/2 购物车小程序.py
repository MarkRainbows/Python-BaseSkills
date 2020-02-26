#Author:never give up  range your dream
shopping_list = [("iphone",3600),("opple",600),("redbull",800),("supermilk",360),("supercar",5300)]
shopping_cart = []
salary = input("Welcome to the shoppingmarket!  please input your salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for l in (shopping_list): #****
            print(shopping_list.index(l), l)#******
        choose = input("please choose your shopping number:")
        if choose.isdigit():
            choose = int(choose) #******
            if choose < len(shopping_list) > 0:#*********
                choose_buy = shopping_list[choose] #******
                p_item = choose_buy[1] #******
                if salary >= p_item:
                    shopping_cart.append(choose_buy)
                    salary -= p_item
                    print("your buying:%s your balance:%s" % (choose_buy, salary))#**********
                else:
                    print("your balance is not enouch!")
            else:
                print("your choos e number is wrong!")
        elif choose == "q":
            print("--------------------your shopping list--------------------")
            for i in shopping_cart:
                print(shopping_cart.index(i),i)
            print("your balance:",salary)
            break
        else:
            print("your input is not correct!")
else:
    print("your input is not correct!")








