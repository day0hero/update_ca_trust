# update_ca_trust
Use this program to update the certificate trust on a Linux (RHEL/CentOS/Fedora) system. 

### Program execution:
```python
python3 update_ca_trust.py <certificate_authority_pem_file>
```
### What's happening?
- Program accepts a single argument (root certificate)
- Converts input to absolute path
- Copies the certificate to `/etc/pki/ca-trust/source/anchors/`
- Runs `update-ca-trust extract`


