import csv

data = open('WoWs Ship Name.csv', 'r') #Imports CSV file into data object
csv_data = csv.reader(data) #Reads CSV data into csv_data object

ship_data = {} #Creates Dictionary to store ship data
target_ships = []


for row in csv_data: #Converts all CSV data and puts into ship_data Dictionary
    ship_data[row[0]] = {'Citadel Position': row[1], 'Bow Armour': row[2], 'Icebreaker Bow': row[3], 'Icebreaker Type': row[4], 'Turtleback Protection': row[5], 'Gun Caliber': row[6], 'Overmatch Potential': row[7], 'Tier': row[8], 'Class': row[9]}

def overmatchCheck(tier, overmatch_value):
    for key, value in ship_data.items():
       if (float(tier) - float(value["Tier"])) <= 2:
           if value['Icebreaker Bow'] == 'None':
               if value['Bow Armour'] != "":
                   if float(overmatch_value) < float(value['Bow Armour']):
                       print(str(int(float(value['Tier']))) + " - " + key)

           #elif float(overmatch_value) < float(value["Icebreaker Bow"]):
               #print(key)
           elif value['Icebreaker Bow'] != "":
               if float(overmatch_value) < float(value['Icebreaker Bow']):
                   print(str(int(float(value['Tier']))) + " - " + key)
           else:
               print(str(int(float(value['Tier']))) + " - " + key)




user_input = input("Enter Ship Name or Gun Caliber").lower().capitalize()
user_input2 = input("Is this a ship or gun caliber?").lower()



if user_input2 == 'ship':
    overmatch_value = ship_data[user_input]['Overmatch Potential']
    tier = int(ship_data[user_input]['Tier'])
    overmatchCheck(tier, overmatch_value)

elif user_input2 == 'gun caliber' or 'caliber' or 'gun':
    tier = input("What is the ship tier? If no tier write NA")
    overmatch_value = int(user_input) / 14.3
    overmatchCheck(tier, overmatch_value)


