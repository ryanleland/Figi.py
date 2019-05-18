# Figi.py

Simple OpenFIGI client for Python 3.

## Usage

You can perform a search with the following:

    from figi import Figi
    client = Figi("{FIGI_API_KEY}")

    print(client.search("AAPL", exchCode="US", securityType="Common Stock"))

Which will result in the following output:

    [{'figi': 'BBG000B9XRY4', 'name': 'APPLE INC', 'ticker': 'AAPL', 'exchCode': 'US', 'compositeFIGI': 'BBG000B9XRY4', 'uniqueID': 'EQ0010169500001000', 'securityType': 'Common Stock', 'marketSector': 'Equity', 'shareClassFIGI': 'BBG001S5N8V8', 'uniqueIDFutOpt': None, 'securityType2': 'Common Stock', 'securityDescription': 'AAPL'}]
