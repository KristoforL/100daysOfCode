#Day 22 of Code

### Practice in understanding bitwise operators ###


# & Bitwise Operator
# The & bitwise operator will combine the bits for each number and return 1 if both are 1 at the same position
print(11 & 12)
#1011 & 1100 = 1000
#1000 is the bit for 8


# | Bitwise operator
# The | operator will combine the bits for the numbers and place a 1 if either of the two bits being compared are 1
print(11 | 12)
#1011 & 1100 = 1111
#1111 is the bit for 15

#Bitwise left shift will add bits from the right most of the bits and hence making a new number. Also you can decide how many spaces you want to add with the number after declaring the left shift, i.e. 1,2,4,32
print(11<<2)
#1011 leftshift by 2 is not 101100
#This is now 44
print(11<<1)
#Same thing as above but only moved on one digit
#1011 << 1 = 10110
#This is 22

#The right shift does the opposite of the left shift where it adds zeros to the left side and then removes that same amount of bits from the right side
print(11>>2)
#1011 >> 2 is now 0010
#This is 2
print( 11>>1)
#1011 >> 1 is now 0101
#This is 5

#Xor is going to combine the numbers and place a one only if the numbers are different
print(11^12)
#1011 ^ 1100 = 0111
#This is 7

#This is complimenet and usually is the negative of the number minus 1
print(~11)
#1011 turns into  00001011 and then inversed
#11110100 and because it leads with one we know it is negative and we drop the first digit for now
#1110100 then is reverted to 0001011 and then you add 1 bit to the bit
# 0001011 + 0000001 = 1100
# Now lets not forget the negative from the leading one and we -12
# Same rules apply to the below but from my practice compliments are just the negtive of the number you want to compliment -1

print(~57)

print(~14)

print(~1048)