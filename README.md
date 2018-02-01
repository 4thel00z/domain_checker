# Domain Checker

[![asciicast](https://asciinema.org/a/96taoEnEMRx2fYOGxUGFt70DL.png)](https://asciinema.org/a/96taoEnEMRx2fYOGxUGFt70DL)

This script can be used to check if the domain you want is already registered.

```
python3 domain_checker.py test

 ['test---------------------------------------------shghsgjsss.website',
 'test-----hey.website',
 'test---server.com',
 'test---site.com',
 'test--ggfgfgh.club',
 'test--page.com',
 'test--server.com',
 'test--site.com',
 'test--testyesue3.space', ...
 
# Write to a file 
python3 domain_checker.py test --out /tmp/domains.json
 
# Write to a file and do not write to stdout
python3 domain_checker.py test --out /tmp/domains.json --print False
 

```