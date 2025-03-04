import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode



class TestHtmlNode(unittest.TestCase):
    def test_to_html(self):
        self.assertRaises(NotImplementedError, HTMLNode().to_html)

    def test_props_to_html(self):
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank",
        })
        self.assertEqual(' href="https://www.google.com" target="_blank"', node.props_to_html())

    def test_empty_node_repr(self):
        node = HTMLNode()
        self.assertEqual("""HTMLNode(None, None, children: None, None)""", repr(node))

    def test_node_repr(self):
        node = HTMLNode("p", "This is a text node", )
        self.assertEqual('HTMLNode(p, This is a text node, children: None, None)', repr(node))


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual("<p>This is a paragraph of text.</p>", node.to_html())

    def test_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        print(node.props_to_html())
        self.assertEqual('<a href="https://www.google.com">Click me!</a>', node.to_html())

    def test_no_value(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)

    def test_no_tag(self):
        node = LeafNode(value="This is a paragraph of text.", tag=None)
        self.assertEqual("This is a paragraph of text.", node.to_html())



class TestParentNode(unittest.TestCase):

    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual("<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>", node.to_html())

    def test_to_html_with_props(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text", {"href": "https://www.google.com"}),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            """<p><b>Bold text</b>Normal text<i href="https://www.google.com">italic text</i>Normal text</p>""",
            node.to_html())
