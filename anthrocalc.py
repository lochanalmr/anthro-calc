from menu import *
from modules import *
import sys

VERSION = "1.1.0"

def main():
    print("======================================")
    print("          AnthroCalc v" + VERSION)
    print("=======================================")
    
    g = 0
    while g == 0:
        try:
            menu_display()
            option = option_selection()

            match option:
                case "BMI":
                    bmi_module()
                case "BAI":
                    bai_module()
            
            print("\nCalculated and classified by AnthroCalc v" + VERSION)
            while True:
                c = input("Press [E] to exit, or [R] to return to main menu: ")
                if c != "" and c is not None:
                    c = c.upper()
                if c == "" or c is None:
                    continue
                elif c == "E":
                    sys.exit(0)
                elif c == "R":
                    break
                else:
                    continue
        except KeyboardInterrupt:
            break
        

if __name__ == "__main__":
    main()