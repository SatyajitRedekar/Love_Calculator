def calculate_love_score(name_one , name_two):
    names = name_one+name_two
    names.lower
    total = 0
    total_2 = 0
    for letters in names:
        if "t" == letters :
            total+=1 
        if "r" == letters :
            total+=1 
        if "u" == letters :
            total+=1 
        if "e" == letters :
            total+=1
        
    for letters in names:
        if "l" == letters :
            total_2+=1 
        if "o" == letters :
            total_2+=1 
        if "v" == letters :
            total_2+=1 
        if "e" == letters :
            total_2+=1
        
    print(str(total) + str(total_2))

name_1 = str(input("Enter Your Name : "))
name_2 = str(input("Enter Your Patner's Name : "))
    
calculate_love_score(name_1 , name_2)