class leaf:
    def __init__(self, val=1):
        self.val = val

    def __str__(self):
        return str(self.val)

class node:
    def __init__(self, val=7):
        self.val = val
        self.Zero = leaf()
        self.One = leaf()
        self.Two = leaf()
        self.Three = leaf()
        self.Four = leaf()
        self.Five = leaf()
        self.Six = leaf()

    def __str__(self):
        return str(self.val)

    def _update_val(self):
        self.val = self.Zero.val + self.One.val + self.Two.val + self.Three.val + self.Four.val + self.Five.val + self.Six.val
        if isinstance(self.Zero, node): self.Zero._update_val()
        if isinstance(self.One, node): self.One._update_val()
        if isinstance(self.Two, node): self.Two._update_val()
        if isinstance(self.Three, node): self.Three._update_val()
        if isinstance(self.Four, node): self.Four._update_val()
        if isinstance(self.Five, node): self.Five._update_val()
        if isinstance(self.Six, node): self.Six._update_val()

    def treeDepth(self,pRoot):
        if(not isinstance(pRoot, node)):
            return 0
        else:
            nZero = self.treeDepth(pRoot.Zero)
            nOne = self.treeDepth(pRoot.One)
            nTwo = self.treeDepth(pRoot.Two)
            nThree = self.treeDepth(pRoot.Three)
            nFour = self.treeDepth(pRoot.Four)
            nFive = self.treeDepth(pRoot.Five)
            nSix = self.treeDepth(pRoot.Six)
            return max(nZero + 1, nOne + 1, nTwo + 1, nThree + 1, nFour + 1, nFive + 1, nSix + 1)

    def update_root(self, _root):
        for i in range(_root.treeDepth(_root)-1):
            _root._update_val()

    def insert_Zero(self):
        assert isinstance(self.Zero, leaf) # assert：斷言，true->continue，false->exception
        self.Zero = node()
        self.val += self.Zero.val - 1
        
    def insert_One(self):
        assert isinstance(self.One, leaf)
        self.One = node()
        self.val += self.One.val - 1

    def insert_Two(self):
        assert isinstance(self.Two, leaf)
        self.Two = node()
        self.val += self.Two.val - 1

    def insert_Three(self):
        assert isinstance(self.Three, leaf)
        self.Three = node()
        self.val += self.Three.val - 1

    def insert_Four(self):
        assert isinstance(self.Four, leaf)
        self.Four = node()
        self.val += self.Four.val - 1

    def insert_Five(self):
        assert isinstance(self.Five, leaf)
        self.Five = node()
        self.val += self.Five.val - 1

    def insert_Six(self):
        assert isinstance(self.Six, leaf)
        self.Six = node()
        self.val += self.Six.val - 1

    def plant_tree(self, pRoot, attrs):
        for attr in attrs:
            if attr == 'A':
                try:
                    pRoot.insert_Zero()
                except AssertionError:
                    pRoot = pRoot.Zero
                    pRoot.plant_tree(pRoot, attr)
                pRoot = pRoot.Zero
            elif attr == 'B':
                try:
                    pRoot.insert_One()
                except AssertionError:
                    pRoot = pRoot.One
                    pRoot.plant_tree(pRoot, attr)
                pRoot = pRoot.One
            elif attr == 'C':
                try:
                    pRoot.insert_Two()
                except AssertionError:
                    pRoot = pRoot.Two
                    pRoot.plant_tree(pRoot, attr)
                pRoot = pRoot.Two
            elif attr == 'D':
                try:
                    pRoot.insert_Three()
                except AssertionError:
                    pRoot = pRoot.Three
                    pRoot.plant_tree(pRoot, attr)
                pRoot = pRoot.Three
            elif attr == 'E':
                try:
                    pRoot.insert_Four()
                except AssertionError:
                    pRoot = pRoot.Four
                    pRoot.plant_tree(pRoot, attr)
                pRoot = pRoot.Four
            elif attr == 'F':
                try:
                    pRoot.insert_Five()
                except AssertionError:
                    pRoot = pRoot.Five
                    pRoot.plant_tree(pRoot, attr)
                pRoot = pRoot.Five
            else:
                try:
                    pRoot.insert_Six()
                except AssertionError:
                    pRoot = pRoot.Six
                    pRoot.plant_tree(pRoot, attr)
                pRoot = pRoot.Six


def compress(message):
    tree_dict, m_len, i = {}, len(message), 0
    while i < m_len:
        # case I
        if message[i] not in tree_dict.keys():
            yield (0, message[i])
            tree_dict[message[i]] = len(tree_dict) + 1
            i += 1
        # case III
        elif i == m_len - 1:
            yield (tree_dict.get(message[i]), '')
            i += 1
        else:
            for j in range(i + 1, m_len):
                # case II
                if message[i:j + 1] not in tree_dict.keys():
                    yield (tree_dict.get(message[i:j]), message[j])
                    tree_dict[message[i:j + 1]] = len(tree_dict) + 1
                    i = j + 1
                    break
                # case III
                elif j == m_len - 1:
                    yield (tree_dict.get(message[i:j + 1]), '')
                    i = j + 1

    print("message:", message, "\ntree dict keys:", tree_dict.keys())

def uncompress(packed):
    unpacked, tree_dict = '', {}
    for index, ch in packed:
        if index == 0:
            unpacked += ch
            tree_dict[len(tree_dict) + 1] = ch
        else:
            term = tree_dict.get(index) + ch
            unpacked += term
            tree_dict[len(tree_dict) + 1] = term
    return unpacked

def main():
    messages = ['ABBCBCABABCAABCAAB', 'AAHHHAAAKAAAGGGFFKIIIHHHAFFFEEEAHIIKKKAGGGFFEEEAAAKAAKKKIIHHHAAAFAAKKKAAKKKAFFFCCCDDKKKIAAAKAAAEFFGGGAAAHIKKKAAAEEEAAAKKKAAIIFFFGADDCCCFFFIIIDDDGFFFEAKAIIIFFFAKKAACCDDCCCAAAFFFAAAIAAAFFGGAAAKKIIHAAAEEEAKKKKGGGFFEEEHAFFFGDCIIIAKKAFFFAKKAIIIKKIIIAKKAADDDCCCAAKAAIIFFFAAAKKKACCCAAAIIKKKAKAAAKACCDDDKAGGGAAKKACDDDKIIHFFFEEFAKAAGGGHHHCFFFKIIIHHIIIAAAGGAAAKKKAAAKAIKKKCCCFFFEEAAAGGGFFAHHAAAFFGFFFBBAAAKIIHHHAAAKKKAAAFFFGGGFFAAKKKAACCCIIIAAKAAAKAAAKIIIAAACDDDGGGFEAAABEFFFGGAAAKKKAAKKAAFFFAKAKKKIIIAAAKAAAKKAAAKKAAHHHIIIKAAAEEEFCCCIIIHHHIKKKDDDAFEEEFFAAAHABBBCDGGDDAAHHHIIKKKAFFEEEFAKKKIHHHAAAFGGGAAAKAAAEEEFFFEEEAAHIIKKKKFFEEEKKKIHHHAAGGGFEAAAEEFFGGGDDKKKAAAEEEFAAAKKKAAAEEEAAAKKAAAKAAAKAAACCAAKAIIIAAABBBAAKAAAKKKIIHHHAAEEFIIHHBBBEFFFAAAIIIAAAGGFFAAAHHHFFFAKKACHHHIAAAIAAAEFFFCAAIFFFCCAAAGGGFFFAAAHHIIIKKKAAAKKAAADDDKIIHHHAABBFFFKCCCIIIKKIIIAAAEEEAEFFFGGGDAAAEEEAAAIAKKAAAKKAIIIAKAFFFEEBBCCAAAIIIACCCAAAFFFAAAKKAKAAAHHHBCCCDAAAEEAAAKAAAFFFAAAHHHIIIAKAAAFFFAAKKKAAAKKKAAACCCAAAKAAAIIAAAEFFFAAAKKKAAAKKKAAAKAAAKKAAAKK', 'AAAAAAAAA']
    
    for m in messages:
        pack = compress(m)
        unpack = uncompress(pack)

    root = node()
    root.plant_tree(root, 'AABC')
    root.plant_tree(root, 'BC')
    # root.insert_Zero()
    # root.Zero.insert_Zero()

    # root.Zero.insert_One()
    # root.Zero.Zero.insert_Zero()
    # root.Zero.Zero.Zero.insert_Zero()
    # root.Zero.Zero.Zero.insert_Six()
    # root.Zero.Zero.Zero.Six.insert_Four()
    # root.insert_One()
    # root.insert_Five()

    print("Tree depth:", root.treeDepth(root))
    root.update_root(root)
    print("root value:", root.val)

    print(root.Zero.Zero)
    print(root.Zero.Zero.One)

if __name__ == '__main__':
    main()


# def compress(uncompressed):
#     """Compress a string to a list of output symbols."""

#     # Build the dictionary.
#     dict_size = 256
#     dictionary = dict((chr(i), chr(i)) for i in range(dict_size))

#     w = ""
#     result = []
#     for c in uncompressed:
#         wc = w + c
#         if wc in dictionary:
#             w = wc
#         else:
#             result.append(dictionary[w])
#             # Add wc to the dictionary.
#             dictionary[wc] = dict_size
#             dict_size += 1
#             w = c

#     # Output the code for w.
#     if w:
#         result.append(dictionary[w])
#     return result


# def decompress(compressed):
#     """Decompress a list of output ks to a string."""
#     from io import StringIO

#     # Build the dictionary.
#     dict_size = 256
#     dictionary = dict((chr(i), chr(i)) for i in range(dict_size))

#     # use StringIO, otherwise this becomes O(N^2)
#     # due to string concatenation in a loop
#     result = StringIO()
#     w = compressed.pop(0)
#     result.write(w)
#     for k in compressed:
#         if k in dictionary:
#             entry = dictionary[k]
#         elif k == dict_size:
#             entry = w + w[0]
#         else:
#             raise ValueError('Bad compressed k: %s' % k)
#         result.write(entry)

#         # Add w+entry[0] to the dictionary.
#         dictionary[dict_size] = w + entry[0]
#         dict_size += 1

#         w = entry
#     return result.getvalue()

# def main():
#     from io import StringIO
#     # How to use:
#     compressed = compress('TOBEORNOTTOBEORTOBEORNOT')
#     print (compressed)
#     decompressed = decompress(compressed)
#     print (decompressed)

#     print(dict((i, i) for i in range(256)))

# if __name__ == "__main__":
#     main()