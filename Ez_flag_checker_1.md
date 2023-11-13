# WannaGame Freshman 2023
## EZ FLAG CHECKER 1

Level: medium

Description: A simple flagchecker 1

Author: dream

### Solution

I really don't wanna write this because this chall is freaking annoying and time consuming. But anyway, here is the solution for you guys.

Opening the python script, we see a lot of obfuscated stuffs. The first thing I'm gonna do is to rename all of this using "Find and Replace" feature on your favorite text editor.

After deobfuscating and adding some comments, our code look somewhat like this:
```python=
# Param2 might be a string of 2-digit numbers
# This function uses numbers from that string to shuffle our input
def func1(our_input, param2):
    list_num = [int(param2[i:i+2],10) for i in range(0,len(param2),2)]
    param2 = [our_input[i] for i in list_num]
    param2 = ''.join(param2)
    return param2

# This function takes a string of character and takes each character, turns it into a 8 bit binary string and combine them into one string
def func2(param):
    result = []
    for i in param:
        list_bin = bin(ord(i))[2:].zfill(8)
        result.append(list_bin)
    return ''.join(result)

# Swaps 0 with O, then 1 with 0
def func3(param):
    return param.replace("0", "O").replace("1", "0")

# Swaps 0 with 1, then O with 0
def func4(param):
    return param.replace("0", "1").replace("O", "0")

# Each iteration, this function takes a string of 8 bit and turn it into ascii character
# It returns the combination of those ascii character
def func5(param):
    result = ""
    for i in range(0, len(param), 8):
        bin_str = param[i:i+8]
        num = int(bin_str, 2)
        char = chr(num)
        result += char
    return result

a = input("\t\t\t\t\tWELCOME TO THE FRIST FLAGCHECKER CHALLENGE!!!!!!!!!!!!!!\n\t\t\t\t\t\t\tPLEASE SUBMIT YOUR FLAG:\n\t\t\t\t\t").ljust(100,'0')
b = "OO00O0O0OO00OOO0OO00OOOOOO00OO0OOO00OO00OO00OOO0OO00OOO0OO00O0OOOO00OOOOOO00O00OOO00OOO0OO000OO0OO00OOO0OO00OOO0OO00OO0OOO00O00OOO00OO0OOO00OO0OOO00OO00OO00O000OO00O0OOOO00OO0OOO00OO00OO00O00OOO00O0OOOO00O0OOOO00OOOOOO000OO0OO00O0OOOO000OOOOO00O0O0OO00O000OO00O0O0OO00OO00OO00O0OOOO00OOO0OO00O00OOO00OO00OO00OOOOOO00OO00OO00O0O0OO00OOOOOO00OOOOOO00OOO0OO00OO00OO000OOOOO00OO0OOO00OOOOOO00O0OOOO00O0O0OO00OO00OO00O0OOOO00OO00OO00OO00OO00OOO0OO000OOOOO00O0O0OO000OO0OO00OOO0OO00OOOOOO00O0O0OO00O0OOOO00OO0OOO00OO00OO00OOO0OO00OO0OOO00O0O0OO00O0O0OO00OOO0OO00O000OO00OOO0OO00OO00OO00OOOOOO00OOOOOO00OOO0OO00O0O0OO00OO0OOO00OOO0OO00O00OOO00OO0OOO00OO0OOO000OOOOO00OOOOOO00O0OOOO00O0O0OO000OOOOO00OO0OOO00O0O0OO00O0O0OO00OO0OOO00OO00OO00OOOOOO00OOO0OO00O00OOO00O0OOOO00O00OOO00O00OOO00OOO0OO00OOOOOO00O0O0OO00OO00OO00OO0OOO00OO0OOO00O000OO00OOOOOO000OOOOO00O0OOOO00OOOOOO00O0OOOO00OO00OO00OO0OOO00O0OOOO00OO00OO000OO0OO00O0OOOO00O000OO00O00OOO00OOOOOO00OO00OO00O0O0OO00O0O0OO00O00OOO00O0OOOO000OO0OO00OOOOOO00O000OO00OO0OOO000OO0"
c = "O0000OO0O0000O00O00O0O00O000O0OOO000OO0OO00OOO00O0O0O00OO00O000OO00O00OOO00OO0OOO00OOO00O0O00000OO00OOO0O000OO00O00O0000O0OOO0O0O000O0O0O00O0OO0O00000O0O0OO0OO0O0O00000OO00OOO0O0OO0OO0O00O0OOOO000O0OOO00O0OO0O0O00000O0O00000O0O00000O00O0OO0O0O00000O00O00OOO00OO0O0O00OO0OOO000OO00O0O00000O0O0O000O0OO0OOOOO00O0OOOO000000O000O0OOO00O00O0O000OO00O0OOO0OOOO00OOOOO00O00O0O00O0OO0O0O00000O000O0OOO0O0OOOOOO00OO00OO0OO000O0O0OO00O00OO00OO000O0O0O0O00000O00OO00OO00OO00OOO00OOO0O0O0O0OOO00O0000O0O0OO0OO00OO0O0O0O00000"

if (func3(func2(func1(a,func5(func4(b)))))) == c:
    print("\t\t\t\t\t\t\t\tCORRECT!")
else:
    print("\t\t\t\t\t\t\t\tWRONG!")
```

Oops ![image](https://github.com/san601/WannaGame-Freshman-2023/assets/144963803/ac23428b-9183-4cfa-a866-3e57888c3d0a)

We need to know how data is being manipulated so that we can reverse the proccess.

```python=
if (func3(func2(func1(a,func5(func4(b)))))) == c:
    print("\t\t\t\t\t\t\t\tCORRECT!")
else:
    print("\t\t\t\t\t\t\t\tWRONG!")
```

So basically, func4 and func5, which are applied to string b, will return a list of 2-digit numbers that will be used to shuffle our input. We need to get that string first.

```python=
index = func5(func4(b))
print(index)
```
This return
```51023114061911262237423644094857534163035001382045343318591054231255171300152162280458255230164661053227084043243947603556490729```

One more thing to be consider is func5 and func2 are actually doing opposite things. On one side, func2 converts string of character to string of binary. On the other si binary string back to string of character. We can use this insight to reverse back to the original state of a string.

```python=
'''
def func3(param):
    return param.replace("0", "O").replace("1", "0")
'''
def func3_rev(param):
    return param.replace("0", "1").replace("O", "0")

def func5(param):
    result = ""
    for i in range(0, len(param), 8):
        bin_str = param[i:i+8]
        num = int(bin_str, 2)
        char = chr(num)
        result += char
    return result

print(func5(func3_rev(c)))
```
 
This result in the shuffled string 
```y{ktrcVnldc_1soEui}I_1Ihti___i_leds_WH4?tmsD0mi_tP3'Sfu_ff1ToRe_```

Our last step is to reverse it back to the flag using the index string above.

```python=
flag = list("a" * len(res))
# Same algo as func1
list_num = [int(index[i:i+2],10) for i in range(0,len(index),2)]
for i in range(len(list_num)):
    # A bit tricky but not hard
    flag[list_num[i]] = res[i]
print(''.join(flag))
```

And this prints out 
```
W1{ImPreSsiVe_tHis_ch4ll_Dn't_mk3_iT_dIfficu1t_foR_y0u_doEs_1t?}
```
