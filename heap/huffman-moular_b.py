__license__ = 'GolluM (c) EPITA'

__docformat__ = 'reStructuredText'

__revision__ = '$Id: huffman.py 2016-04-04'



from binaryTrees import *


################################################################################
#
# COMPRESSION



def buildFrequencyList(outputList, dataIN):

    """Build a tuple list according to the character frequencies in the input.


    :param outputList: the list to store the result. Each value is a tuple which first element is the frequency of the character
     stored in the second part.

    :param dataIN: the data from which we want to build the frequencies list.

    :type outputList: tuple<int, str> list

    :type dataIN: str


    :Example:


    >>> L = []

    >>> buildFrequencyList(L, 'bbaabtttaabtctce')

    >>> L
    [(4, 'b'), (4, 'a'), (5, 't'), (2, 'c'), (1, 'e')]

    """

    ll = len(outputList)

    for x in dataIN:

        pos = 0

        hasNotYetChanged = True

        while pos < ll and hasNotYetChanged:

            #print(ll, pos, outputList[pos],  outputList)

            if outputList[pos][1] == x:

                outputList[pos] = outputList[pos][0] + 1, outputList[pos][1]

                hasNotYetChanged = False

            pos += 1

        if hasNotYetChanged:

            outputList.append((1, x))

            ll += 1




def buildHuffmanTree(inputList):

    """Process the frequency list into an Huffman tree according to the algorithm.


    :param inputList: the frequencies list from :func:`buildFrequencyList`.

    :type inputList: tuple<int, str> list

    :return: returns an huffman tree containing all the datas from the list.

    :rtype: BinTree


    :Example:


    >>> H = buildHuffmanTree(L)

    >>> prettyPrint(H)

    .
    / \\
    / \\
    / \\
    / \\

    .      .
    / \ / \\
    / \ / \\

    t  b a  .
            / \\

            c  e

    """

    if inputList == []:

        return None

    if len(inputList) == 1:

        return newBinTree(inputList[0][1], None, None)

    #making a sorted array (insertion sorting)

    ll = len(inputList)#usefull later

    for x in range(0, ll, 1):

        posMin = x #getting actual minimun

        for y in range(x + 1, ll, 1):

            if inputList[posMin][0] > inputList[y][0]: #oups, there is a number < minimun

                posMin = y #updating actual minimun

        if posMin != x: #if the minimun changed : extange the minimun with this one

            tmp = inputList[posMin]

            inputList[posMin] = inputList[x]

            inputList[x] = tmp
    #making nodes for each value in array

    lResTmp = []#will contain all leaf of the tree

    for x in range(0, ll, 1):

        lResTmp.append(newBinTree(inputList[x][1], None, None))

    #print("lResTmp", debugTre(lResTmp))

    min = inputList[0][0] #get minimun occurence of the list

    pos = 0 #position in lResTmp

    level = [] #actual level in the tree

    lastL = [] #last level in the tree : joining them and putting them in level

    unWantedNode = None #in case of an odd number of node on the level

    #making tree

    while len(level) != 1 or pos < ll:

        #print(len(level), "level", debugTre(level), "lastL", debugTre(lastL))

        #print("level", level, "lastL", lastL)

        lastL = level # added in level earlier

        if None != unWantedNode:

            lastL.append(unWantedNode)

            unWantedNode = None

        level = [] #making a new level

        if pos < ll:

            min = inputList[pos][0] #getting a new minimun

            #making old nodes and new nodes of the same level

        while pos < ll and  inputList[pos][0] == min:

            lastL.append(lResTmp[pos])

            #print("adding in lastL", debugTre(lastL))

            pos += 1

        lal = len(lastL)

        #making the actual level by putting together to old nodes ; depending on even/odd number of node(s)

        if lal % 2 == 0:

            posInlastL = 0

            while posInlastL < lal:

                level.append(newBinTree("", lastL[posInlastL], lastL[posInlastL+1]))

                posInlastL += 2

        else:
 
            if lal != 1:

                posInlastL = 0

                while posInlastL < lal - 1:

                    #print("lastL", debugTre(lastL), posInlastL, lal)

                    level.append(newBinTree("", lastL[posInlastL], lastL[posInlastL+1]))

                    posInlastL += 2

            unWantedNode = lastL[lal - 1]

    return level[0]




def parcTree(b, prec, l):

    if b.left == b.right: #leaf

        l.append((prec, b.key))

    else :

        parcTree(b.left, prec + "0", l)

        parcTree(b.right, prec + "1", l)



def encodeDataq(huffmanTree, dataIN):

    """Encode the input string to its binary string representation.


    :param huffmanTree: the huffman tree from :func:`buildHuffmanTree`.

    :param dataIN: the data we want to encode.

    :type huffmanTree: BinTree

    :type dataIN: str

    :return: returns the binary string.

    :rtype: str


    :Example:


    >>> encodeData(H, 'bbaabtttaabtctce')

    '01011010010000001010010011000110111'

    """

    if huffmanTree == None:

        return"Bad Inpout : Empty tree :/"

    #Getting list

    l =[]

    parcTree(huffmanTree, "", l)

    print(l)

    #making string

    res = ""

    ll = len(l)

    for x in dataIN:

        pos = 0

        found = False

        while pos < ll and not found:

            if l[pos][1] == x:

                found = True

                res += l[pos][0]

            pos += 1

        if not found:

            res += "<failed : " + x + "not in tree :/>"

    return res



#print(encodeDataq(tmp(), "bbaabtttaabtctce"), "\n01011010010000001010010011000110111")



def encodeTree(huffmanTree):

    """Encodes an huffman tree to its binary representation using a preOrder traversal:

    * each leaf key is encoded into its binary representation on 8 bits preceded by '1'

    * each time we go left we add a '0' to the result


    :param huffmanTree: the huffman tree to encode.

    :type huffmanTree: BinTree

    :return: returns a string corresponding to the binary representation of the huffman tree.

    :rtype: str


    :Example:


    >>> encodeTree(H)

    '0010111010010110001001011000010101100011101100101'

    """

    #fix me

    return ""



def toBinary(dataIN):

    """Compress a string containing the binary representation to its real compressed string.


    :param dataIN: the data to compress.

    :type dataIN: str

    :return: returns a tuple: the compressed string corresponding to the input and the number of bits for the alignment.

    :rtype: tuple<str, int>

class:Example:


    >>> toBinary('01011010010000001010010011000110111')

    ('Z@¤Æ\\x07', 5)

    >>> toBinary('0010111010010110001001011000010101100011101100101')

    ('.\\x96%\\x85c²\\x01', 7)


    .. warning:: some characters in the output string may not be visibles if you print it.

    """

    # FIXME

    return ""



def compression(dataIN):

    """Compress a string using the Huffman algorithm.


    :param dataIN: the data to compress.

    :type dataIN: str

    :return: returns the compressed data (and its number of bits for the alignment) and the compressed tree (and its number of bits for the alignment).

    :rtype: tuple< tuple<str, int>, tuple<str, int> >


    :Example:


    >>> compression('bbaabtttaabtctce')

    (('Z@¤Æ\\x07', 5), ('.\\x96%\\x85c²\\x01', 7))

    """

    # FIXME

    return None




################################################################################
#

# DECOMPRESSION




def decodeTree(dataIN, alignement):

    """Decodes an huffman tree from it binary representation:

    * a '0' means we add a new internal node and go to its left node

    * an '1' means the next 8 values are the encoded character of the current leaf.


    :param dataIN: the real binary string containing the encoded huffman tree.

    :param alignement: the number of bits to ignore at the end of the input.

    :type dataIN: str

    :type alignement: int

    :return: returns decoded huffman tree

    :rtype: BinTree


    :Example:


    >>> H = decodeTree('.\\x96%\\x85c²\\x01', 7)

    >>> prettyPrint(H)

    .
    / \\
    / \\
    / \\
    / \\

        . .
    / \ / \\
    / \ / \\

    t b  a .
            / \\

            c e

    """

    # FIXME

    return None



def decodeData(huffmanTree, dataIN, alignement):

    """Decode a binary string using the corresponding huffman tree into something more readable.


    :param huffmanTree: the huffman tree for decoding.

    :param dataIN: the input binary string we want to decode.

    :param alignement: the number of bits to ignore at the end of the input.

    :type huffmanTree: BinTree

    :type dataIN: str

    :type alignement: int

    :return: returns the decoded text

    :rtype: str


    :Example:


    >>> decodeData(H, 'Z@¤Æ\\x07', 5)

    'bbaabtttaabtctce'

    """

    # FIXME

    return None



def decompression(dataIN):

    """Decompress the data compressed using the Huffman algorithm :func:`compression`


    :param dataIN: the compressed data and huffman tree, and their respectives alignment bits.

    :type dataIN: tuple< tuple<str, int>, tuple<str, int> >

    :return: returns the decompressed text.

    :rtype: str


    :Example:


    >>> decompression((('Z@¤Æ\\x07', 5), ('.\\x96%\\x85c²\\x01', 7)))

    'bbaabtttaabtctce'

    """

    # FIXME

    return ""