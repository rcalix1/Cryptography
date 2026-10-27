## RSA

For asymmetric encryption

* https://rcalix1.github.io/Cryptography/RSA/350RSA_steps.pdf
* https://rcalix1.github.io/Cryptography/RSA/RSA_gcd_EEA_details.pdf

## Break RSA


### Factorization

* 4 = 2 * 2
* 123456 = 2**6 * 3 * 643
* 1234567 = 127 * 9721
* 


---

## EEA - Extended Euclidean Algorithm (EEA)

```python




def xgcd(x, y):
    """Extended Euclidean Algorithm (EEA)"""

    # Example: x=17, y=43
    #
    # The ordinary Euclidean Algorithm finds gcd(17,43) = 1.
    #
    # The EXTENDED Euclidean Algorithm also finds two integers
    # s and t such that:
    #
    #     17*s + 43*t = gcd(17,43) = 1
    #
    # This is called Bezout's identity.
    # s and t are simply integer coefficients (multipliers).
    #
    # For example, s=-5 and t=2:
    #     17*(-5) + 43*(2) = -85 + 86 = 1
    #
    # This is useful for RSA because -5 is the modular inverse
    # of 17 modulo 43:
    #     17*(-5) mod 43 = 1
    #     -5 mod 43 = 38 (positive equivalent)

    # Initialize coefficients.
    # s0,t0 describe x: 17 = 1*17 + 0*43
    # s1,t1 describe y: 43 = 0*17 + 1*43
    s1, s0 = 0, 1
    t1, t0 = 1, 0

    while y:
        # Integer division: quotient without decimals.
        # First iteration: 17 // 43 = 0
        # Second iteration: 43 // 17 = 2
        q = x // y

        # Euclidean Algorithm:
        # Replace x with y and y with the remainder.
        #
        # (17,43) -> (43,17)
        # (43,17) -> (17,9)  because 43 mod 17 = 9
        # (17,9)  -> (9,8)
        # (9,8)   -> (8,1)
        # (8,1)   -> (1,0)
        #
        # When y=0, x contains the GCD.
        x, y = y, x % y

        # Update the coefficients to match the new remainders.
        #
        # Mathematical idea:
        # If x = s0*17 + t0*43
        # and y = s1*17 + t1*43,
        # then the new remainder x-q*y has coefficients:
        # (s0-q*s1) and (t0-q*t1).
        #
        # This preserves Bezout's identity throughout the loop.
        s1, s0 = s0 - q * s1, s1
        t1, t0 = t0 - q * t1, t1

    # Final result for xgcd(17,43):
    # x  = 1   (GCD)
    # s0 = -5  (coefficient of 17)
    # t0 = 2   (coefficient of 43)
    #
    # Verification: 17*(-5) + 43*(2) = 1
    return x, s0, t0




```

---

## Text to Int


```



def text2Int(text):
    """Convert a text string into an integer"""

    # Example: text = "AB"
    #
    # ord() converts each character to its ASCII/Unicode number:
    # A = 65, B = 66
    #
    # map(ord, text) produces [65, 66]
    #
    # x << 8 shifts x left by 8 bits (equivalent to x * 256).
    # Each character occupies one byte (8 bits) in this code.
    #
    # reduce() combines the character values into one integer:
    # Start with 65
    # (65 << 8) + 66 = 65*256 + 66 = 16706
    #
    # Therefore, "AB" becomes the integer 16706.

    return reduce(lambda x, y : (x << 8) + y, map(ord, text))


def int2Text(number, size):
    """Convert an integer into a text string"""

    # Example: number = 16706, size = 2 bytes
    #
    # Reverse the conversion: 16706 -> "AB"
    #
    # size << 3 means size * 8 (convert bytes to bits).
    # For size=2, this gives 16 bits.
    #
    # range(0, 16, 8) produces [0, 8].
    # reversed() produces [8, 0] to extract the first byte first.
    #
    # number >> j shifts right by j bits.
    # & 0xff keeps only the last 8 bits (0xff = 255).
    #
    # First byte:  (16706 >> 8) & 255 = 65 -> chr(65) = "A"
    # Second byte: (16706 >> 0) & 255 = 66 -> chr(66) = "B"
    #
    # join() combines the characters into "AB".
    # lstrip("\x00") removes leading zero bytes, if present.

    text = "".join([chr((number >> j) & 0xff)
                    for j in reversed(range(0, size << 3, 8))])
    return text.lstrip("\x00")




```


more detailed 


```



def text2Int(text):
    """Convert a text string into an integer"""

    # Example: text = "CAT"
    #
    # Step 1: Convert characters to ASCII numbers:
    #    C = 67, A = 65, T = 84
    #
    # Step 2: Represent each character as 8 bits:
    #    C = 01000011
    #    A = 01000001
    #    T = 01010100
    #
    # Step 3: Combine the three bytes into one binary number:
    #    01000011 01000001 01010100
    #
    # Step 4: Convert this binary number to decimal:
    #    67*256^2 + 65*256 + 84 = 4407636
    #
    # The << 8 operation shifts bits left by one byte:
    #    67 << 8 = 17152
    #    17152 + 65 = 17217
    #    17217 << 8 = 4407552
    #    4407552 + 84 = 4407636
    #
    # reduce() repeats this process for every character.
    # Result: "CAT" -> 4407636

    return reduce(lambda x, y: (x << 8) + y, map(ord, text))


def int2Text(number, size):
    """Convert an integer into a text string"""

    # Example: number = 4407636, size = 3
    #
    # Step 1: Express the integer as 3 bytes:
    #    01000011 01000001 01010100
    #       67       65       84
    #
    # Step 2: Extract one byte at a time, starting from the left.
    #
    #    number >> 16  = 67
    #    number >> 8   = 17217
    #    number >> 0   = 4407636
    #
    # Step 3: Apply & 0xff (binary 11111111).
    # This keeps only the rightmost 8 bits:
    #
    #    (4407636 >> 16) & 255 = 67
    #    (4407636 >> 8)  & 255 = 65
    #    (4407636 >> 0)  & 255 = 84
    #
    # Step 4: Convert ASCII numbers back into characters:
    #    chr(67) = "C"
    #    chr(65) = "A"
    #    chr(84) = "T"
    #
    # Step 5: join() combines them into "CAT".
    # lstrip("\x00") removes any leading zero bytes.
    #
    # Result: 4407636 -> "CAT"

    text = "".join([chr((number >> j) & 0xff)
                    for j in reversed(range(0, size << 3, 8))])
    return text.lstrip("\x00")



```

even more detailed 


```


def encrypt(ptext, pk, mod):
    """Encrypt message with RSA public key"""

    # EXAMPLE: Encrypt the word "CAT"
    #
    # Public key: e = 17, n = 3233
    #
    # RSA encryption:
    #     ciphertext = plaintext^e mod n
    #
    # The plaintext must first be converted into integers.
    # Each integer must be smaller than n = 3233.
    #
    # ASCII representation:
    #
    # Character     Decimal       Binary
    #     C            67         01000011
    #     A            65         01000001
    #     T            84         01010100
    #
    # We cannot encrypt "CAT" as one integer because:
    #
    # "CAT" = 01000011 01000001 01010100
    #       = 4407636, which is larger than n = 3233.
    #
    # Therefore, we divide the message into smaller blocks.

    size = modSize(mod)

    # n = 3233 = 0x0CA1 (hexadecimal)
    #
    # One hexadecimal digit represents 4 bits.
    # Two hexadecimal digits represent one byte.
    #
    # 0C A1 = 2 bytes, so size = 2.
    #
    # We reserve one byte, leaving size-1 = 1 byte
    # for each plaintext block.

    output = []

    # output will contain the encrypted bytes.
    # Initially, the list is empty.

    while ptext:

        # FIRST ITERATION:
        # ptext = "CAT"
        # len(ptext) = 3
        # size - 1 = 1
        #
        # min(3,1) = 1
        #
        # Therefore, we encrypt only "C".
        nbytes = min(len(ptext), size - 1)

        # Extract the first nbytes characters.
        #
        # ptext[:1] = "C"
        #
        # text2Int("C") = 67
        #
        # Therefore, aux1 = 67.
        aux1 = text2Int(ptext[:nbytes])

        # RSA requires m < n.
        #
        # 67 < 3233, so encryption can proceed.
        assert aux1 < mod

        # Encrypt using modular exponentiation:
        #
        #     c = m^e mod n
        #
        # FIRST BLOCK ("C"):
        #     c = 67^17 mod 3233 = 641
        #
        # SECOND BLOCK ("A"):
        #     c = 65^17 mod 3233 = 2790
        #
        # THIRD BLOCK ("T"):
        #     c = 84^17 mod 3233 = 2159
        #
        # The plaintext integers 67, 65, 84
        # become ciphertext integers 641, 2790, 2159.
        aux2 = pow(aux1, pk, mod)

        # Convert each encrypted integer into bytes.
        #
        # Why? We want to store the encrypted message
        # as a sequence of bytes, not one enormous integer.
        #
        # size + 2 = 4 bytes per ciphertext block.
        #
        # For "C":
        #     641 decimal = 0x00000281
        #     Bytes = [0, 0, 2, 129]
        #
        # For "A":
        #     2790 decimal = 0x00000AE6
        #     Bytes = [0, 0, 10, 230]
        #
        # For "T":
        #     2159 decimal = 0x0000086F
        #     Bytes = [0, 0, 8, 111]
        #
        # output += appends these bytes to the list.
        #
        # After all three iterations:
        #
        # output = [
        #     0, 0, 2, 129,
        #     0, 0, 10, 230,
        #     0, 0, 8, 111
        # ]
        #
        # The fixed block length lets the decrypt()
        # function separate the ciphertext into blocks.
        output += int2List(aux2, size + 2)

        # Remove the plaintext characters already encrypted.
        #
        # Iteration 1: "CAT" -> "AT"
        # Iteration 2: "AT"  -> "T"
        # Iteration 3: "T"   -> ""
        #
        # When ptext is empty, the while loop stops.
        ptext = ptext[nbytes:]

    # Return the complete encrypted byte sequence.
    return output



```


---


## Step 1 — Divisibility and Prime Numbers

A number $a$ divides another number $b$ if the remainder of dividing $b$ by $a$ is zero.

$$
b \bmod a = 0
$$

For example:

$$
35 \bmod 7 = 0
$$

Therefore, 7 divides 35.

A **prime number** is an integer greater than 1 that has exactly two positive divisors: 1 and itself.

Examples:

- 7 is prime: divisors are 1 and 7.
- 12 is not prime: divisors are 1, 2, 3, 4, 6, 12.
- 1 is neither prime nor composite.

**Why this matters in cryptography:** Large prime numbers are fundamental to public-key cryptographic algorithms such as RSA.


```




# Step 1: Divisibility and prime numbers

def get_divisors(n):
    """Find all positive integers that divide n exactly."""
    divisors = []

    for i in range(1, n + 1):
        if n % i == 0:   # % computes the remainder
            divisors.append(i)

    return divisors


def is_prime(n):
    """A prime has exactly two positive divisors."""
    if n < 2:
        return False

    return len(get_divisors(n)) == 2


# Example 1: Divisibility
a = 7
b = 35

print("Remainder:", b % a)
print("Does 7 divide 35?", b % a == 0)

# Example 2: Prime numbers
for n in [1, 7, 12, 13, 21, 29]:
    print(f"{n}: divisors = {get_divisors(n)}, "
          f"prime = {is_prime(n)}")




```





---

## Step 2 — Generating Prime Numbers: Sieve of Eratosthenes

The **Sieve of Eratosthenes** is an efficient algorithm for finding all prime numbers up to a given limit $n$.

**Algorithm:**

1. Create a list of integers from 2 to $n$.
2. Start with 2, the first prime number.
3. Eliminate all multiples of 2 (except 2 itself).
4. Move to the next remaining number (3) and eliminate its multiples.
5. Continue until reaching $\sqrt{n}$.

**Why stop at $\sqrt{n}$?**

Every composite number $n$ has at least one prime divisor less than or equal to $\sqrt{n}$. Therefore, all composite numbers will have been eliminated by that point.

For example, to find primes up to 30, we only need to check prime divisors up to:

$$
\sqrt{30} \approx 5.48
$$

The resulting primes are:

$$
2,3,5,7,11,13,17,19,23,29
$$

**Cryptography connection:** Generating small primes is useful when testing candidate numbers for large-prime generation in public-key cryptography.



### Sieve of Eratosthenes — Visual Example

We want all prime numbers between 1 and 30.

1. Write down numbers 2 through 30.
2. Start at **2**. Keep 2, but cross out its multiples: 4, 6, 8, 10...
3. Move to **3**. Keep 3, but cross out its multiples: 6, 9, 12, 15...
4. Move to **5**. Keep 5, but cross out its multiples: 10, 15, 20, 25...
5. **Everything left is prime!**

### Final Result

| | | | | | |
|---|---|---|---|---|---|
| 1 | **2** | **3** | ~~4~~ | **5** | ~~6~~ |
| **7** | ~~8~~ | ~~9~~ | ~~10~~ | **11** | ~~12~~ |
| **13** | ~~14~~ | ~~15~~ | ~~16~~ | **17** | ~~18~~ |
| **19** | ~~20~~ | ~~21~~ | ~~22~~ | **23** | ~~24~~ |
| ~~25~~ | ~~26~~ | ~~27~~ | ~~28~~ | **29** | ~~30~~ |

**Bold** = prime number  
~~Crossed out~~ = composite number  
1 = neither prime nor composite

### Why Stop at the Square Root?

For numbers up to 30:

$$
\sqrt{30} \approx 5.48
$$

Every composite number up to 30 has at least one prime factor no greater than 5.48.

Therefore, we only need to check multiples of **2, 3, and 5**.

**Key idea:** Instead of testing every number individually, eliminate multiples of known primes. The numbers remaining are prime.

**Cryptography connection:** The Sieve of Eratosthenes efficiently generates small primes, which can help eliminate unsuitable candidates when generating large primes for public-key cryptography.






```



# Step 2: Sieve of Eratosthenes

def sieve(n):
    """
    Find all prime numbers from 2 to n.

    is_prime[i] = True means i is still
    considered a possible prime.
    """

    # Initially assume all numbers are prime
    is_prime = [True] * (n + 1)

    # 0 and 1 are not prime
    is_prime[0] = False
    is_prime[1] = False

    # Only check candidates up to sqrt(n)
    for p in range(2, int(n**0.5) + 1):

        if is_prime[p]:

            # Mark multiples of p as composite
            # Start at p*p because smaller
            # multiples were already eliminated
            for multiple in range(p*p, n + 1, p):
                is_prime[multiple] = False

    # Collect numbers still marked as prime
    primes = []

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)

    return primes


# Example: Generate primes up to 100
n = 100

primes = sieve(n)

print("Prime numbers up to", n)
print(primes)
print("Number of primes:", len(primes))





```




---




## Step 3 — Modular Arithmetic

**Modular arithmetic is like a clock.** When we reach a certain number, we start counting again from zero.

For example, with modulo 7, the only possible remainders are:

$$
0,1,2,3,4,5,6
$$

### 1. Basic Modulo

The modulo operator gives us the **remainder after division**.

For example:

$$
17 \bmod 7 = 3
$$

Because:

$$
17 = 2(7)+3
$$

### 2. Modular Addition

$$
(5+6)\bmod 7=4
$$

We add 5 + 6 = 11, then divide by 7. The remainder is 4.

### 3. Modular Subtraction

$$
(3-5)\bmod 7=5
$$

Since 3 − 5 = −2, we wrap around modulo 7 and obtain 5.

### 4. Modular Multiplication

$$
(4\times5)\bmod7=6
$$

Because 20 divided by 7 leaves a remainder of 6.

### 5. Modular Exponentiation

$$
3^4\bmod7=4
$$

Because $3^4=81$, and 81 divided by 7 leaves a remainder of 4.

**Why this matters in cryptography:** RSA and Diffie–Hellman use modular exponentiation with very large integers.



```




# Step 3: Modular Arithmetic

mod = 7

# Basic modulo
print("17 mod 7 =", 17 % mod)

# Addition
print("(5 + 6) mod 7 =", (5 + 6) % mod)

# Subtraction
print("(3 - 5) mod 7 =", (3 - 5) % mod)

# Multiplication
print("(4 * 5) mod 7 =", (4 * 5) % mod)

# Exponentiation
print("3^4 mod 7 =", (3**4) % mod)

# Python's efficient modular exponentiation
print("Using pow():", pow(3, 4, mod))

# Demonstrate the wrap-around
print("\nCounting modulo 7:")
for i in range(21):
    print(f"{i} mod 7 = {i % 7}")





```


---




## Step 4 — Finite Fields and Groups

A **finite field** is a collection of numbers in which we can perform addition, subtraction, multiplication, and division (except division by zero), and the results remain in the same collection.

For example, consider the integers modulo 7:

$$
F_7=\{0,1,2,3,4,5,6\}
$$

Because 7 is prime, these numbers form a finite field.

**Example: Multiplication modulo 7**

$$
3\times5=15
$$

$$
15\bmod7=1
$$

Notice something interesting: multiplying 3 by 5 produces 1 modulo 7.

Therefore, **5 is the multiplicative inverse of 3 modulo 7**.

This means division is possible:

$$
1/3 \equiv 5 \pmod 7
$$

A **group** is a mathematical structure with one operation, such as addition, that satisfies closure, associativity, identity, and inverses.

A finite field has two compatible operations, addition and multiplication, with additional properties.

**Cryptography connection:** Finite fields are used in AES, elliptic-curve cryptography, and other cryptographic algorithms.


```




# Step 4: Finite field modulo 7

p = 7

print("Multiplication table modulo 7\n")

# Column headings
print("    ", end="")
for j in range(p):
    print(f"{j:3}", end="")
print()

print("-" * 26)

# Every result is reduced modulo 7
for i in range(p):
    print(f"{i:3} |", end="")

    for j in range(p):
        result = (i * j) % p
        print(f"{result:3}", end="")

    print()

# Find multiplicative inverses
print("\nMultiplicative inverses modulo 7:")

for a in range(1, p):
    for b in range(1, p):
        if (a * b) % p == 1:
            print(f"{a} inverse = {b}")
            break




```




---



## Step 5 — Euclidean Algorithm (GCD)

The **Greatest Common Divisor (GCD)** is the largest positive integer that divides two numbers exactly.

For example, consider 48 and 18.

- Divisors of 48: 1, 2, 3, 4, 6, 8, 12, 16, 24, 48
- Divisors of 18: 1, 2, 3, 6, 9, 18

The largest common divisor is **6**.

### Euclidean Algorithm

Instead of finding every divisor, we repeatedly calculate remainders:

$$
48 = 2(18)+12
$$

$$
18 = 1(12)+6
$$

$$
12 = 2(6)+0
$$

When the remainder becomes zero, the last nonzero remainder is the GCD.

Therefore:

$$
\gcd(48,18)=6
$$

**Why this matters in cryptography:** RSA requires choosing a public exponent $e$ that has no common divisor with $\phi(n)$ other than 1.

In other words:

$$
\gcd(e,\phi(n))=1
$$

The Euclidean algorithm lets us check this efficiently.




```












# Step 5: Euclidean Algorithm

def gcd(a, b):
    """
    Find the greatest common divisor of a and b.

    Example: a=48, b=18
    """

    while b != 0:

        # Divide a by b and get the remainder
        remainder = a % b

        print(f"{a} = {a//b}({b}) + {remainder}")

        # Replace a with b, and b with remainder
        a = b
        b = remainder

    # When b becomes zero, a is the GCD
    return abs(a)


print("GCD =", gcd(48, 18))

# Verify using Python's built-in library
import math
print("Python math.gcd =", math.gcd(48, 18))



```



---


