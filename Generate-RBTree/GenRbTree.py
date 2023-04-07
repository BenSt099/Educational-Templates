import sys


###############################################
################ Tex Snippets #################
###############################################


texpackages = r"""
%%%%%%%%%%%%%%%%%%%%%%
%%%%%%  Imports %%%%%%
%%%%%%%%%%%%%%%%%%%%%%
\usepackage{tikz}
\usetikzlibrary{trees}
\usetikzlibrary{arrows}
\usetikzlibrary{arrows.meta}
%%%%%%%%%%%%%%%%%%%%%%
"""

headertex = """
\begin{center}
    \begin{tikzpicture}[level distance=1.6cm,
        level 1/.style={sibling distance=8cm},
        level 2/.style={sibling distance=4cm},
        level 3/.style={sibling distance=2cm},
        node distance=3.5cm,
        ->,-{Stealth[round,open,fill=black]},
        blackNode/.style = {shape=circle,fill=darkgray,text=white,minimum size=2em,outer sep=0.2cm},
        redNode/.style = {fill=purple,text=white,rounded corners=2mm,minimum size=2em,outer sep=0.2cm},
        endNode/.style = {shape=circle,draw=black,fill=darkgray,text=white,outer sep=0.2cm},
        innerBlackNode/.style = {shape=circle,fill=darkgray,text=white,minimum size=2em}, % inner node for double-black-state
        innerRedNode/.style = {shape=circle,fill=purple,text=white,minimum size=2em}, % inner node for red-black-state
        outerNode/.style = {shape=circle,very thick,draw=darkgray,fill=white,outer sep=0.2cm, inner sep=-0.6mm, distance=0.01cm,line width=0.9mm}
        ]
"""

rootdouble = "\node[*] {\tikz\node[*]{+};}"

root = "\node[*]{+}"

element = "child{node[*]{+} }"

main = """
"""

footertex = """
        \end{tikzpicture}
\end{center}
"""


numInput = ""
colInput = ""
arrelements = []

###############################################
################## Funtions ###################
###############################################


def _parse(inputnum, inputcol, inputel):
    arr = inputel.split("*")
    str = arr[0] + inputcol + arr[1]
    arr2 = str.split("+")
    return arr2[0] + inputnum + arr2[1]


def printConsoleLineStart():
    print("GEN+RedBlackTree - v1")
    print()


def takeInput():
    print("__________________________")
    print()
    numInput = input("Numbers: ")
    colInput = input("Colors : ")


def parseToLatex():
    numbers = numInput.split(",")
    colors = colInput.split(",")

    arrelements.append(_parse(numbers[0], colors[0], root) + "\n") ## root-element
    
    i = 1
    while i < len(numbers):
        arrelements[i] = _parse(numbers[i], colors[i], element)
        i+=1
        
    print(arrelements)


def writeToFile():
    with open("rbtree_generated.tex", "w", encoding="utf-8") as outputFile:
        outputFile.write("...")


def printConsoleLineEnd():
    print()
    print("Stopping GEN+RedBlackTree - v1 ...")
    print("Good Bye!")


def exitScript():
    sys.exit()


###############################################
################## Main Func ##################
###############################################


def main():
    printConsoleLineStart()
    takeInput()
    parseToLatex()
    #writeToFile()
    printConsoleLineEnd()
    exitScript()
    
main()