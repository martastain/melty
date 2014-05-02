import uuid

from melty.utils import *


class Blank():
    def __init__(self, duration):
        assert type(duration) == int
        self.duration = duration

    def __repr__(self):
        return "<blank length=\"{}\"/>\n".format(self.duration)


class Clip():
    def __init__(self, path, **kwargs):
        self.id   = str(uuid.uuid1())
        self.path = path
        self.args = kwargs

    def __repr__(self):
        wfile = """<producer id="{}">\n""".format(self.id)
        wfile+= """    <property name="resource">{}</property>\n""".format(self.path)
        wfile+= indent(mkprops(self.args))
        wfile+= """</producer>\n"""
        return wfile


class Transition():
    def __init__(self, **kwargs):
        self.args = kwargs

    def __repr__(self):
        wfile = """<transition>\n"""
        wfile+= indent(mkprops(self.args))
        wfile+= """</transition>\n"""
        return wfile


class Playlist():
    def __init__(self):
        self.id   = str(uuid.uuid1())
        self.segments = []

    def add(self, segment):
        assert type(segment) in [Blank, Clip]
        self.segments.append(segment)

    def add_clip(self, path, **kwargs):
        self.add(Clip(path, **kwargs))

    def add_blank(self, duration):
        self.add(Blank(duration))

    def __repr__(self):
        wfile = """<playlist id="{}">\n""".format(self.id)
        for segment in self.segments:
            wfile += indent(segment.__repr__())
        wfile += """</playlist>\n"""
        return wfile


class Tractor():
    def __init__(self):
        self.tracks = []
        self.transitions = []

    def add_track(self, track):
        assert type(track) in [Clip, Playlist, Tractor]
        self.tracks.append(track)

    def add_transition(self, transition=False, **kwargs):
        if transition:
            assert type(transition) == Transition
        else:
            transition = Transition(**kwargs)
        self.transitions.append(transition)

    def __repr__(self):
        wfile = """<tractor>\n"""
        wfile+= """    <multitrack>\n"""
        for track in self.tracks:
            wfile += indent(track.__repr__(), 8)
        wfile+= """    </multitrack>\n"""
        if self.transitions:
            for transition in self.transitions:
                wfile += indent(transition.__repr__(), 4)
        wfile+= """</tractor>\n"""
        return wfile


