from heapq import heapify, heappop, heappush


class Node:
    def __init__(self, ch, freq, left=None, right=None):
        self.ch, self.freq = ch, freq
        self.left, self.right = left, right

    def __lt__(self, other):
        return self.freq < other.freq


def getHuffmanTree(text):
    if not text:
        return 0

    freq = {ch: text.count(ch) for ch in set(text)}
    pq = [Node(k, v) for k, v in freq.items()]
    heapify(pq)

    while len(pq) > 1:
        left, right = heappop(pq), heappop(pq)
        new_freq = left.freq + right.freq
        heappush(pq, Node(None, new_freq, left, right))

    return pq[0]


codes = dict()


def traverse(node, traversed=''):
    if node.ch:
        codes[node.ch] = traversed
    else:
        if node.left:
            new_input = traversed + '0'
            traverse(node.left, new_input)
        if node.right:
            new_input = traversed + '1'
            traverse(node.right, new_input)


def get_encoded_text(text):
    return ''.join(codes[ch] for ch in text)


def decode(encoded_text, tree):
    output = ''
    node = tree
    for bit in encoded_text:
        if bit == '0':
            node = node.left
        else:
            node = node.right
        if node.ch:
            output += node.ch
            node = tree

    return output


string = "A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED"
new_tree = getHuffmanTree(string)
traverse(new_tree)
encoded = get_encoded_text(string)
print(encoded)
print(decode(encoded, new_tree))
