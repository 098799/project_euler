digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
xtens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hund = "hundred"
a = "and"
thou = "onethousand"

###For up to and including 99:
#print(9*len(''.join(digits)) + len(''.join(teens)) + len(''.join(xtens)))

twodigits = 9*len(''.join(digits)) + len(''.join(teens)) + 10*len(''.join(xtens))
hundreds = 9*len(hund) + len(''.join(digits))
prefixes = 99*(9*len(hund) + len(''.join(digits)) + 9*len(a))
onethousand = len(thou)

print(prefixes + 10*twodigits + hundreds + onethousand)
