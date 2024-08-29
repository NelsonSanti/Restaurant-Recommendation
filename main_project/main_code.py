import os
import time

category_restaurant = {'Italian': [{"Name": 'Bistrô Porto', 
                                   "Price": "3/5", 
                                   "Rating": "5/5", 
                                   "Address": "Rua Padre Cruz, 150"},

                                   {"Name": 'Amatriciana', 
                                   "Price": "2/5", 
                                   "Rating": "4/5", 
                                   "Address": "Rua Afonso Aveiro, 2"},

                                   {"Name": 'Buona Cucina', 
                                   "Price": "1/5", 
                                   "Rating": "2/5", 
                                   "Address": "Avenida Comandante Valódia, 7"},

                                   {"Name": 'Gillardino Gourmet', 
                                   "Price": "4/5", 
                                   "Rating": "5/5", 
                                   "Address": "Rua do Ouro, 8"
                                   }],

                        'Japanese': [{"Name": 'Sushi House', 
                                     "Price": "3/5", 
                                     "Rating": "4/5", 
                                     "Address": 
                                     "Rua das Aves, 15"},

                                    {"Name": 'Sushi Bar', 
                                    "Price": "1/5", 
                                    "Rating": "2/5", 
                                    "Address": "Rua do Sol, 5"},

                                    {"Name": 'Sushi Garden', 
                                    "Price": "2/5", 
                                    "Rating": "3/5", 
                                    "Address": "Rua da Pasteleira, 10"},

                                    {"Name": 'Sushi Time', 
                                    "Price": "4/5", 
                                    "Rating": "5/5", 
                                    "Address": "Rua da Prata, 56"
                                    }],

                        'Mexican': [{"Name": 'El Mariachi', 
                                    "Price": "1/5", 
                                    "Rating": "2/5", 
                                    "Address": 
                                    "Rua das Tomatinas, 15"},

                                    {"Name": 'El Paso', 
                                    "Price": "2/5", 
                                    "Rating": "3/5", 
                                    "Address": 
                                    "Rua do Passo Largo, 10"},

                                    {"Name": 'El Camino', 
                                    "Price": "3/5", 
                                    "Rating": "4/5", 
                                    "Address": "Rua do Caminho Longo, 5"}, 

                                    {"Name": 'El Burrito', 
                                    "Price": "5/5", 
                                    "Rating": "5/5", 
                                    "Address": "Rua do Esperto, 2"
                                    }],

                        'Chinese': [{"Name": 'China House', 
                                    "Price": "2/5", 
                                    "Rating": "3/5", 
                                    "Address": 
                                    "Rua da Anémona, 15"},

                                    {"Name": 'China Garden', 
                                    "Price": "1/5", 
                                    "Rating": "1/5", 
                                    "Address": "Rua do Jardim, 10"},

                                    {"Name": 'China Wok', 
                                    "Price": "3/5", 
                                    "Rating": "4/5", 
                                    "Address": "Rua do Lago, 5"},

                                    {"Name": 'China Town', 
                                    "Price": "4/5", 
                                    "Rating": "5/5", 
                                    "Address": "Rua do Areeiro, 2"
                                    }],

                        'Portuguese': [{"Name": 'Casa do Bacalhau', 
                                       "Price": "3/5", 
                                       "Rating": "4/5", 
                                       "Address": "Rua do Zé do Pipo, 40"},

                                       {"Name": 'Casa do Mar', 
                                       "Price": "2/5", 
                                       "Rating": "3/5", 
                                       "Address": "Rua das Camélias, 4"},

                                       {"Name": 'Casa do Pão', 
                                       "Price": "1/5", 
                                       "Rating": "2/5", 
                                       "Address": "Rua António Farinha, 1"},

                                       {"Name": 'Casa do Chá', 
                                       "Price": "4/5", 
                                       "Rating": "5/5", 
                                       "Address": "Rua Rainha Isabel II, 13"
                                    }]
                        }

#body of the project
print("Welcome to our restaurant neighborhood recommendation system!")
print("We have the following restaurant types available: \n")
print("1 - Italian")
print("2 - Japanese")
print("3 - Mexican")
print("4 - Portuguese")
print("5 - Chinese")
print("\n")
print("Please, from 1 to 5 choose one of the categories above: \n")

#user input
while True:
    print("Welcome to our restaurant neighborhood recommendation system!")
    print("We have the following restaurant types available: \n")
    print("1 - Italian")
    print("2 - Japanese")
    print("3 - Mexican")
    print("4 - Portuguese")
    print("5 - Chinese")
    print("\n")
    print("Please, from 1 to 5 choose one of the categories above: \n")
    category = input("Enter the category number: ")
    match category:
        case "1":
            print("\nYou chose Italian restaurants!")
            print("Here are the options available: \n")
            for restaurant in category_restaurant['Italian']:
                for i in restaurant:
                    print(i, ":", restaurant[i])
                print("\n")
            break           
        case "2":
            print("\nYou chose Japanese restaurants!")
            print("Here are the options available: \n")
            for restaurant in category_restaurant['Japanese']:
                for i in restaurant:
                    print(i, ":", restaurant[i])
                print("\n")
            break    
        case "3":
            print("\nYou chose Mexican restaurants!")
            print("Here are the options available: \n")
            for restaurant in category_restaurant['Mexican']:
                for i in restaurant:
                    print(i, ":", restaurant[i])
                print("\n")
            break  
        case "4":
            print("\nYou chose Portuguese restaurants!")
            print("Here are the options available: \n")
            for restaurant in category_restaurant['Portuguese']:
                for i in restaurant:
                    print(i, ":", restaurant[i])
                print("\n")
            break  
        case "5":
            print("\nYou chose Chinese restaurants!")
            print("Here are the options available: \n")
            for restaurant in category_restaurant['Chinese']:
                for i in restaurant:
                    print(i, ":", restaurant[i])
                print("\n")
            break   
        case default:
            print("Invalid input. Please, choose a number from 1 to 5.")
            time.sleep(3)
            os.system('cls')

#restart function
def restart():
    while True:
        category = input("Enter the category number: ")
        match category:
            case "1":
                print("\nYou chose Italian restaurants!")
                print("Here are the options available: \n")
                for restaurant in category_restaurant['Italian']:
                    for i in restaurant:
                        print(i, ":", restaurant[i])
                    print("\n")
                break           
            case "2":
                print("\nYou chose Japanese restaurants!")
                print("Here are the options available: \n")
                for restaurant in category_restaurant['Japanese']:
                    for i in restaurant:
                        print(i, ":", restaurant[i])
                    print("\n")
                break    
            case "3":
                print("\nYou chose Mexican restaurants!")
                print("Here are the options available: \n")
                for restaurant in category_restaurant['Mexican']:
                    for i in restaurant:
                        print(i, ":", restaurant[i])
                    print("\n")
                break  
            case "4":
                print("\nYou chose Portuguese restaurants!")
                print("Here are the options available: \n")
                for restaurant in category_restaurant['Portuguese']:
                    for i in restaurant:
                        print(i, ":", restaurant[i])
                    print("\n")
                break  
            case "5":
                print("\nYou chose Chinese restaurants!")
                print("Here are the options available: \n")
                for restaurant in category_restaurant['Chinese']:
                    for i in restaurant:
                        print(i, ":", restaurant[i])
                    print("\n")
                break   
            case default:
                print("Invalid input. Please, choose a number from 1 to 5.")
                time.sleep(3)
                os.system('cls')
    print("Do you want to check another category?", "\n" "1 - Yes", "\n" "2 - No: ")
    answer = input("\nPlease make your choice: ")
    if answer == "1":
        os.system('cls')
        restart()
    elif answer == "2":
        print("Thank you for using our system! Have a great day!")
        time.sleep(3)
        os.system('cls')
    else:
        print("Invalid input. Please, choose a number from 1 to 2.")
        time.sleep(3)
        os.system('cls')
        restart_another_category()

#restart function part 2
def restart_another_category():
    print("Do you want to check another category?", "\n" "1 - Yes", "\n" "2 - No: ")
    answer = input("\nPlease make your choice: ")
    if answer == "1":
        os.system('cls')
        restart()
    elif answer == "2":
        print("Thank you for using our system! Have a great day!")
        time.sleep(3)
        os.system('cls')
    else:
        print("Invalid input. Please, choose a number from 1 to 2.")
        time.sleep(3)
        os.system('cls')
        restart_another_category()

print("Do you want to check another category?", "\n" "1 - Yes", "\n" "2 - No: ")
answer = input("\nPlease make your choice: ")
if answer == "1":
    os.system('cls')
    restart()
elif answer == "2":
    print("Thank you for using our system! Have a great day!")
    time.sleep(3)
    os.system('cls')
else:
    print("Invalid input. Please, choose a number from 1 to 2.")
    time.sleep(3)
    os.system('cls')
    restart_another_category()
