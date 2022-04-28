from lark import Lark

phonetic_grammer = """
    word: sound+
    sound: PAUSE | phone | stress

    stress: PRIM_STRESS | SEC_STRESS
    phone: HW | REVERSE_EPSILON_R | ASH | SCHWA | CARET | SCRIPT_A
         | AI | A_UPSILON | B | D | ETH | D_EZH | EPSILON | EI
         | F | G | H | LONG_E | I | J | LONG_U | K | L | M
         | N | AGMA | OPEN_O | OPEN_OI | LONG_O | P | R | S | ESH
         | T | THETA | T_ESH | UW | UPSILON | V | W | Z | EZH

    PAUSE: "_"
    PRIM_STRESS: "\'"
    SEC_STRESS: ","

    ASH: "/&/"
    SCHWA: "/-/"
    CARET: "/@/"
    REVERSE_EPSILON_R: "/(@)/r" | "/[@]/r"
    SCRIPT_A: "/A/"
    AI: "/aI/"
    A_UPSILON: "/AU/"
    B: "b"
    D: "d"
    ETH: "/D/"
    D_EZH: "/dZ/"
    EPSILON: "/E/"
    EI: "/eI/"
    F: "f"
    G: "g"
    H: "h"
    HW: "/hw/"
    LONG_E: "/i/"
    I: "/I/"
    J: "/j/"
    LONG_U: "/ju/"
    K: "k"
    L: "l"
    M: "m"
    N: "n"
    AGMA: "/N/"
    OPEN_O: "/O/"
    OPEN_OI: "//Oi//"
    LONG_O: "/oU/"
    P: "p"
    R: "r"
    S: "s"
    ESH: "/S/"
    T: "t"
    THETA: "/T/"
    T_ESH: "/tS/"
    UW: "/u/"
    UPSILON: "/U/"
    V: "v"
    W: "w"
    Z: "z"
    EZH: "/Z/"

    %import common.WS
    %ignore WS
"""
parser = Lark(phonetic_grammer, start='word', parser='lalr')

def lex_word(text):
    # Returns a list of sound types after lexical analysis
    tokens = list(parser.lex(text))
    types  = list(map(lambda tok: tok.type, tokens))
    return types
