import os

PRE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Parks</title>
    <link rel="icon" href="./images/sunsets/sunset.png">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Quicksand">
    <link rel="stylesheet" href="./style.css">
</head>

<body class="parks-page">
    <h1>National Parks!</h1>
    <p>I enjoy touching grass, and I've been to a few national parks. Here are some of my favorite scenes I've photographed.</p>

    <main>
        <section aria-label="Photo gallery of national parks" class="parks-gallery">

"""

def get_parks():
    parks = []
    for filename in os.listdir('./images/parks'):
        if filename.endswith('.JPG'):
            park_name = filename[:-4]
            parks.append(park_name)
    return sorted(parks)

def get_fullsize_URL(park: str) -> str:
    if park == 'grand canyon':
        return r"https://media.githubusercontent.com/media/albtang/albtang.github.io/main/images/parks/grand%20canyon.jpg"
    return f"https://media.githubusercontent.com/media/albtang/albtang.github.io/main/images/parks/{park}.JPG"

def get_thumbnail_URL(park: str) -> str:
    return f"https://media.githubusercontent.com/media/albtang/albtang.github.io/main/images/parks/{park}-thumbnail.jpg"

def get_title(park: str) -> str:
    if park == 'joshua':
        return 'Joshua Tree'
    if park == 'rainier':
        return 'Mt. Rainier'
    return park.title()

def generate_html():
    parks = get_parks()
    html = PRE
    tab = '    '
    for park in parks:
        html += 3 * tab + '<figure class="park-card">\n'
        fullsize_url = get_fullsize_URL(park)
        thumbnail_url = get_thumbnail_URL(park)
        title = get_title(park)
        html += 4 * tab + f'<a href="{fullsize_url}">\n'
        html += 5 * tab + f'<img src="{thumbnail_url}" width="240" height="240" loading="lazy" decoding="async" alt="{title}">\n'
        html += 4 * tab + f'</a>\n'
        html += 4 * tab + f'<figcaption>{title}</figcaption>\n'
        html += 3 * tab + '</figure>\n'
    html += 2 * tab + '</section>\n'
    html += tab + '</main>\n'
    html += '</body>\n</html>\n'
    return html

with open('parks.html', 'w') as f:
    f.write(generate_html())
