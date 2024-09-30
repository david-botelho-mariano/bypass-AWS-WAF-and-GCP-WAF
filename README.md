# Bypass top tier WAF through junk
This bypass tool works in cases where the WAF does not limit the size of POST/PUT/PATCH/DELETE type requests. It works on the following WAF services:
- [X] AWS WAF
- [X] GCP WAF (Google cloud armor)
- [X] Cloudflare
- [X] Akamai
- [X] Azure WAF
- [X] Fortiweb by Fortinet
- [X] Barracuda WAF
- [X] Sucuri
- [X] Radware AppWall
- [X] F5 BIG-IP WAAP
- [X] Palo Alto

# TO-DO
- [X] Support JSON requests
- [ ] Support URL Encoded requests
- [ ] Support Multipart requests
- [ ] Support XML requests

# Installation and configuration

1) `git clone https://github.com/david-botelho-mariano/bypass-top-tier-WAF-through-junk/`
2) `cd bypass-top-tier-WAF-through-junk`
3) `docker run --rm -it -v "./bypass-top-tiers-WAF-with-junk.py:/bypass-top-tiers-WAF-with-junk.py" -p 1234:1234 mitmproxy/mitmproxy mitmproxy -p 1234 -s /bypass-top-tiers-WAF-with-junk.py`
4) Configure your tool to use the following proxy: "http://127.0.0.1:1234". For example:
    1) `curl -x http://127.0.1:1234 -H "Content-Type: application/json" -d '{"foo":"bar"}' https://public.requestbin.com/r/en5tykm755uhh`
    2) `sqlmap -u "http://example.com/vulnerable_page.php?id=1" --proxy "http://127.0.0.1:1234"`
    3) In burp suite: <img width="1440" alt="image" src="https://github.com/user-attachments/assets/0af30b85-6c5e-447e-91e2-ca7da7f06b12">


# Inspired by the following work:
- https://github.com/assetnote/nowafpls
