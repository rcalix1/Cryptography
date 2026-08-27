# Cryptography

Examples and code on cryptographic systems

* link 

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
