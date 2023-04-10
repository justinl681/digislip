import tkinter
import customtkinter
import webbrowser

"""
DigiSlip
A free and open source digital flight slip for wannabe air traffic controllers
Created by: @justin681#6376
MIT License
"""

class App(customtkinter.CTk):

    def __init__(self):

        super().__init__() # Initialise the window

        self.width = 800 # Change this to change the width of the window, 800 is a good minimum width
        self.height = 400 # Change this to change the height of the window, 400 is a good minimum height

        self.pinned = True # Set the window to be pinned by default

        self.airlines = """Canadian
AirBalistic
AirFrans
Belta
Bliss
JetBloo
KoreenAir
Oantas
Aer Dingus
Americano
Speedbird
Doncor
HardJet
Lifthansa
Oatar
Old Zealand
Scandialien
Spirit
Thay
Turkish
United
Wizz Air
Cafe Pacific
Emarates
Jet3
KLN
Singadoor
Byanair
KOT
Northeast
Tui
Flybe
Pepsi
Havoc
Quake
Gyro
Warlock
Lancer
Xenon
Cobra
Uplift
Raider
Worldstar
Jester
Kestral
TomJet
Supertransport
UPS
DHL
FedEx
Python""".split("\n")
        self.airlines.sort() # Create a list of airlines

        self.stages = [
            "At Gate",
            "Pushback",
            "Taxi",
            "Takeoff",
            "Climb",
            "Cruise",
            "Descent",
            "Approach",
            "Landing",
        ] # Create a list of flight stages

        self.airports = [
            "IBAR",
            "IHEN",
            "ILAR",
            "IPAP",
            "IGRV",
            "IJAF",
            "IZOL",
            "ISCM",
            "ICDS",
            "ITKO",
            "ILKL",
            "IPPH",
            "IGAR",
            "IBLT",
            "IRFD",
            "IMLR",
            "ITRC",
            "IBTH",
            "IUFO",
            "ISAU",
            "ISKP"
        ]
        self.airports.sort()

        self.geometry(f"{self.width}x{self.height}") # Set the size of the window
        self.title("DigiSlip") # Set the title of the window
        self.attributes('-topmost', True) # Set the window to be on top of all other windows, even when not focused, useful when quickly switching between windows
        self.resizable(False, False) # Disable resizing in the x and y direction
        # self.iconbitmap("icon.ico") # Set the icon of the window

        self.add_flight_button = customtkinter.CTkButton(self, text="Add Flight", command=self.add_flight) # Create a button
        self.add_flight_button.place(x=70, y=10) # Place the button on the window

        self.pin_button = customtkinter.CTkButton(self, text="Unpin", command=self.pin, width=50) # Create a button
        self.pin_button.place(x=10, y=10) # Place the button on the window

        self.show_chart_menu = customtkinter.CTkOptionMenu(self, width=100, values=self.airports) # Create an entry
        self.show_chart_menu.place(x=220, y=10) # Place the entry on the window

        self.show_chart_button = customtkinter.CTkButton(self, text="Show Chart", command=self.show_chart) # Create a button
        self.show_chart_button.place(x=330, y=10) # Place the button on the window

        self.flights_frame = customtkinter.CTkScrollableFrame(self, width=self.width-40, height=self.height-70) # Create a scrollable frame
        self.flights_frame.place(x=10, y=50) # Place the scrollable frame on the window

        self.flights = [] # Create a list to store all the flights

    def add_flight(self):   

        flight = Flight(self.flights_frame, self.airlines, self.stages) # Create a flight
        flight.pack() # Pack the flight into the scrollable frame
        self.flights.append(flight) # Add the flight to the list of flights

    def pin(self):

        self.pinned = not self.pinned # Toggle the pin state
        self.attributes('-topmost', self.pinned) # Toggle pinning the window

        if self.pinned: # If the window is pinned

            self.pin_button.configure(text="Unpin") # Change the text of the pin button to "Pin"

        else: # If the window is not pinned

            self.pin_button.configure(text="Pin") # Change the text of the pin button to "Unpin"

    def show_chart(self):

        airport = self.show_chart_menu.get() # Get the airport from the entry

        if airport in self.airports: # If the airport is in the list of airports

            webbrowser.open(f"https://ptfs.xyz/charts/dark/{airport} Ground Chart.png") # Open the airport chart in the default browser
    
class Flight(customtkinter.CTkFrame):

    def __init__(self, master, airlines, stages, airline=None, flight_number=None, flight_stage=None, flight_stage_info=None):

        super().__init__(master) # Initialise the frame

        self.grid_columnconfigure(0, weight=1) # Make the first column expand to fill the frame
        self.grid_columnconfigure(1, weight=1) # Make the second column expand to fill the frame
        self.grid_columnconfigure(2, weight=1) # Make the third column expand to fill the frame
        self.grid_columnconfigure(3, weight=1) # Make the fourth column expand to fill the frame
        self.grid_columnconfigure(4, weight=1) # Make the fifth column expand to fill the frame

        self.airline = customtkinter.CTkOptionMenu(self, width=200, values=airlines) # Create an option menu

        if airline != None: # If the airline is not None

            self.airline.set(airline) # Set the airline to the airline passed to the function

        self.airline.grid(row=0, column=0, padx=5, pady=5) # Place the airline option menu on the frame

        self.flight_number = customtkinter.CTkEntry(self, width=50) # Create an entry box

        if flight_number != None: # If the flight number is not None

            self.flight_number.insert(0, flight_number) # Set the flight number to the flight number passed to the function
            
        self.flight_number.grid(row=0, column=1, padx=5, pady=5) # Place the flight number entry on the frame
 
        self.flight_stage = customtkinter.CTkOptionMenu(self, width=100, values=stages) # Create an option menu

        if flight_stage != None: # If the flight stage is not None

            self.flight_stage.set(flight_stage) # Set the flight stage to the flight stage passed to the function
            
        self.flight_stage.grid(row=0, column=2, padx=5, pady=5) # Place the flight stage option menu on the frame

        self.flight_stage_info = customtkinter.CTkEntry(self, width=100) # Create an entry box

        if flight_stage_info != None: # If the flight stage info is not None

            self.flight_stage_info.insert(0, flight_stage_info) # Set the flight stage info to the flight stage info passed to the function

        self.flight_stage_info.grid(row=0, column=3, padx=5, pady=5) # Place the flight stage info entry on the frame

        self.delete_button = customtkinter.CTkButton(self, text="Delete Flight", command=self.delete, hover_color="#a64949") # Create a button
        self.delete_button.grid(row=0, column=6, padx=5, pady=5) # Place the delete button on the frame

    def delete(self):

        self.destroy() # Destroy the frame of the flight, only triggers when the delete button is pressed

if __name__ == "__main__":

    # Create the window and run the app

    app = App()
    app.mainloop()