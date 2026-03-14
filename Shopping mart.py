import os
import time 

class Mart:


    def main_menu(self):
        print("Welcome To Our Store")
        print("1 - Show Products")
        print("2 - Buy Products")
        print("3-  Admin Panel")
        print("4 - Exit")


    def show_products(self):
        os.system("cls")
        file=open("mart.txt","r")
        lines=file.readlines()
        print(f"{'No.':<5}{'Name.':<20}{'Price.':<10}")
        for index,line in enumerate(lines):
            line=line.strip()
            item_name,item_price,item_quant=line.split(",")
            print(f"{index:<5}{item_name:<20}{item_price:<10}")
        file.close()

    def buy_product(self):
        os.system("cls")
        file=open("mart.txt","r")
        lines=file.readlines()
        print(f"{'No.':<5}{'Name':<20}{'Price':<10}")
        products_dict={}
        for index,line in enumerate(lines):
            line=line.strip()
            item_name,item_price,item_quant=line.split(",")
            products_dict[item_name.lower()]=int(item_price)
            print(f"{index:<5}{item_name:<20}{item_price:<10}")
        
        total_bill=0
        bought_products=[]
        while True:
            product=input("\nEnter the name of product (or done to exit): ").lower()

            if(product=="done"):
                break
            elif product in products_dict:
                quant=int(input(("Enter the quantity of item : ")))
                price=products_dict[product]
                sub_total=quant*price
                total_bill+=sub_total
                bought_products.append((product,quant,price,total_bill))
            else:
                print("Product not found")
            print("\nProduct Name        Quantity")
            for product,quant,price,total_bill in bought_products:
                print(f"{product:<15}       {quant}")
        print(f"\nThe total bill is : {total_bill}")
    def add_product(self):
        os.system("cls")
        item_name=input("Enter the item name : ")
        item_price=int(input("Enter the item price : "))
        item_quant=int(input("Enter the item quantity : "))

        data=f"{item_name},{item_price},{item_quant}\n"
        file=open("mart.txt","a")
        file.write(data)
        file.close()

    def for_admin(self):
        print("Welcome to the Admin Panel")
        print("1 - Add Product ")
        print("2 - Exit")

    def admin_panel(self):
        while True:
            os.system("cls")
            admin_login_pass="1234"
            admin_pass=input("Enter the password : ")
            if admin_pass==admin_login_pass:
                print("Login Successfull")
                time.sleep(3)
                os.system("cls")
                m1.for_admin()
                choice= int(input("Enter the choice : "))
                while True:
                    match choice:
                        case 1:
                            m1.add_product()
                            print("\nItem Added Successfully\n")
                            print("1- Add another product")
                            add_again=input("Enter the choice (or done to exit): ")
                            if(add_again=="done"):
                                return 0
                            elif(add_again=="1"):
                                continue
                            os.system("cls")
                        case 2:
                            os.system("cls")
                            print("Good Bye")
                            print("See You Soon")
                            time.sleep(3)
                            os.system("cls")
                            return 0
                
            else:
                print("Incorrect Password")
                print("Try Again")
                time.sleep(3)
                os.system("cls")
                break
            

m1=Mart()

while True:

    m1.main_menu()
    choice=int(input("\nEnter the choice : "))
    match choice:
        case 1:
            while True:
                m1.show_products()
                key=input("\n\nEnter a to exit : ")
                if key==('a'):
                    break
            os.system("cls")
        case 2:
            while True:
                m1.buy_product()
                key=input("\nEnter a to exit : ")
                if key==('a'):
                    break
                os.system("cls")

        case 3:
                m1.admin_panel()
                os.system("cls")
        case 4:
            print("Good Bye")
            time.sleep(2)
            os.system("cls")
            break

# Shawaiz Hassan