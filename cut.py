import marimo

__generated_with = "0.13.11"
app = marimo.App(width="medium")


@app.cell
def _():
    from PIL import Image
    return (Image,)


@app.cell
def _(Image):
    im = Image.open('01-raw/131100_000000.png')
    im
    return (im,)


@app.cell
def _(im):
    im.size
    return


@app.cell
def _(im):
    cropped_top = im.crop((0, 48, 100, 100))
    cropped_top
    return


@app.cell
def _(im):
    cropped_bottom = im.crop((0, 800, 100, 885))
    cropped_bottom
    return


@app.cell
def _(im):
    cropped10 = im.crop((10, 0, 1910, 875))
    cropped10
    return (cropped10,)


@app.cell
def _(Image):
    cropped11 = Image.open('01-raw/131100_000820.png').crop((10, 55, 1910, 875))
    cropped11
    return (cropped11,)


@app.cell
def _(Image):
    cropped12 = Image.open('01-raw/131100_001640.png').crop((10, 55, 1910, 875))
    cropped12
    return (cropped12,)


@app.cell
def _(Image):
    cropped13 = Image.open('01-raw/131100_002460.png').crop((10, 55, 1910, 951))
    cropped13
    return (cropped13,)


@app.cell
def _(Image):
    cropped00 = Image.open('01-raw/129200_000000.png').crop((10, 0, 1910, 875))
    cropped00
    return (cropped00,)


@app.cell
def _(Image):
    cropped01 = Image.open('01-raw/129200_000820.png').crop((10, 55, 1910, 875))
    cropped01
    return (cropped01,)


@app.cell
def _(Image):
    cropped02 = Image.open('01-raw/129200_001640.png').crop((10, 55, 1910, 875))
    cropped02
    return (cropped02,)


@app.cell
def _(Image):
    cropped03 = Image.open('01-raw/129200_002460.png').crop((10, 55, 1910, 951))
    cropped03
    return (cropped03,)


@app.cell
def _(
    Image,
    cropped00,
    cropped01,
    cropped02,
    cropped03,
    cropped10,
    cropped11,
    cropped12,
    cropped13,
):
    images = [[cropped00, cropped01, cropped02, cropped03], [cropped10, cropped11, cropped12, cropped13]]

    w = sum(col[0].size[0] for col in images)
    h = sum(img.size[1] for img in images[0])
    result = Image.new('RGBA', (w, h))

    x = 0
    for col in images:
        col_w = col[0].size[0]
        y = 0
        for img in col:
            result.paste(img, (x, y))
            y += img.size[1]
        x += col_w
    result
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
