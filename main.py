import string
import key_setup
import token_parser
import os
import checking
import pandas as pd
import fitz


if __name__ == "__main__":
    print("running inside main.py")

    # # Initial filepath setup
    # text_input_path_base = os.path.join("..", "MonthlyStatements")
    # test_file_name             = "test_file.txt"
    # january_statement_filename = "january_statement.txt"
    # april_statement_filename = "April_statement.txt"

  
    # # Read input files
    # input_path = os.path.join(text_input_path_base,april_statement_filename)
    # with open(input_path, "r") as f:
    #     content = f.read()

    # print(content)

    # # Remove newlines and split by spaces
    # tokens = content.replace("\n", " ").split()

    # print(tokens)

    # Initial filepath setup
    text_input_path_base = os.path.join("..", "MonthlyStatements")
    test_file_name             = "test_file.txt"
    january_statement_filename = "january_statement.txt"
    february_statement_filename_pdf = "february_statement.pdf"
    march_statement_filename_pdf = "march_statement.pdf"
    april_statement_filename_txt = "April_statement.txt"
    april_statement_filename_pdf = "april_statement.pdf"
    february_statement_filename_nfcu_pdf = "february_statement_nfcu.pdf"
    march_statement_filename_nfcu_pdf = "march_statement_nfcu.pdf"
    april_statement_filename_nfcu_pdf = "april_statement_nfcu.pdf"

    pdf_path = os.path.join(text_input_path_base,march_statement_filename_nfcu_pdf)

    doc = fitz.open(pdf_path)

    text = ""
    for page in doc:
        text += page.get_text()

    # Remove newlines and split by spaces
    tokens = text.replace("\n", " ").split()

    print(tokens)

    # Keep $ for amounts, replace everything else to nothing then
    # strip everything else
    punctuation_to_strip = string.punctuation.replace('$', '')  # everything except $
    tokens     = [t.lower().strip(punctuation_to_strip) for t in tokens]

    # Setup token index
    i_token = 0
 
    # transaction_output = token_parser.extract_transaction_metadata_capital_one_statements(tokens,i_token)
    transaction_output = token_parser.extract_transaction_metadata_navy_federal_credit_union_statements(tokens,i_token)
    print(f"len(transaction_output) = {len(transaction_output)}")
    print(f"transaction_output = {transaction_output}")

    checking_output = checking.total_checking(transaction_output)


    df = pd.DataFrame(transaction_output)
    print(f"data frame is:\n{df}")

    spending_summary = df.groupby("category")["amount"].sum()
    print(f"Spending Summary: \n{spending_summary}")

    # category_amounts = dict(zip(spending_summary["category"], spending_summary["amount"]))
    # print(category_amounts["vehicle"])
    categories = key_setup.getCategories().keys()
    print(categories)

    # spending_summary["category"]

    percentages = []
    for category in spending_summary.index:
        amount = spending_summary[category]
        pctg = amount / checking_output * 100
        percentages.append(pctg)
        print(category, pctg)




    # print (spending_summary)


