# Generated from CrawLang.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,38,321,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,1,0,5,0,70,8,0,10,0,12,0,73,9,0,1,0,5,0,76,8,0,10,0,12,0,79,
        9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,2,3,2,88,8,2,1,2,1,2,1,2,1,2,1,2,1,
        3,1,3,1,3,3,3,98,8,3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,106,8,4,1,5,1,5,
        1,5,1,5,1,5,1,5,5,5,114,8,5,10,5,12,5,117,9,5,1,6,1,6,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,3,7,129,8,7,1,8,1,8,5,8,133,8,8,10,8,12,8,
        136,9,8,1,8,5,8,139,8,8,10,8,12,8,142,9,8,1,8,1,8,1,9,1,9,1,9,1,
        9,5,9,150,8,9,10,9,12,9,153,9,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,3,11,167,8,11,1,12,1,12,1,12,1,13,1,13,
        1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,3,15,
        186,8,15,1,16,1,16,1,16,1,16,3,16,192,8,16,1,17,1,17,3,17,196,8,
        17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,3,19,208,8,
        19,1,20,1,20,3,20,212,8,20,1,20,1,20,1,21,1,21,3,21,218,8,21,1,22,
        5,22,221,8,22,10,22,12,22,224,9,22,1,22,1,22,1,23,1,23,1,23,3,23,
        231,8,23,1,24,1,24,1,24,5,24,236,8,24,10,24,12,24,239,9,24,1,25,
        1,25,1,25,5,25,244,8,25,10,25,12,25,247,9,25,1,26,1,26,1,26,5,26,
        252,8,26,10,26,12,26,255,9,26,1,27,1,27,1,27,5,27,260,8,27,10,27,
        12,27,263,9,27,1,28,1,28,1,28,5,28,268,8,28,10,28,12,28,271,9,28,
        1,29,1,29,1,29,5,29,276,8,29,10,29,12,29,279,9,29,1,30,1,30,1,30,
        5,30,284,8,30,10,30,12,30,287,9,30,1,31,1,31,1,31,1,31,5,31,293,
        8,31,10,31,12,31,296,9,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,
        1,33,1,33,1,33,1,33,1,33,5,33,311,8,33,10,33,12,33,314,9,33,3,33,
        316,8,33,1,33,1,33,1,33,1,33,0,0,34,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,
        66,0,6,1,0,2,3,1,0,27,29,1,0,25,26,1,0,37,38,1,0,33,36,1,0,31,32,
        322,0,71,1,0,0,0,2,83,1,0,0,0,4,87,1,0,0,0,6,94,1,0,0,0,8,105,1,
        0,0,0,10,107,1,0,0,0,12,118,1,0,0,0,14,128,1,0,0,0,16,130,1,0,0,
        0,18,145,1,0,0,0,20,156,1,0,0,0,22,159,1,0,0,0,24,168,1,0,0,0,26,
        171,1,0,0,0,28,175,1,0,0,0,30,185,1,0,0,0,32,191,1,0,0,0,34,195,
        1,0,0,0,36,197,1,0,0,0,38,207,1,0,0,0,40,211,1,0,0,0,42,215,1,0,
        0,0,44,222,1,0,0,0,46,230,1,0,0,0,48,232,1,0,0,0,50,240,1,0,0,0,
        52,248,1,0,0,0,54,256,1,0,0,0,56,264,1,0,0,0,58,272,1,0,0,0,60,280,
        1,0,0,0,62,288,1,0,0,0,64,299,1,0,0,0,66,305,1,0,0,0,68,70,3,14,
        7,0,69,68,1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,77,
        1,0,0,0,73,71,1,0,0,0,74,76,3,2,1,0,75,74,1,0,0,0,76,79,1,0,0,0,
        77,75,1,0,0,0,77,78,1,0,0,0,78,80,1,0,0,0,79,77,1,0,0,0,80,81,3,
        4,2,0,81,82,5,0,0,1,82,1,1,0,0,0,83,84,3,6,3,0,84,85,3,16,8,0,85,
        3,1,0,0,0,86,88,3,12,6,0,87,86,1,0,0,0,87,88,1,0,0,0,88,89,1,0,0,
        0,89,90,5,1,0,0,90,91,5,21,0,0,91,92,3,16,8,0,92,93,5,22,0,0,93,
        5,1,0,0,0,94,95,3,8,4,0,95,97,5,21,0,0,96,98,3,10,5,0,97,96,1,0,
        0,0,97,98,1,0,0,0,98,99,1,0,0,0,99,100,5,22,0,0,100,7,1,0,0,0,101,
        106,5,15,0,0,102,103,3,12,6,0,103,104,5,15,0,0,104,106,1,0,0,0,105,
        101,1,0,0,0,105,102,1,0,0,0,106,9,1,0,0,0,107,108,3,12,6,0,108,115,
        5,15,0,0,109,110,5,19,0,0,110,111,3,12,6,0,111,112,5,15,0,0,112,
        114,1,0,0,0,113,109,1,0,0,0,114,117,1,0,0,0,115,113,1,0,0,0,115,
        116,1,0,0,0,116,11,1,0,0,0,117,115,1,0,0,0,118,119,7,0,0,0,119,13,
        1,0,0,0,120,129,3,16,8,0,121,129,3,64,32,0,122,129,3,20,10,0,123,
        129,3,22,11,0,124,129,3,26,13,0,125,129,3,36,18,0,126,129,3,66,33,
        0,127,129,5,20,0,0,128,120,1,0,0,0,128,121,1,0,0,0,128,122,1,0,0,
        0,128,123,1,0,0,0,128,124,1,0,0,0,128,125,1,0,0,0,128,126,1,0,0,
        0,128,127,1,0,0,0,129,15,1,0,0,0,130,134,5,23,0,0,131,133,3,18,9,
        0,132,131,1,0,0,0,133,136,1,0,0,0,134,132,1,0,0,0,134,135,1,0,0,
        0,135,140,1,0,0,0,136,134,1,0,0,0,137,139,3,14,7,0,138,137,1,0,0,
        0,139,142,1,0,0,0,140,138,1,0,0,0,140,141,1,0,0,0,141,143,1,0,0,
        0,142,140,1,0,0,0,143,144,5,24,0,0,144,17,1,0,0,0,145,146,3,12,6,
        0,146,151,5,15,0,0,147,148,5,19,0,0,148,150,5,15,0,0,149,147,1,0,
        0,0,150,153,1,0,0,0,151,149,1,0,0,0,151,152,1,0,0,0,152,154,1,0,
        0,0,153,151,1,0,0,0,154,155,5,20,0,0,155,19,1,0,0,0,156,157,3,40,
        20,0,157,158,5,20,0,0,158,21,1,0,0,0,159,160,5,4,0,0,160,161,5,21,
        0,0,161,162,3,60,30,0,162,163,5,22,0,0,163,166,3,14,7,0,164,167,
        3,24,12,0,165,167,1,0,0,0,166,164,1,0,0,0,166,165,1,0,0,0,167,23,
        1,0,0,0,168,169,5,5,0,0,169,170,3,14,7,0,170,25,1,0,0,0,171,172,
        5,6,0,0,172,173,3,28,14,0,173,174,3,14,7,0,174,27,1,0,0,0,175,176,
        5,21,0,0,176,177,3,30,15,0,177,178,3,32,16,0,178,179,3,34,17,0,179,
        180,5,22,0,0,180,29,1,0,0,0,181,186,5,20,0,0,182,183,3,40,20,0,183,
        184,5,20,0,0,184,186,1,0,0,0,185,181,1,0,0,0,185,182,1,0,0,0,186,
        31,1,0,0,0,187,192,5,20,0,0,188,189,3,60,30,0,189,190,5,20,0,0,190,
        192,1,0,0,0,191,187,1,0,0,0,191,188,1,0,0,0,192,33,1,0,0,0,193,196,
        1,0,0,0,194,196,3,40,20,0,195,193,1,0,0,0,195,194,1,0,0,0,196,35,
        1,0,0,0,197,198,5,7,0,0,198,199,3,60,30,0,199,200,5,20,0,0,200,37,
        1,0,0,0,201,208,5,15,0,0,202,208,5,16,0,0,203,204,5,21,0,0,204,205,
        3,60,30,0,205,206,5,22,0,0,206,208,1,0,0,0,207,201,1,0,0,0,207,202,
        1,0,0,0,207,203,1,0,0,0,208,39,1,0,0,0,209,210,5,15,0,0,210,212,
        5,30,0,0,211,209,1,0,0,0,211,212,1,0,0,0,212,213,1,0,0,0,213,214,
        3,60,30,0,214,41,1,0,0,0,215,217,3,38,19,0,216,218,3,62,31,0,217,
        216,1,0,0,0,217,218,1,0,0,0,218,43,1,0,0,0,219,221,5,8,0,0,220,219,
        1,0,0,0,221,224,1,0,0,0,222,220,1,0,0,0,222,223,1,0,0,0,223,225,
        1,0,0,0,224,222,1,0,0,0,225,226,3,42,21,0,226,45,1,0,0,0,227,231,
        3,44,22,0,228,229,5,26,0,0,229,231,3,44,22,0,230,227,1,0,0,0,230,
        228,1,0,0,0,231,47,1,0,0,0,232,237,3,46,23,0,233,234,7,1,0,0,234,
        236,3,46,23,0,235,233,1,0,0,0,236,239,1,0,0,0,237,235,1,0,0,0,237,
        238,1,0,0,0,238,49,1,0,0,0,239,237,1,0,0,0,240,245,3,48,24,0,241,
        242,7,2,0,0,242,244,3,48,24,0,243,241,1,0,0,0,244,247,1,0,0,0,245,
        243,1,0,0,0,245,246,1,0,0,0,246,51,1,0,0,0,247,245,1,0,0,0,248,253,
        3,50,25,0,249,250,7,3,0,0,250,252,3,50,25,0,251,249,1,0,0,0,252,
        255,1,0,0,0,253,251,1,0,0,0,253,254,1,0,0,0,254,53,1,0,0,0,255,253,
        1,0,0,0,256,261,3,52,26,0,257,258,7,4,0,0,258,260,3,52,26,0,259,
        257,1,0,0,0,260,263,1,0,0,0,261,259,1,0,0,0,261,262,1,0,0,0,262,
        55,1,0,0,0,263,261,1,0,0,0,264,269,3,54,27,0,265,266,7,5,0,0,266,
        268,3,54,27,0,267,265,1,0,0,0,268,271,1,0,0,0,269,267,1,0,0,0,269,
        270,1,0,0,0,270,57,1,0,0,0,271,269,1,0,0,0,272,277,3,56,28,0,273,
        274,5,9,0,0,274,276,3,56,28,0,275,273,1,0,0,0,276,279,1,0,0,0,277,
        275,1,0,0,0,277,278,1,0,0,0,278,59,1,0,0,0,279,277,1,0,0,0,280,285,
        3,58,29,0,281,282,5,10,0,0,282,284,3,58,29,0,283,281,1,0,0,0,284,
        287,1,0,0,0,285,283,1,0,0,0,285,286,1,0,0,0,286,61,1,0,0,0,287,285,
        1,0,0,0,288,289,5,21,0,0,289,294,3,60,30,0,290,291,5,19,0,0,291,
        293,3,60,30,0,292,290,1,0,0,0,293,296,1,0,0,0,294,292,1,0,0,0,294,
        295,1,0,0,0,295,297,1,0,0,0,296,294,1,0,0,0,297,298,5,22,0,0,298,
        63,1,0,0,0,299,300,5,11,0,0,300,301,5,21,0,0,301,302,3,60,30,0,302,
        303,5,22,0,0,303,304,5,20,0,0,304,65,1,0,0,0,305,306,5,15,0,0,306,
        315,5,21,0,0,307,312,5,15,0,0,308,309,5,19,0,0,309,311,5,15,0,0,
        310,308,1,0,0,0,311,314,1,0,0,0,312,310,1,0,0,0,312,313,1,0,0,0,
        313,316,1,0,0,0,314,312,1,0,0,0,315,307,1,0,0,0,315,316,1,0,0,0,
        316,317,1,0,0,0,317,318,5,22,0,0,318,319,5,20,0,0,319,67,1,0,0,0,
        29,71,77,87,97,105,115,128,134,140,151,166,185,191,195,207,211,217,
        222,230,237,245,253,261,269,277,285,294,312,315
    ]

class CrawLangParser ( Parser ):

    grammarFileName = "CrawLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'char'", "'int'", "'if'", "'else'", 
                     "'for'", "'return'", "'not'", "'and'", "'or'", "'print'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "','", "';'", 
                     "'('", "')'", "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'='", "'=='", "'!='", "'<'", "'>'", "'<='", 
                     "'>='", "'<<'", "'>>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "SPACE", "COMMENT_BLOCK", "COMMENT_LINE", "VALID_VARIABLE_NAME", 
                      "LITERAL", "INT", "CHAR", "COMMA", "SEMICOLON", "LPAREN", 
                      "RPAREN", "LCURL", "RCURL", "PLUS", "MINUS", "TIMES", 
                      "DIVIDE", "MOD", "ASSIGN", "EQ", "NEQ", "LTHAN", "GTHAN", 
                      "LEQ", "GEQ", "SHIFT_LEFT", "SHIFT_RIGHT" ]

    RULE_funclist = 0
    RULE_function_def = 1
    RULE_main_func = 2
    RULE_func_header = 3
    RULE_func_name_decl = 4
    RULE_formal_list = 5
    RULE_base_type = 6
    RULE_statement = 7
    RULE_block = 8
    RULE_decl = 9
    RULE_assignment_statement = 10
    RULE_if_stmt = 11
    RULE_else_part = 12
    RULE_for_loop = 13
    RULE_loop_cntrl = 14
    RULE_loop_init = 15
    RULE_loop_cond = 16
    RULE_loop_incr = 17
    RULE_return_statement = 18
    RULE_primary_expr = 19
    RULE_assignment = 20
    RULE_postfix_expr = 21
    RULE_boolneg_expr = 22
    RULE_sign_expr = 23
    RULE_mul_expr = 24
    RULE_add_expr = 25
    RULE_shift_expr = 26
    RULE_rel_expr = 27
    RULE_eq_expr = 28
    RULE_lmul_expr = 29
    RULE_expr = 30
    RULE_arg_list = 31
    RULE_print = 32
    RULE_function_call = 33

    ruleNames =  [ "funclist", "function_def", "main_func", "func_header", 
                   "func_name_decl", "formal_list", "base_type", "statement", 
                   "block", "decl", "assignment_statement", "if_stmt", "else_part", 
                   "for_loop", "loop_cntrl", "loop_init", "loop_cond", "loop_incr", 
                   "return_statement", "primary_expr", "assignment", "postfix_expr", 
                   "boolneg_expr", "sign_expr", "mul_expr", "add_expr", 
                   "shift_expr", "rel_expr", "eq_expr", "lmul_expr", "expr", 
                   "arg_list", "print", "function_call" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    SPACE=12
    COMMENT_BLOCK=13
    COMMENT_LINE=14
    VALID_VARIABLE_NAME=15
    LITERAL=16
    INT=17
    CHAR=18
    COMMA=19
    SEMICOLON=20
    LPAREN=21
    RPAREN=22
    LCURL=23
    RCURL=24
    PLUS=25
    MINUS=26
    TIMES=27
    DIVIDE=28
    MOD=29
    ASSIGN=30
    EQ=31
    NEQ=32
    LTHAN=33
    GTHAN=34
    LEQ=35
    GEQ=36
    SHIFT_LEFT=37
    SHIFT_RIGHT=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FunclistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main_func(self):
            return self.getTypedRuleContext(CrawLangParser.Main_funcContext,0)


        def EOF(self):
            return self.getToken(CrawLangParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CrawLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(CrawLangParser.StatementContext,i)


        def function_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CrawLangParser.Function_defContext)
            else:
                return self.getTypedRuleContext(CrawLangParser.Function_defContext,i)


        def getRuleIndex(self):
            return CrawLangParser.RULE_funclist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunclist" ):
                listener.enterFunclist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunclist" ):
                listener.exitFunclist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunclist" ):
                return visitor.visitFunclist(self)
            else:
                return visitor.visitChildren(self)




    def funclist(self):

        localctx = CrawLangParser.FunclistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_funclist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 68
                    self.statement() 
                self.state = 73
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 77
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 74
                    self.function_def() 
                self.state = 79
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 80
            self.main_func()
            self.state = 81
            self.match(CrawLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_header(self):
            return self.getTypedRuleContext(CrawLangParser.Func_headerContext,0)


        def block(self):
            return self.getTypedRuleContext(CrawLangParser.BlockContext,0)


        def getRuleIndex(self):
            return CrawLangParser.RULE_function_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_def" ):
                listener.enterFunction_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_def" ):
                listener.exitFunction_def(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_def" ):
                return visitor.visitFunction_def(self)
            else:
                return visitor.visitChildren(self)




    def function_def(self):

        localctx = CrawLangParser.Function_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.func_header()
            self.state = 84
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(CrawLangParser.LPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(CrawLangParser.BlockContext,0)


        def RPAREN(self):
            return self.getToken(CrawLangParser.RPAREN, 0)

        def base_type(self):
            return self.getTypedRuleContext(CrawLangParser.Base_typeContext,0)


        def getRuleIndex(self):
            return CrawLangParser.RULE_main_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain_func" ):
                listener.enterMain_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain_func" ):
                listener.exitMain_func(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_func" ):
                return visitor.visitMain_func(self)
            else:
                return visitor.visitChildren(self)




    def main_func(self):

        localctx = CrawLangParser.Main_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_main_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2 or _la==3:
                self.state = 86
                self.base_type()


            self.state = 89
            self.match(CrawLangParser.T__0)
            self.state = 90
            self.match(CrawLangParser.LPAREN)
            self.state = 91
            self.block()
            self.state = 92
            self.match(CrawLangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_headerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_name_decl(self):
            return self.getTypedRuleContext(CrawLangParser.Func_name_declContext,0)


        def LPAREN(self):
            return self.getToken(CrawLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CrawLangParser.RPAREN, 0)

        def formal_list(self):
            return self.getTypedRuleContext(CrawLangParser.Formal_listContext,0)


        def getRuleIndex(self):
            return CrawLangParser.RULE_func_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_header" ):
                listener.enterFunc_header(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_header" ):
                listener.exitFunc_header(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_header" ):
                return visitor.visitFunc_header(self)
            else:
                return visitor.visitChildren(self)




    def func_header(self):

        localctx = CrawLangParser.Func_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_func_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.func_name_decl()
            self.state = 95
            self.match(CrawLangParser.LPAREN)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2 or _la==3:
                self.state = 96
                self.formal_list()


            self.state = 99
            self.match(CrawLangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_name_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VALID_VARIABLE_NAME(self):
            return self.getToken(CrawLangParser.VALID_VARIABLE_NAME, 0)

        def base_type(self):
            return self.getTypedRuleContext(CrawLangParser.Base_typeContext,0)


        def getRuleIndex(self):
            return CrawLangParser.RULE_func_name_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_name_decl" ):
                listener.enterFunc_name_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_name_decl" ):
                listener.exitFunc_name_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_name_decl" ):
                return visitor.visitFunc_name_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_name_decl(self):

        localctx = CrawLangParser.Func_name_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_func_name_decl)
        try:
            self.state = 105
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.match(CrawLangParser.VALID_VARIABLE_NAME)
                pass
            elif token in [2, 3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.base_type()
                self.state = 103
                self.match(CrawLangParser.VALID_VARIABLE_NAME)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Formal_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def base_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CrawLangParser.Base_typeContext)
            else:
                return self.getTypedRuleContext(CrawLangParser.Base_typeContext,i)


        def VALID_VARIABLE_NAME(self, i:int=None):
            if i is None:
                return self.getTokens(CrawLangParser.VALID_VARIABLE_NAME)
            else:
                return self.getToken(CrawLangParser.VALID_VARIABLE_NAME, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CrawLangParser.COMMA)
            else:
                return self.getToken(CrawLangParser.COMMA, i)

        def getRuleIndex(self):
            return CrawLangParser.RULE_formal_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormal_list" ):
                listener.enterFormal_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormal_list" ):
                listener.exitFormal_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormal_list" ):
                return visitor.visitFormal_list(self)
            else:
                return visitor.visitChildren(self)




    def formal_list(self):

        localctx = CrawLangParser.Formal_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_formal_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.base_type()
            self.state = 108
            self.match(CrawLangParser.VALID_VARIABLE_NAME)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 109
                self.match(CrawLangParser.COMMA)
                self.state = 110
                self.base_type()
                self.state = 111
                self.match(CrawLangParser.VALID_VARIABLE_NAME)
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Base_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CrawLangParser.RULE_base_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBase_type" ):
                listener.enterBase_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBase_type" ):
                listener.exitBase_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBase_type" ):
                return visitor.visitBase_type(self)
            else:
                return visitor.visitChildren(self)




    def base_type(self):

        localctx = CrawLangParser.Base_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_base_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(CrawLangParser.BlockContext,0)


        def print_(self):
            return self.getTypedRuleContext(CrawLangParser.PrintContext,0)


        def assignment_statement(self):
            return self.getTypedRuleContext(CrawLangParser.Assignment_statementContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(CrawLangParser.If_stmtContext,0)


        def for_loop(self):
            return self.getTypedRuleContext(CrawLangParser.For_loopContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(CrawLangParser.Return_statementContext,0)


        def function_call(self):
            return self.getTypedRuleContext(CrawLangParser.Function_callContext,0)


        def SEMICOLON(self):
            return self.getToken(CrawLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CrawLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = CrawLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_statement)
        try:
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.print_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 122
                self.assignment_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 123
                self.if_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 124
                self.for_loop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 125
                self.return_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 126
                self.function_call()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 127
                self.match(CrawLangParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCURL(self):
            return self.getToken(CrawLangParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(CrawLangParser.RCURL, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CrawLangParser.DeclContext)
            else:
                return self.getTypedRuleContext(CrawLangParser.DeclContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CrawLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(CrawLangParser.StatementContext,i)


        def getRuleIndex(self):
            return CrawLangParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = CrawLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(CrawLangParser.LCURL)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==3:
                self.state = 131
                self.decl()
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 78744016) != 0):
                self.state = 137
                self.statement()
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 143
            self.match(CrawLangParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def base_type(self):
            return self.getTypedRuleContext(CrawLangParser.Base_typeContext,0)


        def VALID_VARIABLE_NAME(self, i:int=None):
            if i is None:
                return self.getTokens(CrawLangParser.VALID_VARIABLE_NAME)
            else:
                return self.getToken(CrawLangParser.VALID_VARIABLE_NAME, i)

        def SEMICOLON(self):
            return self.getToken(CrawLangParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CrawLangParser.COMMA)
            else:
                return self.getToken(CrawLangParser.COMMA, i)

        def getRuleIndex(self):
            return CrawLangParser.RULE_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl" ):
                listener.enterDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl" ):
                listener.exitDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = CrawLangParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.base_type()
            self.state = 146
            self.match(CrawLangParser.VALID_VARIABLE_NAME)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 147
                self.match(CrawLangParser.COMMA)
                self.state = 148
                self.match(CrawLangParser.VALID_VARIABLE_NAME)
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 154
            self.match(CrawLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(CrawLangParser.AssignmentContext,0)


        def SEMICOLON(self):
            return self.getToken(CrawLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CrawLangParser.RULE_assignment_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_statement" ):
                listener.enterAssignment_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_statement" ):
                listener.exitAssignment_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = CrawLangParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.assignment()
            self.state = 157
            self.match(CrawLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(CrawLangParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(CrawLangParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(CrawLangParser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(CrawLangParser.StatementContext,0)


        def else_part(self):
            return self.getTypedRuleContext(CrawLangParser.Else_partContext,0)


        def getRuleIndex(self):
            return CrawLangParser.RULE_if_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stmt" ):
                listener.enterIf_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stmt" ):
                listener.exitIf_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = CrawLangParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(CrawLangParser.T__3)
            self.state = 160
            self.match(CrawLangParser.LPAREN)
            self.state = 161
            self.expr()
            self.state = 162
            self.match(CrawLangParser.RPAREN)
            self.state = 163
            self.statement()
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 164
                self.else_part()
                pass

            elif la_ == 2:
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(CrawLangParser.StatementContext,0)


        def getRuleIndex(self):
            return CrawLangParser.RULE_else_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_part" ):
                listener.enterElse_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_part" ):
                listener.exitElse_part(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_part" ):
                return visitor.visitElse_part(self)
            else:
                return visitor.visitChildren(self)




    def else_part(self):

        localctx = CrawLangParser.Else_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_else_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(CrawLangParser.T__4)
            self.state = 169
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loop_cntrl(self):
            return self.getTypedRuleContext(CrawLangParser.Loop_cntrlContext,0)


        def statement(self):
            return self.getTypedRuleContext(CrawLangParser.StatementContext,0)


        def getRuleIndex(self):
            return CrawLangParser.RULE_for_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_loop" ):
                listener.enterFor_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_loop" ):
                listener.exitFor_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop" ):
                return visitor.visitFor_loop(self)
            else:
                return visitor.visitChildren(self)




    def for_loop(self):

        localctx = CrawLangParser.For_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_for_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(CrawLangParser.T__5)
            self.state = 172
            self.loop_cntrl()
            self.state = 173
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_cntrlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(CrawLangParser.LPAREN, 0)

        def loop_init(self):
            return self.getTypedRuleContext(CrawLangParser.Loop_initContext,0)


        def loop_cond(self):
            return self.getTypedRuleContext(CrawLangParser.Loop_condContext,0)


        def loop_incr(self):
            return self.getTypedRuleContext(CrawLangParser.Loop_incrContext,0)


        def RPAREN(self):
            return self.getToken(CrawLangParser.RPAREN, 0)

        def getRuleIndex(self):
            return CrawLangParser.RULE_loop_cntrl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop_cntrl" ):
                listener.enterLoop_cntrl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop_cntrl" ):
                listener.exitLoop_cntrl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_cntrl" ):
                return visitor.visitLoop_cntrl(self)
            else:
                return visitor.visitChildren(self)




    def loop_cntrl(self):

        localctx = CrawLangParser.Loop_cntrlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_loop_cntrl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(CrawLangParser.LPAREN)
            self.state = 176
            self.loop_init()
            self.state = 177
            self.loop_cond()
            self.state = 178
            self.loop_incr()
            self.state = 179
            self.match(CrawLangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(CrawLangParser.SEMICOLON, 0)

        def assignment(self):
            return self.getTypedRuleContext(CrawLangParser.AssignmentContext,0)


        def getRuleIndex(self):
            return CrawLangParser.RULE_loop_init

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop_init" ):
                listener.enterLoop_init(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop_init" ):
                listener.exitLoop_init(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_init" ):
                return visitor.visitLoop_init(self)
            else:
                return visitor.visitChildren(self)




    def loop_init(self):

        localctx = CrawLangParser.Loop_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_loop_init)
        try:
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.match(CrawLangParser.SEMICOLON)
                pass
            elif token in [8, 15, 16, 21, 26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.assignment()
                self.state = 183
                self.match(CrawLangParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_condContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(CrawLangParser.SEMICOLON, 0)

        def expr(self):
            return self.getTypedRuleContext(CrawLangParser.ExprContext,0)


        def getRuleIndex(self):
            return CrawLangParser.RULE_loop_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop_cond" ):
                listener.enterLoop_cond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop_cond" ):
                listener.exitLoop_cond(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_cond" ):
                return visitor.visitLoop_cond(self)
            else:
                return visitor.visitChildren(self)




    def loop_cond(self):

        localctx = CrawLangParser.Loop_condContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_loop_cond)
        try:
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.match(CrawLangParser.SEMICOLON)
                pass
            elif token in [8, 15, 16, 21, 26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.expr()
                self.state = 189
                self.match(CrawLangParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_incrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(CrawLangParser.AssignmentContext,0)


        def getRuleIndex(self):
            return CrawLangParser.RULE_loop_incr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop_incr" ):
                listener.enterLoop_incr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop_incr" ):
                listener.exitLoop_incr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_incr" ):
                return visitor.visitLoop_incr(self)
            else:
                return visitor.visitChildren(self)




    def loop_incr(self):

        localctx = CrawLangParser.Loop_incrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_loop_incr)
        try:
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [8, 15, 16, 21, 26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.assignment()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CrawLangParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(CrawLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CrawLangParser.RULE_return_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_statement" ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_statement" ):
                listener.exitReturn_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = CrawLangParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(CrawLangParser.T__6)
            self.state = 198
            self.expr()
            self.state = 199
            self.match(CrawLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VALID_VARIABLE_NAME(self):
            return self.getToken(CrawLangParser.VALID_VARIABLE_NAME, 0)

        def LITERAL(self):
            return self.getToken(CrawLangParser.LITERAL, 0)

        def LPAREN(self):
            return self.getToken(CrawLangParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(CrawLangParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(CrawLangParser.RPAREN, 0)

        def getRuleIndex(self):
            return CrawLangParser.RULE_primary_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary_expr" ):
                listener.enterPrimary_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary_expr" ):
                listener.exitPrimary_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary_expr" ):
                return visitor.visitPrimary_expr(self)
            else:
                return visitor.visitChildren(self)




    def primary_expr(self):

        localctx = CrawLangParser.Primary_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_primary_expr)
        try:
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.match(CrawLangParser.VALID_VARIABLE_NAME)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.match(CrawLangParser.LITERAL)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 203
                self.match(CrawLangParser.LPAREN)
                self.state = 204
                self.expr()
                self.state = 205
                self.match(CrawLangParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.variable_name = None # Token

        def expr(self):
            return self.getTypedRuleContext(CrawLangParser.ExprContext,0)


        def ASSIGN(self):
            return self.getToken(CrawLangParser.ASSIGN, 0)

        def VALID_VARIABLE_NAME(self):
            return self.getToken(CrawLangParser.VALID_VARIABLE_NAME, 0)

        def getRuleIndex(self):
            return CrawLangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = CrawLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 209
                localctx.variable_name = self.match(CrawLangParser.VALID_VARIABLE_NAME)
                self.state = 210
                self.match(CrawLangParser.ASSIGN)


            self.state = 213
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Postfix_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary_expr(self):
            return self.getTypedRuleContext(CrawLangParser.Primary_exprContext,0)


        def arg_list(self):
            return self.getTypedRuleContext(CrawLangParser.Arg_listContext,0)


        def getRuleIndex(self):
            return CrawLangParser.RULE_postfix_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfix_expr" ):
                listener.enterPostfix_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfix_expr" ):
                listener.exitPostfix_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfix_expr" ):
                return visitor.visitPostfix_expr(self)
            else:
                return visitor.visitChildren(self)




    def postfix_expr(self):

        localctx = CrawLangParser.Postfix_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_postfix_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.primary_expr()
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 216
                self.arg_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolneg_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def postfix_expr(self):
            return self.getTypedRuleContext(CrawLangParser.Postfix_exprContext,0)


        def getRuleIndex(self):
            return CrawLangParser.RULE_boolneg_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolneg_expr" ):
                listener.enterBoolneg_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolneg_expr" ):
                listener.exitBoolneg_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolneg_expr" ):
                return visitor.visitBoolneg_expr(self)
            else:
                return visitor.visitChildren(self)




    def boolneg_expr(self):

        localctx = CrawLangParser.Boolneg_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_boolneg_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 219
                self.match(CrawLangParser.T__7)
                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 225
            self.postfix_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sign_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolneg_expr(self):
            return self.getTypedRuleContext(CrawLangParser.Boolneg_exprContext,0)


        def MINUS(self):
            return self.getToken(CrawLangParser.MINUS, 0)

        def getRuleIndex(self):
            return CrawLangParser.RULE_sign_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSign_expr" ):
                listener.enterSign_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSign_expr" ):
                listener.exitSign_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_expr" ):
                return visitor.visitSign_expr(self)
            else:
                return visitor.visitChildren(self)




    def sign_expr(self):

        localctx = CrawLangParser.Sign_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_sign_expr)
        try:
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 15, 16, 21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.boolneg_expr()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self.match(CrawLangParser.MINUS)
                self.state = 229
                self.boolneg_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mul_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sign_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CrawLangParser.Sign_exprContext)
            else:
                return self.getTypedRuleContext(CrawLangParser.Sign_exprContext,i)


        def TIMES(self, i:int=None):
            if i is None:
                return self.getTokens(CrawLangParser.TIMES)
            else:
                return self.getToken(CrawLangParser.TIMES, i)

        def DIVIDE(self, i:int=None):
            if i is None:
                return self.getTokens(CrawLangParser.DIVIDE)
            else:
                return self.getToken(CrawLangParser.DIVIDE, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(CrawLangParser.MOD)
            else:
                return self.getToken(CrawLangParser.MOD, i)

        def getRuleIndex(self):
            return CrawLangParser.RULE_mul_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul_expr" ):
                listener.enterMul_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul_expr" ):
                listener.exitMul_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_expr" ):
                return visitor.visitMul_expr(self)
            else:
                return visitor.visitChildren(self)




    def mul_expr(self):

        localctx = CrawLangParser.Mul_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_mul_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.sign_expr()
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 939524096) != 0):
                self.state = 233
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 939524096) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 234
                self.sign_expr()
                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Add_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mul_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CrawLangParser.Mul_exprContext)
            else:
                return self.getTypedRuleContext(CrawLangParser.Mul_exprContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(CrawLangParser.PLUS)
            else:
                return self.getToken(CrawLangParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(CrawLangParser.MINUS)
            else:
                return self.getToken(CrawLangParser.MINUS, i)

        def getRuleIndex(self):
            return CrawLangParser.RULE_add_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd_expr" ):
                listener.enterAdd_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd_expr" ):
                listener.exitAdd_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_expr" ):
                return visitor.visitAdd_expr(self)
            else:
                return visitor.visitChildren(self)




    def add_expr(self):

        localctx = CrawLangParser.Add_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_add_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.mul_expr()
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25 or _la==26:
                self.state = 241
                _la = self._input.LA(1)
                if not(_la==25 or _la==26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 242
                self.mul_expr()
                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Shift_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def add_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CrawLangParser.Add_exprContext)
            else:
                return self.getTypedRuleContext(CrawLangParser.Add_exprContext,i)


        def SHIFT_LEFT(self, i:int=None):
            if i is None:
                return self.getTokens(CrawLangParser.SHIFT_LEFT)
            else:
                return self.getToken(CrawLangParser.SHIFT_LEFT, i)

        def SHIFT_RIGHT(self, i:int=None):
            if i is None:
                return self.getTokens(CrawLangParser.SHIFT_RIGHT)
            else:
                return self.getToken(CrawLangParser.SHIFT_RIGHT, i)

        def getRuleIndex(self):
            return CrawLangParser.RULE_shift_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShift_expr" ):
                listener.enterShift_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShift_expr" ):
                listener.exitShift_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShift_expr" ):
                return visitor.visitShift_expr(self)
            else:
                return visitor.visitChildren(self)




    def shift_expr(self):

        localctx = CrawLangParser.Shift_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_shift_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.add_expr()
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37 or _la==38:
                self.state = 249
                _la = self._input.LA(1)
                if not(_la==37 or _la==38):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 250
                self.add_expr()
                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rel_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def shift_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CrawLangParser.Shift_exprContext)
            else:
                return self.getTypedRuleContext(CrawLangParser.Shift_exprContext,i)


        def LTHAN(self, i:int=None):
            if i is None:
                return self.getTokens(CrawLangParser.LTHAN)
            else:
                return self.getToken(CrawLangParser.LTHAN, i)

        def GTHAN(self, i:int=None):
            if i is None:
                return self.getTokens(CrawLangParser.GTHAN)
            else:
                return self.getToken(CrawLangParser.GTHAN, i)

        def GEQ(self, i:int=None):
            if i is None:
                return self.getTokens(CrawLangParser.GEQ)
            else:
                return self.getToken(CrawLangParser.GEQ, i)

        def LEQ(self, i:int=None):
            if i is None:
                return self.getTokens(CrawLangParser.LEQ)
            else:
                return self.getToken(CrawLangParser.LEQ, i)

        def getRuleIndex(self):
            return CrawLangParser.RULE_rel_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRel_expr" ):
                listener.enterRel_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRel_expr" ):
                listener.exitRel_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRel_expr" ):
                return visitor.visitRel_expr(self)
            else:
                return visitor.visitChildren(self)




    def rel_expr(self):

        localctx = CrawLangParser.Rel_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_rel_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.shift_expr()
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 128849018880) != 0):
                self.state = 257
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 128849018880) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 258
                self.shift_expr()
                self.state = 263
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Eq_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rel_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CrawLangParser.Rel_exprContext)
            else:
                return self.getTypedRuleContext(CrawLangParser.Rel_exprContext,i)


        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(CrawLangParser.EQ)
            else:
                return self.getToken(CrawLangParser.EQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(CrawLangParser.NEQ)
            else:
                return self.getToken(CrawLangParser.NEQ, i)

        def getRuleIndex(self):
            return CrawLangParser.RULE_eq_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEq_expr" ):
                listener.enterEq_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEq_expr" ):
                listener.exitEq_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEq_expr" ):
                return visitor.visitEq_expr(self)
            else:
                return visitor.visitChildren(self)




    def eq_expr(self):

        localctx = CrawLangParser.Eq_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_eq_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.rel_expr()
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31 or _la==32:
                self.state = 265
                _la = self._input.LA(1)
                if not(_la==31 or _la==32):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 266
                self.rel_expr()
                self.state = 271
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lmul_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eq_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CrawLangParser.Eq_exprContext)
            else:
                return self.getTypedRuleContext(CrawLangParser.Eq_exprContext,i)


        def getRuleIndex(self):
            return CrawLangParser.RULE_lmul_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLmul_expr" ):
                listener.enterLmul_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLmul_expr" ):
                listener.exitLmul_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLmul_expr" ):
                return visitor.visitLmul_expr(self)
            else:
                return visitor.visitChildren(self)




    def lmul_expr(self):

        localctx = CrawLangParser.Lmul_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_lmul_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.eq_expr()
            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 273
                self.match(CrawLangParser.T__8)
                self.state = 274
                self.eq_expr()
                self.state = 279
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lmul_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CrawLangParser.Lmul_exprContext)
            else:
                return self.getTypedRuleContext(CrawLangParser.Lmul_exprContext,i)


        def getRuleIndex(self):
            return CrawLangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = CrawLangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.lmul_expr()
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 281
                self.match(CrawLangParser.T__9)
                self.state = 282
                self.lmul_expr()
                self.state = 287
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(CrawLangParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CrawLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(CrawLangParser.ExprContext,i)


        def RPAREN(self):
            return self.getToken(CrawLangParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CrawLangParser.COMMA)
            else:
                return self.getToken(CrawLangParser.COMMA, i)

        def getRuleIndex(self):
            return CrawLangParser.RULE_arg_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg_list" ):
                listener.enterArg_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg_list" ):
                listener.exitArg_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg_list" ):
                return visitor.visitArg_list(self)
            else:
                return visitor.visitChildren(self)




    def arg_list(self):

        localctx = CrawLangParser.Arg_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_arg_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(CrawLangParser.LPAREN)
            self.state = 289
            self.expr()
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 290
                self.match(CrawLangParser.COMMA)
                self.state = 291
                self.expr()
                self.state = 296
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 297
            self.match(CrawLangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(CrawLangParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(CrawLangParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(CrawLangParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(CrawLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CrawLangParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = CrawLangParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(CrawLangParser.T__10)
            self.state = 300
            self.match(CrawLangParser.LPAREN)
            self.state = 301
            self.expr()
            self.state = 302
            self.match(CrawLangParser.RPAREN)
            self.state = 303
            self.match(CrawLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VALID_VARIABLE_NAME(self, i:int=None):
            if i is None:
                return self.getTokens(CrawLangParser.VALID_VARIABLE_NAME)
            else:
                return self.getToken(CrawLangParser.VALID_VARIABLE_NAME, i)

        def LPAREN(self):
            return self.getToken(CrawLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CrawLangParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(CrawLangParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CrawLangParser.COMMA)
            else:
                return self.getToken(CrawLangParser.COMMA, i)

        def getRuleIndex(self):
            return CrawLangParser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = CrawLangParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(CrawLangParser.VALID_VARIABLE_NAME)
            self.state = 306
            self.match(CrawLangParser.LPAREN)
            self.state = 315
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 307
                self.match(CrawLangParser.VALID_VARIABLE_NAME)
                self.state = 312
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==19:
                    self.state = 308
                    self.match(CrawLangParser.COMMA)
                    self.state = 309
                    self.match(CrawLangParser.VALID_VARIABLE_NAME)
                    self.state = 314
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 317
            self.match(CrawLangParser.RPAREN)
            self.state = 318
            self.match(CrawLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





