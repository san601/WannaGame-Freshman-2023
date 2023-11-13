# WannaGame Freshman 2023
## EZ FLAG CHECKER 2

Level: hard

Description: A simple flagchecker 2

Author: dream

### Solution

First, as usual, I used IDA to look at the main function and found out a set of simultaneous equations.

![image](https://github.com/san601/WannaGame-Freshman-2023/assets/144963803/3d9a8fbd-4a04-4b58-b0b6-008a6bf18c48)

Using z3 to solve it, I got this fake flag instead of the real flag. This took me a few hours in the contest lol. Very painful.

![image](https://github.com/san601/WannaGame-Freshman-2023/assets/144963803/6dfaf625-86b7-4fa7-b360-1766174ea462)

I noticed that if I use that flag on a debugger, it turned out to be the correct one. So I knew that there was some kind of anti-debugger trick inside.

![image](https://github.com/san601/WannaGame-Freshman-2023/assets/144963803/99313b1b-e941-4f3b-b095-8c80638c894d)

Continue examining using IDA, a bunch of ptrace functions appeared so I knew that this was the ptrace anti-debugging mechanism. 

It's very easy to bypass this, just set a breakpoint at ptrace function, finish the function and then set RAX register to 0x0. [For more information](https://jaybailey216.com/debugging-stripped-binaries/)

From now on, this is my attempt to solve this challenge at home because I couldn't finish it on time at the contest.
This is the actual function to check our input.

![image](https://github.com/san601/WannaGame-Freshman-2023/assets/144963803/f7b7a008-e34c-4b3a-a783-b444e002a40c)

Let's see its code.

```c=
void __noreturn sub_55AC0CFA696C()
{
  unsigned __int64 v0; // rax
  void *v1; // rsp
  _BYTE v2[8]; // [rsp+8h] [rbp-180h] BYREF
  int i; // [rsp+10h] [rbp-178h]
  int j; // [rsp+14h] [rbp-174h]
  int n; // [rsp+18h] [rbp-170h]
  int ii; // [rsp+1Ch] [rbp-16Ch]
  int v7; // [rsp+20h] [rbp-168h]
  int v8; // [rsp+24h] [rbp-164h]
  unsigned __int64 k; // [rsp+28h] [rbp-160h]
  unsigned __int64 m; // [rsp+30h] [rbp-158h]
  size_t v11; // [rsp+38h] [rbp-150h]
  unsigned __int64 v12; // [rsp+40h] [rbp-148h]
  unsigned __int64 v13; // [rsp+48h] [rbp-140h]
  _BYTE *v14; // [rsp+50h] [rbp-138h]
  _DWORD s[66]; // [rsp+58h] [rbp-130h] BYREF
  unsigned __int64 v16; // [rsp+160h] [rbp-28h]

  v16 = __readfsqword(0x28u);
  for ( i = 0; i <= 17; ++i )
    putchar(dword_55AC0CFA9240[i]);
  __isoc99_scanf("%255s", s);
  v11 = strlen((const char *)s);
  if ( v11 <= 7 || (v11 & 3) != 0 )
  {
    for ( j = 0; j <= 5; ++j )
      putchar(dword_55AC0CFA9290[j]);
    exit(0);
  }
  v12 = (v11 >> 2) - 1;
  v13 = (v11 >> 2) - 2;
  v0 = 16 * ((4 * v12 + 15) / 0x10);
  while ( v2 != &v2[-(v0 & 0xFFFFFFFFFFFFF000LL)] )
    ;
  v1 = alloca(v0 & 0xFFF);
  if ( (v0 & 0xFFF) != 0 )
    *(_QWORD *)&v2[(v0 & 0xFFF) - 8] = *(_QWORD *)&v2[(v0 & 0xFFF) - 8];
  v14 = v2;
  for ( k = 0LL; k < v12; ++k )
  {
    v7 = s[k];
    v8 = s[k + 1];
    *(_DWORD *)&v14[4 * k] = v8 ^ v7;
  }
  for ( m = 0LL; m < v12; ++m )
  {
    if ( *(_DWORD *)&v14[4 * m] != dword_55AC0CFA92E0[m] )
    {
      for ( n = 0; n <= 4; ++n )
        putchar(dword_55AC0CFA9290[n]);
      exit(0);
    }
  }
  for ( ii = 0; ii <= 7; ++ii )
    putchar(dword_55AC0CFA92C0[ii]);
  exit(0);
}
```

Paying attention to these lines of code where it calculates and compares stuffs. v12 is our input's length divided by 4 and then minus 1.

```c=
for ( k = 0LL; k < v12; ++k )
{
  v7 = s[k];
  v8 = s[k + 1];
  *(_DWORD *)&v14[4 * k] = v8 ^ v7;
}
for ( m = 0LL; m < v12; ++m )
{
  if ( *(_DWORD *)&v14[4 * m] != dword_55AC0CFA92E0[m] )
  {
    // Not satisfy, printing "Wrong"
    for ( n = 0; n <= 4; ++n )
      putchar(dword_55AC0CFA9290[n]);
    exit(0);
  }
}
```

So basically, this piece of code use 

This is the value of dword_55AC0CFA92E0, where it compares our decrypted input with:

![image](https://github.com/san601/WannaGame-Freshman-2023/assets/144963803/4e0c4831-473c-43d4-9056-a094f49c7c12)

Let's put those value into python for future use.

```python=
check = [0x67, 0x66, 0x0C, 0x00, 0x47, 0x08, 
         0x0E, 0x47, 0x02, 0x00, 0x3D, 0x01, 
         0x11, 0x31, 0x24, 0x06, 0x3B, 0x29, 
         0x53, 0x43, 0x00, 0x13, 0x41, 0x40, 
         0x2F, 0x04, 0x41, 0x50, 0x2F, 0x61, 
         0x5D, 0x3B, 0x05, 0x02, 0x4F, 0x22]

```

I'm stuck at this point so maybe this writeups will be updated later.

![image](https://github.com/san601/WannaGame-Freshman-2023/assets/144963803/f87d9ead-1942-433f-903c-7de0c5a62124)

