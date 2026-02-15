import string
import key_setup
import token_parser
import statement_data
import os


if __name__ == "__main__":
    print("running inside main.py")

    # Initial filepath setup
    text_input_path_base = os.path.join("..", "MonthlyStatements")
    test_file_name             = "test_file.txt"
    january_statement_filename  = "january_statement.txt"
    december_statement_filename = "december_statement.txt"

  
    # Read input files
    input_path = os.path.join(text_input_path_base,december_statement_filename)
    with open(input_path, "r") as f:
        content = f.read()

    print(content)

    # Remove newlines and split by spaces
    tokens = content.replace("\n", " ").split()

    print(tokens)

    # Keep $ for amounts, strip everything else
    punctuation_to_strip = string.punctuation.replace('$', '')  # everything except $
    tokens     = [t.lower().strip(punctuation_to_strip) for t in tokens]

    # Setup token index
    i_token = 0
 
    transaction_data_list = token_parser.extract_transaction_metadata(tokens,i_token)

    if transaction_data_list is not None:

        for idx, classData in enumerate(transaction_data_list):
            print(f"printing data for index {idx}")
            classData.printStatementData() # call the print funciton
            print("\n")
