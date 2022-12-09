def C_Adder(num1,num2): #Very simple adder for complex numbers takes two complex numbers in as strings and adds them together
    num1 = num1.split("+") #Currently does not work for negatives yet
    num2 = num2.split("+")
    real1 = num1[0]
    imaginary1 = num1[1]
    real2 = num2[0]
    imaginary2 = num2[1]
    realresult = int(real1) + int(real2)
    imaginaryresult = int(imaginary1[1:len(imaginary1)-1]) + int(imaginary2[1:len(imaginary2)-1])
    result = str(realresult) + "+" + str(imaginaryresult) + "i"
    return result
def C_Multiplier(num1,num2): #Complex number multiplier multiplies two complex numbers together
    num1 = num1.split("+")
    num2 = num2.split("+")
    real1 = num1[0]
    imaginary1 = num1[1]
    real2 = num2[0]
    imaginary2 = num2[1]
    realresult = int(real1) * int(real2) + int(imaginary1[1:len(imaginary1)-1]) * int(imaginary2[1:len(imaginary2)-1]) * -1
    imaginaryresult = int(real1) * int(imaginary2[1:len(imaginary2)-1]) + int(real2) * int(imaginary1[1:len(imaginary1)-1])
    result = str(realresult) + "+" + str(imaginaryresult) + "i"
    return result
print(C_Adder("44 + 15i","7 + -24i"))
print(C_Multiplier("2 + 3i","1 + 4i"))
####