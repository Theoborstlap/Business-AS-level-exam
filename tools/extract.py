import sys, re


def extract(path, max_pages=2):
    data = open(path, 'rb').read()
    # find content streams
    streams = re.findall(rb'stream\r?\n(.*?)\r?\nendstream', data, re.S)
    out_pages = []
    for s in streams[:max_pages]:
        txt = []
        for m in re.finditer(rb'\((.*?)(?<!\\)\)\s*Tj', s, re.S):
            raw = m.group(1)
            raw = raw.replace(b'\\(', b'(').replace(b'\\)', b')').replace(b'\\\\', b'\\')
            try:
                txt.append(raw.decode('cp1252'))
            except Exception:
                txt.append(raw.decode('latin-1', 'replace'))
        out_pages.append('\n'.join(txt))
    return out_pages


if __name__ == '__main__':
    path = sys.argv[1]
    pages = extract(path, int(sys.argv[2]) if len(sys.argv) > 2 else 2)
    for i, p in enumerate(pages, 1):
        print(f"===== PAGE {i} =====")
        print(p)
