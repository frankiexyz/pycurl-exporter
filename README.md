# pycurl-exporter
A simple Prometheus exporter for curl

By using pycurl, you can exporter the metric for a curl result.


The exporter will collect stuffs like curl total time, pretransfer time, name looking time and also HTTP status code.


And we can actually collect some unique headers like Cloudflare RAYID. 


All you need to do is install pycurl "pip install pycurl" 
```
pip install pycurl
```


Expected output is like the following
```
#curl test123.xyz:9095/?target=test123.com/test.png
NAMELOOKUP_TIME 0.061559
CONNECT_TIME 0.077495
STATUS_CODE 200
PRETRANSFER_TIME 0.077974
REDIRECT_TIME 0.0
STARTTRANSFER_TIME 0.123312
TOTAL_TIME 0.171082
CF_HIT 1

```
