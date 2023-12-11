import dataclasses

import gphoto2 as gp


@dataclasses.dataclass
class Config:
    camera: gp.Camera

    def __init__(self, camera):
        self.camera = camera
        self.camera_config = self.camera.get_config()

    def _resolve_nested(self, name):
        names = name.split('.')
        widget = self.camera_config
        for n in names:
            widget = widget.get_child_by_name(n)
        return widget

    def _choice_index(self, widget, value):
        choices = [widget.get_choice(i) for i in range(widget.count_choices())]
        if value in choices:
            return choices.index(value)
        return None

    def __getitem__(self, name):
        widget = self._resolve_nested(name)
        return widget.get_value()

    def __setitem__(self, name, value):
        widget = self._resolve_nested(name)
        widget_type = widget.get_type()

        if widget_type == gp.GP_WIDGET_RADIO or widget_type == gp.GP_WIDGET_MENU:
            value_index = self._choice_index(widget, value)
            if value_index is not None:
                widget.set_value(value)
                return
        widget.set_value(value)

    def choices(self, name):
        widget = self._resolve_nested(name)
        widget_type = widget.get_type()

        if widget_type not in [gp.GP_WIDGET_RADIO, gp.GP_WIDGET_MENU]:
            return None

        choices = [widget.get_choice(i) for i in range(widget.count_choices())]
        return choices

    def _to_dict(self, widget, result: dict):
        children_count = widget.count_children()
        for i in range(children_count):
            child = widget.get_child(i)
            name = child.get_name()
            if child.count_children() > 0:
                result[name] = {}
                self._to_dict(child, result[name])
            else:
                value = child.get_value()
                result[name] = value

    def to_dict(self):
        root_dict = {}
        self._to_dict(self.camera_config, root_dict)
        return root_dict

    def from_dict(self, config_dict: dict, current_widget=None):
        if current_widget is None:
            current_widget = self.camera_config

        for key, value in config_dict.items():
            try:
                child_widget = current_widget.get_child_by_name(key)
            except gp.GPhoto2Error:
                print(f"Warning: Config key '{key}' not found in camera config.")
                continue

            if isinstance(value, dict):
                self.from_dict(value, child_widget)
            else:
                widget_type = child_widget.get_type()
                if widget_type == gp.GP_WIDGET_RADIO or widget_type == gp.GP_WIDGET_MENU:
                    value_index = self._choice_index(child_widget, value)
                    if value_index is not None:
                        if child_widget.get_value() == value:
                            print(f"ignoring value for {key} - already set")
                            continue
                        print(f"setting value for {key}: {value}")
                        child_widget.set_value(value)
                        continue
                if value is not None:
                    if child_widget.get_value() != value:
                        print(f"ignoring value for {key} - already set")
                        continue
                    print(f"setting value for {key}: {value}")
                    child_widget.set_value(value)


camera = gp.Camera()
config: Config
try:
    camera.init()
    # text = camera.get_summary()
    # print('Summary')
    # print('=======')
    # print(str(text))
    config = Config(camera)
except gp.GPhoto2Error as e:
    print(e)
    print(f"Try: killall gvfsd-gphoto2")

config['capturetarget'] = 'Internal RAM'
config['capturesettings.shutterspeed'] = '1'
import pprint

pprint.pprint(config.to_dict())
print(config.choices('capturesettings.shutterspeed'))
# config = camera.get_config()
# target = config.get_child_by_name('capturetarget')
# value = target.get_choice(0)
# target.set_value(value)
# camera.set_config(config)
# config = camera.get_config()
# for k,v in config.items():
#     print(f"{k}: {v}")
# target = config.get_child_by_name('capturetarget')
# choices = gp.CameraWidget.get_choices(target)
# for k in target.get_choices():
#     print(f"{k}")
# target.set_value('Internal RAM')
print(f"Capturing to {camera.get_config().get_child_by_name('capturetarget').get_value()}")
# help(camera.capture)
# help(camera.wait_for_event)
file_path = camera.capture(gp.GP_CAPTURE_IMAGE)
print(f"{file_path.folder}/{file_path.name}")
camera_file = camera.file_get(file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL)
camera_file.save(f'/home/johntron/Downloads/{file_path.name}')
event_type, event_data = camera.wait_for_event(20 * 1000)
if event_type == gp.GP_EVENT_CAPTURE_COMPLETE:
    print("capture complete")
if event_type == gp.GP_EVENT_FILE_ADDED:
    print("file added")
if event_type == gp.GP_EVENT_TIMEOUT:
    print("timeout")
if event_type == gp.GP_EVENT_UNKNOWN:
    print("unknown")
print(event_data)
camera.exit()
