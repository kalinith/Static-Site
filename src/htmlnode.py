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
        if self.props == None:
            return propstring
        for prop1 in self.props:
            propstring = propstring + f' {prop1}="{self.props[prop1]}"'
        return propstring

    def __repr__(self):
        return f"Tag: {self.tag}\nValue:{self.value}\nChildren:{self.children}\nProps:{self.props_to_html()}"

    def __eq__(self, target):
        isequal = True
        if self.tag != target.tag:
            isequal = False
        if self.value != target.value:
            isequal = False
        if self.children != target.children:
            isequal = False
        return isequal

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        # for now I'm assuming if there is no tag there will be no props
        if self.value == None:
            raise ValueError
        else:
            body = f'{self.value}'

        if self.tag == None:
            pre = ""
            attr = ""
            post = ""
        else:
            pre = f"<{self.tag}"
            post = f"</{self.tag}>"
            attr = str(self.props_to_html())+">"

        return pre+attr+body+post
