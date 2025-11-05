## XOR Hash

#  Message Integrity

## 🧪 Crypto Lab

* **Topic**: One-way Hash Functions and MAC
* **Objective**: Understand how to encrypt and decrypt messages by assigning inverted numbers to letters (A=26, ..., Z=1)



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
