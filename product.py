class Product(object):
# Attributes:
    def __init__(self, price, itemName, weight, brand, cost):
        self.price = price
        self.itemName = itemName
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
# Methods:
# Sell: changes status to "sold"
    def sell(self):
        self.status = "sold"
        return self
# Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
    def addTax(self, tax):
        taxAmount = tax * self.price
        self.price += taxAmount
        print "Tax:",taxAmount
        return self
# Return: takes reason for return as a parameter and changes status accordingly. If the item is being returned because it is defective 
# change status to defective and change price to 0. If it is being returned in the box, like new mark it as for sale. 
# If the box has been opened set status to used and apply a 20% discount
    def returnProduct(self,reason):
        if reason == "defective": # reason is not for each product that why we dont say "self.reason"
            self.status = "defective"
            self.price = 0
        if reason == "box":
            self.status = "for sale"
        if reason == "openBox":
            self.status = "used"
            discount =(0.20 * self.price)
            self.price = self.price - discount
            print "Reason:", reason
            print "Discount:",discount
        return self
# Display Info: show all product details.
    def displayInfo(self):
        print "Price:", self.price
        print "Name:", self.itemName
        print "Status:",self.status
        print "Brand:", self.brand
        print "Weight:", self.weight
        print "Cost:", self.cost
        print "\n"

shoes = Product(50, "Snickers", "5", "Nike", 2)
shoes.displayInfo()
print "---------------"
shoes.returnProduct("openBox")
print "---------------"
shoes.displayInfo()
print "---------------"
shoes.addTax(.18)
print "---------------"
shoes.displayInfo()