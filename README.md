# Bypass top tier WAF through junk
This bypass works in cases where the WAF does not limit the size of POST/PUT/PATCH/DELETE type requests. It works on the following WAF services:
- [X] AWS WAF.
- [X] GCP WAF (Google cloud armor).
- [X] Cloudflare.
- [X] Akamai.
- [X] Azure WAF.
- [X] Fortiweb by Fortinet.
- [X] Barracuda WAF.
- [X] Sucuri.
- [X] Radware AppWall.
- [X] F5 BIG-IP WAAP.
- [X] Palo Alto.


# TO-DO
- [X] Support JSON requests.
- [ ] Support URL Encoded requests.
- [ ] Support Multipart requests.
- [ ] Support XML requests.

# Installation
https://docs.mitmproxy.org/stable/overview-installation/

# Configuration

1) git clone https://github.com/david-botelho-mariano/bypass-top-tier-WAF-through-junk/
2) cd bypass-top-tier-WAF-through-junk
3) docker run --rm -it -v "./bypass-top-tiers-WAF-with-junk.py:/bypass-top-tiers-WAF-with-junk.py" -p 1234:1234 mitmproxy/mitmproxy mitmproxy -p 1234 -s /bypass-top-tiers-WAF-with-junk.py

4) curl -x http://127.0.1:1234 -H "Content-Type: application/json" -d '{"foo":"bar"}' https://public.requestbin.com/r/en5tykm755uhh

# Inspired by the following work:
- https://github.com/assetnote/nowafpls
