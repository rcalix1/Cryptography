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

# Stream Ciphers

## Symmetric Encryption

### Stream Ciphers

1. Making the **one-time pad (OTP)** practical.

2. The idea in the **stream cipher** is to replace the totally random key with a **pseudorandom key**.

A **PRG (Pseudorandom Generator)** is a function `G` that takes a short seed and generates a much longer pseudorandom sequence.

**G: {0,1}^s → {0,1}^n**

where `s` is the length of the seed and `n` is much larger than `s`:

**n >> s**

The generator `G` must be **efficiently computable**.

The function `G` is deterministic; only the **seed** is random.

---

## How the Pseudorandom Generator Is Used

The seed, which is short, is the key `K`.

The generator `G` expands the seed:

**K → G(K)**

This produces the pseudorandom sequence.

We then XOR the pseudorandom sequence with the message:

**c = m ⊕ G(K)**

So the encryption and decryption functions are:

**c = E(K,m) := m ⊕ G(K)**

**D(K,c) := c ⊕ G(K)**

Since XORing twice with the same value cancels it:

**m = c ⊕ G(K)**

---

## Stream Cipher Encryption and Decryption

Encryption itself is as simple as it can be. You just XOR the byte from the pseudorandom stream with the plaintext byte to get the encrypted byte.

You generate the same pseudorandom byte stream for decryption. The decryption itself consists of XORing the received byte with the pseudorandom byte.

Encryption:

**c = m ⊕ G(K)**

Decryption:

**m = c ⊕ G(K)**

---

## Security Warning: Reusing the Same Key

* Key Stream Re-use Attack

WEP has used stream ciphers such as this. The implementation was incorrect and therefore it is insecure.

If you have two ciphertexts generated with the same key:

**C₁ = m₁ ⊕ PRG(K)**

**C₂ = m₂ ⊕ PRG(K)**

XOR the two ciphertexts:

**C₁ ⊕ C₂**

Then:

**C₁ ⊕ C₂ = (m₁ ⊕ PRG(K)) ⊕ (m₂ ⊕ PRG(K))**

Because:

**PRG(K) ⊕ PRG(K) = 0**

we obtain:

**C₁ ⊕ C₂ = m₁ ⊕ m₂**

This leaks information about the plaintexts and can allow the cipher to be broken.

---

# Message Integrity

Make sure the files/messages have not been changed.

The basic approach is to provide a **MAC**.

**MAC = Message Authentication Code**

Alice and Bob share a key `K`.

Alice uses a MAC signing algorithm, denoted by `S()`:

**tag ← S(K,m)**

Alice sends the message `m` along with the tag.

Bob uses a MAC verification algorithm `V()`.

Bob verifies:

**V(K,m,tag) = yes or no**

---

# Cryptographic Hash Functions

A **hash function** is an algorithm that maps data of **variable length** to data of a **fixed length**.

Hash functions are primarily used to generate fixed-length output data that acts as a shortened reference to the original data.

This is useful when the original data is too cumbersome to use in its entirety.

A **hash table** is an example.

A hash table is a data structure used to implement an associative array. It maps **keys to values**.

Example:

    John Smith   → 01
    Peter Chen   → 00
    Gerald Knapp → 02

---

## Simple Hash Functions

Practically all algorithms for computing the hash code of a message view the message as a sequence of **n-bit blocks**.

The message is processed one block at a time in an iterative fashion to produce an **n-bit hash code**.

Perhaps the simplest hash function consists of starting with the first n-bit block, XORing it bit-by-bit with the second n-bit block, XORing the result with the next n-bit block, and so on.

We will refer to this as the **XOR hash algorithm**.

---

# XOR

XOR means **one or the other, but not both**.

| A | B | A XOR B |
|---|---|---------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

Example:

    Plaintext:   10111101
    Key:         00110010
                 --------
    Ciphertext:  10001111

To decrypt, XOR the ciphertext with the same key:

    Ciphertext:  10001111
    Key:         00110010
                 --------
    Plaintext:   10111101

---




# Block Ciphers

Block ciphers encrypt data by dividing a message into blocks of a fixed size. Each plaintext block is transformed into a corresponding ciphertext block.

## Procedure for Block Ciphers

When a block cipher is used to encrypt a long message, the message is first divided into blocks of the correct length.

For example:

```text
Plaintext:

[ Block 1 ][ Block 2 ][ Block 3 ] ... [ Block n ]
```

If the last block is only partially filled, padding is added so that it has the required block length.

The block cipher then uses a chosen mode of operation to determine how the individual blocks are encrypted.

## Modes of Operation

There are different ways of breaking up and encrypting a message. These are called **modes of operation**.

One example is **Electronic Codebook (ECB)**.

## Electronic Codebook (ECB)

In Electronic Codebook mode, each plaintext block is encrypted independently.

```text
Plaintext:

[   ][   ][ m1 ][   ][ m2 ]
              |           |
              v           v
Ciphertext:

[   ][   ][ c1 ][   ][ c2 ]
```

An important property of ECB is:

$$
m_1 = m_2 \quad \Rightarrow \quad c_1 = c_2
$$

If two plaintext blocks contain the same data, they produce the same ciphertext.

For example:

```text
Plaintext:

[    ][ READ ][    ][    ][ READ ][    ]

Ciphertext:

[    ][ #XR37 ][    ][    ][ #XR37 ][    ]
```

Since

$$
m_1 = m_2
$$

then

$$
c_1 = c_2
$$

This means that an attacker may be able to learn something about the original message even without decrypting the ciphertext.

## Patterns in ECB

Suppose the plaintext represents an image containing repeated blocks.

```text
+---+---+---+---+---+
|   |   |   |   |   |
+---+---+---+---+---+
|   | X | X | X |   |
+---+---+---+---+---+
|   |   |   | X |   |
+---+---+---+---+---+
|   |   |   | X |   |
+---+---+---+---+---+
|   |   |   | X |   |
+---+---+---+---+---+
```

After ECB encryption, the values contained in the blocks change, but identical plaintext blocks still produce identical ciphertext blocks.

```text
+---+---+---+---+---+
|   |   |   |   |   |
+---+---+---+---+---+
|   |111|111|111|   |
+---+---+---+---+---+
|   |   |   |111|   |
+---+---+---+---+---+
|   |   |   |111|   |
+---+---+---+---+---+
|   |   |   |111|   |
+---+---+---+---+---+
```

Therefore, the **pattern may persist** in the encrypted data.

This is an important weakness of Electronic Codebook mode.

## Accessibility

The block cipher diagrams are represented using text so that their meaning does not depend on images, color, or visual appearance. The essential information represented by each diagram is also described in the surrounding text.



---




## Cipher Block Chaining (CBC)

In order to encrypt messages that are longer than the block size, different modes of operation can be used.

One important mode is **Cipher Block Chaining (CBC)**.

In CBC, the plaintext is divided into blocks. Each plaintext block is XORed with the ciphertext from the previous block before being encrypted.

The first plaintext block does not have a previous ciphertext block. Therefore, an **Initialization Vector (IV)** is used.

Conceptually:

```text
                 Plaintext 1
                     |
IV ---------------- XOR
                     |
                     v
Key ----------> [ Block Cipher ]
                     |
                     v
               Ciphertext 1
                     |
                     +--------------------+
                                          |
                                    Plaintext 2
                                          |
                                         XOR
                                          |
                                          v
Key ------------------------------> [ Block Cipher ]
                                          |
                                          v
                                    Ciphertext 2
                                          |
                                          +--------------------+
                                                               |
                                                         Plaintext 3
                                                               |
                                                              XOR
                                                               |
                                                               v
Key ---------------------------------------------------> [ Block Cipher ]
                                                               |
                                                               v
                                                         Ciphertext 3
```

The CBC encryption process can be represented mathematically as

$$
C_1 = E_K(P_1 \oplus IV)
$$

and for the remaining blocks,

$$
C_i = E_K(P_i \oplus C_{i-1})
$$

where:

- $P_i$ is the current plaintext block.
- $C_i$ is the current ciphertext block.
- $C_{i-1}$ is the previous ciphertext block.
- $E_K$ represents encryption using key $K$.
- $\oplus$ represents the XOR operation.
- $IV$ is the Initialization Vector.

The use of the IV and the previous ciphertext block helps prevent identical plaintext blocks from producing identical ciphertext blocks.

---

## Cipher Feedback (CFB) Mode

Another mode of operation is **Cipher Feedback (CFB)** mode.

CFB is similar to CBC, but it uses a block cipher to create a **self-synchronizing stream cipher**.

Instead of XORing the plaintext with the previous ciphertext before block encryption, the previous ciphertext is encrypted first. The result is then XORed with the plaintext.

For the first block, the Initialization Vector is encrypted:

```text
        Initialization Vector
                 |
                 v
Key ------> [ Block Cipher ]
                 |
                 v
Plaintext 1 ---> XOR
                 |
                 v
            Ciphertext 1
                 |
                 +-------------------+
                                     |
                                     v
Key -------------------------> [ Block Cipher ]
                                     |
                                     v
Plaintext 2 -----------------------> XOR
                                     |
                                     v
                                Ciphertext 2
                                     |
                                     +-------------------+
                                                         |
                                                         v
Key --------------------------------------------> [ Block Cipher ]
                                                         |
                                                         v
Plaintext 3 -------------------------------------------> XOR
                                                         |
                                                         v
                                                    Ciphertext 3
```

The CFB encryption process can be represented as

$$
C_1 = P_1 \oplus E_K(IV)
$$

and for subsequent blocks,

$$
C_i = P_i \oplus E_K(C_{i-1})
$$

where:

- $P_i$ is the plaintext block.
- $C_i$ is the ciphertext block.
- $C_{i-1}$ is the previous ciphertext block.
- $E_K$ represents encryption using key $K$.
- $\oplus$ represents the XOR operation.
- $IV$ is the Initialization Vector.

Because the previous ciphertext is fed back into the encryption process, CFB is called **Cipher Feedback mode**.

---


# Block Ciphers

A **block cipher** maps a fixed number of input bits to a fixed number of output bits.

Conceptually:

```text
 n bits of input  ----->  n bits of output
```

A plaintext block is processed by a block cipher encryption algorithm using a key:

```text
                         Key
                          |
                          v
Plaintext Block ---> [ Encryption ] ---> Ciphertext Block
     n bits                               n bits
```

The size of the key does not necessarily have to be the same as the block size.

## Classic Examples

Two classic examples of block ciphers are **3DES** and **AES**.

### 3DES

3DES uses a block size of

$$
n = 64 \text{ bits}
$$

and can use a key size of

$$
K = 168 \text{ bits}.
$$

### AES

AES uses a block size of

$$
n = 128 \text{ bits}
$$

and supports key sizes of

$$
K = 128,\ 192,\ \text{or}\ 256 \text{ bits}.
$$

---

# How Block Ciphers Work

Block ciphers are typically built using a sequence of **iterations**, often called **rounds**.

## Step 1: Start With a Key

We begin with a key $K$.

For example, AES may use a 128-bit key:

$$
K = 128 \text{ bits}.
$$

## Step 2: Generate Round Keys

The original key is expanded into a sequence of keys called **round keys**.

Conceptually:

```text
                         Key K
                           |
          +----------------+----------------+
          |                |                |
          v                v                v
         K1               K2               K3       ...       Kn
```

This process is commonly called the **key expansion** or **key schedule**.

## Step 3: Apply the Round Function

The message is encrypted through a sequence of rounds.

Let the round function be represented by

$$
R(K_i,m_i)
$$

where the inputs are:

- $K_i$ — the current round key
- $m_i$ — the current state of the message

The output of one round becomes the input to the next round.

Conceptually:

```text
              K1          K2          K3                    Kn
               |           |           |                     |
               v           v           v                     v
Message ---> [ R ] ---> [ R ] ---> [ R ] ---> ... ---> [ R ] ---> Ciphertext
               |           |           |
              m1          m2          m3
```

Therefore, encryption consists of repeatedly transforming the current state of the message using the appropriate round key.

---

# AES Example

For AES, the message is divided into blocks of **128 bits**.

For example:

```text
Message:

+----------------+----------------+----------------+
|    Block 1     |    Block 2     |    Block 3     |
|    128 bits    |    128 bits    |    128 bits    |
+----------------+----------------+----------------+
```

Each 128-bit block is then processed by AES.

The original key $K$ is expanded into a sequence of round keys:

```text
                         Key K
                           |
       +-------------------+-------------------+
       |                   |                   |
       v                   v                   v
      K1                  K2                  K3       ...       Kn
       |                   |                   |                  |
       v                   v                   v                  v
m --> [R(K1,m)] --> m1 --> [R(K2,m1)] --> m2 --> ... --> [R(Kn,mn)] --> C
```

Here:

- $m$ is the original 128-bit plaintext block.
- $m_1,m_2,\ldots$ represent intermediate states of the message.
- $K_1,K_2,\ldots,K_n$ are the round keys.
- $R$ represents the round transformation.
- $C$ is the final 128-bit ciphertext block.

The important idea is that AES does not transform the plaintext into ciphertext in a single operation. Instead, it performs a sequence of transformations using different round keys derived from the original key.

---



# Data Encryption Standard (DES)

**DES** stands for **Data Encryption Standard**.

DES is an important historical example of a block cipher.

The basic structure of a block cipher can be represented as:

```text
                         Key
                          |
                          v
Plaintext Block ---> [ Encryption ] ---> Ciphertext Block
     n bits                               n bits
```

The plaintext block and ciphertext block contain the same number of bits.

DES was developed in the 1970s based on work at IBM. In 1997, DES was broken through exhaustive key search. DES was eventually replaced as a standard by AES.

---

# DES and Feistel Networks

The basic idea behind DES is to build a **Feistel Network**.

Suppose we have a collection of round functions

$$
f_1,f_2,\ldots,f_d
$$

that map bit strings to bit strings.

The input block is divided into two parts:

$$
L_0
$$

and

$$
R_0
$$

representing the left and right halves of the input.

Conceptually, the Feistel network consists of a sequence of rounds:

```text
             Round 1           Round 2                    Round d

 L0 -----------+------------------+--------------------------+
               |                  |
               |                 ...
               v
              [f1]
               |
               v
 R0 ---------> XOR
               |
               +-------> R1

 R0 -------------------> L1
```

The process is repeated for multiple rounds.

For each round $i=1,\ldots,d$:

$$
L_i = R_{i-1}
$$

and

$$
R_i = f_i(R_{i-1}) \oplus L_{i-1}
$$

where $\oplus$ represents the XOR operation.

Thus, the right side from the previous round becomes the new left side:

$$
L_i = R_{i-1}
$$

while the new right side is produced by applying the round function to the previous right side and XORing the result with the previous left side:

$$
R_i = f_i(R_{i-1}) \oplus L_{i-1}.
$$

Conceptually:

```text
             Ri-1
              |
       +------+------+
       |             |
       |             v
       |          [ fi ]
       |             |
       |             v
       |            XOR <----- Li-1
       |             |
       |             v
       |             Ri
       |
       +------------------------> Li
```

The important relationships are therefore:

$$
L_i = R_{i-1}
$$

$$
R_i = f_i(R_{i-1}) \oplus L_{i-1}
$$

---

## Inverting a Feistel Round

An important property of the Feistel structure is that the process can be inverted.

From

$$
L_{i+1}=R_i
$$

we immediately obtain

$$
R_i=L_{i+1}.
$$

The forward equation is

$$
R_{i+1}=f_{i+1}(R_i)\oplus L_i.
$$

Therefore, we can recover the previous left side:

$$
L_i=f_{i+1}(L_{i+1})\oplus R_{i+1}.
$$

So the inverse relationships are:

$$
R_i=L_{i+1}
$$

and

$$
L_i=f_{i+1}(L_{i+1})\oplus R_{i+1}.
$$

This is an important feature of the Feistel network: **the round function itself does not need to be invertible for the overall Feistel structure to be invertible.**

## Accessibility

The DES and Feistel network diagrams are represented using text and are also described using equations and surrounding text. The material therefore does not depend on images, color, or visual position alone to communicate the encryption process.


---




# DES Implementation

DES uses a **64-bit input block** and a **16-round Feistel network**.

The 64-bit input is divided into two 32-bit halves:

```text
             64-bit Input
                  |
          +-------+-------+
          |               |
       32 bits          32 bits
          |               |
          +-------+-------+
                  |
                  v
        [ 16-Round Feistel Network ]
                  |
                  v
             64-bit Output
```

For DES, the round functions can be represented as

$$
f_1,\ldots,f_{16}.
$$

Each round operates on the two 32-bit halves of the current state.

---

# DES Round Function

A major component of DES is the round function $f$.

The round function receives:

- a **32-bit** input
- a **48-bit** round key

and produces a **32-bit** output.

Conceptually:

```text
32-bit input
     |
     v
[ Expansion ]
     |
     v
48 bits ----------------+
                        |
                        v
                     [ XOR ] <----- 48-bit Round Key
                        |
                        v
                    48 bits
                        |
                        v
                  [ S-Boxes ]
                        |
                        v
                    32 bits
```

## Expansion

The 32-bit input is first expanded to 48 bits.

$$
32\text{ bits} \rightarrow 48\text{ bits}
$$

This expansion is performed by rearranging and repeating some of the input bits.

The resulting 48-bit value is then XORed with the 48-bit round key:

$$
E(R) \oplus K_i
$$

where:

- $R$ is the 32-bit input to the round function
- $E(R)$ is the expanded 48-bit value
- $K_i$ is the 48-bit round key for round $i$

---

# S-Boxes

The resulting 48 bits are divided into eight groups of 6 bits.

```text
48 bits

+------+------+------+------+------+------+------+------+
| 6 bit| 6 bit| 6 bit| 6 bit| 6 bit| 6 bit| 6 bit| 6 bit|
+------+------+------+------+------+------+------+------+
   |      |      |      |      |      |      |      |
   v      v      v      v      v      v      v      v
  [S1]   [S2]   [S3]   [S4]   [S5]   [S6]   [S7]   [S8]
   |      |      |      |      |      |      |      |
 4 bits 4 bits 4 bits 4 bits 4 bits 4 bits 4 bits 4 bits
   |      |      |      |      |      |      |      |
   +------+------+------+------+------+------+------+
                         |
                         v
                      32 bits
```

Each **S-box** maps 6 bits to 4 bits:

$$
S_i:\{0,1\}^6 \rightarrow \{0,1\}^4.
$$

The eight S-boxes therefore transform

$$
48\text{ bits} \rightarrow 32\text{ bits}.
$$

The S-box functions are implemented using lookup tables.

## S-Box Lookup Example

For a 6-bit input, the **outer two bits** determine the row of the S-box table, while the **middle four bits** determine the column.

For example, consider:

```text
0 1101 1
| ---- |
|   |  |
+---|--+----> outer bits
    |
    +-------> middle four bits
```

The outer bits are

```text
01
```

and the middle four bits are

```text
1101
```

These values identify a location in the S-box lookup table.

For example, if that location contains

```text
1001
```

then the mapping is

$$
011011 \rightarrow 1001.
$$

Thus, a 6-bit input to an S-box produces a 4-bit output.

The outputs from all eight S-boxes are combined to produce the 32-bit result used by the DES round function.

---



# Triple DES (3DES)

The relatively small key size of DES eventually made exhaustive key searches practical. One approach to extending the useful life of DES was to increase the effective key size by applying DES multiple times.

This approach is called **Triple DES (3DES)**.

3DES uses three DES operations with three keys:

$$
K_1,\ K_2,\ K_3
$$

For a plaintext message $m$, 3DES can be represented as

$$
3E((K_1,K_2,K_3),m) = E(K_1,D(K_2,E(K_3,m)))
$$

In other words:

```text
                            K3             K2             K1
                             |              |              |
                             v              v              v
Plaintext m ------------> [ E ] --------> [ D ] --------> [ E ] --------> Ciphertext
```

where:

- $E$ represents DES encryption.
- $D$ represents DES decryption.
- $K_1$, $K_2$, and $K_3$ are the DES keys.

The use of multiple DES operations increases the effective key size, but it also makes the process significantly slower than a single DES operation.

---

# Advanced Encryption Standard (AES)

**AES** stands for **Advanced Encryption Standard**.

DES eventually became too vulnerable to exhaustive key searches, creating the need for a new encryption standard.

AES was selected through a competition organized by NIST. The winning algorithm was **Rijndael**, designed by Joan Daemen and Vincent Rijmen.

AES uses a fixed block size of

$$
128\text{ bits}.
$$

AES supports three key sizes:

$$
128,\ 192,\ \text{and}\ 256\text{ bits}.
$$

A larger key provides a larger possible key space.

---

# Basic AES Structure

AES operates on a 128-bit block of data.

The input is represented as a matrix of bytes called the **state**.

Encryption consists of a sequence of rounds. The exact number of rounds depends on the key size:

- 128-bit key: 10 rounds
- 192-bit key: 12 rounds
- 256-bit key: 14 rounds

The original encryption key is expanded into a sequence of **round keys**.

Conceptually:

```text
128-bit Plaintext
       |
       v
+----------------+
|      State     |
+----------------+
       |
       | XOR Round Key
       v
+----------------+
|    AES Round   |
+----------------+
       |
       | XOR Round Key
       v
+----------------+
|    AES Round   |
+----------------+
       |
      ...
       |
       v
+----------------+
|  Final Round   |
+----------------+
       |
       v
128-bit Ciphertext
```

Each round changes the state so that the bits of the original plaintext become increasingly mixed throughout the block.

Two important ideas used throughout AES are:

1. **Substitution**
2. **Permutation**

These operations are repeatedly applied across the rounds.

---

# AES Round Operations

The main AES round operations are:

1. **SubBytes** — bytes are replaced using a substitution table.
2. **ShiftRows** — rows of the state are shifted.
3. **MixColumns** — values within each column are mathematically mixed.
4. **AddRoundKey** — the state is XORed with the current round key.

Conceptually:

```text
State
  |
  v
[ SubBytes ]
  |
  v
[ ShiftRows ]
  |
  v
[ MixColumns ]
  |
  v
[ AddRoundKey ] <----- Round Key
  |
  v
New State
```

The process is repeated over multiple rounds.

The final round is slightly different because it does not perform the MixColumns operation.

The repeated substitution and permutation operations cause changes in the input to spread throughout the encrypted block.

---

# Substitution in AES

An important component of AES is the **S-box**, or substitution box.

The S-box performs a byte substitution:

$$
\{0,1\}^8 \rightarrow \{0,1\}^8.
$$

In other words, each 8-bit input value is mapped to another 8-bit value using the AES substitution table.

Conceptually:

```text
Input Byte ---> [ S-Box ] ---> Output Byte
   8 bits                       8 bits
```

This substitution is performed on every byte of the AES state.

The substitution operation, together with the permutation and mixing operations in later steps, helps ensure that changes to the input spread throughout the ciphertext.



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








---


---


---


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
