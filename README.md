PayPalCSV
=========

This utility converts a PayPal CSV into an importable format for other accounting software.<br />
Currently, this has only been tested with Xero.

####Features

* Separate PayPal Fees from a transaction and write them as separate transactions.
* Updates the "Withdraw Funds to a Bank Account" transaction so the "From/To" fields are between you and a bank account.

####How to use the script

* Install Python 3.3.1 or higher
* Download script.py and make sure it's in the same folder as your PayPal CSV file
* Rename your PayPal CSV file to "input.csv"
* Open script.py using your favorite text editor. Change the "account_email" to your PalPal account email, and "bank_account" to your bank.
* Run the script: `python3 script.py`
* You should see a new CSV file, called "output.csv" in the same folder as your script.

####Want to contribute?
* Submit a pull request!
* Submit a GitHub issue to request new features, report bugs, and ask questions specific to PayPalCSV.
