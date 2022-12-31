from pandas import read_excel, read_sql_table, read_sql_query, ExcelWriter
import sqlite3

print("Before Inputting any file, Here are some Key points to be Taken care of:")
print("")
print("1.) You Have to input the path of the file as follows: \"D:/Client_File/Master_book.xlsx\"")
print("\t You can copy the path by right clicking on the file and selecting \"Copy as Path\"")
print("")
print("2.) You have to Name the Taxable Value column of both the files as \"Taxable Value\" strictly caps sensitive")
print("")
print("3.) You have to Name the Invoice No. column of both the files as \"Invoice No\" strictly caps sensitive")
print("")
print("4.) You have to Name the SGST column of both the files as \"SGST\" strictly caps sensitive")
print("")
print("5.) You have to Name the IGST column of both the files as \"IGST\" strictly caps sensitive")
print("")
print("6.) You have to Name the GSTIN column of both the files as \"GSTIN\" strictly caps sensitive")
print("\tOtherwise the file won't work as Expected")
print("")
print("7.) Close both the Excel files before entering here")
print("")
print("Make your excel file Clean and Raw i.e. It should look like just one giant table.")
print("")
print("This is still a prototype version of this, very less amount of error handling is done. Feel free to list down the problems")
input("Hit Enter to Continue:")

# Taking Path as input for the Excel file
bookpath = "Master Sheet Books.xlsx"
m2bpath = "Master Sheet 2B.xlsx"
# bookpath = input("Enter the Path of the BOOK: ").replace('\\','/').replace('"','')
# m2bpath = input("Enter the Path of the 2b File: ").replace('\\','/').replace('"','')
excel_df1 = read_excel(bookpath)
excel_df2 = read_excel(m2bpath)

margin_error_check = input('''Do you want any margin of error for your balancing? For eg:\n1,
 +1 and -1 in records is acceptable and considered as a match\nY for YES, N for NO \n''')

margin_error = 0
if margin_error_check.lower() in ['y','yes']:
    margin_error = int(input("Enter Margin of Error as for eg:\n 1 for 1Rs. , 5 for 5Rs.\n "))
# dropping any existing remarks
excel_df1 = excel_df1.drop('Remarks', axis=1, errors='ignore').dropna(axis=0,how='all').fillna(0)
excel_df2 = excel_df2.drop('Remarks', axis=1, errors='ignore').dropna(axis=0,how='all').fillna(0)

# Converting the Existing Taxable Value to int by deleting all the Commas and Fullstops
taxable_value1 = excel_df1["Taxable Value"].tolist()
taxable_value2 = excel_df2["Taxable Value"].tolist()
taxable_value_count = 0
for value in taxable_value1:
    try:
        excel_df1.at[taxable_value_count, "Taxable Value"] = int(
            str(value).replace(',', '').split(".", 1)[0])
        taxable_value_count += 1
    except ValueError:
        excel_df1.at[taxable_value_count, "Taxable Value"] = int("0")
        taxable_value_count += 1

taxable_value_count = 0
for value in taxable_value2:
    try:
        excel_df2.at[taxable_value_count, "Taxable Value"] = int(
            str(value).replace(',', '').split(".", 1)[0])
        taxable_value_count += 1
    except ValueError:
        excel_df2.at[taxable_value_count, "Taxable Value"] = int("0")
        taxable_value_count += 1

SGST_value1 = excel_df1["SGST"].tolist()
SGST_value2 = excel_df2["SGST"].tolist()
taxable_value_count = 0
for value in SGST_value1:
    try:
        excel_df1.at[taxable_value_count, "SGST"] = int(
            str(value).replace(',', '').split(".", 1)[0])
        taxable_value_count += 1
    except ValueError:
        excel_df1.at[taxable_value_count, "SGST"] = int("0")
        taxable_value_count += 1

taxable_value_count = 0
for value in SGST_value2:
    try:
        excel_df2.at[taxable_value_count, "SGST"] = int(
            str(value).replace(',', '').split(".", 1)[0])
        taxable_value_count += 1
    except ValueError:
        excel_df2.at[taxable_value_count, "SGST"] = int("0")
        taxable_value_count += 1


CGST_value1 = excel_df1["IGST"].tolist()
CGST_value2 = excel_df2["IGST"].tolist()
taxable_value_count = 0
for value in CGST_value1:
    try:
        excel_df1.at[taxable_value_count, "IGST"] = int(
            str(value).replace(',', '').split(".", 1)[0])
        taxable_value_count += 1
    except ValueError:
        excel_df1.at[taxable_value_count, "IGST"] = int("0")
        taxable_value_count += 1


taxable_value_count = 0
for value in CGST_value2:
    try:
        excel_df2.at[taxable_value_count, "IGST"] = int(
            str(value).replace(',', '').split(".", 1)[0])
        taxable_value_count += 1
    except ValueError:
        excel_df2.at[taxable_value_count, "IGST"] = int("0")
        taxable_value_count += 1


# Creating a connection and assigning a cursor
# con = sqlite3.connect(':memory:')
con = sqlite3.connect('balance.db')
cur = con.cursor()

# Creating Database Table for Excel file Master Sheet Books
cur.execute(
    'CREATE TABLE IF NOT EXISTS books (GSTIN text, Taxable Value number);')
cur.execute('CREATE TABLE IF NOT EXISTS twob (GSTIN text, Taxable Value number);')
con.commit()

# Converting Excel file Master Sheet Books to a sql database
excel_df1.to_sql('books', con, if_exists='replace', index=False)
excel_df2.to_sql('twob', con, if_exists='replace', index=False)

# adding Remarks Table and Setting by default as No match.
cur.execute('''
    ALTER TABLE books
        ADD Remarks TEXT;
        ''')
cur.execute('''
    ALTER TABLE twob
        ADD Remarks TEXT;
    ''')
con.commit()
cur.execute("UPDATE twob SET Remarks=\"Not in Books\";")
cur.execute("UPDATE books SET Remarks=\"Not in 2b\";")
con.commit()

cur.execute("SELECT GSTIN,\"Taxable Value\",IGST,SGST,\"Invoice No\" FROM books")
books = cur.fetchall()

# Selecting all the matched results from database and Setting remarks to match.
for book in books:
    cur.execute('SELECT "Invoice No" FROM twob WHERE GSTIN = ? AND "Taxable Value" = ? AND IGST = ? AND SGST = ? AND Remarks ="Not in Books" LIMIT 1',
                (book[0], book[1], book[2], book[3]))
    match = cur.fetchall()
    if len(match) != 0:
        cur.execute(
            "UPDATE twob SET Remarks =\"Match\" WHERE \"Invoice No\"= ?", (match[0][0],))
        con.commit()
        cur.execute(
            'UPDATE books SET Remarks = "Match" WHERE "Invoice No" = ?', (book[4],))
        con.commit()
    else:
        cur.execute('SELECT "Invoice No",\"Taxable Value\",IGST,SGST FROM twob WHERE GSTIN = ? AND "Invoice No" = ? AND Remarks ="Not in Books" LIMIT 1',
                (book[0], book[4]))
        match2 = cur.fetchall()
        if len(match2) != 0:
            if ((match2[0][1])+margin_error) >= book[1]:
                if((match2[0][1])-margin_error) <= book[1]:
                    cur.execute("UPDATE twob SET Remarks =\"Match\" WHERE \"Invoice No\"= ?", (match2[0][0],))
                    con.commit()
                    cur.execute('UPDATE books SET Remarks = "Match" WHERE "Invoice No" = ?', (book[4],))
                    con.commit()

# Reading the database and Printing it on the excel file.
notmatchinbooks = read_sql_query(
    "select * from books where Remarks = \"Not in 2b\"", "sqlite:///balance.db")
notmatchin2b = read_sql_query(
    "select * from twob where Remarks = \"Not in Books\"", "sqlite:///balance.db")
overallbooks = read_sql_table('books', "sqlite:///balance.db")
overall2b = read_sql_table('twob', "sqlite:///balance.db")
with ExcelWriter(bookpath, mode="a", if_sheet_exists="replace") as writer:
    overallbooks.to_excel(writer, sheet_name="overall")
    notmatchinbooks.to_excel(writer, sheet_name="not in 2b")


with ExcelWriter(m2bpath, mode="a", if_sheet_exists="replace") as writer:
    overall2b.to_excel(writer, sheet_name="overall")
    notmatchin2b.to_excel(writer, sheet_name="not in books")


con.close()
