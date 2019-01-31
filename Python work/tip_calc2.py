bill = float(input("Total bill amount?"))
service = input("Level of service?")
split = int(input("Split with how many people?"))
good= float(0.20 * bill)
fair=float (1.15 * bill)
bad= float(0.10*bill)
gbill=float(good + bill)
fbill=float(fair + bill)
bbill=float(bad + bill)
split2= int(bill // split)
if service == "good":
    print ("Tip amount: {:0.2f}".format(good))
    print ("Total amount: {:0.2f}".format(gbill))
    
if service == "fair":
    print ("Tip amount: {:0.2f}".format(fair))
    print ("Total amount: {:0.2f}".format(fbill))

if service == "bad":
    print ("Tip amount: {:0.2f}".format(bad))
    print ("Total amount: {:0.2f}".format(bbill))