# Bypass top tiers WAF with junk
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
- [ ] Support URL Encoded requests.
- [ ] Support Multipart requests.
- [ ] Support XML requests.

# Inspired by the following work:
- https://github.com/assetnote/nowafpls
