# I AM NOT AN ACCOUNTANT, AND I AM CERTIANLY NOT **YOUR** ACCOUNTANT.
# USE AT YOUR OWN RISK.

Usage:

1. Get a Blocktrail API key.

2. Gather CSVs.

3. Instantiate a Bifocal object.
  CSVs are passed in by filepath. API keys are strings.
```
b = bifocal.Bifocal(addresses=None, polo_key=None,
             polo_secret=None, blocktrail_key=None,
             coinbase_csv=None, celery_csv=None)
```

4 .Results can be found in the `results` dictionary.
```
b.results['BTC']['FIFO']
b.results['SJCX']['LIFO']
```


Assumptions:

Exchanges only get deposits from the user.

Exchanges only give withdrawals to the user.

Goals:
* Accept cryptocurrency addresses as inputs
* Compile data about Bitcoin and other cryptocurrency buys and sells via block explorer APIs.
* Calculate holdings, gains and losses in USD using public price APIs.
* Provide spreadsheets detailing transactions and gains.
* Provide choice of FIFO vs LIFO

Supports:
Bitcoin

Counterparty tokens traded against Bitcoin

Poloniex

Parsing Coinbase Reports

Parsing (modified) Celery histories


Unsolved problems:

Counterparty block explorer APIs only return the most recent 100 transactions for an address.

Todo:

More tests.

Credit for much of the accounting code goes to https://github.com/vst/accfifo
His code is released under the BSD License, and files containing it include the license text.

All other code released under AGPLv3.
