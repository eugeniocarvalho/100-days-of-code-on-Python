import colorgram

image_colors = colorgram.extract('/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-018/image.jpg', 30)

colors = []

for color in image_colors:
  element = (
    color.rgb.r,
    color.rgb.g,
    color.rgb.b
  )

  colors.append(element)

print(colors)