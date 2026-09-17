## Integrity


```

>>> sudo apt-get install openssl

>>> sudo apt-get install ghex


```

## Create a hash



```

openssl dgst dgsttype filename

```

Replace the dgsttype with a specific one-way hash algorithm, such as -md5, -sha1, -sha256

## Keyed Hash


```

openssl dgst -md5 -hmac "abcdefg" filename

```


Please generate a keyed hash using HMAC-MD5, HMC-SHA256, and HMAC-SHA1 for any file that
you choose. 



## The Randomness of One-way Hash

To understand the properties of one-way hash functions, we would like to do the following exercise for MD5
or SHA256:


* Create a text file of any length.
* Generate the hash value H1 for this file using a specific hash algorithm.
* Flip one bit of the input file. You can achieve this modification using ghex.
* Generate the hash value H2 for the modified file.
5. Please observe whether H1 and H2 are similar or not. Please describe your observations in the lab
report.








