__all__ = ["indent", "mkprops"]

def indent(istr, w=4):
    return "\n".join(["{}{}".format(" "*w, line) for line in istr.split("\n") if line]) + "\n"

def mkprops(props):
    wfile = ""
    for prop in props.keys():
        val = props[prop]
        prop = prop.replace("luma_","luma.")
        if prop == "mkin":
            prop = "in"
        elif prop == "mkout":
            prop = "out"
        wfile += """<property name="{}">{}</property>\n""".format(prop, val)
    return wfile
