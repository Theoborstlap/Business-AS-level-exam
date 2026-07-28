import sys


def validate(path):
    data = open(path, 'rb').read()
    assert data[:8] == b'%PDF-1.4', 'bad header'
    assert data.rstrip().endswith(b'%%EOF'), 'no EOF'
    i = data.rfind(b'startxref')
    xref = int(data[i + 9:].split()[0])
    seg = data[xref:].split(b'\n')
    assert seg[0] == b'xref', seg[0]
    first, count = map(int, seg[1].split())
    bad = 0
    for n in range(1, count):
        off = int(seg[2 + n].split()[0])
        exp = ('%d 0 obj' % n).encode()
        if data[off:off + len(exp)] != exp:
            bad += 1
    pages = data.count(b'/Type /Page ')
    print(f"{path}: {len(data):,} bytes, {count-1} objects, ~{pages} pages, "
          f"xref-errors={bad}  {'OK' if bad == 0 else 'FAIL'}")
    return bad == 0


if __name__ == '__main__':
    ok = True
    for p in sys.argv[1:]:
        ok &= validate(p)
    sys.exit(0 if ok else 1)
