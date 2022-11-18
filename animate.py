def animate(image, image_index):
    image_index = increase_index()
    image = robot[image_index]
    window.blit(image, (250,150))