import string
import key_setup
import token_parser
import os


if __name__ == "__main__":
    print("running inside main.py")

    # Initial filepath setup
    text_input_path_base = os.path.join("..", "MonthlyStatements")
    test_file_name             = "test_file.txt"
    january_statement_filename = "january_statement.txt"

    # Initial key setup
    month_keys   = key_setup.month_keys
    name_keys    = key_setup.name_keys
  
    # Read input files
    input_path = os.path.join(text_input_path_base,january_statement_filename)
    with open(input_path, "r") as f:
        content = f.read()

    print(content)

    # Remove newlines and split by spaces
    tokens = content.replace("\n", " ").split()

    print(tokens)

    # Keep $ for amounts, strip everything else
    punctuation_to_strip = string.punctuation.replace('$', '')  # everything except $
    month_keys    = [m.lower().strip(punctuation_to_strip) for m in month_keys]
    name_keys     = [n.lower().strip(punctuation_to_strip) for n in name_keys]
    tokens     = [t.lower().strip(punctuation_to_strip) for t in tokens]

    # Setup token index
    i_token = 0

    # Setup transaction metadata to save off 
    transaction_month = ""
    transaction_day   = 0
    posting_month     = ""
    posting_day       = 0
    
    token_parser.extract_transaction_metadata(tokens,i_token,month_keys,name_keys)
