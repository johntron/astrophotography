import gphoto2 as gp
camera = gp.Camera()
camera.init()
text = camera.get_summary()
print('Summary')
print('=======')
print(str(text))
camera.exit()