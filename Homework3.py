#Homework Assignment #3: "If" Statements

def Param_comp(p1,p2,p3):
    if int(p1)==int(p2)==int(p3): #case where all 3 parameters are equal
        are_equal=True
    elif int(p1)==int(p2) or int(p1)==int(p3) or int(p2)==int(p3): #case where 2 of the parameters are equal:
        are_equal=True
    else:
        are_equal=False
    return are_equal

Out_equal=Param_comp(6,5,"5")

print(Out_equal)


