import os

PRE = """
<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Quicksand">
<link rel="stylesheet" href="./style.css">

<head>
    <title>Parks</title>
    <link rel="icon" href="./images/sunsets/sunset.png">
</head>

<body>
<h1>National Parks!</h1>
<p>I enjoy touching grass, and I've been to a few national parks. Here are some of my favorite scenes I've photographed.</p>
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
    html += '<table>\n'
    for i in range(0, len(parks), 3):
        html += '    <tr>\n'
        for j in range(3):
            if i + j < len(parks):
                park = parks[i + j]
                fullsize_url = get_fullsize_URL(park)
                thumbnail_url = get_thumbnail_URL(park)
                html += f'        <td><a href="{fullsize_url}"><img src="{thumbnail_url}" height="240"></a></td>\n'
        html += '    </tr>\n'
        html += '    <tr>\n'
        for j in range(3):
            if i + j < len(parks):
                park = parks[i + j]
                html += f'        <td>{get_title(park)}</td>\n'
        html += '    </tr>\n'
    html += '</table>\n'
    html += '</body>\n</html>'
    return html

with open('parks.html', 'w') as f:
    f.write(generate_html())
