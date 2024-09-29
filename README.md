# Bypass top tier WAF through junk
This tool works in cases where the WAF does not limit the size of POST/PUT/PATCH/DELETE type requests. It works on the following WAF services:
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
mitmproxy --set block_global=false -s modify_request.py

curl -x http://84.247.175.xxx:8080 -H "Content-Type: application/json" -d '{"foo":"bar"}' http://xopo91d41t.oastify.com/

# Inspired by the following work:
- https://github.com/assetnote/nowafpls
