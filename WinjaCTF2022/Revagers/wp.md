# Revagers



```bash
$ file vault
vault: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=6e13567d323e964495a72a78a8333208dc7aaf40, for GNU/Linux 3.2.0, stripped
```



Using IDA64 to disassemble, and we get c pseu-code:

```c
__int64 __fastcall main(int a1, char **a2, char **a3)
{
  if ( a1 == 2 )
  {
    if ( strlen(a2[1]) == 41 )
      sub_1159(a2[1]);
    else
      printf("[!] Incorrect Passcode");
  }
  else
  {
    printf("[!] ERR! Usage ./vault <Passcode>");
  }
  return 0LL;
}
```



so the flag's length is 41.



sub_1159(a2[1]) function:

```c
int __fastcall sub_1159(const char *a1)
{
int result; // eax

result = *((unsigned __int8 *)a1 + 1);
if ( (_BYTE)result == 57 )
{
result = *((unsigned __int8 *)a1 + 15);
if ( (_BYTE)result == 53 )
{
result = *((unsigned __int8 *)a1 + 33);
if ( (_BYTE)result == 83 )
{
result = *((unsigned __int8 *)a1 + 4);
if ( (_BYTE)result == 50 )
{
result = *((unsigned __int8 *)a1 + 16);
if ( (_BYTE)result == 54 )
{
result = *((unsigned __int8 *)a1 + 7);
if ( (_BYTE)result == 53 )
{
result = *((unsigned __int8 *)a1 + 10);
if ( (_BYTE)result == 97 )
{
result = *((unsigned __int8 *)a1 + 32);
if ( (_BYTE)result == 95 )
{
result = *((unsigned __int8 *)a1 + 19);
if ( (_BYTE)result == 54 )
{
result = *((unsigned __int8 *)a1 + 6);
if ( (_BYTE)result == 56 )
{
result = *((unsigned __int8 *)a1 + 40);
if ( (_BYTE)result == 68 )
{
result = *((unsigned __int8 *)a1 + 25);
if ( (_BYTE)result == 51 )
{
result = *((unsigned __int8 *)a1 + 5);
if ( (_BYTE)result == 51 )
{
result = *((unsigned __int8 *)a1 + 31);
if ( (_BYTE)result == 102 )
{
result = *((unsigned __int8 *)a1 + 38);
if ( (_BYTE)result == 48 )
{
result = *((unsigned __int8 *)a1 + 21);
if ( (_BYTE)result == 102 )
{
result = *((unsigned __int8 *)a1 + 8);
if ( (_BYTE)result == 51 )
{
result = *((unsigned __int8 *)a1 + 39);
if ( (_BYTE)result == 82 )
{
result = *((unsigned __int8 *)a1 + 23);
if ( (_BYTE)result == 48 )
{
result = *((unsigned __int8 *)a1 + 12);
if ( (_BYTE)result == 51 )
{
result = *((unsigned __int8 *)a1 + 24);
if ( (_BYTE)result == 102 )
{
result = *(unsigned __int8 *)a1;
if ( (_BYTE)result == 56 )
{
result = *((unsigned __int8 *)a1 + 14);
if ( (_BYTE)result == 53 )
{
result = *((unsigned __int8 *)a1 + 26);
if ( (_BYTE)result == 54 )
{
result = *((unsigned __int8 *)a1 + 27);
if ( (_BYTE)result == 50 )
{
result = *((unsigned __int8 *)a1 + 13);
if ( (_BYTE)result == 101 )
{
result = *((unsigned __int8 *)a1 + 28);
if ( (_BYTE)result == 48 )
{
result = *((unsigned __int8 *)a1 + 9);
if ( (_BYTE)result == 52 )
{
result = *((unsigned __int8 *)a1 + 29);
if ( (_BYTE)result == 53 )
{
result = *((unsigned __int8 *)a1 + 20);
if ( (_BYTE)result == 99 )
{
result = *((unsigned __int8 *)a1 + 11);
if ( (_BYTE)result == 49 )
{
result = *((unsigned __int8 *)a1 + 37);
if ( (_BYTE)result == 49 )
{
result = *((unsigned __int8 *)a1 + 36);
if ( (_BYTE)result == 114 )
{
result = *((unsigned __int8 *)a1 + 30);
if ( (_BYTE)result == 99 )
{
result = *((unsigned __int8 *)a1 + 17);
if ( (_BYTE)result == 55 )
{
result = *((unsigned __int8 *)a1 + 34);
if ( (_BYTE)result == 84 )
{
result = *((unsigned __int8 *)a1 + 3);
if ( (_BYTE)result == 99 )
{
result = *((unsigned __int8 *)a1 + 22);
if ( (_BYTE)result == 55 )
{
result = *((unsigned __int8 *)a1 + 18);
if ( (_BYTE)result == 50 )
{
result = *((unsigned __int8 *)a1 + 35);
if ( (_BYTE)result == 52 )
{
if ( a1[2] == 102 )
{
puts("[+] You cracked the vault.");
result = printf(
"[+] Your flag is flag{%s}",
a1);
}
else
{
result = printf("[!] Incorrect Passcode");
}
```

In the pseu-code, I get every byte of flag. 

After a carefully rearrangement, I get the following:

```
a1   ==56
a1+1 ==57
a1+2 ==102
a1+3 ==99
a1+4 ==50
a1+5 ==51
a1+6 ==56
a1+7 ==53
a1+8 ==51
a1+9 ==52
a1+10==97
a1+11==49
a1+12==51
a1+13==101
a1+14==53
a1+15==53
a1+16==54
a1+17==55
a1+18==50
a1+19==54
a1+20==99
a1+21==102
a1+22==55
a1+23==48
a1+24==102
a1+25==51
a1+26==54
a1+27==50
a1+28==48
a1+29==53
a1+30==99
a1+31==102
a1+32==95
a1+33==83
a1+34==84
a1+35==52
a1+36==114
a1+37==49
a1+38==48
a1+39==82
a1+40==68
```



```
56, 57, 102, 99, 50, 51, 56, 53, 51, 52, 97, 49, 51, 101, 53, 53, 54, 55, 50, 54, 99, 102, 55, 48, 102, 51, 54, 50, 48, 53, 99, 102, 95, 83, 84, 52, 114, 49, 48, 82, 68

FROM DECIMAL:
89fc238534a13e556726cf70f36205cf_ST4r10RD
```





flag{89fc238534a13e556726cf70f36205cf_ST4r10RD}