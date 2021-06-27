
#               Alarm Clock               #


from datetime import datetime as dt
from playsound import playsound
import time


def main():

    date_flag = 0
    print()
    Time = input("Enter time in format HH:MM:SS : ")
    print()
    choice = input("Do you want to set the alarm for Specific Date (y/n) :")
    if choice == "y":
        date_flag = 1
        print()
        specific_date = input("Set a Date for the alarm in MM/DD/YY : ")
        print()
        print(f"Your alarm is set for {Time} on {specific_date}")
        print()
    else:
        print()
        print(f"Your alarm is set for {Time}")
        
    
    hour = int(Time[:2])
    min = int(Time[3:5])
    sec = int(Time[6:8])

    while True:
        current_time = dt.now()
   
        if date_flag == 1:
            
            if specific_date == current_time.strftime("%D"):
                if hour == current_time.hour:
                    if min == current_time.minute:
                        if sec == current_time.second:
                            print()
                            for i in range(3):
                                print("..........Wake up..........")  
                                time.sleep(1)   
                            playsound('Enter the path where you saved the sound track')
                            break
        else:
            
            if hour == current_time.hour:
                if min == current_time.minute:
                    if sec == current_time.second:
                        print()
                        for i in range(3):
                            print("..........Wake up..........")  
                            time.sleep(1)
                        playsound('Enter the path where you saved the sound track')
                        break
                          


if __name__ == "__main__":
  
  
    main()
