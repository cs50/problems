import sys

from PIL import Image, ImageOps

EXTENSIONS = (".jpg", ".jpeg", ".png")

# Ensure proper usage
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

# Ensure JPEG or PNG
if not sys.argv[1].lower().endswith(EXTENSIONS):
    sys.exit("Invalid input")
if not sys.argv[2].lower().endswith(EXTENSIONS):
    sys.exit("Invalid output")

# Open shirt
try:
    shirt = Image.open("shirt.png")
except FileNotFoundError:
    sys.exit("Missing shirt")

# Open photo
try:
    photo = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")

# Resize photo
photo = ImageOps.fit(photo, shirt.size)

# Overlay shirt
photo.paste(shirt, shirt)

# Save result
photo.save(sys.argv[2])
