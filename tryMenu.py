
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import random
from datetime import date
from datetime import datetime



root  = Tk()

prices = {"Beef Pita Wrap":80,
          "Chicken Pita Wrap": 80,
        "Kebab Wrap":85,
        "Chicken Kebab Wrap" :85,
        "Hotdog Wrap": 85,
        "Small Pita Wrap": 85,
        "Beef Rice": 130,
        "Chicken Rice":130,
        "Kebab Rice":150,
        "Chicken Kebab Rice":150,
        "Hotdog Rice": 150,
        "Rice Bowl":85,
        "Beef Rice Steak":240,
        "Chicken Rice Steak":180,
        "Beef and Chicken Platter":210,
        "Beef and Kebab Platter":210,
        "Chicken and Kebab Platter":210,
        "Turks Java Rice":25
          }

root.title("TURKS")
root.state('zoomed')#
# ------------------------------------FUNCTIONS--------------------------------------------- #

#Generating a random Order ID when starting a new order

def ORDER_ID():
    numbers = [0,1,2,3,4,5,6,7,8,9]
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    order_id = "TURKS_"
    random_letters =""
    random_digits = ""
    for i in range(0,3):
        random_letters += random.choice(letters)
        random_digits +=str(random.choice(numbers))


    order_id += random_letters +random_digits
    return order_id


#region add to order button
def add():
#updating the transaction label
    current_order= orderTransaction.cget("text")
    added_dish = displayLabel.cget("text") + "...." + str(prices [displayLabel.cget("text")]) + "$ "
    updated_order=current_order + added_dish
    orderTransaction.configure(text=updated_order)

    # updating the order total label
    order_total = orderTotalLabel.cget("text").replace("TOTAL : ","")
    order_total = order_total.replace("$", "")
    updated_total = int(order_total) + prices[displayLabel.cget("text")]
    orderTotalLabel.configure(text="TOTAL : " + str(updated_total) + "$")

def remove():
    dish_to_remove =displayLabel.cget("text") + "...." + str(prices [displayLabel.cget("text")]) 
    transaction_list = orderTransaction.cget("text").split("$ ")
    transaction_list.pop(len(transaction_list) - 1)

    if dish_to_remove in transaction_list:
        #update transaction label
        transaction_list.remove(dish_to_remove)
        updated_order = ""
        for item in transaction_list:
            updated_order += item + "$ "
        
        orderTransaction.configure(text  = updated_order)

        #update transaction total
        order_total = orderTotalLabel.cget("text").replace("TOTAL : ","")
        order_total = order_total.replace("$", "")
        updated_total = int(order_total) - prices[displayLabel.cget("text")]
        orderTotalLabel.configure(text="TOTAL : " + str(updated_total) + "$")

#end region

#region Display Button Function
def displayBeefPitaWrap():
    beefPitaWrap.configure(relief = 'sunken', style = 'SelectedDish.TFrame')

   
    chickenPitaWrap.configure(style="DishFrame.TFrame")
    kebabWrap.configure(style="DishFrame.TFrame")
    chickenKebabWrap.configure(style="DishFrame.TFrame")
    hotdogWrap.configure(style="DishFrame.TFrame")
    smallPitaWrap.configure(style="DishFrame.TFrame")
    beefRice.configure(style="DishFrame.TFrame")
    chickenRice.configure(style="DishFrame.TFrame")
    kebabRice.configure(style="DishFrame.TFrame")
    chickenKebabRice.configure(style="DishFrame.TFrame")
    hotdogRice.configure(style="DishFrame.TFrame")
    riceBowl.configure(style="DishFrame.TFrame")
    beefRiceSteak.configure(style="DishFrame.TFrame")
    chickenRiceSteak.configure(style="DishFrame.TFrame")
    beefandChickenPlatter.configure(style="DishFrame.TFrame")
    beefandKebabPlatter.configure(style="DishFrame.TFrame")
    chickenandKebabPlatter.configure(style="DishFrame.TFrame")
    turksJavaRice.configure(style="DishFrame.TFrame")
    

    displayLabel.configure(image = beefPitaWrapImage, text = 'Beef Pita Wrap', font = ("Helvetica", 30, 'bold'),
                           foreground = 'Black', compound ='bottom', padding = (5,5,5,5) )
    
def displayChickenPitaWrap():
    chickenPitaWrap.configure(relief = 'sunken', style = 'SelectedDish.TFrame')

    beefPitaWrap.configure(style="DishFrame.TFrame")
  
    kebabWrap.configure(style="DishFrame.TFrame")
    chickenKebabWrap.configure(style="DishFrame.TFrame")
    hotdogWrap.configure(style="DishFrame.TFrame")
    smallPitaWrap.configure(style="DishFrame.TFrame")
    beefRice.configure(style="DishFrame.TFrame")
    chickenRice.configure(style="DishFrame.TFrame")
    kebabRice.configure(style="DishFrame.TFrame")
    chickenKebabRice.configure(style="DishFrame.TFrame")
    hotdogRice.configure(style="DishFrame.TFrame")
    riceBowl.configure(style="DishFrame.TFrame")
    beefRiceSteak.configure(style="DishFrame.TFrame")
    chickenRiceSteak.configure(style="DishFrame.TFrame")
    beefandChickenPlatter.configure(style="DishFrame.TFrame")
    beefandKebabPlatter.configure(style="DishFrame.TFrame")
    chickenandKebabPlatter.configure(style="DishFrame.TFrame")
    turksJavaRice.configure(style="DishFrame.TFrame")

    displayLabel.configure(image = chickenPitaWrapImage, text = 'Chicken Pita Wrap', font = ("Helvetica", 30, 'bold'),
                           foreground = 'Black', compound ='bottom', padding = (5,5,5,5) )
    
def displaykebabWrap():
    kebabWrap.configure(relief = 'sunken', style = 'SelectedDish.TFrame')

    beefPitaWrap.configure(style="DishFrame.TFrame")
    chickenPitaWrap.configure(style="DishFrame.TFrame")
    
    chickenKebabWrap.configure(style="DishFrame.TFrame")
    hotdogWrap.configure(style="DishFrame.TFrame")
    smallPitaWrap.configure(style="DishFrame.TFrame")
    beefRice.configure(style="DishFrame.TFrame")
    chickenRice.configure(style="DishFrame.TFrame")
    kebabRice.configure(style="DishFrame.TFrame")
    chickenKebabRice.configure(style="DishFrame.TFrame")
    hotdogRice.configure(style="DishFrame.TFrame")
    riceBowl.configure(style="DishFrame.TFrame")
    beefRiceSteak.configure(style="DishFrame.TFrame")
    chickenRiceSteak.configure(style="DishFrame.TFrame")
    beefandChickenPlatter.configure(style="DishFrame.TFrame")
    beefandKebabPlatter.configure(style="DishFrame.TFrame")
    chickenandKebabPlatter.configure(style="DishFrame.TFrame")
    turksJavaRice.configure(style="DishFrame.TFrame")

    displayLabel.configure(image =kebabWrapImage, text = 'Kebab Wrap', font = ("Helvetica", 30, 'bold'),
                           foreground = 'Black', compound ='bottom', padding = (5,5,5,5) )

def displaychickenKebabWrap():
    chickenKebabWrap.configure(relief = 'sunken', style = 'SelectedDish.TFrame')

    beefPitaWrap.configure(style="DishFrame.TFrame")
    chickenPitaWrap.configure(style="DishFrame.TFrame")
    kebabWrap.configure(style="DishFrame.TFrame")
    
    hotdogWrap.configure(style="DishFrame.TFrame")
    smallPitaWrap.configure(style="DishFrame.TFrame")
    beefRice.configure(style="DishFrame.TFrame")
    chickenRice.configure(style="DishFrame.TFrame")
    kebabRice.configure(style="DishFrame.TFrame")
    chickenKebabRice.configure(style="DishFrame.TFrame")
    hotdogRice.configure(style="DishFrame.TFrame")
    riceBowl.configure(style="DishFrame.TFrame")
    beefRiceSteak.configure(style="DishFrame.TFrame")
    chickenRiceSteak.configure(style="DishFrame.TFrame")
    beefandChickenPlatter.configure(style="DishFrame.TFrame")
    beefandKebabPlatter.configure(style="DishFrame.TFrame")
    chickenandKebabPlatter.configure(style="DishFrame.TFrame")
    turksJavaRice.configure(style="DishFrame.TFrame")

    displayLabel.configure(image = chickenKebabWrapImage, text = 'Chicken Kebab Wrap', font = ("Helvetica", 30, 'bold'),
                           foreground = 'Black', compound ='bottom', padding = (5,5,5,5) )
    

def displayhotdogWrap():
    hotdogWrap.configure(relief = 'sunken', style = 'SelectedDish.TFrame')

    beefPitaWrap.configure(style="DishFrame.TFrame")
    chickenPitaWrap.configure(style="DishFrame.TFrame")
    kebabWrap.configure(style="DishFrame.TFrame")
    chickenKebabWrap.configure(style="DishFrame.TFrame")
    
    smallPitaWrap.configure(style="DishFrame.TFrame")
    beefRice.configure(style="DishFrame.TFrame")
    chickenRice.configure(style="DishFrame.TFrame")
    kebabRice.configure(style="DishFrame.TFrame")
    chickenKebabRice.configure(style="DishFrame.TFrame")
    hotdogRice.configure(style="DishFrame.TFrame")
    riceBowl.configure(style="DishFrame.TFrame")
    beefRiceSteak.configure(style="DishFrame.TFrame")
    chickenRiceSteak.configure(style="DishFrame.TFrame")
    beefandChickenPlatter.configure(style="DishFrame.TFrame")
    beefandKebabPlatter.configure(style="DishFrame.TFrame")
    chickenandKebabPlatter.configure(style="DishFrame.TFrame")
    turksJavaRice.configure(style="DishFrame.TFrame")

    displayLabel.configure(image = hotdogWrapImage, text = 'Hotdog Wrap', font = ("Helvetica", 30, 'bold'),
                           foreground = 'Black', compound ='bottom', padding = (5,5,5,5) )


def displaysmallPitaWrap():
    smallPitaWrap.configure(relief = 'sunken', style = 'SelectedDish.TFrame')

    beefPitaWrap.configure(style="DishFrame.TFrame")
    chickenPitaWrap.configure(style="DishFrame.TFrame")
    kebabWrap.configure(style="DishFrame.TFrame")
    chickenKebabWrap.configure(style="DishFrame.TFrame")
    hotdogWrap.configure(style="DishFrame.TFrame")
   
    beefRice.configure(style="DishFrame.TFrame")
    chickenRice.configure(style="DishFrame.TFrame")
    kebabRice.configure(style="DishFrame.TFrame")
    chickenKebabRice.configure(style="DishFrame.TFrame")
    hotdogRice.configure(style="DishFrame.TFrame")
    riceBowl.configure(style="DishFrame.TFrame")
    beefRiceSteak.configure(style="DishFrame.TFrame")
    chickenRiceSteak.configure(style="DishFrame.TFrame")
    beefandChickenPlatter.configure(style="DishFrame.TFrame")
    beefandKebabPlatter.configure(style="DishFrame.TFrame")
    chickenandKebabPlatter.configure(style="DishFrame.TFrame")
    turksJavaRice.configure(style="DishFrame.TFrame")

    displayLabel.configure(image = smallPitaWrapImage, text = 'Small Pita Wrap', font = ("Helvetica", 30, 'bold'),
                           foreground = 'Black', compound ='bottom', padding = (5,5,5,5) )
    
def displaybeefRice():
    beefRice.configure(relief = 'sunken', style = 'SelectedDish.TFrame')

    beefPitaWrap.configure(style="DishFrame.TFrame")
    chickenPitaWrap.configure(style="DishFrame.TFrame")
    kebabWrap.configure(style="DishFrame.TFrame")
    chickenKebabWrap.configure(style="DishFrame.TFrame")
    hotdogWrap.configure(style="DishFrame.TFrame")
    smallPitaWrap.configure(style="DishFrame.TFrame")
    
    chickenRice.configure(style="DishFrame.TFrame")
    kebabRice.configure(style="DishFrame.TFrame")
    chickenKebabRice.configure(style="DishFrame.TFrame")
    hotdogRice.configure(style="DishFrame.TFrame")
    riceBowl.configure(style="DishFrame.TFrame")
    beefRiceSteak.configure(style="DishFrame.TFrame")
    chickenRiceSteak.configure(style="DishFrame.TFrame")
    beefandChickenPlatter.configure(style="DishFrame.TFrame")
    beefandKebabPlatter.configure(style="DishFrame.TFrame")
    chickenandKebabPlatter.configure(style="DishFrame.TFrame")
    turksJavaRice.configure(style="DishFrame.TFrame")

    displayLabel.configure(image = beefRiceImage, text = 'Beef Rice', font = ("Helvetica", 30, 'bold'),
                           foreground = 'Black', compound ='bottom', padding = (5,5,5,5) )
    
def displaychickenRice():
    chickenRice.configure(relief = 'sunken', style = 'SelectedDish.TFrame')
    beefPitaWrap.configure(style="DishFrame.TFrame")
    chickenPitaWrap.configure(style="DishFrame.TFrame")
    kebabWrap.configure(style="DishFrame.TFrame")
    chickenKebabWrap.configure(style="DishFrame.TFrame")
    hotdogWrap.configure(style="DishFrame.TFrame")
    smallPitaWrap.configure(style="DishFrame.TFrame")
    beefRice.configure(style="DishFrame.TFrame")
    
    kebabRice.configure(style="DishFrame.TFrame")
    chickenKebabRice.configure(style="DishFrame.TFrame")
    hotdogRice.configure(style="DishFrame.TFrame")
    riceBowl.configure(style="DishFrame.TFrame")
    beefRiceSteak.configure(style="DishFrame.TFrame")
    chickenRiceSteak.configure(style="DishFrame.TFrame")
    beefandChickenPlatter.configure(style="DishFrame.TFrame")
    beefandKebabPlatter.configure(style="DishFrame.TFrame")
    chickenandKebabPlatter.configure(style="DishFrame.TFrame")
    turksJavaRice.configure(style="DishFrame.TFrame")

    displayLabel.configure(image = chickenRiceImage, text = 'Chicken Rice', font = ("Helvetica", 30, 'bold'),
                           foreground = 'Black', compound ='bottom', padding = (5,5,5,5) )
    
def displaykebabRice():
    kebabRice.configure(relief = 'sunken', style = 'SelectedDish.TFrame')

    beefPitaWrap.configure(style="DishFrame.TFrame")
    chickenPitaWrap.configure(style="DishFrame.TFrame")
    kebabWrap.configure(style="DishFrame.TFrame")
    chickenKebabWrap.configure(style="DishFrame.TFrame")
    hotdogWrap.configure(style="DishFrame.TFrame")
    smallPitaWrap.configure(style="DishFrame.TFrame")
    beefRice.configure(style="DishFrame.TFrame")
    chickenRice.configure(style="DishFrame.TFrame")
    
    chickenKebabRice.configure(style="DishFrame.TFrame")
    hotdogRice.configure(style="DishFrame.TFrame")
    riceBowl.configure(style="DishFrame.TFrame")
    beefRiceSteak.configure(style="DishFrame.TFrame")
    chickenRiceSteak.configure(style="DishFrame.TFrame")
    beefandChickenPlatter.configure(style="DishFrame.TFrame")
    beefandKebabPlatter.configure(style="DishFrame.TFrame")
    chickenandKebabPlatter.configure(style="DishFrame.TFrame")
    turksJavaRice.configure(style="DishFrame.TFrame")

    displayLabel.configure(image = kebabRiceImage, text = 'Kebab Rice', font = ("Helvetica", 30, 'bold'),
                           foreground = 'Black', compound ='bottom', padding = (5,5,5,5) )
    
    
def displaychickenKebabRice():
    chickenKebabRice.configure(relief = 'sunken', style = 'SelectedDish.TFrame')

    beefPitaWrap.configure(style="DishFrame.TFrame")
    chickenPitaWrap.configure(style="DishFrame.TFrame")
    kebabWrap.configure(style="DishFrame.TFrame")
    chickenKebabWrap.configure(style="DishFrame.TFrame")
    hotdogWrap.configure(style="DishFrame.TFrame")
    smallPitaWrap.configure(style="DishFrame.TFrame")
    beefRice.configure(style="DishFrame.TFrame")
    chickenRice.configure(style="DishFrame.TFrame")
    kebabRice.configure(style="DishFrame.TFrame")
    
    hotdogRice.configure(style="DishFrame.TFrame")
    riceBowl.configure(style="DishFrame.TFrame")
    beefRiceSteak.configure(style="DishFrame.TFrame")
    chickenRiceSteak.configure(style="DishFrame.TFrame")
    beefandChickenPlatter.configure(style="DishFrame.TFrame")
    beefandKebabPlatter.configure(style="DishFrame.TFrame")
    chickenandKebabPlatter.configure(style="DishFrame.TFrame")
    turksJavaRice.configure(style="DishFrame.TFrame")

    displayLabel.configure(image = chickenKebabRiceImage, text = 'Chicken Kebab Rice', font = ("Helvetica", 30, 'bold'),
                           foreground = 'Black', compound ='bottom', padding = (5,5,5,5) )
    
def displayhotdogRice():
    hotdogRice.configure(relief = 'sunken', style = 'SelectedDish.TFrame')

    beefPitaWrap.configure(style="DishFrame.TFrame")
    chickenPitaWrap.configure(style="DishFrame.TFrame")
    kebabWrap.configure(style="DishFrame.TFrame")
    chickenKebabWrap.configure(style="DishFrame.TFrame")
    hotdogWrap.configure(style="DishFrame.TFrame")
    smallPitaWrap.configure(style="DishFrame.TFrame")
    beefRice.configure(style="DishFrame.TFrame")
    chickenRice.configure(style="DishFrame.TFrame")
    kebabRice.configure(style="DishFrame.TFrame")
    chickenKebabRice.configure(style="DishFrame.TFrame")
   
    riceBowl.configure(style="DishFrame.TFrame")
    beefRiceSteak.configure(style="DishFrame.TFrame")
    chickenRiceSteak.configure(style="DishFrame.TFrame")
    beefandChickenPlatter.configure(style="DishFrame.TFrame")
    beefandKebabPlatter.configure(style="DishFrame.TFrame")
    chickenandKebabPlatter.configure(style="DishFrame.TFrame")
    turksJavaRice.configure(style="DishFrame.TFrame")

    displayLabel.configure(image = hotdogRiceImage, text = 'Hotdog Rice', font = ("Helvetica", 30, 'bold'),
                           foreground = 'Black', compound ='bottom', padding = (5,5,5,5) )
    
def displayriceBowl():
    riceBowl.configure(relief = 'sunken', style = 'SelectedDish.TFrame')

    beefPitaWrap.configure(style="DishFrame.TFrame")
    chickenPitaWrap.configure(style="DishFrame.TFrame")
    kebabWrap.configure(style="DishFrame.TFrame")
    chickenKebabWrap.configure(style="DishFrame.TFrame")
    hotdogWrap.configure(style="DishFrame.TFrame")
    smallPitaWrap.configure(style="DishFrame.TFrame")
    beefRice.configure(style="DishFrame.TFrame")
    chickenRice.configure(style="DishFrame.TFrame")
    kebabRice.configure(style="DishFrame.TFrame")
    chickenKebabRice.configure(style="DishFrame.TFrame")
    hotdogRice.configure(style="DishFrame.TFrame")
    
    beefRiceSteak.configure(style="DishFrame.TFrame")
    chickenRiceSteak.configure(style="DishFrame.TFrame")
    beefandChickenPlatter.configure(style="DishFrame.TFrame")
    beefandKebabPlatter.configure(style="DishFrame.TFrame")
    chickenandKebabPlatter.configure(style="DishFrame.TFrame")
    turksJavaRice.configure(style="DishFrame.TFrame")

    displayLabel.configure(image = riceBowlImage, text = 'Rice Bowl', font = ("Helvetica", 30, 'bold'),
                           foreground = 'Black', compound ='bottom', padding = (5,5,5,5) )
    
def displaybeefRiceSteak():
    beefRiceSteak.configure(relief = 'sunken', style = 'SelectedDish.TFrame')

    beefPitaWrap.configure(style="DishFrame.TFrame")
    chickenPitaWrap.configure(style="DishFrame.TFrame")
    kebabWrap.configure(style="DishFrame.TFrame")
    chickenKebabWrap.configure(style="DishFrame.TFrame")
    hotdogWrap.configure(style="DishFrame.TFrame")
    smallPitaWrap.configure(style="DishFrame.TFrame")
    beefRice.configure(style="DishFrame.TFrame")
    chickenRice.configure(style="DishFrame.TFrame")
    kebabRice.configure(style="DishFrame.TFrame")
    chickenKebabRice.configure(style="DishFrame.TFrame")
    hotdogRice.configure(style="DishFrame.TFrame")
    riceBowl.configure(style="DishFrame.TFrame")
    
    chickenRiceSteak.configure(style="DishFrame.TFrame")
    beefandChickenPlatter.configure(style="DishFrame.TFrame")
    beefandKebabPlatter.configure(style="DishFrame.TFrame")
    chickenandKebabPlatter.configure(style="DishFrame.TFrame")
    turksJavaRice.configure(style="DishFrame.TFrame")

    displayLabel.configure(image = beefRiceSteakImage, text = 'Beef Rice Steak', font = ("Helvetica", 30, 'bold'),
                           foreground = 'Black', compound ='bottom', padding = (5,5,5,5) )
    
def displaychickenRiceSteak():
    chickenRiceSteak.configure(relief = 'sunken', style = 'SelectedDish.TFrame')

    beefPitaWrap.configure(style="DishFrame.TFrame")
    chickenPitaWrap.configure(style="DishFrame.TFrame")
    kebabWrap.configure(style="DishFrame.TFrame")
    chickenKebabWrap.configure(style="DishFrame.TFrame")
    hotdogWrap.configure(style="DishFrame.TFrame")
    smallPitaWrap.configure(style="DishFrame.TFrame")
    beefRice.configure(style="DishFrame.TFrame")
    chickenRice.configure(style="DishFrame.TFrame")
    kebabRice.configure(style="DishFrame.TFrame")
    chickenKebabRice.configure(style="DishFrame.TFrame")
    hotdogRice.configure(style="DishFrame.TFrame")
    riceBowl.configure(style="DishFrame.TFrame")
    beefRiceSteak.configure(style="DishFrame.TFrame")
    
    beefandChickenPlatter.configure(style="DishFrame.TFrame")
    beefandKebabPlatter.configure(style="DishFrame.TFrame")
    chickenandKebabPlatter.configure(style="DishFrame.TFrame")
    turksJavaRice.configure(style="DishFrame.TFrame")

    displayLabel.configure(image = chickenRiceSteakImage, text = 'Chicken Rice Steak', font = ("Helvetica", 30, 'bold'),
                           foreground = 'Black', compound ='bottom', padding = (5,5,5,5) )
    
def displaybeefAndChickenPlatter():
    beefandChickenPlatter.configure(relief = 'sunken', style = 'SelectedDish.TFrame')

    beefPitaWrap.configure(style="DishFrame.TFrame")
    chickenPitaWrap.configure(style="DishFrame.TFrame")
    kebabWrap.configure(style="DishFrame.TFrame")
    chickenKebabWrap.configure(style="DishFrame.TFrame")
    hotdogWrap.configure(style="DishFrame.TFrame")
    smallPitaWrap.configure(style="DishFrame.TFrame")
    beefRice.configure(style="DishFrame.TFrame")
    chickenRice.configure(style="DishFrame.TFrame")
    kebabRice.configure(style="DishFrame.TFrame")
    chickenKebabRice.configure(style="DishFrame.TFrame")
    hotdogRice.configure(style="DishFrame.TFrame")
    riceBowl.configure(style="DishFrame.TFrame")
    beefRiceSteak.configure(style="DishFrame.TFrame")
    chickenRiceSteak.configure(style="DishFrame.TFrame")
    
    beefandKebabPlatter.configure(style="DishFrame.TFrame")
    chickenandKebabPlatter.configure(style="DishFrame.TFrame")
    turksJavaRice.configure(style="DishFrame.TFrame")

    displayLabel.configure(image = BeefandchickenPlatterImage, text = 'Beef and Chicken Platter', font = ("Helvetica", 30, 'bold'),
                           foreground = 'Black', compound ='bottom', padding = (5,5,5,5) )
    
def displayBeefandKebabPlatter():
    beefandKebabPlatter.configure(relief = 'sunken', style = 'SelectedDish.TFrame')

    beefPitaWrap.configure(style="DishFrame.TFrame")
    chickenPitaWrap.configure(style="DishFrame.TFrame")
    kebabWrap.configure(style="DishFrame.TFrame")
    chickenKebabWrap.configure(style="DishFrame.TFrame")
    hotdogWrap.configure(style="DishFrame.TFrame")
    smallPitaWrap.configure(style="DishFrame.TFrame")
    beefRice.configure(style="DishFrame.TFrame")
    chickenRice.configure(style="DishFrame.TFrame")
    kebabRice.configure(style="DishFrame.TFrame")
    chickenKebabRice.configure(style="DishFrame.TFrame")
    hotdogRice.configure(style="DishFrame.TFrame")
    riceBowl.configure(style="DishFrame.TFrame")
    beefRiceSteak.configure(style="DishFrame.TFrame")
    chickenRiceSteak.configure(style="DishFrame.TFrame")
    beefandChickenPlatter.configure(style="DishFrame.TFrame")
    
    chickenandKebabPlatter.configure(style="DishFrame.TFrame")
    turksJavaRice.configure(style="DishFrame.TFrame")

    displayLabel.configure(image = BeefandKebabPlatterImage, text = 'Beef and Kebab Platter', font = ("Helvetica", 30, 'bold'),
                           foreground = 'Black', compound ='bottom', padding = (5,5,5,5) )
    
def displaychickenandKebabPlatter():
    chickenandKebabPlatter.configure(relief = 'sunken', style = 'SelectedDish.TFrame')

    beefPitaWrap.configure(style="DishFrame.TFrame")
    chickenPitaWrap.configure(style="DishFrame.TFrame")
    kebabWrap.configure(style="DishFrame.TFrame")
    chickenKebabWrap.configure(style="DishFrame.TFrame")
    hotdogWrap.configure(style="DishFrame.TFrame")
    smallPitaWrap.configure(style="DishFrame.TFrame")
    beefRice.configure(style="DishFrame.TFrame")
    chickenRice.configure(style="DishFrame.TFrame")
    kebabRice.configure(style="DishFrame.TFrame")
    chickenKebabRice.configure(style="DishFrame.TFrame")
    hotdogRice.configure(style="DishFrame.TFrame")
    riceBowl.configure(style="DishFrame.TFrame")
    beefRiceSteak.configure(style="DishFrame.TFrame")
    chickenRiceSteak.configure(style="DishFrame.TFrame")
    beefandChickenPlatter.configure(style="DishFrame.TFrame")
    beefandKebabPlatter.configure(style="DishFrame.TFrame")
    
    turksJavaRice.configure(style="DishFrame.TFrame")

    displayLabel.configure(image = chickenandkebabImage, text = 'Chicken and Kebab Platter', font = ("Helvetica", 30, 'bold'),
                           foreground = 'Black', compound ='bottom', padding = (5,5,5,5) )
    
def displayturksJavaRice():
    turksJavaRice.configure(relief = 'sunken', style = 'SelectedDish.TFrame')
    #ito yong mpag magiiba ng color then babalik sa dati
    beefPitaWrap.configure(style="DishFrame.TFrame")
    chickenPitaWrap.configure(style="DishFrame.TFrame")
    kebabWrap.configure(style="DishFrame.TFrame")
    chickenKebabWrap.configure(style="DishFrame.TFrame")
    hotdogWrap.configure(style="DishFrame.TFrame")
    smallPitaWrap.configure(style="DishFrame.TFrame")
    beefRice.configure(style="DishFrame.TFrame")
    chickenRice.configure(style="DishFrame.TFrame")
    kebabRice.configure(style="DishFrame.TFrame")
    chickenKebabRice.configure(style="DishFrame.TFrame")
    hotdogRice.configure(style="DishFrame.TFrame")
    riceBowl.configure(style="DishFrame.TFrame")
    beefRiceSteak.configure(style="DishFrame.TFrame")
    chickenRiceSteak.configure(style="DishFrame.TFrame")
    beefandChickenPlatter.configure(style="DishFrame.TFrame")
    beefandKebabPlatter.configure(style="DishFrame.TFrame")
    chickenandKebabPlatter.configure(style="DishFrame.TFrame")
  

    displayLabel.configure(image = TurksJavaRiceImage, text = 'Turks Java Rice', font = ("Helvetica", 30, 'bold'),
                           foreground = 'Black', compound ='bottom', padding = (5,5,5,5) )

    
#region for generating receipt from order button
def order():
    new_receipt = orderIDLabel.cget("text")
    new_receipt = new_receipt.replace("ORDER ID : ","")
    transaction_list = orderTransaction.cget("text").split("$ ")
    transaction_list.pop(len(transaction_list) - 1)

    order_day = date.today()
    order_time = datetime.now()

    for item in transaction_list: 
        item +="$ "

    
    with open(new_receipt, 'w') as file:
        file.write("TURKS")
        file.write("\n")
        file.write("____________________________________________")
        file.write("\n")
        file.write(order_day.strftime("%x"))
        file.write("\n")
        file.write(order_time.strftime("%x"))
        file.write("\n\n")

        for item in transaction_list:
            file.write(item + "\n")
        file.write("\n\n")
        file.write(orderTotalLabel.cget("text"))

    orderTotalLabel.configure(text = "TOTAL : 0$")
    orderIDLabel.configure(text = "ORDER ID: " + ORDER_ID())
    orderTransaction.configure(text = "")
        






# ---------------------------------- STYLING AND IMAGES ------------------------------------ #
#region Style configurations
s = ttk.Style()
s.configure('MainFrame.TFrame', background = "#FFFFFF")
s.configure('MenuFrame.TFrame', background = "#FFFFFF")
s.configure('DisplayFrame.TFrame', background = "#FFFFFF")
s.configure('OrderFrame.TFrame', background = "#FFFFFF")
s.configure('DishFrame.TFrame', background = "#949494", relief = "raised")
s.configure('SelectedDish.TFrame', background = '#bebebe')
s.configure('MenuLabel.TLabel',
            background = "#0F1110",
            font = ("Arial", 10, "italic"),
            foreground = "white",
            padding = (5, 5, 5, 5),
            width = 30
            )

s.configure('orderTotalLabel.TLabel',
            background = "#a9a9a9",
            font = ("Arial", 10, "bold"),
            foreground = "black",
            padding = (2, 2, 2, 2),
            anchor = "w"
            )
s.configure('orderTransaction.TLabel',
            background = "#949494",
            font = ('Helvetica', 18),
            foreground = "black",
            wraplength = 290,
            anchor = "NSEW",
            padding = (5,5,5,5)
            )

# endregion

# region Images

# Top Banner images
LogoImageObject = Image.open("Untitled design (10).png").resize((140, 140))
LogoImage = ImageTk.PhotoImage(LogoImageObject)

TopBannerImageObject = Image.open("Untitled Design (9).png").resize((1920, 140))
TopBannerImage = ImageTk.PhotoImage(TopBannerImageObject)



# Menu images
displayDefaultImageObject = Image.open("white-Screenshot 2024-10-21 201844.png").resize((800,600))
displayDefaultImage = ImageTk.PhotoImage(displayDefaultImageObject)

beefPitaWrapImageObject = Image.open("Beef-Wrap.png").resize((800,550))
beefPitaWrapImage = ImageTk.PhotoImage(beefPitaWrapImageObject)

chickenPitaWrapImageObject = Image.open("Chicken-Wrap.png").resize((800,550))
chickenPitaWrapImage = ImageTk.PhotoImage(chickenPitaWrapImageObject)

kebabWrapImageObject = Image.open("Beef-Kebab.png").resize((800,550))
kebabWrapImage = ImageTk.PhotoImage(kebabWrapImageObject)

chickenKebabWrapImageObject = Image.open("Chicken-Kebab.png").resize((800,550))
chickenKebabWrapImage = ImageTk.PhotoImage(chickenKebabWrapImageObject)

hotdogWrapImageObject = Image.open("Hotdog-Wrap.png").resize((800,550))
hotdogWrapImage = ImageTk.PhotoImage(hotdogWrapImageObject)

smallPitaWrapImageObject = Image.open("Small-Wrap.png").resize((800,550))
smallPitaWrapImage = ImageTk.PhotoImage(smallPitaWrapImageObject)

beefRiceImageObject = Image.open("Beef-Rice.png").resize((800,550))
beefRiceImage = ImageTk.PhotoImage(beefRiceImageObject)

chickenRiceImageObject = Image.open("Chicken-Rice.png").resize((800,550))
chickenRiceImage = ImageTk.PhotoImage(chickenRiceImageObject)

kebabRiceImageObject = Image.open("Beef-Kebab-Rice.png").resize((800,550))
kebabRiceImage = ImageTk.PhotoImage(kebabRiceImageObject)

chickenKebabRiceImageObject = Image.open("Chicken-Kebab-Rice.png").resize((800,550))
chickenKebabRiceImage = ImageTk.PhotoImage(chickenKebabRiceImageObject)

hotdogRiceImageObject = Image.open("Hotdog-Rice.png").resize((800,550))
hotdogRiceImage = ImageTk.PhotoImage(hotdogRiceImageObject)

riceBowlImageObject = Image.open("Rice-Bowl.png").resize((800,550))
riceBowlImage = ImageTk.PhotoImage(riceBowlImageObject)

beefRiceSteakImageObject = Image.open("Beef-Steak.png").resize((800,550))
beefRiceSteakImage = ImageTk.PhotoImage(beefRiceSteakImageObject)

chickenRiceSteakImageObject = Image.open("Chicken-Steak.png").resize((800,550))
chickenRiceSteakImage = ImageTk.PhotoImage(chickenRiceSteakImageObject)

BeefandchickenPlatterImageObject = Image.open("Beef-and-Chicken-Platter.png").resize((800,550))
BeefandchickenPlatterImage = ImageTk.PhotoImage(BeefandchickenPlatterImageObject)

BeefandKebabPlatterImageObject = Image.open("Beef-and-Kebab-Platter.png").resize((800,550))
BeefandKebabPlatterImage = ImageTk.PhotoImage(BeefandKebabPlatterImageObject)

chickenandkebabImageObject = Image.open("Chicken-and-Kebab-Platter.png").resize((800,550))
chickenandkebabImage = ImageTk.PhotoImage(chickenandkebabImageObject)

TurksJavaRiceImageObject = Image.open("turks-java-rice.png").resize((800,550))
TurksJavaRiceImage = ImageTk.PhotoImage(TurksJavaRiceImageObject)







#end region
#----------------------------------- WIDGETS ----------------------------------------------- #

# region Frames

# Section Frames
mainFrame = ttk.Frame(root, width = 1920, height = 1080, style = 'MainFrame.TFrame')
mainFrame.grid(row = 0, column = 0, sticky = "NSEW")

topBannerFrame = ttk.Frame(mainFrame)
topBannerFrame.grid(row = 0, column = 0, sticky = "NSEW", columnspan = 3)

menuFrame = ttk.Frame(mainFrame, style = 'MenuFrame.TFrame')
menuFrame.grid(row = 1, column = 0, padx = 3, pady = 3, sticky = "NSEW")



displayFrame = ttk.Frame(mainFrame, style = "DisplayFrame.TFrame")
displayFrame.grid(row = 1, column = 1, padx = 3, pady = 3, sticky = "NSEW")

orderFrame = ttk.Frame(mainFrame, style = "OrderFrame.TFrame")
orderFrame.grid(row = 1, column = 2, padx = 3, pady = 3, sticky = "NSEW")

#
menuCanvas = Canvas(mainFrame, bg="#FFFFFF", highlightthickness=0)
menuCanvas.grid(row=1, column=0, padx=3, pady=3, sticky="NSEW")

scrollbar = ttk.Scrollbar(mainFrame, orient="vertical", command=menuCanvas.yview)
scrollbar.grid(row=1, column=0, sticky="NSE", padx=(0, 10))

menuCanvas.configure(yscrollcommand=scrollbar.set)

menuFrame = ttk.Frame(menuCanvas, style='MenuFrame.TFrame')

menuCanvas.create_window((0, 0), window=menuFrame, anchor="nw")
menuCanvas.bind("<Configure>", lambda e: menuCanvas.configure(scrollregion=menuCanvas.bbox("all")))



#

#Dish Frames
#Page 1
beefPitaWrap = ttk.Frame(menuFrame, style = "DishFrame.TFrame")
beefPitaWrap.grid(row = 1, column = 0, sticky = "NSEW")

chickenPitaWrap = ttk.Frame(menuFrame,style ="DishFrame.TFrame")
chickenPitaWrap.grid(row = 2, column = 0, sticky ="NSEW")

kebabWrap = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
kebabWrap.grid(row = 3, column = 0, sticky ="NSEW")

chickenKebabWrap = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
chickenKebabWrap .grid(row = 4, column = 0, sticky ="NSEW")

hotdogWrap = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
hotdogWrap.grid(row = 5, column = 0, sticky ="NSEW")

smallPitaWrap = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
smallPitaWrap .grid(row = 6, column = 0, sticky ="NSEW")

#PAGE 2

beefRice = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
beefRice.grid(row = 7, column = 0, sticky ="NSEW")

chickenRice= ttk.Frame(menuFrame, style ="DishFrame.TFrame")
chickenRice.grid(row = 8, column = 0, sticky ="NSEW")

kebabRice = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
kebabRice .grid(row = 9, column = 0, sticky ="NSEW")

chickenKebabRice = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
chickenKebabRice .grid(row = 10, column = 0, sticky ="NSEW")

hotdogRice = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
hotdogRice.grid(row = 11, column = 0, sticky ="NSEW")

riceBowl= ttk.Frame(menuFrame, style ="DishFrame.TFrame")
riceBowl.grid(row = 12, column = 0, sticky ="NSEW")

beefRiceSteak= ttk.Frame(menuFrame, style ="DishFrame.TFrame")
beefRiceSteak.grid(row = 13, column = 0, sticky ="NSEW")

chickenRiceSteak= ttk.Frame(menuFrame, style ="DishFrame.TFrame")
chickenRiceSteak.grid(row = 14, column = 0, sticky ="NSEW")

beefandChickenPlatter= ttk.Frame(menuFrame, style ="DishFrame.TFrame")
beefandChickenPlatter.grid(row = 15, column = 0, sticky ="NSEW")

beefandKebabPlatter= ttk.Frame(menuFrame, style ="DishFrame.TFrame")
beefandKebabPlatter.grid(row = 16, column = 0, sticky ="NSEW")

chickenandKebabPlatter= ttk.Frame(menuFrame, style ="DishFrame.TFrame")
chickenandKebabPlatter.grid(row = 17, column = 0, sticky ="NSEW")

turksJavaRice= ttk.Frame(menuFrame, style ="DishFrame.TFrame")
turksJavaRice.grid(row = 18, column = 0, sticky ="NSEW")

#

# Dish Frames - configure rows and columns
menuFrame.columnconfigure(0, weight=1)
menuFrame.rowconfigure(0, weight=1)

orderFrame.columnconfigure(0, weight=1)
orderFrame.rowconfigure(0, weight=0 )

"""displayFrame.columnconfigure(0, weight=1)
displayFrame.rowconfigure(0, weight=1)"""
#

#end region

#region top banner section
LogoLabel = ttk.Label(topBannerFrame, image = LogoImage, background = "#0F1110")
LogoLabel.grid(row = 0, column = 0, sticky = "W")

RestaurantBannerLabel = ttk.Label(topBannerFrame, image = TopBannerImage, background = "#0F1110")
RestaurantBannerLabel.grid(row = 0, column = 1, sticky = "NSEW")

#endregion

#region Menu Section
MainMenuLabel = ttk.Label(menuFrame, text = "MENU", style = "MenuLabel.TLabel")
MainMenuLabel.grid(row = 0, column = 0, sticky = "WE")
MainMenuLabel.configure(
    anchor = "center",
    font = ("Helvetica", 14, "bold"))


beefPitaWrapLabel = ttk.Label(beefPitaWrap, text ="Beef Pita Wrap .... 80$", style ="MenuLabel.TLabel")
beefPitaWrapLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

chickenPitaWrapLabel = ttk.Label(chickenPitaWrap, text ="Chicken Pita Wrap ..... 80$", style ="MenuLabel.TLabel")
chickenPitaWrapLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

kebabWrapLabel = ttk.Label(kebabWrap, text ="Kebab Wrap ..... 85$", style ="MenuLabel.TLabel")
kebabWrapLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

chickenKebabWrapLabel = ttk.Label(chickenKebabWrap, text ="Chicken Kebab Wrap ..... 85$", style ="MenuLabel.TLabel")
chickenKebabWrapLabel.grid(row = 0, column = 0, padx =10, pady = 10, sticky = "W")

hotdogWrapLabel = ttk.Label(hotdogWrap, text ="Hotdog Wrap ..... 85$", style ="MenuLabel.TLabel")
hotdogWrapLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

smallPitaWrapLabel = ttk.Label(smallPitaWrap, text ="Small Pita Wrap .... 85$", style ="MenuLabel.TLabel")
smallPitaWrapLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

beefRiceLabel = ttk.Label(beefRice, text ="Beef Rice .... 130$", style ="MenuLabel.TLabel")
beefRiceLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

chickenRiceLabel = ttk.Label(chickenRice, text ="Chicken Rice .... 130$", style ="MenuLabel.TLabel")
chickenRiceLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

kebabRiceLabel = ttk.Label(kebabRice, text ="Kebab Rice .... 150$", style ="MenuLabel.TLabel")
kebabRiceLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

chickenKebabRiceLabel = ttk.Label(chickenKebabRice, text ="Chicken Kebab Rice .... 150$", style ="MenuLabel.TLabel")
chickenKebabRiceLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")
 
hotdogRiceLabel = ttk.Label(hotdogRice, text ="Hotdog Rice .... 150$", style ="MenuLabel.TLabel")
hotdogRiceLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

riceBowlLabel = ttk.Label(riceBowl, text ="Rice Bowl .... 85$", style ="MenuLabel.TLabel")
riceBowlLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")


beefRiceSteakLabel = ttk.Label(beefRiceSteak, text ="Beef Rice Steak .... $240", style ="MenuLabel.TLabel")
beefRiceSteakLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

chickenRiceSteakLabel = ttk.Label(chickenRiceSteak, text ="Chicken Rice Steak.... 180$", style ="MenuLabel.TLabel")
chickenRiceSteakLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

beefandChickenPlatterLabel = ttk.Label(beefandChickenPlatter, text ="Beef and Chicken Platter..210$", style ="MenuLabel.TLabel")
beefandChickenPlatterLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

beefandKebabPlatterLabel = ttk.Label(beefandKebabPlatter, text ="Beef and Kebab Platter..210$", style ="MenuLabel.TLabel")
beefandKebabPlatterLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

chickenandKebabPlatterLabel = ttk.Label(chickenandKebabPlatter, text ="Chicken and Kebab Platter..210$", style ="MenuLabel.TLabel")
chickenandKebabPlatterLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

turksJavaRiceLabel = ttk.Label(turksJavaRice, text ="Turks Java Rice .... 25$", style ="MenuLabel.TLabel")
turksJavaRiceLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

#region Order Section
orderTitleLabel = ttk.Label(orderFrame, text = "YOUR ORDER",style="MenuLabel.TLabel")

orderTitleLabel.configure(
    foreground="white", background="black",
    font=("Helvetica", 14, "bold"), anchor = "center",
    padding = (5, 5, 5, 5),
)
orderTitleLabel.grid(row = 0, column = 0, sticky = "N")

orderIDLabel = ttk.Label(orderFrame, text = "ORDER ID : " + ORDER_ID())
orderIDLabel.configure(
    background = "black",
    foreground = "white",
    font = ("Helvetica", 11, "italic"),
    anchor = "center",padding = (5, 5, 5, 5)
)
orderIDLabel.grid(row = 1, column = 0, sticky = "NSEW")

orderTransaction = ttk.Label(orderFrame, style = 'orderTransaction.TLabel')
orderTransaction.grid(row = 2, column = 0, sticky = "NSEW", padx=0, pady=0, )


orderTotalLabel = ttk.Label(orderFrame, text ="TOTAL : 0$", style = "orderTotalLabel.TLabel")
orderTotalLabel.grid(row = 3, column = 0, sticky = "EW")

orderButton = ttk.Button(orderFrame, text = "ORDER", command = order)
orderButton.grid(row = 4, column = 0, sticky = "EW")


#Button

beefPitaWrapButton = ttk.Button(beefPitaWrap, text ="Display", command = displayBeefPitaWrap)
beefPitaWrapButton.grid(row = 0, column = 1, padx = 10)

chickenPitaWrapButton = ttk.Button(chickenPitaWrap, text ="Display", command = displayChickenPitaWrap)
chickenPitaWrapButton.grid(row = 0, column = 1, padx = 10)

kebabWrapButton = ttk.Button(kebabWrap, text ="Display", command = displaykebabWrap)
kebabWrapButton.grid(row = 0, column = 1, padx = 10)

chickenKebabWrapButton = ttk.Button(chickenKebabWrap, text ="Display", command = displaychickenKebabWrap)
chickenKebabWrapButton.grid(row = 0, column = 1, padx = 10)

hotdogWrapButton = ttk.Button(hotdogWrap, text ="Display", command = displayhotdogWrap)
hotdogWrapButton.grid(row = 0, column = 1, padx = 10)

smallPitaWrapButton = ttk.Button(smallPitaWrap, text ="Display",command = displaysmallPitaWrap)
smallPitaWrapButton.grid(row = 0, column = 1, padx = 10)

beefRiceButton = ttk.Button(beefRice, text ="Display", command = displaybeefRice)
beefRiceButton.grid(row = 0, column = 1, padx = 10)

chickenRiceButton = ttk.Button(chickenRice, text ="Display", command = displaychickenRice)
chickenRiceButton.grid(row = 0, column = 1, padx = 10)

kebabRiceButton = ttk.Button(kebabRice, text ="Display", command = displaykebabRice)
kebabRiceButton.grid(row = 0, column = 1, padx = 10)

chickenKebabRiceButton = ttk.Button(chickenKebabRice, text ="Display", command = displaychickenKebabRice)
chickenKebabRiceButton.grid(row = 0, column = 1, padx = 10)

hotdogRiceButton = ttk.Button(hotdogRice, text ="Display", command = displayhotdogRice)
hotdogRiceButton.grid(row = 0, column = 1, padx = 10)

riceBowlButton = ttk.Button(riceBowl, text ="Display", command = displayriceBowl)
riceBowlButton.grid(row = 0, column = 1, padx = 10)

beefRiceSteakButton = ttk.Button(beefRiceSteak, text ="Display", command = displaybeefRiceSteak)
beefRiceSteakButton.grid(row = 0, column = 1, padx = 10)

chickenRiceSteakButton = ttk.Button(chickenRiceSteak, text ="Display", command = displaychickenRiceSteak)
chickenRiceSteakButton.grid(row = 0, column = 1, padx = 10)

beefandChickenPlatterButton = ttk.Button(beefandChickenPlatter, text ="Display", command = displaybeefAndChickenPlatter)
beefandChickenPlatterButton.grid(row = 0, column = 1, padx = 10)

beefandKebabPlatterButton = ttk.Button(beefandKebabPlatter, text ="Display", command = displayBeefandKebabPlatter)
beefandKebabPlatterButton.grid(row = 0, column = 1, padx = 10)

chickenandKebabPlatterButton = ttk.Button(chickenandKebabPlatter, text ="Display", command = displaychickenandKebabPlatter)
chickenandKebabPlatterButton.grid(row = 0, column = 1, padx = 10)

turksJavaRiceButton = ttk.Button(turksJavaRice, text ="Display", command = displayturksJavaRice)
turksJavaRiceButton.grid(row = 0, column = 1, padx = 10)

#end region

#region display section
displayLabel = ttk.Label(displayFrame, image = displayDefaultImage)
displayLabel.grid(row = 0, column = 0 , sticky = "NSEW", columnspan = 2)
displayLabel.configure(background = "#FFFFFF")

addOrderButton = ttk.Button(displayFrame, text = "ADD TO ORDER", command = add)
addOrderButton.grid(row = 1, column = 0, padx = 2, sticky = "NSEW")

removeOrderButton = ttk.Button(displayFrame, text = "REMOVE", command = remove)
removeOrderButton.grid(row = 1, column = 1, padx = 2, sticky = "NSEW")



#end region

#----------------------------- GRID CONFIGURATIONS -------------------------------------------#
#
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainFrame.columnconfigure(0, weight=1)
mainFrame.columnconfigure(1, weight=1)
mainFrame.columnconfigure(2, weight=1)

mainFrame.rowconfigure(1, weight=1)
#
menuFrame.columnconfigure(2, weight = 1)
menuFrame.rowconfigure(1, weight = 1)
menuFrame.rowconfigure(2, weight = 1)
menuFrame.rowconfigure(3, weight = 1)
menuFrame.rowconfigure(4, weight = 1)
menuFrame.rowconfigure(5, weight = 1)
menuFrame.rowconfigure(6, weight = 1)

#

root.update_idletasks()
menuCanvas.config(scrollregion=menuCanvas.bbox("all"))

#

orderFrame.columnconfigure(0, weight = 1)
orderFrame.rowconfigure(2, weight = 1)





root.mainloop()