import check50

FILES = [
    "muppet_01_out.jpg",
    "muppet_02_out.jpg",
    "muppet_03_out.jpg",
    "muppet_04_out.jpg",
    "muppet_05_out.jpg",
    "muppet_06_out.jpg",
]

for file in FILES:
    print(check50.hash(file))