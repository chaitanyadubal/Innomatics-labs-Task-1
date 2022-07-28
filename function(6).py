def is_leap(year):
    leap = False
    
    if 1900<=year and year<=100000:
        leap = False
    if year%4==0 and year%100!=0:
            return True
        
    elif year%400==0 and year%100==0 :
            return True
        
    else:
            return leap

year = int(raw_input())
print is_leap(year)
