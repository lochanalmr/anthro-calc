def menu_display():
    print("\nMenu: ")
    print("BMI: Body Mass Index")
    print("BAI: Body Adiposity Index")
    print("WHR: Waist to Hip Ratio")
    #print("WHTR: Waist to Height Ratio")
    #print("RFM: Relative Fat Mass")
    print("MM: MultiMeasure")
    #print("H: Learn more about these functions")


def option_selection():
    option = ""

    while option == "":
        try:
            option = input("\nSelect an option: ")

            #add options here
            if option != "" and not None:
                option = option.upper()
                if option != "BMI" and option != "BAI" and option != "WHR" and option != "MM":
                    print("Not a supported option")
                    option = ""

        except KeyboardInterrupt:
            break

    return option