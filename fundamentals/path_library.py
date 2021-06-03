from pathlib import Path

# absolute path
# /urs/...

# relative path
path = Path("sample_dir")
print(path.exists())
print(path.mkdir())
print(path.rmdir())

path = Path("")
for file in path.glob('*.py'):
    print(file)