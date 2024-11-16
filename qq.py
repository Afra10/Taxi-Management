import datetime
import random
import sys
import priceplans

cities = [ "alvin", "jamz", "razi", "mali", "zuhar"]

def getPrice(startCity, endCity, vehicle):
    startCity_lower = startCity.lower()
    endCity_lower = endCity.lower()

    if startCity_lower == endCity_lower:
        return 0  # If traveling between the same cities, the price is 0 KMD
    else:
        if vehicle == 2: #car
            price = priceplans.price_plan[startCity_lower][endCity_lower] * 2
        elif vehicle == 3: #van
            price = priceplans.price_plan[startCity_lower][endCity_lower] * 3
        else: #Trishaw
            price = priceplans.price_plan[startCity_lower][endCity_lower]
    
    return price

def isLuckyPassenger():
    return random.randint(1, 1000000) == 1


def getRandomReduction():
    return random.randint(1, 15)
        
def getInvoice(startCity, endCity, vehicle, promo):
    price = getPrice(startCity, endCity, vehicle)
    randomReduction = getRandomReduction() if isLuckyPassenger() else 0
    if (promo == 0):
        finalPayment = price - randomReduction
    else:
        finalPayment = price - promo 
        randomReduction = 0

    date = datetime.datetime.now().strftime("%Y-%m-%d")
    time = datetime.datetime.now().strftime("%H.%M.%S")
    
    print("finalPayment : ")
    print(finalPayment)
    print("date: ")
    print(date)
    print("time : ")
    print(time)
    print(" Start City : ")
    print(startCity)
    print("End City : ")
    print(endCity)
    print("Promo : ")
    print(promo)
    print("Random Reduction : ")
    print(randomReduction)
    

    filename = f"{date}_{time}_{random.randint(1000, 9999)}.txt"

    with open(filename, "w") as f:
        f.write(
            f"Date: {date}\nTime: {time}\nStart: {startCity}\nEnd: {endCity}\nAmount: {price} KMD\nPromo: {promo} KMD\nRandom Reduction: {randomReduction} KMD\nFinal Payment: {finalPayment} KMD")

def getPricePlan():
    return priceplans.price_plan
    
def getPromo(code):
    if code.startswith("pro"):
        if code[3:].isdigit():
            promo = int(code[3:])
            return promo
        else:
            print("Promo code is not valid. promo = 0 KMD")
            return 0
    else: 
        print("Promo code is not valid. promo = 0 KMD")
        return 0
    
def main():
    while True:
        # input commands
        commands = [command.lower()for command in input("Enter the command : ").split()]
        length = len(commands)
        
        if (commands[0] != "dm"):
            print("Please enter a valid command.")
            continue
            
        else:
            if (length == 2):
                if (commands[1] == "/"):
                    print("dm <start_city> <end_city> : Shows the price between the two cities and generates an invoice file for the trip")
                    print("dm <start_city> <end_city> /pro2 : Shows the price between the two cities after applying the promo code. The promo code amount is deducted from the final bill value. This will generate an invoice file for the trip with a promo details. 2 KMD is reduced here.")
                    print("dm /price : Show the full price plan for the whole country (for all 3 vhicles)")
                    print("dm <start_city> <end_city> /c : Shows the price between the two cities and generates an invoice file for the trip. This uses a car (c for car while /v for a van. Default is Trishaw")
                    print("dm <start_city> <end_city> /pro10 /v :Shows the price between the two cities while apply a 10 KMD reduction to total bill. The rider prefers a van")
                    print("dm / : Show how this 'dm' command functions")
                    
                elif (commands[1] == "/price"):
                    print("full price plan for the whole country (for all 3 vhicles) :")
                    pricePlan = getPricePlan()
                    print(pricePlan)
                    
                else:
                    print("Please enter a valid command.")
                    continue
                    
            elif (length == 3):
                    if (commands[1] in cities):
                            if (commands[2] in cities):
                                print("Invoice : ")
                                promo = 0
                                invoice = getInvoice(commands[1], commands[2], 1, promo)
                            else:
                                print("Please enter a valid command.")
                                continue
                    
                    else:
                        print("Please enter a valid command.")
                        continue
                        
            elif (length == 4):
                #only promo
                    if (commands[1] in cities):
                            if (commands[2] in cities):
                                promo = getPromo(commands[3])
                                print("Invoice : ")
                                invoice = getInvoice(commands[1], commands[2], 1, promo)
                            else:
                                print("Please enter a valid command.")
                                continue
                    
                    else:
                        print("Please enter a valid command.")
                        continue
                        
                #only vehicle
                    if (commands[1] in cities):
                            if (commands[2] in cities):
                                #car
                                if (commands[3] == "/c"):
                                    promo = getPromo(commands[3])
                                    print("Invoice : ")
                                    invoice = getInvoice(commands[1], commands[2], 2, promo)
                                #van    
                                elif (commands[3] == "/v"):
                                    promo = getPromo(commands[3])
                                    print("Invoice : ")
                                    invoice = getInvoice(commands[1], commands[2], 3, promo)
                                    
                                else:
                                    print("Please enter a valid command.")
                                    continue
                            else:
                                print("Please enter a valid command.")
                                continue
                    
                    else:
                        print("Please enter a valid command.")
                        continue
                        
            elif (length == 5):
                    if (commands[1] in cities):
                            if (commands[2] in cities):
                                #car
                                if (commands[4] == "/c"):
                                    print("Invoice : ")
                                    invoice = getInvoice(commands[1], commands[2], 2, promo)
                                #van    
                                elif (commands[4] == "/v"):
                                    print("Invoice : ")
                                    invoice = getInvoice(commands[1], commands[2], 3, promo)
                                    
                                else:
                                    print("Please enter a valid command.")
                                    continue
                            else:
                                print("Please enter a valid command.")
                                continue
                    
                    else:
                        print("Please enter a valid command.")
                        continue      
            else:
                print("Please enter a valid command.")
                continue
                    
if __name__ == "__main__":
    main()