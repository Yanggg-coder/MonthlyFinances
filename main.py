import string
import key_setup


if __name__ == "__main__":
    print("running inside main.py")

    # Initial filepath setup
    text_input_path_base        = "..\\MonthlyStatements"
    test_file_name             = "test_file.txt"
    january_statement_filename = "january_statement.txt"

    # Initial key setup
    month_keys = key_setup.month_keys
    name_keys  = key_setup.name_keys

    # Read input files
    with open(f"{text_input_path_base}\\{january_statement_filename}", "r") as f:
        content = f.read()

    print(content)

    # Remove newlines and split by spaces
    tokens = content.replace("\n", " ").split()

    print(tokens)

    # Keep $ for amounts, strip everything else
    punctuation_to_strip = string.punctuation.replace('$', '')  # everything except $
    month_keys = [m.lower().strip(punctuation_to_strip) for m in month_keys]
    name_keys  = [n.lower().strip(punctuation_to_strip) for n in name_keys]
    tokens     = [t.lower().strip(punctuation_to_strip) for t in tokens]

    # Setup token index
    i_token = 0

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

                while (i_token < len(tokens)) and (tokens[i_token] not in month_keys) and (tokens[i_token] not in name_keys):
                    print(tokens[i_token])
                    i_token = i_token + 1

                print('found all information from this charge\n')

        # Otherwise, keep looking for the initial statemnt charge
        else:
            i_token = i_token + 1

        print(f"i_token = {i_token}")
