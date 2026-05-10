
import key_setup
import re

def extract_transaction_metadata_capital_one_statements(tokens, i_token):

    # Get the month keys and the name keys
    month_keys, name_keys = key_setup.getMonthKeys(), key_setup.getNameKeys()

    # Get the categories dictionary
    categories = key_setup.getCategories()
    print("now in token_parser file: Print the categories like grocery, " \
    "household, travel and so on as well as the companies in the cetegory. -- ")
    print('categories:')
    print(categories)
    #category, keys = categories.items():

    print("now print item and keys individually")
    for item, key in categories.items():
        print(item,key)
        print(item)
    print(item)

    # return
    # Setup transaction metadata to save off 
    transaction_month = ""
    transaction_day   = 0
    posting_month     = ""
    posting_day       = 0

    transactions = []

    while i_token < len(tokens):


        # Found initial statement charge
        if tokens[i_token] in month_keys: 
            print('extract_transaction_metadata: found the first month token')

            # Save off transaction metadata
            transaction_month = tokens[i_token]
            transaction_day   = tokens[i_token + 1]

            # Increment by two and see if we can find the next charge
            i_token = i_token + 2 
            
            if i_token < len(tokens) and tokens[i_token] in month_keys:
                print('extract_transaction_metadata: found the second month token')

                # Save off posting metadata
                posting_month = tokens[i_token]
                posting_day   = tokens[i_token + 1]

                # create trans date and post date
                tran_date= transaction_month + ' ' + transaction_day
                post_date= posting_month + ' ' + posting_day

                # print out the metadata
                print(f"""\nextract_transaction_metadata:\ntransaction date: {transaction_month} {transaction_day} \nposting date:     {posting_month} {posting_day}\n""")

                print(f"Alternative method of transction date and posting date: \ntransaction date:{tran_date} \nposting date: {post_date}")

                # If we find the posting date, do stuff
                i_token = i_token + 2

                # Call the token parser and extract the rest of the transaction metadata
                i_token, token_str, charge_metadata, category_type = transaction_metadata(tokens, i_token, month_keys, name_keys, categories)

                transaction = {
                    "transaction_date": tran_date,
                    "post_date": post_date,
                    "description": token_str,
                    "amount": charge_metadata,
                    "category": category_type

                }

                print(f"transaction dictionary: {transaction}")

                if transaction["description"] == 'capitalonemobilepymt':
                    transaction["amount"] = 0
                
                else:
                    transaction["amount"]

                transactions.append(transaction)

        # Otherwise, keep looking for the initial statemnt charge
        else:
            i_token = i_token + 1

        print(f"extract_transaction_metadata: i_token = {i_token}")

    print(f"final transactions:{transactions} \nThis is the output from function extract_transaction_metadata, which is being called from the main.py")
    return transactions

def extract_transaction_metadata_navy_federal_credit_union_statements(tokens, i_token):

    # Get the month keys and the name keys
    month_keys, name_keys, month_map = key_setup.getMonthKeys(), key_setup.getNameKeys(), key_setup.getMonthMap()

    # Get the categories dictionary
    categories = key_setup.getCategories()
    print("now in token_parser file: Print the categories like grocery, " \
    "household, travel and so on as well as the companies in the cetegory. -- ")
    print('categories:')
    print(categories)
    #category, keys = categories.items():

    print("now print item and keys individually")
    for item, key in categories.items():
        print(item,key)
        print(item)
    print(item)

    # return
    # Setup transaction metadata to save off 
    transaction_month = ""
    transaction_day   = 0
    posting_month     = ""
    posting_day       = 0

    transactions = []

    while i_token < len(tokens):
        
        # Extract the current token
        token_i =  tokens[i_token]
        print(token_i)

        # Check if the current token has a date format
        if re.fullmatch(r"\d{2}/\d{2}/\d{2}",token_i):
            
            # Extract the transaction date information
            transaction_month = token_i[0:2]
            print(type(transaction_month))
            print(transaction_month)
            transaction_month = month_map[transaction_month]
            transaction_day   = token_i[3:5]
            tran_date = transaction_month + ' ' + transaction_day

            # Increment the token counter by one
            i_token = i_token + 1

            # Extract the current token
            token_i =  tokens[i_token]

            # Check if the current token has a date format
            if re.fullmatch(r"\d{2}/\d{2}/\d{2}",token_i):

                # Extract the posting date information
                posting_month = token_i[0:2]
                posting_month = month_map[posting_month]
                posting_day   = token_i[3:5]
                post_date = posting_month + ' ' + posting_day

                # Increment the token counter by one
                i_token = i_token + 1

                # Call the token parser and extract the rest of the transaction metadata            
                i_token, token_str, charge_metadata, category_type = transaction_metadata(tokens, i_token, month_keys, name_keys, categories)

                transaction = {
                    "transaction_date": tran_date,
                    "post_date": post_date,
                    "description": token_str,
                    "amount": charge_metadata,
                    "category": category_type

                }

                print(f"transaction dictionary: {transaction}")

                if re.search("paymentreceived",transaction["description"]):
                    transaction["amount"] = 0
                
                else:
                    transaction["amount"]

                transactions.append(transaction)

        # Otherwise, keep looking for the initial statemnt charge

        else:
            i_token = i_token + 1

    return transactions

def transaction_metadata(tokens,i_token,month_keys,name_keys,categories):

    token_str = []
    while (i_token < len(tokens)) and (tokens[i_token] not in month_keys) and (tokens[i_token] not in name_keys):
        token = tokens[i_token]

        if token != "":
            print(f'transaction_metadata: {token}')
            print(f'transaction_metadata: {token[0]}')
        else:
            print('transaction_metadata: token is empty "" ')
            print(f'transaction_metadata: {token}')
            i_token = i_token + 1
            continue
            

        if token[0] == "$":
            print("transaction_metadata: this token is a $")
            print(f'transaction_metadata: {token}')
            charge_amount = float(token[1:].replace(",", ""))
            print(f"transaction_metadata: charge_metadata = {charge_amount}")
            i_token = i_token + 1
            break
        else:
            token_str.append(token)
            print(token_str)
            i_token = i_token + 1

    token_str = "".join(token_str)
    print(f"transaction_metadata: token_str = {token_str}")

    category_type = find_transaction_type(token_str,categories)
    print(f'transaction_metadata: category was found to be a {category_type}')
    print('transaction_metadata: found all information from this charge\n')

    return i_token, token_str, charge_amount, category_type

def find_transaction_type(token_str,categories):

    
    # Search through the categories and find which
    # type the transaction is:
    for category, keys in categories.items():
        
        # Search through each key in this categories keys
        
       for key in keys:
           if re.search(re.escape(key), token_str):
               print(f"find_transaction_type: type is {category}!")
               return category
    
    print(f"Can't find category for this transaction information {token_str}. There is no key matchs.")
    return f"unknow key {token_str}"          




            
 
        #         stop_search = True
        #         break
            

        # if stop_search:
        #     break
    



