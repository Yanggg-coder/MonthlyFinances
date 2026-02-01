
import key_setup
import re

def extract_transaction_metadata(tokens, i_token, month_keys, name_keys):

    # Setup transaction metadata to save off 
    transaction_month = ""
    transaction_day   = 0
    posting_month     = ""
    posting_day       = 0

    while i_token < len(tokens):

        # Found initial statement charge
        if tokens[i_token] in month_keys: 
            print('found the first month token')

            # Save off transaction metadata
            transaction_month = tokens[i_token]
            transaction_day   = tokens[i_token + 1]

            # Increment by two and see if we can find the next charge
            i_token = i_token + 2 
            if i_token < len(tokens) and tokens[i_token] in month_keys:
                print('found the second month token')

                # Save off posting metadata
                posting_month = tokens[i_token]
                posting_day   = tokens[i_token + 1]

                # print out the metadata
                print(f"""transaction date: {transaction_month} {transaction_day} \nposting date:     {posting_month} {posting_day}""")

                # If we find the posting date, do stuff
                i_token = i_token + 2

                # Call the token parser and extract the rest of the transaction metadata
                i_token, charge_metadata = transaction_metadata(tokens, i_token, month_keys, name_keys)

        # Otherwise, keep looking for the initial statemnt charge
        else:
            i_token = i_token + 1

        print(f"i_token = {i_token}")


def transaction_metadata(tokens,i_token,month_keys,name_keys):

    token_str = []
    while (i_token < len(tokens)) and (tokens[i_token] not in month_keys) and (tokens[i_token] not in name_keys):
        token = tokens[i_token]

        if token != "":
            print(token)
            print(token[0])
        else:
            print("token is empty \"\" ")
            print(token)
            i_token = i_token + 1
            continue
            

        if token[0] == "$":
            print("this token is a $")
            print(token)
            i_token = i_token + 1
            charge_metadata = float(token[1:].replace(",", ""))
            print(f"charge_metadata = {charge_metadata}")
            break
        else:
            token_str.append(token)

        i_token = i_token + 1

    token_str = "".join(token_str)
    print(f"token_str = {token_str}")

    find_transaction_type(token_str)

    print('found all information from this charge\n')

    return i_token, charge_metadata

def find_transaction_type(token_str):
    
    grocery_keys  = key_setup.grocery_keys
    grocery_keys  = [g.lower() for g in grocery_keys]


    for key in grocery_keys:
        if re.search(key, token_str):
            print("type is grocery!")