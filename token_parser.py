
def extract_transaction_metadata(tokens, i_token, month_keys, name_keys):

    while (i_token < len(tokens)) and (tokens[i_token] not in month_keys) and (tokens[i_token] not in name_keys):
        print(tokens[i_token])
        i_token = i_token + 1

    print('found all information from this charge\n')