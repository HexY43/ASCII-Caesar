## Introduction
### ASCII Caesar Cipher
This algorithm is a simple **substitution** cipher that replaces each letter in a message with a letter in some fixed position in the ASCII table depending on the provided key.

### How does it work?
Convert each letter in the message to its corresponding ASCII value and eliminate the offset by subtracting $32$ and add it to a list, then:
$$
\left(Ciphertext = (Coresponding \;ASCII + Key) \% 91 + 32\right) \\
Plaintext = (Coresponding \;ASCII - Key) \% 91 + 32
$$
Notice that we are adding back the offset of $32$ after dealing with the ASCII value.

### Usage and use cases
1. Ecrypting a message (plaintext) using a specific key
```python
python ascii_caesar.py -e "MESSAGE" -k KEY
# Key is an integer between 32 and 132
```
2. Decrypting a message (ciphertext) using a specific key
```python
python ascii_caesar.py -d "MESSAGE" -k KEY
# Key is an integer between 32 and 132
```
3. Bruteforcing a ciphertext to find the key
```python
python ascii_caesar.py -b "MESSAGE"
```

### Limitations
1. If your message contains double quotes **and/or backticks (`)**, please wrap the message in single quotes:
```python
# Example: Encrpyting a message that contains a double quote
# Message to encrypt: "A KIND WORD IS A FORM OF CHARITY."

python ascii_caesar.py -e '"A KIND WORD IS A FORM OF CHARITY."' -k 100
```
```python
# Example: Decrypting a message that contains a backtick (`)
# Message to decrypt: 9MJWJ`NX`STYMNSL`MJF[NJW`NS`YMJ`XHFQJX`YMFS`LTTI`HMFWFHYJW

# Using a specific key
python ascii_caesar.py -d '9MJWJ`NX`STYMNSL`MJF[NJW`NS`YMJ`XHFQJX`YMFS`LTTI`HMFWFHYJW' -k 64
# Bruteforcing
python ascii_caesar.py -b '9MJWJ`NX`STYMNSL`MJF[NJW`NS`YMJ`XHFQJX`YMFS`LTTI`HMFWFHYJW'
```
2. If your message contains a single quote, please wrap the message in double quotes:
```python
# Example: Encrpyting a message that contains a single quote
# Message to encrypt: I head Allah's Messenger (Peace and Blessings Be Upon Him) saying regarding Ramadan: Whoever prayed at night in it (the month of Ramadan) out of sincere Faith and hoping for a reward from Allah, then all his previous sins will be forgiven.

python ascii_caesar.py -e "I head Allah's Messenger (Peace and Blessings Be Upon Him) saying regarding Ramadan: Whoever prayed at night in it (the month of Ramadan) out of sincere Faith and hoping for a reward from Allah, then all his previous sins will be forgiven." -k 32
```
```python
# Example: Decrypting a message that contains a single quote
# Message to decrypt: z'3+4A/9A2/9:+:/4/4-A:5Az'99+8H9A56/4/54

# Using a specific key
python ascii_caesar.py -d "z'3+4A/9A2/9:+:/4/4-A:5Az'99+8H9A56/4/54" -k 33
# Bruteforcing
python ascii_caesar.py -b "z'3+4A/9A2/9:+:/4/4-A:5Az'99+8H9A56/4/54"
```
3. **If your message contains a double qoute and a single quote and/or backticks, the algorithm will sadly not work. :((**