## Space Relays

题目提供了一个chall.pcap流量包。

用wireshark打开，可以发现只有TCP包，且源和目的IP都是相同的。

我们再看data部分，发现是A与B之间的通信。

追踪TCP流：

```python
Hi Rain Turkey
 
Nice Meeting you D4663R!!
 
I am have secret message retrived from Russia Army which could highly help Ukraine
 
Ohh is it form of text or morse code or did they use any form of encryption
 
I have found the message but I am sharing with you inform of PNG image
 
Got it!
 
I hope you have got all checksum which I send you in mail
 
Yah got them.
 
Now I am sending
 
Ok
 
7a
 
Mismatch, It should be 7647966b7343c29048673252e490f736
```

可以知道，通信流量传输的是一张PNG图片。而且，使用明文或哈希值进行传输。

如果传输的数据是错误的，回复消息会提示“7aMismatch, It should be  XXXXXX”。





先提取出tcp.payload字段：

```bash
tshark -r chall.pcap -T fields -e tcp.payload -Y "tcp.payload" > chall.txt
```



再将字段转换为图片的十六进制数据：

```python

import hashlib

dmd5 = {}
for i in range(256):
    s = str(hex(i)[2:].zfill(2))
    h = hashlib.md5(s.encode()).hexdigest()
    dmd5[h] = s
    # print(s,h)

lines = open(r"C:\\Users\\l\\Downloads\\chall.txt",'r').readlines()
content = ''
for i in range(0,len(lines),2):
    send = lines[i].strip()
    assert(len(send)==4)
    s1 = chr(int(send[0:2],16))
    s2 = chr(int(send[2:4],16))
    s = s1+s2
    res = lines[i+1].strip()
    ls1 = [chr(int(res[j:j+2],16)) for j in range(0,len(res), 2)]
    res2 = ''.join(ls1)
    # Mismatch, It should be 
    
    if 'Mismatch' in res2:
        md5hash = res2[len("Mismatch, It should be "):]
        content += dmd5[md5hash]
    else:
        content += s

with open('C:\\Users\\l\\Downloads\\3.txt', 'w') as f:
    f.write(content)
```



用010Editor将十六进制数据保存为图片。



![1662718226783](wp.assets/1662718226783.png)

```
flag{84eb28300b2ce04827d81e057b0bfc1d_pi3c3S_M4Ke$_in7O_A_4RT}
```



