from textnode import TextNode,TextType

test =TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
test2 = TextNode("THIS IS ANOTHER TEXT",TextType.BOLD)

print(test)
print(test2)