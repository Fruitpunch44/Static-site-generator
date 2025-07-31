from htmlnode import HTML_Node
import pytest

def test_for_html_node():
    node = HTML_Node("div", "Hello", ["child1", "child2"], {"class": "container"})
    assert node.tag == "div"
    assert node.value == "Hello"
    assert node.children == ["child1", "child2"]
    assert node.props == {"class": "container"}

def test_for_html_node2():
    node = HTML_Node("p", "test paragraph", ["child1", "child2"], {"style": "color: red"})
    assert node.tag == "p"
    assert node.value == "test paragraph"
    assert node.children == ["child1", "child2"]
    assert node.props == {"style": "color: red"}

def test_for_html_node3():
    node = HTML_Node("href", "https://google.com", ["child1", "child2"], {"class": "container"})
    assert node.tag == "href"
    assert node.value == "https://google.com"
    assert node.children == ["child1", "child2"]
    assert node.props == {"class": "container"}

def test_repr():
    node = HTML_Node("p", "paragraph", None, {"style": "color: red"})
    assert repr(node) == 'HTMLNODE(p,paragraph,childrenNone,{"style": "color: red"})'