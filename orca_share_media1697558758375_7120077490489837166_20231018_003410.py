
year_of_Birth = input("Birth YEAR:xxxx")

_yearCycler = 1990
Ans_picker = (int(year_of_Birth) - _yearCycler) % 12 + 1

if Ans_picker == 1:
        Zodiac_sign = ("Horse") 
    
elif Ans_picker == 2:
        Zodiac_sign = ("Goat")  
    
elif Ans_picker == 3:
        Zodiac_sign = ("Monkey")   
    
elif Ans_picker == 4:
        Zodiac_sign = ("Rooster")  
    
elif Ans_picker == 5:
        Zodiac_sign = ("Dog")  
    
elif Ans_picker == 6:
        Zodiac_sign = ("Pig") 
    
elif Ans_picker == 7:
        Zodiac_sign = ("Rat")
    
elif Ans_picker == 8:
        Zodiac_sign = ("Ox") 
    
elif Ans_picker == 9:
        Zodiac_sign = ("Tiger")
    
elif Ans_picker == 10:
        Zodiac_sign = ("Rabit")
    
elif Ans_picker == 11:
        Zodiac_sign = ("Dragon")
    
elif Ans_picker == 12:
        Zodiac_sign = ("Snake")

        
print("Your zodiac sign is", Zodiac_sign)