# Pycards

[![Build Status](https://travis-ci.org/MrLucasCardoso/pycards.svg?branch=master)](https://travis-ci.org/MrLucasCardoso/pycards)  [![Code Health](https://landscape.io/github/MrLucasCardoso/pycards/master/landscape.svg?style=flat)](https://landscape.io/github/MrLucasCardoso/pycards/master) [![Coverage Status](https://coveralls.io/repos/github/MrLucasCardoso/pycards/badge.svg?branch=master)](https://coveralls.io/github/MrLucasCardoso/pycards?branch=master)

Set of classes for validating, identifying and formatting do credit cards and debit cards.

```shell
$ pip install python-cards
```

#### Example

```python
from pycards import CreditCard

card = CreditCard(number='375371850275506',
                  cardholder='Charles Smith',
                  expire_month='3',
                  expire_year='2017',
                  code=2887)

if card.is_valid:

    print(card.brand)         # Amex
    print(card.cardholder)    # Charles Smith
    print(card.number)        # 375371850275506
    print('Expires: {} ({})'  # Expires: 03/17 (2017-03-01)
          .format(card.expires_string, card.expires))
    print('{}: {}'            # CVV: 2887
          .format(card.code_name, card.code))
    if card.is_expired:
        print('EXPIRED')      # EXPIRED
```

**Note:** Debit cards not avaliable yet.

### Supported Cards

 * Visa -> Visa
 * American Expiress -> Amex
 * Mastercard -> Master
 * Discover -> Discover
 * Diners Club -> Diners 
 * JCB (Japan Credit Bureau) -> JCB
 * Aura -> Aura
 * ELO -> Elo
