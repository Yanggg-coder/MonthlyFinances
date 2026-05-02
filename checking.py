import token_parser

#charged_amount = 0
def total_checking(dictionary_list):

    charged_amount = 0

    for dictionary_i in dictionary_list:
        
        print(dictionary_i["description"])
        print(dictionary_i["amount"])

        if dictionary_i["description"] == 'capital one mobile pymt':
            dictionary_i["amount"] = -dictionary_i["amount"]
        else:
            dictionary_i["amount"]

        previous_amount = dictionary_i["amount"]
        
        charged_amount = charged_amount + previous_amount
        
        print(f"Charged Amount {charged_amount}")

    print(f"Total Charged Amount: {charged_amount}")
    return charged_amount

    # transaction = {
    #                 "transaction_date": tran_date,
    #                 "post_date": post_date,
    #                 "description": token_str,
    #                 "amount": charge_metadata,
    #                 "category": category_type

    #             }