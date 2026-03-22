
import key_setup
import re

def extract_transaction_metadata(tokens, i_token):

    # Get the month keys and the name keys
    month_keys, name_keys = key_setup.getMonthKeys(), key_setup.getNameKeys()

    # Get the categories dictionary
    categories = key_setup.getCategories()


    # Setup transaction metadata to save off 
    transaction_month = ""
    transaction_day   = 0
    posting_month     = ""
    posting_day       = 0

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

                # print out the metadata
                print(f"""\nextract_transaction_metadata:\ntransaction date: {transaction_month} {transaction_day} \nposting date:     {posting_month} {posting_day}\n""")

                # If we find the posting date, do stuff
                i_token = i_token + 2

                # Call the token parser and extract the rest of the transaction metadata
                i_token, charge_metadata, category_type = transaction_metadata(tokens, i_token, month_keys, name_keys, categories)

        # Otherwise, keep looking for the initial statemnt charge
        else:
            i_token = i_token + 1

        print(f"extract_transaction_metadata: i_token = {i_token}")


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
            #i_token = i_token + 1
            break
        else:
            token_str.append(token)
            print(token_str)
            i_token = i_token + 1

    token_str = "".join(token_str)
    print(f"transaction_metadata: token_str = {token_str}")

    category_type = find_transaction_type(token_str,categories)
    print(f'transaction_metadata: category was found to be a {category_type}')
    print('transaction_metadata found all information from this charge\n')

    return i_token, charge_amount, category_type

def find_transaction_type(token_str,categories):

    stop_search = False
    # Search through the categories and find which
    # type the transaction is:
    for category, keys in categories.items():

        # Search through each key in this categories keys
        for key in keys:
            if re.search(re.escape(key), token_str):
                print(f"find_transaction_type: type is {category}!")
                return category
    return category
            

        #         stop_search = True
        #         break
            

        # if stop_search:
        #     break
    



