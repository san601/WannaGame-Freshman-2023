# WannaGame Freshman 2023
## EZ FLAG CHECKER 3

Level: hard

Description: A simple flagchecker3

Author: Okoonzz

### Solution

Let's examine main.main

```
  // Doing something with input
  v40.array = (uint8 *)main__mR4(v40);

  // Doing some other things with input
  v41 = main_rt(v40);

  array = v41.array;
  v14 = v41.len;
  v41.cap = main_dec.len;
  v41.len = (int)main_dec.str;
  v42 = runtime_stringtoslicebyte((runtime_tmpBuf *)v17, *(string *)&v41.len);
  v19 = v42.array;
  cap = v42.cap;
  v9 = (unsigned __int64)encoding_hex_Decode(v42, v42);
  if ( cap < v9 )
    runtime_panicSliceAcap();
  if ( v14 == v9 )
    runtime_memequal();
  else
    v10 = 0;
  if ( !v10 )
  {
    a.cap = (int)&RTYPE_string_0;
    v23 = &off_4B8D20;
    v34.data = os_Stdout;
    v34.tab = (runtime_itab *)&go_itab__ptr_os_File_comma_io_Writer;
    v37.array = (interface_ *)&a.cap;
    v37.len = 1LL;
    v37.cap = 1LL;
    fmt_Fprintln(v34, v37);
    os_Exit(1LL);
  }
  a.array = (interface_ *)&RTYPE_string_0;
  a.len = (int)&off_4B8D30;
  v35.data = os_Stdout;
  v35.tab = (runtime_itab *)&go_itab__ptr_os_File_comma_io_Writer;
  v38.array = (interface_ *)&a;
  v38.len = 1LL;
  v38.cap = 1LL;
  fmt_Fprintln(v35, v38);
```

It's likely that v14 is our input's length and v9 is the hidden flag's length. Using GDB reveals 64 is the hidden flag's length.

![image](https://github.com/san601/WannaGame-Freshman-2023/assets/144963803/c627f94d-4ac0-4279-9c86-35df8790bdf4)

![image](https://github.com/san601/WannaGame-Freshman-2023/assets/144963803/b91133cd-92f8-4651-a7e4-c0ec0b2f9079)

In main._K, this is the part where it initializes a substitution box, which is also a key indicator of RC4 encryption.

![image](https://github.com/san601/WannaGame-Freshman-2023/assets/144963803/6fb2ebc8-62b3-4085-8d82-90c1a8522053)

This is where it scrambles that substitution box. 

![image](https://github.com/san601/WannaGame-Freshman-2023/assets/144963803/4d6b40f2-f172-45c2-a65a-7963fdfbebc6)

Back to main._mR4, as we know v11 stores the substitution box and v9 (might) stores the text that is going to be encrypted. This looks just as a normal RC4 encryption so let's not spend too much time on this.

![image](https://github.com/san601/WannaGame-Freshman-2023/assets/144963803/d184651a-205f-4d48-b640-b75ea1eb1eb3)

It's very likely that the program use 2 functions to encrypt our input.

![image](https://github.com/san601/WannaGame-Freshman-2023/assets/144963803/d68b3d3e-ed38-4ee4-ac95-523e0006896e)

Input the string "W1{aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa}" with GDB and some breakpoints right after those 2 function give us this:

After main_mR4

![image](https://github.com/san601/WannaGame-Freshman-2023/assets/144963803/413db0dd-0f3d-4de7-b5b6-168e8f7ad1b6)

After main_rt

![image](https://github.com/san601/WannaGame-Freshman-2023/assets/144963803/865d97a1-0f9f-43e0-967b-c9a9e643b569)

The difference between those 2 can tell us what does main_rt do. Let's take a closer look.

![image](https://github.com/san601/WannaGame-Freshman-2023/assets/144963803/02be3d1a-8ed4-485d-8da3-32ccd4dbe63b)

![image](https://github.com/san601/WannaGame-Freshman-2023/assets/144963803/b5621ab0-6d24-49cc-a592-e6475ce8be63)

So it only takes 3 last bit and rotate it. Let's keep on examining the main.main function

This is where it compares our input with another encoded string.

![image](https://github.com/san601/WannaGame-Freshman-2023/assets/144963803/b52e5a6b-00e7-415f-b9e2-dd23494bc85c)

Observing it in GDB, we could find those string

![image](https://github.com/san601/WannaGame-Freshman-2023/assets/144963803/3205aeb7-b234-4e4d-8580-0570b6192782)

So everything is clear now. First, find the key by xoring the encrypted text with our initial text.

```
encrypted_text = [0x51, 0x3c, 0x72, 0x62, 0x5d, 0x64, 0xd8, 0x21,
                  0x81, 0xf4, 0x30, 0xb6, 0x6c, 0x2b, 0x22, 0x82,
                  0x77, 0x8e, 0xfd, 0x95, 0x40, 0x62, 0xe3, 0x8a,
                  0xbd, 0xb2, 0xa0, 0x81, 0x45, 0x6e, 0x86, 0xee,
                  0x16, 0x3e, 0x3e, 0x5c, 0x63, 0xf5, 0xd2, 0xf0,
                  0x53, 0x6f, 0x87, 0xab, 0x81, 0x7d, 0xbb, 0x94,
                  0x0f, 0xf4, 0x73, 0xe7, 0x43, 0xc5, 0xa0, 0xb4,
                  0xe4, 0xc2, 0xd4, 0x8d, 0x64, 0xd8, 0xc5, 0x1e]

s = list("W1{aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa}")
print("[", end='')
for i in range(63):
    print(hex(encrypted_text[i] ^ ord(s[i])), end=',')
print(hex(encrypted_text[63] ^ ord(s[63])), end='')
print("]")
```

This gives:

```
[0x6, 0xd, 0x9, 0x3, 0x3c, 0x5, 0xb9, 0x40, 0xe0, 0x95, 0x51, 0xd7, 0xd, 0x4a, 0x43, 0xe3, 0x16, 0xef, 0x9c, 0xf4, 0x21, 0x3, 0x82, 0xeb, 0xdc, 0xd3, 0xc1, 0xe0, 0x24, 0xf, 0xe7, 0x8f, 0x77, 0x5f, 0x5f, 0x3d, 0x2, 0x94, 0xb3, 0x91, 0x32, 0xe, 0xe6, 0xca, 0xe0, 0x1c, 0xda, 0xf5, 0x6e, 0x95, 0x12, 0x86, 0x22, 0xa4, 0xc1, 0xd5, 0x85, 0xa3, 0xb5, 0xec, 0x5, 0xb9, 0xa4, 0x63]
```

Let's rotate main_dec to find its original state and xor it with the key above:

```
def rotate(n):
    binary_str = bin(n)[2:]
    temp = binary_str[-3:]
    rot = temp[1:] + temp[0]
    res = binary_str[:-3] + rot
    return int(res, 2)


xor_key = [0x6, 0xd, 0x9, 0x3, 0x3c, 0x5, 0xb9, 0x40, 0xe0, 0x95, 0x51, 0xd7, 0xd, 0x4a, 0x43, 0xe3, 0x16, 0xef, 0x9c, 0xf4,
           0x21, 0x3, 0x82, 0xeb, 0xdc, 0xd3, 0xc1, 0xe0, 0x24, 0xf, 0xe7, 0x8f, 0x77, 0x5f, 0x5f, 0x3d, 0x2, 0x94, 0xb3,
           0x91, 0x32, 0xe, 0xe6, 0xca, 0xe0, 0x1c, 0xda, 0xf5, 0x6e, 0x95, 0x12, 0x86, 0x22, 0xa4, 0xc1, 0xd5, 0x85,0xa3,
           0xb5, 0xec, 0x5, 0xb9, 0xa4, 0x63]

check = [0x54, 0x3a, 0x71, 0x40, 0x0a, 0x6d, 0x80, 0x31,
         0xa0, 0xe4, 0x62, 0x88, 0x58, 0x16, 0x75, 0x8e,
         0x4c, 0x8c, 0xae, 0xb5, 0x52, 0x74, 0xb5, 0x86,
         0xbd, 0x8a, 0x8b, 0x96, 0x15, 0x50, 0x95, 0xe7,
         0x42, 0x00, 0x1a, 0x51, 0x50, 0xe3, 0xd3, 0xf1,
         0x06, 0x54, 0xae, 0xaf, 0x9c, 0x45, 0xeb, 0x9d,
         0x09, 0xc9, 0x60, 0xec, 0x53, 0x90, 0xb6, 0xba,
         0xed, 0xc2, 0xe9, 0x8b, 0x6a, 0xce, 0x95, 0x1b]

for i in range(len(check)):
    print(chr(rotate(check[i]) ^ xor_key[i]), end='')
```

And we got our flag:

```
W1{C0n9r@t5_U_0n_f1Gur1ng_Ou7_th3_CoRrec7_Key_4nd_rot4ting_bit7}
```
