class ConversionCentiClass:
    def ConversionCentiMethod(feet,inches):
        heightInCenti = feet*15*2.54 + inches*2.54
        return heightInCenti

# Driver Code

print('Height1:',ConversionCentiClass.ConversionCentiMethod(5,7))
print('Height2:',ConversionCentiClass.ConversionCentiMethod(50,70))


