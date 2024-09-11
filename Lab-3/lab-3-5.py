s = input("Enter the String : ")
# x  = False
# for i in s :
#     if(i.isalnum()):
#         continue
#     else:
#         x = True
#         break   
# if x == True :
#     print("All are Alphanumberic")     
# else:
#     print("Atleast one character is not alphanumberic")

def isalpha_numberic(s):
    for i in s:
        if(i.isalnum() == False):
            return False
    return True

print(isalpha_numberic(s))    