import os

TEXT = "I told my son the trampoline is broken, so he can't jump to conclusions anymore."

assert 1 <= len(TEXT) <= 200

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
