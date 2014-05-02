from melty.baseobjects import Blank, Clip, Playlist, Transition, Tractor

class MLTFile():
    def __init__(self, data):
        self.data = data
        self.profile = {
            "description" : "HD 25",
            "width" : 1920, 
            "height" : 1080, 
            "progressive" : 1, 
            "sample_aspect_num" : 1, 
            "sample_aspect_den" : 1, 
            "display_aspect_num" : 16,
            "display_aspect_den" : 9, 
            "frame_rate_num" : 25,
            "frame_rate_den" : 1, 
            "colorspace" : 709
            }

    def __repr__(self):
        wfile = """<?xml version="1.0" encoding="utf-8"?>\n"""
        wfile+= """<mlt>\n"""
        wfile+= """<profile {}/>\n""".format(" ".join(["{}=\"{}\"".format(key, self.profile[key]) for key in self.profile.keys() ]))
        wfile+= str(self.data)
        wfile+= """</mlt>\n"""
        return wfile

    def save(self, fname):
        f = open(fname, "w")
        f.write(self.__repr__())
        f.close()

