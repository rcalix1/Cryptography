## OpenSSL Commands


* link

## First Lab - Secret Key


```

>>> openssl enc -ciphertype -e -in plain.txt -out cipher.bin -K 00112233445566778889aabbccddeeff -iv 0102030405060708




-in <file> input file
-out <file> output file
-e encrypt
-d decrypt
-K/-iv key/iv in hex is the next argument
-[pP] print the iv/key (then exit if -P)



```


Please replace the ciphertype with a specific cipher type, such as -aes-128-cbc, -bf-cbc,
-aes-128-cfb, etc. 



## Encrypt Image - ECB vs. CBC


For the .bmp file, the first 54 bytes contain the header information about the picture, we have
to set it correctly, so the encrypted file can be treated as a legitimate .bmp file. We will replace the
header of the encrypted picture with that of the original picture. 

```

head -c 54 original.bmp > header
$ tail -c +55 original.bmp > body
$ cat header body > new.bmp

```


## Corrupt one bit with "ghex" 

```

>>> ghex

```




