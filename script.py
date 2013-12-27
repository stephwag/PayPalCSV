# Script based on "Edit the CSV and import the gross transaction amounts into Xero"
# http://help.xero.com/Help/howto/Q_ImportPayPal.htm
 
import csv
 
#According to the link above, all transactions except these should be removed from the PayPal CSV file
valid_transactions = ['Completed','Cleared','Refunded','Reversed']

#Change this to your account email
account_email = "you@yoursite.com"

paypal_name = "Paypal, Inc."
withdraw_funds_to_bank_account = "Withdraw Funds to a Bank Account"
paypal_fee = "PayPal Fee"
bank_account = "Bank Account"
 
csvin = open("input.csv", 'r', newline='' )
csvout = open("output.csv", 'w', newline='')
output_fields = ["Date", " Name", " Type", " Status", " Currency", " Net", " Fee", " From Email Address", " To Email Address", " Transaction ID", " Item Title"]

#Set up the reader/writer objects
csvreader = csv.DictReader(csvin)
csvwriter = csv.DictWriter(csvout, fieldnames=output_fields, extrasaction="ignore")

csvwriter.writeheader()
 
for row in csvreader:
               
		if row[" Status"] in valid_transactions:
			gross = row[" Gross"]
			net = row[" Net"]
			fee = row[" Fee"]
			orig_type = row[" Type"]

			row[" Net"] = gross
			row[" Fee"] = "0"

			#If you withdrew funds to your bank, from/to will be changed so the transaction is between you and your bank.
			if orig_type == withdraw_funds_to_bank_account:
				row[" From Email Address"] = account_email
				row[" To Email Address"] = bank_account

			csvwriter.writerow(row)

			#If a fee was charged, separate it to a new line
			if fee != "0":
				row[" Gross"] = fee
				row[" Net"] = fee
				row[" Fee"] = "0"
				row[" Type"] = paypal_fee
				row[" From Email Address"] = account_email
				row[" To Email Address"] = paypal_name

				csvwriter.writerow(row)
 
csvin.close()
csvout.close()
