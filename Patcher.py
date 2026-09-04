IP = "192.168.178.73"
PORT = 9339

def patch():
    with open("Clash of Clans", "rb") as f:
        data = bytearray(f.read())
    host_offset = data.find(b'game.clashofclans.com')

    if host_offset == -1:
        print("[-] Couldn't find game.clashofclans.com")
        return

    if len(IP.encode()) > len(b'game.clashofclans.com'):
        raise ValueError(
            f"IP is too long! Max {len(b'game.clashofclans.com')} characters."
        )

    padded = IP.encode() + b"\x00" * (len(b'game.clashofclans.com') - len(IP.encode()))
    data[host_offset:host_offset + len(b'game.clashofclans.com')] = padded

    print(f"[+] Host patched at 0x{host_offset:X}")

    old_port = (9339).to_bytes(2, "big")
    new_port = PORT.to_bytes(2, "big")

    count = 0
    start = 0

    while True:
        idx = data.find(old_port, start)
        if idx == -1:
            break

        data[idx:idx + 2] = new_port
        print(f"[+] Port Patched at 0x{idx:X}")
        count += 1
        start = idx + 2

    with open("Clash of Clans", "wb") as f:
        f.write(data)

    print(f"\nClient Patched. Enjoy!")

if __name__ == "__main__":
    patch()
