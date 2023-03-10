from financial_transactions.serializers import FinancialTransactionSerializer


def handle_uploaded_file(file):
    lines = file.readlines()

    for line in lines:
        line_decode = line.decode("utf-8")
        if (len(line_decode) == 81):
            type_transaction = int(line_decode[0:1])
            value = (float(line_decode[9:19])/100) * -1 if (type_transaction ==
                                                            2 or type_transaction == 3 or type_transaction == 9) else float(line_decode[9:19])/100
            cnab_data = {
                "type": line_decode[0:1],
                "date": line_decode[1:9],
                "value": value,
                "cpf": line_decode[19:30],
                "card": line_decode[30:42],
                "hour": line_decode[42:48],
                "store_owner": line_decode[48:62],
                "store_name": line_decode[62:80],
            }
            serializer = FinancialTransactionSerializer(data=cnab_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
