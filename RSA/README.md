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




