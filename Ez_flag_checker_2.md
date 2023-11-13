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

Continue examining using IDA, a bunch of ptrace function appeared so I knew that this was the anti-debugging mechanism. 

It's very easy to bypass this, just set a breakpoint at ptrace function, finish the function and then set RAX register to 0x0. [For more information](https://jaybailey216.com/debugging-stripped-binaries/)

I'll use IDA to demonstrate the proce

