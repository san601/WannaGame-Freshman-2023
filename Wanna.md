# WannaGame Freshman 2023
## WELCOME

Level: easy

Description: I just want to welcome you to the WannaGame Freshman 2023!!!

Author: dream

[chall](https://cnsc.uit.edu.vn/ctf/files/d68c3530e27c38b01ab02fd39935b4dd/Welcome?token=eyJ1c2VyX2lkIjo4NTksInRlYW1faWQiOm51bGwsImZpbGVfaWQiOjE2N30.ZVDZtQ.Ln4GZZE5pxQTfkCzurSNLFwU2hs)

### Solution

Open the file with IDA, we can clearly see something that look like the flag but encrypted.

![image](https://hackmd.io/_uploads/SJ_Yq80mT.png)

The string is: 'J1{LBH_QVQ_VG######JRYPBZR_GB_GUR_JNAANTNZR_SERFUZNA_2023!!!!!'

Finishing it up with a '}' at the end and used an online Caesar Cipher decoder to decrypt it, we got the flag:

![image](https://hackmd.io/_uploads/r1efoUR7T.png)


