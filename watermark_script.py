from PIL import Image

fn = "photo.jpg" # Original photo
img = Image.open(fn) # Download it
watermark_white = Image.open('Source\watermark_white.png') # Light watermark
watermark_black = Image.open('Source\watermark_black.png') # Dark watermark

# Choice watermark
choice = int(input("Белая или чёрная? (1/2)\n> ")) 
if choice == 1:
    watermark = watermark_white
else:
    watermark = watermark_black


(width1, height1) = img.size # Image size
(width2, height2) = watermark.size # Watermark size
up_margin, bottom_margin, left_margin, right_margin = 50, 50, 50, 50 # Отступы

# Paste watermark with margrin
img.paste(watermark, (width1 - width2 - bottom_margin, height1 - height2 - right_margin),  watermark)
img.save(f"{fn[:fn.find('.')]}_wm.png") # Save it (name of original photo + "_wm")