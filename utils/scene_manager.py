from utils import title_scene

class SceneMananger(object):
    def __init__(self):
        self.go_to(title_scene.TitleScene())

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self