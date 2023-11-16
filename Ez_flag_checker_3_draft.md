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

Back to main._mR4, as we know v11 stores the substitution box and v9 (might) stores the text that is going to be encrypted.

![image](https://github.com/san601/WannaGame-Freshman-2023/assets/144963803/d184651a-205f-4d48-b640-b75ea1eb1eb3)

After main_mR4

![image](https://github.com/san601/WannaGame-Freshman-2023/assets/144963803/413db0dd-0f3d-4de7-b5b6-168e8f7ad1b6)

After main_rt

![image](https://github.com/san601/WannaGame-Freshman-2023/assets/144963803/865d97a1-0f9f-43e0-967b-c9a9e643b569)

The difference between those 2 can tell us what does main_rt do. Let's take a closer look.

This might check our input after 2 function with main_dec

![image](https://github.com/san601/WannaGame-Freshman-2023/assets/144963803/59da8344-0529-4ee2-802b-7da84614a5f3)
