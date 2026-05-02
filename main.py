import string
import key_setup
import token_parser
import os
import checking


if __name__ == "__main__":
    print("running inside main.py")

    # Initial filepath setup
    text_input_path_base = os.path.join("..", "MonthlyStatements")
    test_file_name             = "test_file.txt"
    january_statement_filename = "january_statement.txt"

  
    # Read input files
    input_path = os.path.join(text_input_path_base,january_statement_filename)
    with open(input_path, "r") as f:
        content = f.read()

    print(content)

    # Remove newlines and split by spaces
    tokens = content.replace("\n", " ").split()

    print(tokens)

    # Keep $ for amounts, replace everything else to nothing then
    # strip everything else
    punctuation_to_strip = string.punctuation.replace('$', '')  # everything except $
    tokens     = [t.lower().strip(punctuation_to_strip) for t in tokens]

    # Setup token index
    i_token = 0
 
    transaction_output = token_parser.extract_transaction_metadata(tokens,i_token)

    checking.total_checking(transaction_output)




