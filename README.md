# Cryptography

Examples and code on cryptographic systems

## What is a secure cipher? 

XOR message with key as big as message (One Time Pad). Defined by Claude Shannon.

## Block Ciphers

# SSL/TLS, Encryption, and XOR: Lecture Notes

## 🔐 SSL/TLS (Secure Sockets Layer / Transport Layer Security)

SSL/TLS is the protocol used to **secure web traffic** (e.g., HTTPS).

There are two main parts:

### 1. Handshake Protocol

* Establish a **shared secret key** using **public-key cryptography**

### 2. Record Layer

* Transmit data using the **shared secret key**
* Ensures:

  * 🔒 Confidentiality
  * 📦 Integrity

#### 🔀 Visual Overview:

```
Laptop  <------->  Server
   K                K
```

---

## 🔑 Symmetric Encryption

### Diagram

```
Alice                                   Bob
  m  ---> [ E ] ---> E(K, m) = c ---> [ D ] ---> D(K, c) = m
           ↑                             ↑
           K                             K
```

* **K** is the shared secret key (e.g., 128 bits)

### Key Concepts

1. ✅ The **encryption algorithm** is **publicly known**
2. ✅ `E` is the **encryption** function
3. ✅ `D` is the **decryption** function
4. ✅ The **only secret** is the key `K`

---

## 🧠 XOR Operation (Lecture 4)

### Concept

XOR means **one or the other, but not both**.

### Truth Table

| Input A | Input B | Output |
| ------- | ------- | ------ |
| 0       | 0       | 0      |
| 0       | 1       | 1      |
| 1       | 0       | 1      |
| 1       | 1       | 0      |

➡️ This forms the basis of simple encryption using XOR.

### Example

```
Plaintext:   10111101
Key:         00110010
---------------------
Ciphertext:  10001111

Decrypt using same key:

Ciphertext:  10001111
Key:         00110010
---------------------
Plaintext:   10111101
```

---

## 🔒 Secure Communication (SSL/TLS in Action)

### Example Scenario

```
Alice (Laptop)  <==== SSL/TLS ====>  Bob (Webserver)
```

### Notes:

* Use **SSL or TLS** to encrypt the data.

### Goals:

1. ✅ No eavesdropping → **Confidentiality**
2. ✅ No tampering → **Integrity**


---


# One-Time Pad (OTP), XOR, and Perfect Secrecy

## 🔁 XOR Refresher

**XOR (Exclusive OR)** means: one or the other, but not both.

### Truth Table

| A | B | A ⊕ B |
| - | - | ----- |
| 0 | 0 | 0     |
| 0 | 1 | 1     |
| 1 | 0 | 1     |
| 1 | 1 | 0     |

---

## 🔐 OTP Encryption/Decryption Example

### Encryption

```
Message :  0110111
Key     :  1011101
-------------------
Cipher  :  1101010
```

### Decryption

```
Cipher  :  1101010
Key     :  1011101
-------------------
Message :  0110111
```

### Equation

```
D(K, C) = K ⊕ C
```

---

## ❓ Quiz: Can You Compute the Key?

**Q:** Given a message `m` and its OTP-encrypted ciphertext `c`, can you compute the key?

### Options:

* ❌ A) No, I cannot compute the key
* ✅ B) Yes, the key is `K = m ⊕ c`
* ❌ C) I can only compute half of the key

### Solution:

```
K = m ⊕ c

m = 0110111
c = 1101110
------------
K = 1011001
```

---

## 🧠 What is Perfect Secrecy?

### Claude Shannon's Contribution

Claude Shannon analyzed the One-Time Pad and introduced the notion of **perfect secrecy**:

> A cipher `(E, D)` has perfect secrecy if:
>
> For all messages `m₀`, `m₁` in message space `M` and all ciphertexts `c`:
>
> `Pr[E(K, m₀) = c] = Pr[E(K, m₁) = c]`

### Meaning

* Given a ciphertext `c`, the probability it came from message `m₀` is the **same** as it coming from `m₁`
* So, ciphertext gives **no info** about the plaintext

### Sets and Notation

* `K ∈ 𝒦` = key space
* `M` = message space
* `C` = ciphertext space
* `K` is chosen **uniformly at random** from `𝒦`

---

## 🧩 Why Can't You Attack OTP?

If you are an attacker and you intercept `c`, the probability that `D(K, c) = m₀` is:

* **Exactly equal** to the probability that `D(K, c) = m₁`

So:

> If all you have is the ciphertext, you have **no information**.

There is **no ciphertext-only attack** possible.

---

## ⚠️ Shannon's Limitation

To have perfect secrecy:

```
length of key ≥ length of message
```

➡️ This is **not efficient** in most real-world use cases.

---

## ❓ Is the OTP Secure?

Yes — it is secure **in theory**, but impractical in many situations.

> Leads to a deeper question:
>
> **What is a good cipher?**

### From Information Theory (Shannon, \~1949)

> A good cipher reveals **no information** about the plaintext.

---

## 🧪 Symmetric Cipher Foundations

### Cryptography Core:

1. Secret key establishment
2. Secure communication using the key

### Cipher Definition:

A cipher is a pair of efficient algorithms `(E, D)`:

```
E(K, M) → C
D(K, C) → M
```

Satisfying:

```
D(K, E(K, M)) = M
```

---

## ⚙️ Randomized vs Deterministic

* `E`: Often **randomized** — uses random bits during encryption
* `D`: Always **deterministic** — produces same output every time

---

## 🧨 OTP Summary

* "OTP" = One-Time Pad (1917)
* Key = Random bitstring, same length as message
* Encryption:

```
C = K ⊕ M
```

---

## ✅ Pros and ❌ Cons of OTP

### ✅ Pros

* Super fast encryption/decryption

### ❌ Cons

* Requires **long keys** (same length as the message)
* Not practical:

  * If message is long, so is the key

---

# Lab 2 — Inverted Number Cipher & Message Integrity

## 🧪 Crypto Lab

* **Topic**: One-way Hash Functions and MAC
* **Objective**: Understand how to encrypt and decrypt messages by assigning inverted numbers to letters (A=26, ..., Z=1)

---

---

# Very Simple Hash Functions and Message Integrity

## 🔐 What Is a Hash Function?

A **cryptographic hash function** is:

* An algorithm that maps **data of variable length** to **data of fixed length**

### Properties and Uses:

* Hash functions are used to generate a **fixed-length digest** of input data
* The digest acts as a **shortened reference** to the original data
* Useful when data is too large to store or compare directly

### Example:

* A **hash table** is a data structure that uses hash functions

  * It maps **keys → values**

```
John Smith  → 01
Peter Chen  → 00
Jane Doe    → 02
```

---

## ⚙️ Simple Hash: XOR Hash Algorithm

### Section 15.4 — Simple Hash Functions

* Most hashing algorithms process the **message as a sequence of n-bit blocks**
* The message is processed **one block at a time**, iteratively
* The **simplest** hash function uses XOR:

> Start with the first `n`-bit block → XOR with the second → XOR the result with the third → …

This produces the **XOR hash code**.

### Effect:

* Each bit in the hash code is the **parity** of that bit position across all blocks
* Also known as a **longitudinal parity check**

### Use Case:

* This can be used as a **data integrity check** for detecting **random transmission errors**
* ⚠️ However, it’s not secure against **intentional tampering**

---

## ✅ Message Integrity with MAC

### Goals:

1. Ensure files **have not been altered**
2. Provide a **Message Authentication Code (MAC)**

### MAC Diagram:

```
  Alice                           Bob
   |                               |
   |--- message m, tag --------->  |
   |                               |
```

* `MAC` = Message Authentication Code
* The tag is **100 bits or so**

### How It Works:

* Alice computes: `tag = S(K, m)` using a **signing algorithm S()**
* Bob verifies: `V(K, m, tag)` using a **verification algorithm V() → yes/no**

---

## 🛠️ MAC Implementation Options

MAC algorithms can be built from other cryptographic primitives:

1. **Cryptographic hash functions**
2. **Block cipher algorithms**

These enable construction of robust MACs with desired security properties for integrity verification.

---

## Summary

* Hash functions map long data to fixed-size digests
* Simple XOR-based hashes are useful for error detection, but not secure
* Message integrity is achieved using MACs
* MACs depend on secret keys and secure algorithms for verification

---

# Toy AES Cipher: SubBytes and ShiftRows Explained

This document explains the **core ideas of AES encryption** as implemented in a simplified (toy) Python version using 8-byte blocks. The main focus is on the two critical AES transformations:

* `SubBytes` (non-linear substitution)
* `ShiftRows` (byte permutation)

---

## 1. SubBytes (S-Box Substitution)

Each byte of the block is replaced using a substitution box (S-Box), which maps values in a non-linear way.

### Toy S-Box Used:

```text
Index → SBOX value
  0   →   6
  1   →   4
  2   →  12
  3   →   5
  4   →   0
  5   →   7
  6   →   2
  7   →  14
  8   →   1
  9   →  15
 10   →   3
 11   →  13
 12   →   8
 13   →  10
 14   →   9
 15   →  11
```

### Example:

```python
input_block = [0, 1, 2, 3, 4, 5, 6, 7]
sub_bytes(input_block) → [6, 4, 12, 5, 0, 7, 2, 14]
```

> Each number is replaced using the S-Box based on its value.

---

## 2. ShiftRows (Byte Permutation)

In real AES, this step shifts rows of the state matrix. In this toy version, we simulate it with a hardcoded reordering.

### Input After SubBytes:

```python
block = [6, 4, 12, 5, 0, 7, 2, 14]
```

### Toy ShiftRows Implementation:

```python
shifted = [
    block[0], block[5], block[2], block[7],
    block[4], block[1], block[6], block[3]
]
```

### Result:

```python
shifted = [6, 7, 12, 14, 0, 4, 2, 5]
```

> This shuffles the bytes to simulate the AES row shifts, increasing diffusion.

---

## Summary Table

| Step          | What It Does      | Example Input         | Example Output        |
| ------------- | ----------------- | --------------------- | --------------------- |
| **SubBytes**  | Replace via S-Box | `[0,1,2,3,...]`       | `[6,4,12,5,...]`      |
| **ShiftRows** | Shuffle positions | `[6,4,12,5,0,7,2,14]` | `[6,7,12,14,0,4,2,5]` |

These steps give AES its strength:

* **SubBytes** → confusion (non-linearity)
* **ShiftRows** → diffusion (spreading input influence)

---

## Next Step

To complete the toy AES model, you can add:

* AddRoundKey (XOR with round key)
* Multiple rounds
* MixColumns (optional for stronger diffusion)

This toy model helps build intuition before working with full 128-bit AES.



---

## OpenSSL

* openssl lets you generate RSA keys as short as 31 bits
* $ openssl genrsa 31
* $ openssl s_client -connect www.google.com:443
* ECC can be faster than RSA because it uses smaller numbers
* $ openssl speed ecdsap256 rsa4096

## TLS

* The protocol of SSL
* TLS stands for Transport Layer Security
* Current TLS version is around TLS 1.3
* TLS protocol handles the hand shake and the packet formatting for secure encapsulation of data
* The handshake relies on certificates and certificate authorities
* $ openssl s_client -connect www.google.com:443

## Is there any particular reason to use Diffie-Hellman over RSA for key exchange in TLS 1.3?

* ANSWER: Forward Secrecy
* TLS 1.3 uses an elliptic curve based Diffie Hellman approach
* Diffie-Hellman defines a key exchange mechanism that allows a client and a server to exchange secret keys in the presence of an eavesdropper
* In a TLS connection using the Diffie-Hellman key exchange, for every new connection from a client, the server typically generates a fresh Diffie-Hellman public-private key pair that is used to exchange keys for that session
* These are known as ephemeral key pairs
* The server’s long-term private key is only used to authenticate the server’s Diffie-Hellman public key (the ephemeral public key)
* Thus, if an attacker compromises the server’s long-term private key, they can impersonate the server but not be able to decrypt any previously encrypted communication
* SINCE The server’s private key was never used as part of the key-exchange (other than simply signing the ephemeral public keys)
* The Diffie-Hellman private keys that were used to compute the session keys are ephemeral
* i.e short lived for the duration of the handshake with that client and then discarded
* NOTE: Ephemeral Diffie-Hellman ciphers take the form TLS_DHE_ / TLS_ECDHE_ unlike their static Diffie-Hellman counterparts that take the form TLS_DH_/TLS_ECDH_
* In contrast, if you consider the RSA handshake in TLS, the client encrypts a random symmetric key to the server’s public key and the server uses it’s private key to decrypt and recover the symmetric key.
* This allows an attacker to passively observe and store encrypted network traffic (which used RSA key exchange for TLS communication)
* If the server’s private key is compromised, then the attacker can retrospectively decrypt the stored encrypted communication
* (since the session keys were encrypted to the server’s public key)
* The RSA key exchange is quite straightforward; the client generates a secret (a 46byte random number), encrypts it with the server’s public key, and sends it in the ClientKeyExchange message.
* To obtain the  secret, the server only needs to decrypt the message.
* The simplicity of the RSA key exchange is also its principal weakness.
* The  secret is encrypted with the server’s public key, which usually remains in use for several years.
* Anyone with access to the corresponding private key can recover the secret and construct the same secret, compromising session security.
* On Diffie-Hellman (DH) key exchange is a key agreement protocol that allows two parties to establish a shared secret over an insecure communication channel.
* The DH key exchange requires six parameters; two (dh_p and dh_g) are called domain parameters and are selected by the server.
* During the negotiation, the client and server each generate two additional parameters.
* Each side sends one of its parameters (dh_Ys and dh_Yc) to the other end, and, with some calculation, they arrive at the shared key.
* Diffie-Hellman (DH) key exchange is better than RSA because the two parties generate the new key together 
