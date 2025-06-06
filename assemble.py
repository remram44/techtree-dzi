import os
from PIL import Image
import shutil
import subprocess


# List all images
images = {}
total = 0
for entry in os.listdir('01-raw'):
    if entry == '.' or entry == '..':
        continue
    basename, ext = entry.split('.')
    assert ext == 'png'
    x, y = basename.split('_')
    x = int(x, 10)
    y = int(y, 10)
    images.setdefault(x, set()).add(y)
    total += 1


# Build ordered array
images = [(x, list(sorted(col))) for x, col in images.items()]
images.sort()


# Create VIPS image
try:
    os.remove('out.v')
except FileNotFoundError:
    pass
try:
    os.remove('out2.v')
except FileNotFoundError:
    pass
subprocess.check_call(['vips', 'black', 'out.v', '100', '100'])


count = 0
tx = 0
for x, col in images:
    #if x > 5000:  # DEBUG
    #    break

    cx1 = 20
    if x == 0:
        cx1 = 0
    cx2 = 1920
    ymax = max(col)

    ty = 0
    for y in col:
        # Crop
        img = Image.open(f'01-raw/{x:06}_{y:06}.png')
        cy1 = 55
        if y == 0:
            cy = 0
        cy2 = 885
        if y == ymax:
            cy2 = 951
        cropped = img.crop((cx1, cy1, cx2, cy2))
        cropped.save('tmp.png')

        subprocess.check_call([
            'vips', 'insert',
            'out.v',
            'tmp.png',
            'out2.v',
            f'{tx}', f'{ty}',
            '--expand=1',
        ])
        os.rename('out2.v', 'out.v')
        count += 1
        print(f"{count} / {total}")

        ty += cy2 - cy1

    tx += cx2 - cx1

try:
    shutil.rmtree('out')
except FileNotFoundError:
    pass
os.mkdir('out')
subprocess.check_call(['vips', 'dzsave', 'out.v', 'out/out', '--suffix', '.png'])
