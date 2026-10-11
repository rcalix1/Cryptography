## Crypto and Quantum Computing 

* https://github.com/rcalix1/quantumComputing
* 



---



# Post-Quantum Cryptography: Algorithms and Cryptanalysis

## Introduction

Post-quantum cryptography (PQC) concerns cryptographic algorithms designed to resist attacks from classical and quantum computers.

Shor's algorithm demonstrated that sufficiently powerful quantum computers could efficiently solve integer factorization and discrete logarithm problems, threatening RSA and elliptic-curve cryptography (ECC) [1].

However, existing quantum computers cannot break modern RSA or ECC at practical cryptographic scales.

Post-quantum cryptographic algorithms execute on conventional computers. Their security depends on mathematical problems believed to be difficult for both classical and quantum algorithms.

In 2024, the National Institute of Standards and Technology (NIST) standardized three post-quantum cryptographic algorithms.

This tutorial examines six algorithms, including three standardized algorithms and three candidates subsequently broken or withdrawn.

## 1. ML-KEM (Kyber)

**Status:** NIST standardized (FIPS 203, 2024)

**Application:** Key encapsulation.

ML-KEM is based on the Module Learning With Errors (Module-LWE) problem.

A simplified Learning With Errors problem is:

    b = A*s + e (mod q)

where:

- A is a publicly known matrix.
- s is a secret vector.
- e is a small random error vector.
- q is an integer modulus.
- b is the resulting public vector.

Without the error vector, recovering the secret could be accomplished using conventional linear algebra under suitable conditions.

The introduction of the error makes recovering the secret computationally difficult for appropriately chosen parameters.

ML-KEM uses structured polynomial and module arithmetic rather than this simplified matrix construction.

### General Procedure

1. Generate a public and private key.
2. Encapsulate a shared secret using the public key.
3. Decapsulate the shared secret using the private key.
4. Use the shared secret with symmetric encryption.

ML-KEM is not itself a general-purpose data encryption algorithm.

**Security:** No publicly known practical attack breaks the standardized ML-KEM parameter sets.

**References:** [2, 3]

---

## 2. ML-DSA (Dilithium)

**Status:** NIST standardized (FIPS 204, 2024)

**Application:** Digital signatures.

ML-DSA is based on structured lattice problems, including Module-LWE and Module-SIS.

The objective of a digital signature is to establish message authenticity and integrity.

### General Procedure

1. Generate a public and private key.
2. Process the message using the signing algorithm.
3. Generate a digital signature using the private key.
4. Verify the signature using the public key.

Conceptually:

    signature = Sign(private_key, message)

    valid = Verify(public_key, message, signature)

The verification algorithm returns whether the signature is valid.

Unlike RSA signatures, ML-DSA does not rely on integer factorization.

**Security:** No publicly known practical attack breaks the standardized ML-DSA parameter sets.

**References:** [4, 5]

---

## 3. SLH-DSA (SPHINCS+)

**Status:** NIST standardized (FIPS 205, 2024)

**Application:** Digital signatures.

SLH-DSA uses cryptographic hash functions rather than lattice-based mathematical problems.

Its construction combines one-time signatures, few-time signatures, and Merkle hash trees.

A simplified Merkle tree combines hashes as follows:

    h1 = H(message1)
    h2 = H(message2)

    root = H(h1 || h2)

where:

- H is a cryptographic hash function.
- || represents concatenation.
- root is the resulting parent hash.

Actual SLH-DSA signatures use substantially more elaborate tree structures.

### General Procedure

1. Generate a public and private key.
2. Process the message using cryptographic hash functions.
3. Construct a signature using hash-based signature structures.
4. Verify the signature using the public key.

**Advantage:** Its mathematical foundation differs from lattice-based cryptography.

**Disadvantage:** Signatures can be relatively large.

**References:** [6, 7]

---

## 4. SIKE (Supersingular Isogeny Key Encapsulation)

**Status:** Broken in 2022

**Application:** Experimental post-quantum key encapsulation.

SIKE was based on mathematical relationships between supersingular elliptic curves.

An isogeny is a special mathematical mapping between elliptic curves that preserves their group structure.

The security assumption involved the difficulty of recovering hidden relationships between elliptic curves.

### Cryptanalytic Failure

In 2022, Castryck and Decru demonstrated a classical attack against the underlying SIDH construction used by SIKE.

The attack exploited additional mathematical structure exposed by the protocol.

This allowed researchers to recover secret information without using a quantum computer.

Certain proposed parameter sets could be broken in hours using conventional hardware.

**Lesson:** A mathematical problem believed to be difficult may contain unexpected structure that makes cryptanalysis possible.

**Reference:** [8]

---

## 5. Rainbow

**Status:** Broken in 2022

**Application:** Experimental post-quantum digital signatures.

Rainbow was a multivariate cryptographic signature algorithm.

Its security relied on the difficulty of solving systems of multivariate polynomial equations over finite fields.

A simplified example is:

    y1 = x1*x2 + x3*x3 + x1

    y2 = x1*x1 + x2*x3 + x2

All arithmetic is performed in a finite field.

Given the outputs y1 and y2, the attacker attempts to recover the unknown inputs.

Actual Rainbow constructions use considerably more variables and specially structured polynomial systems.

### Cryptanalytic Failure

In 2022, Ward Beullens developed a practical attack against Rainbow.

The attack exploited mathematical structure in the public key construction.

Rainbow's proposed security levels were undermined, and it was not standardized.

**Lesson:** The difficulty of a general mathematical problem does not guarantee the security of a particular cryptographic construction.

**Reference:** [9]

---

## 6. HAWK

**Status:** Withdrawn from NIST consideration in July 2026

**Application:** Post-quantum digital signatures.

HAWK is a lattice-based hash-and-sign signature construction involving structured lattices.

It was designed to provide compact signatures and efficient cryptographic operations.

Its security relied on mathematical problems involving lattice isomorphisms and short vectors.

### Cryptanalytic Failure

In July 2026, an AI-assisted cryptanalytic result demonstrated a significant reduction in HAWK's estimated security.

The attack related HAWK key recovery to a shorter-vector problem in a substantially lower-dimensional lattice.

This undermined the proposed security parameters.

The HAWK development team subsequently withdrew the algorithm from NIST's standardization process.

Unlike the SIKE and Rainbow attacks, the HAWK result should not be interpreted as an immediate practical break of every proposed parameter set.

**Lesson:** Cryptanalytic advances can substantially weaken security estimates even without a complete practical key-recovery attack.

**References:** [10, 11]

---

## 7. Summary

| Algorithm | Mathematical Foundation | Application | Status |
|---|---|---|---|
| ML-KEM | Module lattices | Key encapsulation | Standardized |
| ML-DSA | Module lattices | Digital signatures | Standardized |
| SLH-DSA | Hash functions | Digital signatures | Standardized |
| SIKE | Elliptic-curve isogenies | Key encapsulation | Broken |
| Rainbow | Multivariate polynomials | Digital signatures | Broken |
| HAWK | Structured lattices | Digital signatures | Withdrawn |

## 8. Important Observations

1. Post-quantum cryptography does not require a quantum computer.
2. Quantum-resistant does not mean mathematically proven unbreakable.
3. Cryptographic security depends on the underlying mathematical problem, algorithm construction, and implementation.
4. Classical cryptanalysis has already broken several proposed post-quantum algorithms.
5. NIST standardization provides extensive scrutiny but does not guarantee permanent security.
6. AES and other symmetric cryptographic algorithms are affected differently by quantum algorithms than RSA and ECC.

## 9. Questions for Students

1. Why does Shor's algorithm threaten RSA and ECC?
2. What is the purpose of the error vector in Learning With Errors?
3. What is the difference between key encapsulation and digital signatures?
4. Why are hash-based signatures an alternative to lattice-based signatures?
5. How did classical computers break SIKE and Rainbow?
6. Why might a post-quantum algorithm be broken even if its underlying mathematical problem remains difficult?
7. Why did the HAWK cryptanalytic result lead to withdrawal rather than immediate standardization with unchanged parameters?

## References

[1] Shor, P.W. (1997). Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer. SIAM Journal on Computing, 26(5), 1484-1509.

[2] Bos, J.W., Ducas, L., Kiltz, E., Lepoint, T., Lyubashevsky, V., Schanck, J.M., Schwabe, P., Seiler, G. and Stehlé, D. (2018). CRYSTALS - Kyber: A CCA-Secure Module-Lattice-Based KEM. IEEE European Symposium on Security and Privacy, 353-367.

[3] National Institute of Standards and Technology (2024). Module-Lattice-Based Key-Encapsulation Mechanism Standard. FIPS 203.

[4] Ducas, L., Kiltz, E., Lepoint, T., Lyubashevsky, V., Schwabe, P., Seiler, G. and Stehlé, D. (2018). CRYSTALS-Dilithium: A Lattice-Based Digital Signature Scheme. IACR Transactions on Cryptographic Hardware and Embedded Systems, 2018(1), 238-268.

[5] National Institute of Standards and Technology (2024). Module-Lattice-Based Digital Signature Standard. FIPS 204.

[6] Bernstein, D.J., Dobraunig, C., Eichlseder, M., Fluhrer, S., Gazdag, S.L., Hülsing, A., Kampanakis, P., Kölbl, S., Lange, T., Lauridsen, M.M., Mendel, F., Niederhagen, R., Rechberger, C., Rijneveld, J. and Schwabe, P. (2019). SPHINCS+: Submission to the NIST Post-Quantum Project. NIST PQC Submission.

[7] National Institute of Standards and Technology (2024). Stateless Hash-Based Digital Signature Standard. FIPS 205.

[8] Castryck, W. and Decru, T. (2023). An Efficient Key Recovery Attack on SIDH. Advances in Cryptology - EUROCRYPT 2023, Part V, 423-447.

[9] Beullens, W. (2022). Breaking Rainbow Takes a Weekend on a Laptop. Advances in Cryptology - CRYPTO 2022, Part II, 464-479.

[10] HAWK Team (2025). HAWK: High-speed Asymmetric WorKflow, Version 1.1. NIST Additional Digital Signature Submission.

[11] National Institute of Standards and Technology (2026). Status Report on the Second Round of the Additional Digital Signature Schemes for the NIST Post-Quantum Cryptography Standardization Process. NIST IR 8610.
