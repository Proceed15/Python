print("Country, Product and Batch Number")

ProductLotNumber = input("Please enter the Lot number of the product: ")

print("Contry code:", ProductLotNumber[0:3], "\nProduct code:", ProductLotNumber[4:9], "\nBatch number:", ProductLotNumber[-5:15])
