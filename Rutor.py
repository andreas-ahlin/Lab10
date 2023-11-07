from LinkedQFileLab8 import LinkedQ
from molgrafik import Molgrafik


class Ruta:
    def __init__(self, atom="( )", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None


class Syntaxfel(Exception):
    pass


def readFormel(q):
    mol = readMol(q)
    if q.isEmpty():
        return mol
    else:
        raise Syntaxfel("Felaktig gruppstart vid radslutet ")


def readMol(q):
    mol = readGroup(q)
    if q.peek() == "\n":
        return mol
    mol.next = readMol(q)
    return mol


def readGroup(q):
    if q.peek() == "\n":
        return None
    elif q.peek() in '()':
        if q.peek() == '(':
            q.dequeue()
            ruta = Ruta()
            ruta.down = readMol(q)
        elif q.peek() == ')':
            q.dequeue()
            ruta = Ruta()
            if q.isEmpty():
                raise Syntaxfel("Felaktig gruppstart vid radslutet")
            else:
                if q.peek() in '123456789':
                    ruta.num = readNum(q)
        return ruta
    elif q.peek() in '0123456789':
        raise Syntaxfel("Felaktig gruppstart vid radslutet")
    else:
        ruta = Ruta()
        ruta.atom = readAtom(q)
        if q.peek() in '0123456789':
            ruta.num = readNum(q)
        return ruta


def readAtom(q):
    atom = readBLetter(q)
    char = q.peek()
    if char not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        atom = atom + readSLetter(q)
    lista = "H  He  Li  Be  B  C  N  O  F  Ne  Na  Mg  Al  Si  P  S  Cl  Ar  K  Ca  Sc  Ti  V  Cr  Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr  Rb  Sr  Y  Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd  In  Sn  Sb  Te  I  Xe  Cs  Ba  La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu  Hf  Ta  W  Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  Rn  Fr  Ra  Ac  Th  Pa  U  Np  Pu  Am  Cm  Bk  Cf  Es  Fm  Md  No  Lr  Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn  Fl  Lv"
    lista = lista.split('  ')
    if atom not in lista:
        raise Syntaxfel("Okänd atom vid radslutet")
    return atom


def readBLetter(q):
    char = q.dequeue()
    if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return char
    raise Syntaxfel("Saknad stor bokstav vid radslutet " + char)


def readSLetter(q):
    if not q.peek() in '0123456789()\n':
        char = q.dequeue()
        return char
    return ''


def readNum(q):
    char = q.peek()
    if char in '123456789':
        num = q.dequeue()
        if char == '1' and not q.peek() in '0123456789':
            raise Syntaxfel("För litet tal vid radslutet")
        while q.peek() in '0123456789':
            num = num + q.dequeue()
        return int(num)
    elif char == '\n':
        return
    q.dequeue()
    raise Syntaxfel("För litet tal vid radslutet")


def storeMolekyl(molekyl):
    q = LinkedQ()
    molekyl = [*molekyl]
    for char in molekyl:
        q.enqueue(char)
    q.enqueue("\n")
    return q


def kollaMolekyl(molekyl):
    q = storeMolekyl(molekyl)
    try:
        mol = readFormel(q)
        mg = Molgrafik()
        mg.show(mol)
        input('')
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as fel:
        resMol = ''
        while q.peek() != '\n':
            resMol = resMol + q.dequeue()
        return str(fel) + str(resMol)


def main():
    molekyl = str(input(""))
    while molekyl != '#':
        resultat = kollaMolekyl(molekyl)
        print(resultat)
        molekyl = str(input(""))


if __name__ == "__main__":
    main()
