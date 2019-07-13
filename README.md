# ssscache2john
Convert SSSD cache files to John The Ripper format

## Example
```
./ssscache2john.py /var/lib/sss/cache_LDAP.ldb >sss.hashes
john --wordlist=foo.bar sss.hashes
```
