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
        4,1,40,306,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,1,0,1,0,5,0,71,8,0,10,0,12,0,74,9,0,1,0,1,0,1,0,1,1,1,1,1,1,
        1,2,3,2,83,8,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,3,3,93,8,3,1,3,1,
        3,1,4,1,4,1,4,1,4,3,4,101,8,4,1,5,1,5,1,5,1,5,1,5,1,5,5,5,109,8,
        5,10,5,12,5,112,9,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,
        124,8,7,1,8,1,8,1,8,5,8,129,8,8,10,8,12,8,132,9,8,1,8,1,8,1,9,1,
        9,1,9,1,9,5,9,140,8,9,10,9,12,9,143,9,9,1,9,1,9,1,10,1,10,1,10,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,157,8,11,1,12,1,12,1,12,1,
        13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,
        15,3,15,176,8,15,1,16,1,16,1,16,1,16,3,16,182,8,16,1,17,1,17,3,17,
        186,8,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        3,19,199,8,19,1,20,1,20,3,20,203,8,20,1,20,1,20,1,21,5,21,208,8,
        21,10,21,12,21,211,9,21,1,21,1,21,1,22,1,22,1,22,3,22,218,8,22,1,
        23,1,23,1,23,5,23,223,8,23,10,23,12,23,226,9,23,1,24,1,24,1,24,5,
        24,231,8,24,10,24,12,24,234,9,24,1,25,1,25,1,25,5,25,239,8,25,10,
        25,12,25,242,9,25,1,26,1,26,1,26,5,26,247,8,26,10,26,12,26,250,9,
        26,1,27,1,27,1,27,5,27,255,8,27,10,27,12,27,258,9,27,1,28,1,28,1,
        28,5,28,263,8,28,10,28,12,28,266,9,28,1,29,1,29,1,29,5,29,271,8,
        29,10,29,12,29,274,9,29,1,29,3,29,277,8,29,1,30,1,30,1,30,5,30,282,
        8,30,10,30,12,30,285,9,30,1,31,1,31,1,31,1,31,1,31,1,31,1,32,1,32,
        1,32,3,32,296,8,32,1,32,1,32,1,32,1,33,1,33,1,33,3,33,304,8,33,1,
        33,0,0,34,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,56,58,60,62,64,66,0,6,1,0,2,4,1,0,29,31,
        1,0,27,28,1,0,39,40,1,0,35,38,1,0,33,34,309,0,72,1,0,0,0,2,78,1,
        0,0,0,4,82,1,0,0,0,6,89,1,0,0,0,8,100,1,0,0,0,10,102,1,0,0,0,12,
        113,1,0,0,0,14,123,1,0,0,0,16,125,1,0,0,0,18,135,1,0,0,0,20,146,
        1,0,0,0,22,149,1,0,0,0,24,158,1,0,0,0,26,161,1,0,0,0,28,165,1,0,
        0,0,30,175,1,0,0,0,32,181,1,0,0,0,34,185,1,0,0,0,36,187,1,0,0,0,
        38,198,1,0,0,0,40,202,1,0,0,0,42,209,1,0,0,0,44,217,1,0,0,0,46,219,
        1,0,0,0,48,227,1,0,0,0,50,235,1,0,0,0,52,243,1,0,0,0,54,251,1,0,
        0,0,56,259,1,0,0,0,58,276,1,0,0,0,60,278,1,0,0,0,62,286,1,0,0,0,
        64,292,1,0,0,0,66,303,1,0,0,0,68,71,3,14,7,0,69,71,3,2,1,0,70,68,
        1,0,0,0,70,69,1,0,0,0,71,74,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,
        73,75,1,0,0,0,74,72,1,0,0,0,75,76,3,4,2,0,76,77,5,0,0,1,77,1,1,0,
        0,0,78,79,3,6,3,0,79,80,3,16,8,0,80,3,1,0,0,0,81,83,3,12,6,0,82,
        81,1,0,0,0,82,83,1,0,0,0,83,84,1,0,0,0,84,85,5,1,0,0,85,86,5,23,
        0,0,86,87,5,24,0,0,87,88,3,16,8,0,88,5,1,0,0,0,89,90,3,8,4,0,90,
        92,5,23,0,0,91,93,3,10,5,0,92,91,1,0,0,0,92,93,1,0,0,0,93,94,1,0,
        0,0,94,95,5,24,0,0,95,7,1,0,0,0,96,101,5,16,0,0,97,98,3,12,6,0,98,
        99,5,16,0,0,99,101,1,0,0,0,100,96,1,0,0,0,100,97,1,0,0,0,101,9,1,
        0,0,0,102,103,3,12,6,0,103,110,5,16,0,0,104,105,5,21,0,0,105,106,
        3,12,6,0,106,107,5,16,0,0,107,109,1,0,0,0,108,104,1,0,0,0,109,112,
        1,0,0,0,110,108,1,0,0,0,110,111,1,0,0,0,111,11,1,0,0,0,112,110,1,
        0,0,0,113,114,7,0,0,0,114,13,1,0,0,0,115,124,3,16,8,0,116,124,3,
        62,31,0,117,124,3,20,10,0,118,124,3,22,11,0,119,124,3,26,13,0,120,
        124,3,36,18,0,121,124,3,64,32,0,122,124,5,22,0,0,123,115,1,0,0,0,
        123,116,1,0,0,0,123,117,1,0,0,0,123,118,1,0,0,0,123,119,1,0,0,0,
        123,120,1,0,0,0,123,121,1,0,0,0,123,122,1,0,0,0,124,15,1,0,0,0,125,
        130,5,25,0,0,126,129,3,18,9,0,127,129,3,14,7,0,128,126,1,0,0,0,128,
        127,1,0,0,0,129,132,1,0,0,0,130,128,1,0,0,0,130,131,1,0,0,0,131,
        133,1,0,0,0,132,130,1,0,0,0,133,134,5,26,0,0,134,17,1,0,0,0,135,
        136,3,12,6,0,136,141,5,16,0,0,137,138,5,21,0,0,138,140,5,16,0,0,
        139,137,1,0,0,0,140,143,1,0,0,0,141,139,1,0,0,0,141,142,1,0,0,0,
        142,144,1,0,0,0,143,141,1,0,0,0,144,145,5,22,0,0,145,19,1,0,0,0,
        146,147,3,40,20,0,147,148,5,22,0,0,148,21,1,0,0,0,149,150,5,5,0,
        0,150,151,5,23,0,0,151,152,3,58,29,0,152,153,5,24,0,0,153,156,3,
        14,7,0,154,157,3,24,12,0,155,157,1,0,0,0,156,154,1,0,0,0,156,155,
        1,0,0,0,157,23,1,0,0,0,158,159,5,6,0,0,159,160,3,14,7,0,160,25,1,
        0,0,0,161,162,5,7,0,0,162,163,3,28,14,0,163,164,3,14,7,0,164,27,
        1,0,0,0,165,166,5,23,0,0,166,167,3,30,15,0,167,168,3,32,16,0,168,
        169,3,34,17,0,169,170,5,24,0,0,170,29,1,0,0,0,171,176,5,22,0,0,172,
        173,3,40,20,0,173,174,5,22,0,0,174,176,1,0,0,0,175,171,1,0,0,0,175,
        172,1,0,0,0,176,31,1,0,0,0,177,182,5,22,0,0,178,179,3,58,29,0,179,
        180,5,22,0,0,180,182,1,0,0,0,181,177,1,0,0,0,181,178,1,0,0,0,182,
        33,1,0,0,0,183,186,1,0,0,0,184,186,3,40,20,0,185,183,1,0,0,0,185,
        184,1,0,0,0,186,35,1,0,0,0,187,188,5,8,0,0,188,189,3,58,29,0,189,
        190,5,22,0,0,190,37,1,0,0,0,191,199,5,16,0,0,192,199,3,66,33,0,193,
        199,5,20,0,0,194,195,5,23,0,0,195,196,3,58,29,0,196,197,5,24,0,0,
        197,199,1,0,0,0,198,191,1,0,0,0,198,192,1,0,0,0,198,193,1,0,0,0,
        198,194,1,0,0,0,199,39,1,0,0,0,200,201,5,16,0,0,201,203,5,32,0,0,
        202,200,1,0,0,0,202,203,1,0,0,0,203,204,1,0,0,0,204,205,3,58,29,
        0,205,41,1,0,0,0,206,208,5,9,0,0,207,206,1,0,0,0,208,211,1,0,0,0,
        209,207,1,0,0,0,209,210,1,0,0,0,210,212,1,0,0,0,211,209,1,0,0,0,
        212,213,3,38,19,0,213,43,1,0,0,0,214,218,3,42,21,0,215,216,5,28,
        0,0,216,218,3,42,21,0,217,214,1,0,0,0,217,215,1,0,0,0,218,45,1,0,
        0,0,219,224,3,44,22,0,220,221,7,1,0,0,221,223,3,44,22,0,222,220,
        1,0,0,0,223,226,1,0,0,0,224,222,1,0,0,0,224,225,1,0,0,0,225,47,1,
        0,0,0,226,224,1,0,0,0,227,232,3,46,23,0,228,229,7,2,0,0,229,231,
        3,46,23,0,230,228,1,0,0,0,231,234,1,0,0,0,232,230,1,0,0,0,232,233,
        1,0,0,0,233,49,1,0,0,0,234,232,1,0,0,0,235,240,3,48,24,0,236,237,
        7,3,0,0,237,239,3,48,24,0,238,236,1,0,0,0,239,242,1,0,0,0,240,238,
        1,0,0,0,240,241,1,0,0,0,241,51,1,0,0,0,242,240,1,0,0,0,243,248,3,
        50,25,0,244,245,7,4,0,0,245,247,3,50,25,0,246,244,1,0,0,0,247,250,
        1,0,0,0,248,246,1,0,0,0,248,249,1,0,0,0,249,53,1,0,0,0,250,248,1,
        0,0,0,251,256,3,52,26,0,252,253,7,5,0,0,253,255,3,52,26,0,254,252,
        1,0,0,0,255,258,1,0,0,0,256,254,1,0,0,0,256,257,1,0,0,0,257,55,1,
        0,0,0,258,256,1,0,0,0,259,264,3,54,27,0,260,261,5,10,0,0,261,263,
        3,54,27,0,262,260,1,0,0,0,263,266,1,0,0,0,264,262,1,0,0,0,264,265,
        1,0,0,0,265,57,1,0,0,0,266,264,1,0,0,0,267,272,3,56,28,0,268,269,
        5,11,0,0,269,271,3,56,28,0,270,268,1,0,0,0,271,274,1,0,0,0,272,270,
        1,0,0,0,272,273,1,0,0,0,273,277,1,0,0,0,274,272,1,0,0,0,275,277,
        3,64,32,0,276,267,1,0,0,0,276,275,1,0,0,0,277,59,1,0,0,0,278,283,
        3,58,29,0,279,280,5,21,0,0,280,282,3,58,29,0,281,279,1,0,0,0,282,
        285,1,0,0,0,283,281,1,0,0,0,283,284,1,0,0,0,284,61,1,0,0,0,285,283,
        1,0,0,0,286,287,5,12,0,0,287,288,5,23,0,0,288,289,3,58,29,0,289,
        290,5,24,0,0,290,291,5,22,0,0,291,63,1,0,0,0,292,293,5,16,0,0,293,
        295,5,23,0,0,294,296,3,60,30,0,295,294,1,0,0,0,295,296,1,0,0,0,296,
        297,1,0,0,0,297,298,5,24,0,0,298,299,5,22,0,0,299,65,1,0,0,0,300,
        304,5,17,0,0,301,304,5,18,0,0,302,304,5,19,0,0,303,300,1,0,0,0,303,
        301,1,0,0,0,303,302,1,0,0,0,304,67,1,0,0,0,29,70,72,82,92,100,110,
        123,128,130,141,156,175,181,185,198,202,209,217,224,232,240,248,
        256,264,272,276,283,295,303
    ]

class CrawLangParser ( Parser ):

    grammarFileName = "CrawLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'char'", "'int'", "'float'", 
                     "'if'", "'else'", "'for'", "'return'", "'not'", "'and'", 
                     "'or'", "'print'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "','", "';'", "'('", "')'", "'{'", "'}'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'='", "'=='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='", "'<<'", "'>>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "SPACE", "COMMENT_BLOCK", "COMMENT_LINE", 
                      "VALID_VARIABLE_NAME", "INT", "CHAR", "FLOAT", "STRING", 
                      "COMMA", "SEMICOLON", "LPAREN", "RPAREN", "LCURL", 
                      "RCURL", "PLUS", "MINUS", "TIMES", "DIVIDE", "MOD", 
                      "ASSIGN", "EQ", "NEQ", "LTHAN", "GTHAN", "LEQ", "GEQ", 
                      "SHIFT_LEFT", "SHIFT_RIGHT" ]

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
    RULE_boolneg_expr = 21
    RULE_sign_expr = 22
    RULE_mul_expr = 23
    RULE_add_expr = 24
    RULE_shift_expr = 25
    RULE_rel_expr = 26
    RULE_eq_expr = 27
    RULE_lmul_expr = 28
    RULE_expr = 29
    RULE_arg_list = 30
    RULE_print = 31
    RULE_function_call = 32
    RULE_literal = 33

    ruleNames =  [ "funclist", "function_def", "main_func", "func_header", 
                   "func_name_decl", "formal_list", "base_type", "statement", 
                   "block", "decl", "assignment_statement", "if_stmt", "else_part", 
                   "for_loop", "loop_cntrl", "loop_init", "loop_cond", "loop_incr", 
                   "return_statement", "primary_expr", "assignment", "boolneg_expr", 
                   "sign_expr", "mul_expr", "add_expr", "shift_expr", "rel_expr", 
                   "eq_expr", "lmul_expr", "expr", "arg_list", "print", 
                   "function_call", "literal" ]

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
    T__11=12
    SPACE=13
    COMMENT_BLOCK=14
    COMMENT_LINE=15
    VALID_VARIABLE_NAME=16
    INT=17
    CHAR=18
    FLOAT=19
    STRING=20
    COMMA=21
    SEMICOLON=22
    LPAREN=23
    RPAREN=24
    LCURL=25
    RCURL=26
    PLUS=27
    MINUS=28
    TIMES=29
    DIVIDE=30
    MOD=31
    ASSIGN=32
    EQ=33
    NEQ=34
    LTHAN=35
    GTHAN=36
    LEQ=37
    GEQ=38
    SHIFT_LEFT=39
    SHIFT_RIGHT=40

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
            self.state = 72
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 70
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        self.state = 68
                        self.statement()
                        pass

                    elif la_ == 2:
                        self.state = 69
                        self.function_def()
                        pass

             
                self.state = 74
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 75
            self.main_func()
            self.state = 76
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
            self.state = 78
            self.func_header()
            self.state = 79
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

        def RPAREN(self):
            return self.getToken(CrawLangParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(CrawLangParser.BlockContext,0)


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
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0):
                self.state = 81
                self.base_type()


            self.state = 84
            self.match(CrawLangParser.T__0)
            self.state = 85
            self.match(CrawLangParser.LPAREN)
            self.state = 86
            self.match(CrawLangParser.RPAREN)
            self.state = 87
            self.block()
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
            self.state = 89
            self.func_name_decl()
            self.state = 90
            self.match(CrawLangParser.LPAREN)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0):
                self.state = 91
                self.formal_list()


            self.state = 94
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
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.match(CrawLangParser.VALID_VARIABLE_NAME)
                pass
            elif token in [2, 3, 4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.base_type()
                self.state = 98
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
            self.state = 102
            self.base_type()
            self.state = 103
            self.match(CrawLangParser.VALID_VARIABLE_NAME)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 104
                self.match(CrawLangParser.COMMA)
                self.state = 105
                self.base_type()
                self.state = 106
                self.match(CrawLangParser.VALID_VARIABLE_NAME)
                self.state = 112
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
            self.state = 113
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0)):
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
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.print_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 117
                self.assignment_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 118
                self.if_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 119
                self.for_loop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 120
                self.return_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 121
                self.function_call()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 122
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
            self.state = 125
            self.match(CrawLangParser.LCURL)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 316609468) != 0):
                self.state = 128
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2, 3, 4]:
                    self.state = 126
                    self.decl()
                    pass
                elif token in [5, 7, 8, 9, 12, 16, 17, 18, 19, 20, 22, 23, 25, 28]:
                    self.state = 127
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 133
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
            self.state = 135
            self.base_type()
            self.state = 136
            self.match(CrawLangParser.VALID_VARIABLE_NAME)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 137
                self.match(CrawLangParser.COMMA)
                self.state = 138
                self.match(CrawLangParser.VALID_VARIABLE_NAME)
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 144
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
            self.state = 146
            self.assignment()
            self.state = 147
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
            self.state = 149
            self.match(CrawLangParser.T__4)
            self.state = 150
            self.match(CrawLangParser.LPAREN)
            self.state = 151
            self.expr()
            self.state = 152
            self.match(CrawLangParser.RPAREN)
            self.state = 153
            self.statement()
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 154
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
            self.state = 158
            self.match(CrawLangParser.T__5)
            self.state = 159
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
            self.state = 161
            self.match(CrawLangParser.T__6)
            self.state = 162
            self.loop_cntrl()
            self.state = 163
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
            self.state = 165
            self.match(CrawLangParser.LPAREN)
            self.state = 166
            self.loop_init()
            self.state = 167
            self.loop_cond()
            self.state = 168
            self.loop_incr()
            self.state = 169
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
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.match(CrawLangParser.SEMICOLON)
                pass
            elif token in [9, 16, 17, 18, 19, 20, 23, 28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.assignment()
                self.state = 173
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
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.match(CrawLangParser.SEMICOLON)
                pass
            elif token in [9, 16, 17, 18, 19, 20, 23, 28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.expr()
                self.state = 179
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
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [9, 16, 17, 18, 19, 20, 23, 28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
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
            self.state = 187
            self.match(CrawLangParser.T__7)
            self.state = 188
            self.expr()
            self.state = 189
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


        def getRuleIndex(self):
            return CrawLangParser.RULE_primary_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrimaryExpressionContext(Primary_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CrawLangParser.Primary_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(CrawLangParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(CrawLangParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(CrawLangParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpression" ):
                listener.enterPrimaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpression" ):
                listener.exitPrimaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpression" ):
                return visitor.visitPrimaryExpression(self)
            else:
                return visitor.visitChildren(self)


    class PrimaryStringContext(Primary_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CrawLangParser.Primary_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(CrawLangParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryString" ):
                listener.enterPrimaryString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryString" ):
                listener.exitPrimaryString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryString" ):
                return visitor.visitPrimaryString(self)
            else:
                return visitor.visitChildren(self)


    class PrimaryVariableNameContext(Primary_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CrawLangParser.Primary_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VALID_VARIABLE_NAME(self):
            return self.getToken(CrawLangParser.VALID_VARIABLE_NAME, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryVariableName" ):
                listener.enterPrimaryVariableName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryVariableName" ):
                listener.exitPrimaryVariableName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryVariableName" ):
                return visitor.visitPrimaryVariableName(self)
            else:
                return visitor.visitChildren(self)


    class PrimaryLiteralContext(Primary_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CrawLangParser.Primary_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(CrawLangParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryLiteral" ):
                listener.enterPrimaryLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryLiteral" ):
                listener.exitPrimaryLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryLiteral" ):
                return visitor.visitPrimaryLiteral(self)
            else:
                return visitor.visitChildren(self)



    def primary_expr(self):

        localctx = CrawLangParser.Primary_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_primary_expr)
        try:
            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                localctx = CrawLangParser.PrimaryVariableNameContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.match(CrawLangParser.VALID_VARIABLE_NAME)
                pass
            elif token in [17, 18, 19]:
                localctx = CrawLangParser.PrimaryLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.literal()
                pass
            elif token in [20]:
                localctx = CrawLangParser.PrimaryStringContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 193
                self.match(CrawLangParser.STRING)
                pass
            elif token in [23]:
                localctx = CrawLangParser.PrimaryExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 194
                self.match(CrawLangParser.LPAREN)
                self.state = 195
                self.expr()
                self.state = 196
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

        def expr(self):
            return self.getTypedRuleContext(CrawLangParser.ExprContext,0)


        def VALID_VARIABLE_NAME(self):
            return self.getToken(CrawLangParser.VALID_VARIABLE_NAME, 0)

        def ASSIGN(self):
            return self.getToken(CrawLangParser.ASSIGN, 0)

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
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 200
                self.match(CrawLangParser.VALID_VARIABLE_NAME)
                self.state = 201
                self.match(CrawLangParser.ASSIGN)


            self.state = 204
            self.expr()
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

        def primary_expr(self):
            return self.getTypedRuleContext(CrawLangParser.Primary_exprContext,0)


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
        self.enterRule(localctx, 42, self.RULE_boolneg_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 206
                self.match(CrawLangParser.T__8)
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 212
            self.primary_expr()
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
        self.enterRule(localctx, 44, self.RULE_sign_expr)
        try:
            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 16, 17, 18, 19, 20, 23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.boolneg_expr()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.match(CrawLangParser.MINUS)
                self.state = 216
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
        self.enterRule(localctx, 46, self.RULE_mul_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.sign_expr()
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3758096384) != 0):
                self.state = 220
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3758096384) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 221
                self.sign_expr()
                self.state = 226
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
        self.enterRule(localctx, 48, self.RULE_add_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.mul_expr()
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27 or _la==28:
                self.state = 228
                _la = self._input.LA(1)
                if not(_la==27 or _la==28):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 229
                self.mul_expr()
                self.state = 234
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
        self.enterRule(localctx, 50, self.RULE_shift_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.add_expr()
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39 or _la==40:
                self.state = 236
                _la = self._input.LA(1)
                if not(_la==39 or _la==40):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 237
                self.add_expr()
                self.state = 242
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
        self.enterRule(localctx, 52, self.RULE_rel_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.shift_expr()
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 515396075520) != 0):
                self.state = 244
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 515396075520) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 245
                self.shift_expr()
                self.state = 250
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
        self.enterRule(localctx, 54, self.RULE_eq_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.rel_expr()
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33 or _la==34:
                self.state = 252
                _la = self._input.LA(1)
                if not(_la==33 or _la==34):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 253
                self.rel_expr()
                self.state = 258
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
        self.enterRule(localctx, 56, self.RULE_lmul_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.eq_expr()
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 260
                self.match(CrawLangParser.T__9)
                self.state = 261
                self.eq_expr()
                self.state = 266
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


        def function_call(self):
            return self.getTypedRuleContext(CrawLangParser.Function_callContext,0)


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
        self.enterRule(localctx, 58, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.lmul_expr()
                self.state = 272
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==11:
                    self.state = 268
                    self.match(CrawLangParser.T__10)
                    self.state = 269
                    self.lmul_expr()
                    self.state = 274
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.function_call()
                pass


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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CrawLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(CrawLangParser.ExprContext,i)


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
        self.enterRule(localctx, 60, self.RULE_arg_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.expr()
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 279
                self.match(CrawLangParser.COMMA)
                self.state = 280
                self.expr()
                self.state = 285
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 62, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(CrawLangParser.T__11)
            self.state = 287
            self.match(CrawLangParser.LPAREN)
            self.state = 288
            self.expr()
            self.state = 289
            self.match(CrawLangParser.RPAREN)
            self.state = 290
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

        def VALID_VARIABLE_NAME(self):
            return self.getToken(CrawLangParser.VALID_VARIABLE_NAME, 0)

        def LPAREN(self):
            return self.getToken(CrawLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CrawLangParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(CrawLangParser.SEMICOLON, 0)

        def arg_list(self):
            return self.getTypedRuleContext(CrawLangParser.Arg_listContext,0)


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
        self.enterRule(localctx, 64, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(CrawLangParser.VALID_VARIABLE_NAME)
            self.state = 293
            self.match(CrawLangParser.LPAREN)
            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 278856192) != 0):
                self.state = 294
                self.arg_list()


            self.state = 297
            self.match(CrawLangParser.RPAREN)
            self.state = 298
            self.match(CrawLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CrawLangParser.RULE_literal

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LitINTContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CrawLangParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(CrawLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLitINT" ):
                listener.enterLitINT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLitINT" ):
                listener.exitLitINT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLitINT" ):
                return visitor.visitLitINT(self)
            else:
                return visitor.visitChildren(self)


    class LitFLOATContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CrawLangParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(CrawLangParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLitFLOAT" ):
                listener.enterLitFLOAT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLitFLOAT" ):
                listener.exitLitFLOAT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLitFLOAT" ):
                return visitor.visitLitFLOAT(self)
            else:
                return visitor.visitChildren(self)


    class LitCHARContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CrawLangParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CHAR(self):
            return self.getToken(CrawLangParser.CHAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLitCHAR" ):
                listener.enterLitCHAR(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLitCHAR" ):
                listener.exitLitCHAR(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLitCHAR" ):
                return visitor.visitLitCHAR(self)
            else:
                return visitor.visitChildren(self)



    def literal(self):

        localctx = CrawLangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_literal)
        try:
            self.state = 303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                localctx = CrawLangParser.LitINTContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.match(CrawLangParser.INT)
                pass
            elif token in [18]:
                localctx = CrawLangParser.LitCHARContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.match(CrawLangParser.CHAR)
                pass
            elif token in [19]:
                localctx = CrawLangParser.LitFLOATContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 302
                self.match(CrawLangParser.FLOAT)
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





