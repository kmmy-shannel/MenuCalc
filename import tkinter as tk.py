import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

# Maximize the window to full screen
root.state('zoomed')

root.title("TURKS")

# ------------------------------------FUNCTIONS--------------------------------------------- #


# ---------------------------------- STYLING AND IMAGES ------------------------------------ #
#region Style configurations
s = ttk.Style()
s.configure('MainFrame.TFrame', background="#2B2B28")
s.configure('MenuFrame.TFrame', background="#4A4A48")
s.configure('DisplayFrame.TFrame', background="#0F1110")
s.configure('OrderFrame.TFrame', background="#B7C4CF")
s.configure('DishFrame.TFrame', background="#4A4A48", relief="raised")
s.configure('MenuLabel.TLabel',
            background="#0F1110",
            font=("Arial", 13, "italic"),
            foreground="white",
            padding=(5, 5, 5, 5),
            width=25
            )

s.configure('orderTotalLabel.TLabel',
            background="#0F1110",
            font=("Arial", 10, "bold"),
            foreground="white",
            padding=(2, 2, 2, 2),
            anchor="w"
            )
s.configure('orderTransaction.TLabel',
            background="#4A4A48",
            font=('Helvetica', 12),
            foreground="white",
            wraplength=170,
            anchor="nw",
            padding=(3, 3, 3, 3)
            )

# endregion

# region Images

# Top Banner images
LogoImageObject = Image.open("TURKS/turks-logo_horizontal-600x208.png").resize((140, 140))
LogoImage = ImageTk.PhotoImage(LogoImageObject)

TopBannerImageObject = Image.open("TURKS/348s.jpg").resize((900, 140))
TopBannerImage = ImageTk.PhotoImage(TopBannerImageObject)

displayDefaultImageObject = Image.open("TURKS/white-Screenshot 2024-10-21 201844.png").resize((350, 360))
displayDefaultImage = ImageTk.PhotoImage(displayDefaultImageObject)

# Menu images (adjust as needed)
beefPitaWrapImageObject = Image.open("TURKS/Beef-Wrap.png").resize((350, 334))
beefPitaWrapImage = ImageTk.PhotoImage(beefPitaWrapImageObject)

# Additional image loading as shown in your code...

# endregion
# ----------------------------------- WIDGETS ----------------------------------------------- #

# region Frames
mainFrame = ttk.Frame(root, style='MainFrame.TFrame')
mainFrame.grid(row=0, column=0, sticky="NSEW")

topBannerFrame = ttk.Frame(mainFrame)
topBannerFrame.grid(row=0, column=0, sticky="NSEW", columnspan=3)

menuFrame = ttk.Frame(mainFrame, style='MenuFrame.TFrame')
menuFrame.grid(row=1, column=0, padx=3, pady=3, sticky="NSEW")

displayFrame = ttk.Frame(mainFrame, style="DisplayFrame.TFrame")
displayFrame.grid(row=1, column=1, padx=3, pady=3, sticky="NSEW")

orderFrame = ttk.Frame(mainFrame, style="OrderFrame.TFrame")
orderFrame.grid(row=1, column=2, padx=3, pady=3, sticky="NSEW")

# Dish Frames - configure rows and columns
menuFrame.columnconfigure(0, weight=1)
menuFrame.rowconfigure(0, weight=1)

orderFrame.columnconfigure(0, weight=1)
orderFrame.rowconfigure(0, weight=1)

displayFrame.columnconfigure(0, weight=1)
displayFrame.rowconfigure(0, weight=1)

# endregion

# region top banner section
LogoLabel = ttk.Label(topBannerFrame, image=LogoImage, background="#0F1110")
LogoLabel.grid(row=0, column=0, sticky="W")

RestaurantBannerLabel = ttk.Label(topBannerFrame, image=TopBannerImage, background="#0F1110")
RestaurantBannerLabel.grid(row=0, column=1, sticky="NSEW")

# endregion

# region Menu Section
MainMenuLabel = ttk.Label(menuFrame, text="MENU", style="MenuLabel.TLabel")
MainMenuLabel.grid(row=0, column=0, sticky="WE")
MainMenuLabel.configure(
    anchor="center",
    font=("Helvetica", 14, "bold"))

beefPitaWrapLabel = ttk.Label(menuFrame, text="Beef Pita Wrap ..... P80", style="MenuLabel.TLabel")
beefPitaWrapLabel.grid(row=1, column=0, padx=10, pady=10, sticky="W")

# Add buttons for the items
beefPitaWrapButton = ttk.Button(menuFrame, text="Display")
beefPitaWrapButton.grid(row=1, column=1, padx=10)

# Add additional menu items...

# endregion

# region Order Section
orderTitleLabel = ttk.Label(orderFrame, text="ORDER", style="MenuLabel.TLabel")
orderTitleLabel.grid(row=0, column=0, sticky="EW")

orderIDLabel = ttk.Label(orderFrame, text="ORDER ID : ")
orderIDLabel.grid(row=1, column=0, sticky="EW", pady=1)

orderTotalLabel = ttk.Label(orderFrame, text="TOTAL : 0$", style="orderTotalLabel.TLabel")
orderTotalLabel.grid(row=3, column=0, sticky="EW")

orderButton = ttk.Button(orderFrame, text="ORDER")
orderButton.grid(row=4, column=0, sticky="EW")

# endregion

# region Display Section
displayLabel = ttk.Label(displayFrame, image=displayDefaultImage)
displayLabel.grid(row=0, column=0, sticky="NSEW", columnspan=2)
displayLabel.configure(background="#0F1110")

addOrderButton = ttk.Button(displayFrame, text="ADD TO ORDER")
addOrderButton.grid(row=1, column=0, padx=2, sticky="NSEW")

removeOrderButton = ttk.Button(displayFrame, text="REMOVE")
removeOrderButton.grid(row=1, column=1, padx=2, sticky="NSEW")

# endregion

# Configure root to occupy full screen and make grid flexible
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainFrame.columnconfigure(0, weight=1)
mainFrame.columnconfigure(1, weight=1)
mainFrame.columnconfigure(2, weight=1)

mainFrame.rowconfigure(1, weight=1)

root.mainloop()