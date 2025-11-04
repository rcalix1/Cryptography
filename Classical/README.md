## Pre-Modern Ciphers


## 🔄 Inverted Number Cipher — Concept

Convert lowercase letters `a-z` to numbers in **reversed order**:

```
a → 26
b → 25
c → 24
...
z → 1
```

To encrypt:

* Convert each character to lowercase
* For each character `ch` in the text:

  * Convert to ASCII: `n = ord(ch)`
  * Subtract base: `n1 = n - 96`
  * Encrypt: `code = 27 - n1`

To decrypt:

* Every two-digit number becomes a letter:

  * `code = int(num)`
  * `ascii = 96 + (27 - code)`
  * `char = chr(ascii)`

---

## 🧮 Encryption Example

**Plaintext**:

```
"this is the department of cs at lsu"
```

**Key Mapping Rule**: Reverse alphabet order

**Cipher Text (Numbers)**:

```
(7)(19)(18)(8)(8)(18)(8)(23)(22)(11)(26)(9)(7)(14)(22)(13)(7)(12)(21)(24)(8)(26)(7)(15)(8)(6)
```

---

## 🔓 Decryption

To decrypt, reverse the above steps:

* Take each group of 2 digits
* Apply `char = chr(96 + (27 - int(num)))`

**Decrypted Text (no spaces)**:

```
thisisdepartmentofcsatlsu
```

After grouping:

```
"this is the department of cs at lsu"
```

---

## 💻 Sample Pseudocode (EncryptPhrase)

```vb.net
Function EncryptPhrase(text)
  Set ss to zero length string
  Set text equal to all lowercase letters

  If text is not numeric then
    For each character in text
      Set a equal to text at position
      Set n1 equal to ASCII number of a
      Set code equal to 27 - (n1 - 96)
      If code < 10 then
        Set scode = '0' + code
      Else
        Set scode = code
      Concatenate scode with ss
  Else
    Set yy equal to 0
    Set foo equal to zero length string
    For each character in text
      Concatenate foo with foo and text at i
      If yy == 1 then
        Set yy = 0
        Set code = 96 + (27 - foo)
        Set foo = ""
        Set scode = chr(code)
        Concatenate ss with scode
      Else
        Increment yy by 1

Return ss
```

---

## 🐍 Python Equivalent (EncryptPhrase)

```python
def EncryptPhrase(text):
    ss = ""
    text = text.lower()

    if not text.isdigit():
        for i in range(len(text)):
            a = text[i]
            n1 = ord(a)
            code = 27 - (n1 - 96)
            scode = '0' + str(code) if code < 10 else str(code)
            ss += scode
    else:
        yy = 0
        foo = ""
        for i in range(len(text)):
            foo += text[i]
            if yy == 1:
                yy = 0
                code = 96 + (27 - int(foo))
                scode = chr(code)
                foo = ""
                ss += scode
            else:
                yy += 1
    return ss
```

---

## 🧠 Summary

* This cipher teaches reversible encryption using basic ASCII manipulation
* Key concept: inverse mapping of alphabets (A=26 to Z=1)
* Can be implemented in any language (VB.NET, Python, etc.)
* Message integrity is preserved since exact reversibility is enforced

---

## ✅ Outputs From Sample Code

```vb.net
Main Subroutine

  s1 = "this is the department of cs at lsu"
  s2 = "07190808180823221126090714221307122124081226071508"

  result = EncryptPhrase(s1)
  result2 = EncryptPhrase(s2)

  print result
  print result2
```

Expected output (after print):

```
07190808180823221126090714221307122124081226071508
thisisthedepartmentofcsatlsu
```

---

## 🧩 Educational Use

This lab is suitable for:

* Week 2 crypto exercises
* Introducing ASCII encoding
* Understanding symmetric encryption
* Practicing string manipulation
* Discussing message integrity

Let students figure out the mapping, inversion, and decoding logic to reinforce understanding.

