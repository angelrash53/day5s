#Write a function that takes a list of exclusive prices, and tax rate as parameters, then calculate the VAT amount and inclusive prices of each value in the list.
#Return a list of inclusive prices and a list of VAT amount.

exclusiveprices = ["50","60","70"]
print(exclusiveprices)
taxrate = 0.16 #16/100

def calculatevat(exclusiveprices,taxrate):
    inclusiveprice = []
    vatamount = []
    for price in exclusiveprices:
        vat = price * taxrate
        vatamount.append(vat)
        inclusiveprice.append(price + vat)

    return [inclusiveprice,vatamount]

print(calculatevat([50,60,70], 0.16))