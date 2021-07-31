# A Simple Date Database

months = [
    "January",
    
    "February",
    
    "March",
    
    "April",
    
    "May",
    
    "June",
    
    "July",
    
    "August",
    
    "September",
    
    "October",
    
    "November",
    
    "December"
]

endings = ["st", "nd", "rd"] + 17*["th"]\
        + ["st", "nd", "rd"] +7*["th"]\
        + ["st"]
        
        
Year = input("Enter Year: ")

Month = input("Enter Month: ")

Day = input("Enter the day: ")

month_number = int(Month)

day_number = int(Day)

Month_name = months[month_number - 1]

ordinal = Day + endings[day_number - 1]

print(Month_name + " " + ordinal + ", " + Year)