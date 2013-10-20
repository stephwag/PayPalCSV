# Script based on "Edit the CSV and import the gross transaction amounts into Xero"
# http://help.xero.com/Help/howto/Q_ImportPayPal.htm
 
import csv
 
#According to the link above, all transactions except these should be removed from the PayPal CSV file
valid_transactions = ['Completed','Cleared','Refunded','Reversed']
 
csvin = open("input.csv", 'r', newline='' )
csvout = open("output.csv", 'w', newline='')
 
#Set up the reader/writer objects
csvreader = csv.reader(csvin)
csvwriter = csv.writer(csvout, quoting=csv.QUOTE_ALL) #quote all the things
 
#Skip the header, but grab and write it.
headerline = next(csvreader, None)
csvwriter.writerow(headerline)
 
for row in csvreader:
               
        #row[5] in this case has the column with the named transactions (valid_transactions).
        if row[5] in valid_transactions:
                csvwriter.writerow(row)
 
csvin.close()
csvout.close()
