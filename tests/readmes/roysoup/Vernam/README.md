---
# Vernam 2.4.3

### Synopsis
A simple vernam (or OTP) encryption / decription program in python

---
### Code Example
Encode message "super_secret_message" with key "very_secret_key", store in variable "encoded", and print as a list.
~~~
>>> encoded = vernam("super_secret_message", "very_secret_key")
>>> print( encoded )
~~~

Decode message stored in variable "encoded" with key "very_secret_key", store in variable "decoded", and print as a string.
~~~
>>> decoded = vernam(encoded, "very_secret_key")
>>> print( "".join(decoded) )
~~~
---
### Installation
Install:
~~~
>>> $ pip install vernam
~~~
Import:
~~~
>>> $ from vernam import vernam
~~~
---
### CLI Usage
~~~
vernam <message> <key>
~~~
---
### License
[MIT Licence](https://choosealicense.com/licenses/mit/#)

---