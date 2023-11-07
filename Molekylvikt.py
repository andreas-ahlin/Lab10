# Syntaxkontroll

from LinkedQFileLab8 import LinkedQ
from StackCHATGPT import Stack
from Rutor import Ruta
from molgrafik import *
from hashtest import *


class Ruta:
    def __init__(self, atom="( )", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None


class Syntaxfel(Exception):
    pass


def weight(mol, atomdict):

    if mol == None:
        return 0

    if mol.atom == '( )':
        vikt = weight(mol.down, atomdict)
        vikt = vikt*mol.num

    else:
        atomnamn = mol.atom
        vikt = atomdict.search(atomnamn)
        vikt = vikt*mol.num

    return vikt + weight(mol.next, atomdict)


def readFormel(q):

    syntax_stack = Stack()
    mol = readMol(q, syntax_stack)
    if q.peek() == "\n":
        if not syntax_stack.is_empty():
            raise Syntaxfel("Saknad högerparentes vid radslutet")
        q.dequeue()
    return mol


def readMol(q, s):

    mol = readGroup(q, s)
    if q.peek() != '\n' and q.peek() != ")":
        mol.next = readMol(q, s)

    return mol


def readGroup(q, s):
    ruta = Ruta()

    if q.peek() == '(':
        s.push(q.dequeue())
        ruta.down = readMol(q, s)

        if q.peek() == ')':
            if s.is_empty():
                raise Syntaxfel("Felaktig gruppstart vid radslutet ")
            else:
                s.pop()
                q.dequeue()
                if q.peek() in '123456789':
                    ruta.num = readNum(q)
                else:
                    raise Syntaxfel("Saknad siffra vid radslutet ")

    elif q.peek() in '0123456789':
        raise Syntaxfel("Felaktig gruppstart vid radslutet ")

    else:
        ruta.atom = readAtom(q)
        if q.peek() in '0123456789':
            ruta.num = readNum(q)
    return ruta


def readAtom(q):
    atom = readBLetter(q)
    char = q.peek()
    if char not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        atom = atom+readSLetter(q)
    lista = "H  He  Li  Be  B  C  N  O  F  Ne  Na  Mg  Al  Si  P  S  Cl  Ar  K  Ca  Sc  Ti  V  Cr  Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr  Rb  Sr  Y  Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd  In  Sn  Sb  Te  I  Xe  Cs  Ba  La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu  Hf  Ta  W  Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  Rn  Fr  Ra  Ac  Th  Pa  U  Np  Pu  Am  Cm  Bk  Cf  Es  Fm  Md  No  Lr  Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn  Fl  Lv"
    lista = lista.split('  ')

    if atom not in lista:
        raise Syntaxfel("Okänd atom vid radslutet ")

    return atom


def readBLetter(q):
    char = q.dequeue()
    if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return char
    raise Syntaxfel("Saknad stor bokstav vid radslutet " + char)


def readSLetter(q):
    if not q.peek() in '0123456789()\n':
        char = q.dequeue()  # Skippar ifall det bara matas in stor bokstav
        return char
    return ''
    # if char in 'abcdefghijklmnopqrstuvwxyz':
    #     return
    # raise Syntaxfel("Saknad liten bokstav vid radslutet " + char)


def readNum(q):
    char = q.peek()

    if char in '123456789':  # kollar om det kommer en nolla
        num = q.dequeue()
        # Om det första siffran är 1 måste den följas av något annat
        if char == '1' and not q.peek() in '0123456789':
            raise Syntaxfel("För litet tal vid radslutet ")

        while q.peek() in '0123456789':
            num = num+q.dequeue()
        return int(num)
    elif char == '\n':
        return
    q.dequeue()
    raise Syntaxfel("För litet tal vid radslutet ")


def printQueue(q):
    while not q.isEmpty():
        char = q.dequeue()
        print(char, end=" ")
    print()


def storeMolekyl(molekyl):
    q = LinkedQ()
    molekyl = [*molekyl]
    for char in molekyl:
        q.enqueue(char)
    q.enqueue("\n")
    return q


def kollaMolekyl(Molekyl):
    q = storeMolekyl(Molekyl)

    try:
        mol = readFormel(q)
        mg = Molgrafik()
        mg.show(mol)
        atomlista = skapaAtomlista()
        atomDict = lagraHashtabell(atomlista)
        print(weight(mol, atomDict))
        input('')
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as fel:
        resMol = ''
        while q.peek() != '\n':
            resMol = resMol+q.dequeue()
        return str(fel) + str(resMol)


def main():
    molekyl = str(input(""))
    while molekyl != '#':
        resultat = kollaMolekyl(molekyl)
        print(resultat)
        molekyl = str(input(""))


if __name__ == "__main__":
    main()
