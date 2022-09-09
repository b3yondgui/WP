
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