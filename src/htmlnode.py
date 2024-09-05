class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        propstring = ""
        for prop1 in self.props:
            propstring = propstring + f" {prop1}=\"{self.props[prop1]}\""
        return propstring

    def __repr__(self):
        return f"Tag: {self.tag}\nValue:{self.value}\nChildren:{self.children}\nProps:{self.props_to_html()}"

