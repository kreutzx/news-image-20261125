"""Copy the pre-rendered entry.png front page to the output directory.
Standard library only; output verified byte-identical (length + SHA-256).
"""

import hashlib
import os
import shutil
import sys

def file_digest(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()

def verify_identical(src, dst):
    if os.path.getsize(src) != os.path.getsize(dst):
        return False
    return file_digest(src) == file_digest(dst)

def source_path():
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "entry.png")

def output_path():
    dest_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(dest_dir, "entry.png")

def copy_entry():
    src = source_path()
    dst = output_path()
    dest_dir = os.path.dirname(dst)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    os.chmod(dst, 0o644)
    return src, dst

def main():
    src, dst = copy_entry()
    if not verify_identical(src, dst):
        print("error: output is not byte-identical to source", file=sys.stderr)
        return 1
    print("Copied entry.png to " + dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
