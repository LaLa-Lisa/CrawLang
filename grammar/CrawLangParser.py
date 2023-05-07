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
        4,1,36,277,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,5,0,64,8,0,10,0,12,0,
        67,9,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,3,2,77,8,2,1,2,1,2,1,3,1,
        3,1,3,1,3,3,3,85,8,3,1,4,1,4,1,4,1,4,1,4,1,4,5,4,93,8,4,10,4,12,
        4,96,9,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,106,8,6,1,7,1,7,5,7,
        110,8,7,10,7,12,7,113,9,7,1,7,5,7,116,8,7,10,7,12,7,119,9,7,1,7,
        1,7,1,8,1,8,1,8,1,8,5,8,127,8,8,10,8,12,8,130,9,8,1,8,1,8,1,9,1,
        9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,144,8,10,1,11,1,11,
        1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,
        1,14,1,14,3,14,163,8,14,1,15,1,15,1,15,1,15,3,15,169,8,15,1,16,1,
        16,3,16,173,8,16,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,
        18,3,18,185,8,18,1,19,1,19,3,19,189,8,19,1,19,1,19,1,20,1,20,3,20,
        195,8,20,1,21,5,21,198,8,21,10,21,12,21,201,9,21,1,21,1,21,1,22,
        1,22,1,22,3,22,208,8,22,1,23,1,23,1,23,5,23,213,8,23,10,23,12,23,
        216,9,23,1,24,1,24,1,24,5,24,221,8,24,10,24,12,24,224,9,24,1,25,
        1,25,1,25,5,25,229,8,25,10,25,12,25,232,9,25,1,26,1,26,1,26,5,26,
        237,8,26,10,26,12,26,240,9,26,1,27,1,27,1,27,5,27,245,8,27,10,27,
        12,27,248,9,27,1,28,1,28,1,28,5,28,253,8,28,10,28,12,28,256,9,28,
        1,29,1,29,1,29,5,29,261,8,29,10,29,12,29,264,9,29,1,30,1,30,1,30,
        1,30,5,30,270,8,30,10,30,12,30,273,9,30,1,30,1,30,1,30,0,0,31,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,
        48,50,52,54,56,58,60,0,6,1,0,1,2,1,0,25,27,1,0,23,24,1,0,35,36,1,
        0,31,34,1,0,29,30,275,0,65,1,0,0,0,2,70,1,0,0,0,4,73,1,0,0,0,6,84,
        1,0,0,0,8,86,1,0,0,0,10,97,1,0,0,0,12,105,1,0,0,0,14,107,1,0,0,0,
        16,122,1,0,0,0,18,133,1,0,0,0,20,136,1,0,0,0,22,145,1,0,0,0,24,148,
        1,0,0,0,26,152,1,0,0,0,28,162,1,0,0,0,30,168,1,0,0,0,32,172,1,0,
        0,0,34,174,1,0,0,0,36,184,1,0,0,0,38,188,1,0,0,0,40,192,1,0,0,0,
        42,199,1,0,0,0,44,207,1,0,0,0,46,209,1,0,0,0,48,217,1,0,0,0,50,225,
        1,0,0,0,52,233,1,0,0,0,54,241,1,0,0,0,56,249,1,0,0,0,58,257,1,0,
        0,0,60,265,1,0,0,0,62,64,3,2,1,0,63,62,1,0,0,0,64,67,1,0,0,0,65,
        63,1,0,0,0,65,66,1,0,0,0,66,68,1,0,0,0,67,65,1,0,0,0,68,69,5,0,0,
        1,69,1,1,0,0,0,70,71,3,4,2,0,71,72,3,14,7,0,72,3,1,0,0,0,73,74,3,
        6,3,0,74,76,5,19,0,0,75,77,3,8,4,0,76,75,1,0,0,0,76,77,1,0,0,0,77,
        78,1,0,0,0,78,79,5,20,0,0,79,5,1,0,0,0,80,85,5,13,0,0,81,82,3,10,
        5,0,82,83,5,13,0,0,83,85,1,0,0,0,84,80,1,0,0,0,84,81,1,0,0,0,85,
        7,1,0,0,0,86,87,3,10,5,0,87,94,5,13,0,0,88,89,5,17,0,0,89,90,3,10,
        5,0,90,91,5,13,0,0,91,93,1,0,0,0,92,88,1,0,0,0,93,96,1,0,0,0,94,
        92,1,0,0,0,94,95,1,0,0,0,95,9,1,0,0,0,96,94,1,0,0,0,97,98,7,0,0,
        0,98,11,1,0,0,0,99,106,3,14,7,0,100,106,3,18,9,0,101,106,3,20,10,
        0,102,106,3,24,12,0,103,106,3,34,17,0,104,106,5,18,0,0,105,99,1,
        0,0,0,105,100,1,0,0,0,105,101,1,0,0,0,105,102,1,0,0,0,105,103,1,
        0,0,0,105,104,1,0,0,0,106,13,1,0,0,0,107,111,5,21,0,0,108,110,3,
        16,8,0,109,108,1,0,0,0,110,113,1,0,0,0,111,109,1,0,0,0,111,112,1,
        0,0,0,112,117,1,0,0,0,113,111,1,0,0,0,114,116,3,12,6,0,115,114,1,
        0,0,0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,120,1,
        0,0,0,119,117,1,0,0,0,120,121,5,22,0,0,121,15,1,0,0,0,122,123,3,
        10,5,0,123,128,5,13,0,0,124,125,5,17,0,0,125,127,5,13,0,0,126,124,
        1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,131,
        1,0,0,0,130,128,1,0,0,0,131,132,5,18,0,0,132,17,1,0,0,0,133,134,
        3,38,19,0,134,135,5,18,0,0,135,19,1,0,0,0,136,137,5,3,0,0,137,138,
        5,19,0,0,138,139,3,58,29,0,139,140,5,20,0,0,140,143,3,12,6,0,141,
        144,3,22,11,0,142,144,1,0,0,0,143,141,1,0,0,0,143,142,1,0,0,0,144,
        21,1,0,0,0,145,146,5,4,0,0,146,147,3,12,6,0,147,23,1,0,0,0,148,149,
        5,5,0,0,149,150,3,26,13,0,150,151,3,12,6,0,151,25,1,0,0,0,152,153,
        5,19,0,0,153,154,3,28,14,0,154,155,3,30,15,0,155,156,3,32,16,0,156,
        157,5,20,0,0,157,27,1,0,0,0,158,163,5,18,0,0,159,160,3,38,19,0,160,
        161,5,18,0,0,161,163,1,0,0,0,162,158,1,0,0,0,162,159,1,0,0,0,163,
        29,1,0,0,0,164,169,5,18,0,0,165,166,3,58,29,0,166,167,5,18,0,0,167,
        169,1,0,0,0,168,164,1,0,0,0,168,165,1,0,0,0,169,31,1,0,0,0,170,173,
        1,0,0,0,171,173,3,38,19,0,172,170,1,0,0,0,172,171,1,0,0,0,173,33,
        1,0,0,0,174,175,5,6,0,0,175,176,3,58,29,0,176,177,5,18,0,0,177,35,
        1,0,0,0,178,185,5,13,0,0,179,185,5,14,0,0,180,181,5,19,0,0,181,182,
        3,58,29,0,182,183,5,20,0,0,183,185,1,0,0,0,184,178,1,0,0,0,184,179,
        1,0,0,0,184,180,1,0,0,0,185,37,1,0,0,0,186,187,5,13,0,0,187,189,
        5,28,0,0,188,186,1,0,0,0,188,189,1,0,0,0,189,190,1,0,0,0,190,191,
        3,58,29,0,191,39,1,0,0,0,192,194,3,36,18,0,193,195,3,60,30,0,194,
        193,1,0,0,0,194,195,1,0,0,0,195,41,1,0,0,0,196,198,5,7,0,0,197,196,
        1,0,0,0,198,201,1,0,0,0,199,197,1,0,0,0,199,200,1,0,0,0,200,202,
        1,0,0,0,201,199,1,0,0,0,202,203,3,40,20,0,203,43,1,0,0,0,204,208,
        3,42,21,0,205,206,5,24,0,0,206,208,3,42,21,0,207,204,1,0,0,0,207,
        205,1,0,0,0,208,45,1,0,0,0,209,214,3,44,22,0,210,211,7,1,0,0,211,
        213,3,44,22,0,212,210,1,0,0,0,213,216,1,0,0,0,214,212,1,0,0,0,214,
        215,1,0,0,0,215,47,1,0,0,0,216,214,1,0,0,0,217,222,3,46,23,0,218,
        219,7,2,0,0,219,221,3,46,23,0,220,218,1,0,0,0,221,224,1,0,0,0,222,
        220,1,0,0,0,222,223,1,0,0,0,223,49,1,0,0,0,224,222,1,0,0,0,225,230,
        3,48,24,0,226,227,7,3,0,0,227,229,3,48,24,0,228,226,1,0,0,0,229,
        232,1,0,0,0,230,228,1,0,0,0,230,231,1,0,0,0,231,51,1,0,0,0,232,230,
        1,0,0,0,233,238,3,50,25,0,234,235,7,4,0,0,235,237,3,50,25,0,236,
        234,1,0,0,0,237,240,1,0,0,0,238,236,1,0,0,0,238,239,1,0,0,0,239,
        53,1,0,0,0,240,238,1,0,0,0,241,246,3,52,26,0,242,243,7,5,0,0,243,
        245,3,52,26,0,244,242,1,0,0,0,245,248,1,0,0,0,246,244,1,0,0,0,246,
        247,1,0,0,0,247,55,1,0,0,0,248,246,1,0,0,0,249,254,3,54,27,0,250,
        251,5,8,0,0,251,253,3,54,27,0,252,250,1,0,0,0,253,256,1,0,0,0,254,
        252,1,0,0,0,254,255,1,0,0,0,255,57,1,0,0,0,256,254,1,0,0,0,257,262,
        3,56,28,0,258,259,5,9,0,0,259,261,3,56,28,0,260,258,1,0,0,0,261,
        264,1,0,0,0,262,260,1,0,0,0,262,263,1,0,0,0,263,59,1,0,0,0,264,262,
        1,0,0,0,265,266,5,19,0,0,266,271,3,58,29,0,267,268,5,17,0,0,268,
        270,3,58,29,0,269,267,1,0,0,0,270,273,1,0,0,0,271,269,1,0,0,0,271,
        272,1,0,0,0,272,274,1,0,0,0,273,271,1,0,0,0,274,275,5,20,0,0,275,
        61,1,0,0,0,25,65,76,84,94,105,111,117,128,143,162,168,172,184,188,
        194,199,207,214,222,230,238,246,254,262,271
    ]

class CrawLangParser ( Parser ):

    grammarFileName = "CrawLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'char'", "'int'", "'if'", "'else'", "'for'", 
                     "'return'", "'not'", "'and'", "'or'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "','", "';'", "'('", "')'", 
                     "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'<<'", 
                     "'>>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "SPACE", "COMMENT_BLOCK", 
                      "COMMENT_LINE", "VALID_VARIABLE_NAME", "LITERAL", 
                      "INT", "CHAR", "COMMA", "SEMICOLON", "LPAREN", "RPAREN", 
                      "LCURL", "RCURL", "PLUS", "MINUS", "TIMES", "DIVIDE", 
                      "MOD", "ASSIGN", "EQ", "NEQ", "LTHAN", "GTHAN", "LEQ", 
                      "GEQ", "SHIFT_LEFT", "SHIFT_RIGHT" ]

    RULE_funclist = 0
    RULE_function_def = 1
    RULE_func_header = 2
    RULE_func_name_decl = 3
    RULE_formal_list = 4
    RULE_base_type = 5
    RULE_statement = 6
    RULE_block = 7
    RULE_decl = 8
    RULE_assignment_statement = 9
    RULE_if_stmt = 10
    RULE_else_part = 11
    RULE_for_loop = 12
    RULE_loop_cntrl = 13
    RULE_loop_init = 14
    RULE_loop_cond = 15
    RULE_loop_incr = 16
    RULE_return_statement = 17
    RULE_primary_expr = 18
    RULE_assignment = 19
    RULE_postfix_expr = 20
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

    ruleNames =  [ "funclist", "function_def", "func_header", "func_name_decl", 
                   "formal_list", "base_type", "statement", "block", "decl", 
                   "assignment_statement", "if_stmt", "else_part", "for_loop", 
                   "loop_cntrl", "loop_init", "loop_cond", "loop_incr", 
                   "return_statement", "primary_expr", "assignment", "postfix_expr", 
                   "boolneg_expr", "sign_expr", "mul_expr", "add_expr", 
                   "shift_expr", "rel_expr", "eq_expr", "lmul_expr", "expr", 
                   "arg_list" ]

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
    SPACE=10
    COMMENT_BLOCK=11
    COMMENT_LINE=12
    VALID_VARIABLE_NAME=13
    LITERAL=14
    INT=15
    CHAR=16
    COMMA=17
    SEMICOLON=18
    LPAREN=19
    RPAREN=20
    LCURL=21
    RCURL=22
    PLUS=23
    MINUS=24
    TIMES=25
    DIVIDE=26
    MOD=27
    ASSIGN=28
    EQ=29
    NEQ=30
    LTHAN=31
    GTHAN=32
    LEQ=33
    GEQ=34
    SHIFT_LEFT=35
    SHIFT_RIGHT=36

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

        def EOF(self):
            return self.getToken(CrawLangParser.EOF, 0)

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




    def funclist(self):

        localctx = CrawLangParser.FunclistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_funclist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8198) != 0):
                self.state = 62
                self.function_def()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
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




    def function_def(self):

        localctx = CrawLangParser.Function_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.func_header()
            self.state = 71
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




    def func_header(self):

        localctx = CrawLangParser.Func_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_func_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.func_name_decl()
            self.state = 74
            self.match(CrawLangParser.LPAREN)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1 or _la==2:
                self.state = 75
                self.formal_list()


            self.state = 78
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




    def func_name_decl(self):

        localctx = CrawLangParser.Func_name_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_func_name_decl)
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.match(CrawLangParser.VALID_VARIABLE_NAME)
                pass
            elif token in [1, 2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.base_type()
                self.state = 82
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




    def formal_list(self):

        localctx = CrawLangParser.Formal_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_formal_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.base_type()
            self.state = 87
            self.match(CrawLangParser.VALID_VARIABLE_NAME)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 88
                self.match(CrawLangParser.COMMA)
                self.state = 89
                self.base_type()
                self.state = 90
                self.match(CrawLangParser.VALID_VARIABLE_NAME)
                self.state = 96
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




    def base_type(self):

        localctx = CrawLangParser.Base_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_base_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
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


        def assignment_statement(self):
            return self.getTypedRuleContext(CrawLangParser.Assignment_statementContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(CrawLangParser.If_stmtContext,0)


        def for_loop(self):
            return self.getTypedRuleContext(CrawLangParser.For_loopContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(CrawLangParser.Return_statementContext,0)


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




    def statement(self):

        localctx = CrawLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_statement)
        try:
            self.state = 105
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.block()
                pass
            elif token in [7, 13, 14, 19, 24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.assignment_statement()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 101
                self.if_stmt()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 102
                self.for_loop()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 5)
                self.state = 103
                self.return_statement()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 6)
                self.state = 104
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




    def block(self):

        localctx = CrawLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(CrawLangParser.LCURL)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==2:
                self.state = 108
                self.decl()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 19685608) != 0):
                self.state = 114
                self.statement()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 120
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




    def decl(self):

        localctx = CrawLangParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.base_type()
            self.state = 123
            self.match(CrawLangParser.VALID_VARIABLE_NAME)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 124
                self.match(CrawLangParser.COMMA)
                self.state = 125
                self.match(CrawLangParser.VALID_VARIABLE_NAME)
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 131
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




    def assignment_statement(self):

        localctx = CrawLangParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.assignment()
            self.state = 134
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




    def if_stmt(self):

        localctx = CrawLangParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(CrawLangParser.T__2)
            self.state = 137
            self.match(CrawLangParser.LPAREN)
            self.state = 138
            self.expr()
            self.state = 139
            self.match(CrawLangParser.RPAREN)
            self.state = 140
            self.statement()
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 141
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




    def else_part(self):

        localctx = CrawLangParser.Else_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_else_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(CrawLangParser.T__3)
            self.state = 146
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




    def for_loop(self):

        localctx = CrawLangParser.For_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_for_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(CrawLangParser.T__4)
            self.state = 149
            self.loop_cntrl()
            self.state = 150
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




    def loop_cntrl(self):

        localctx = CrawLangParser.Loop_cntrlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_loop_cntrl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(CrawLangParser.LPAREN)
            self.state = 153
            self.loop_init()
            self.state = 154
            self.loop_cond()
            self.state = 155
            self.loop_incr()
            self.state = 156
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




    def loop_init(self):

        localctx = CrawLangParser.Loop_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_loop_init)
        try:
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.match(CrawLangParser.SEMICOLON)
                pass
            elif token in [7, 13, 14, 19, 24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.assignment()
                self.state = 160
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




    def loop_cond(self):

        localctx = CrawLangParser.Loop_condContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_loop_cond)
        try:
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.match(CrawLangParser.SEMICOLON)
                pass
            elif token in [7, 13, 14, 19, 24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.expr()
                self.state = 166
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




    def loop_incr(self):

        localctx = CrawLangParser.Loop_incrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_loop_incr)
        try:
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [7, 13, 14, 19, 24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
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




    def return_statement(self):

        localctx = CrawLangParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(CrawLangParser.T__5)
            self.state = 175
            self.expr()
            self.state = 176
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




    def primary_expr(self):

        localctx = CrawLangParser.Primary_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_primary_expr)
        try:
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.match(CrawLangParser.VALID_VARIABLE_NAME)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.match(CrawLangParser.LITERAL)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 180
                self.match(CrawLangParser.LPAREN)
                self.state = 181
                self.expr()
                self.state = 182
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




    def assignment(self):

        localctx = CrawLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 186
                self.match(CrawLangParser.VALID_VARIABLE_NAME)
                self.state = 187
                self.match(CrawLangParser.ASSIGN)


            self.state = 190
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




    def postfix_expr(self):

        localctx = CrawLangParser.Postfix_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_postfix_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.primary_expr()
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 193
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




    def boolneg_expr(self):

        localctx = CrawLangParser.Boolneg_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_boolneg_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 196
                self.match(CrawLangParser.T__6)
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 202
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




    def sign_expr(self):

        localctx = CrawLangParser.Sign_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_sign_expr)
        try:
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 13, 14, 19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.boolneg_expr()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.match(CrawLangParser.MINUS)
                self.state = 206
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




    def mul_expr(self):

        localctx = CrawLangParser.Mul_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_mul_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.sign_expr()
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 234881024) != 0):
                self.state = 210
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 234881024) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 211
                self.sign_expr()
                self.state = 216
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




    def add_expr(self):

        localctx = CrawLangParser.Add_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_add_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.mul_expr()
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23 or _la==24:
                self.state = 218
                _la = self._input.LA(1)
                if not(_la==23 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 219
                self.mul_expr()
                self.state = 224
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




    def shift_expr(self):

        localctx = CrawLangParser.Shift_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_shift_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.add_expr()
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35 or _la==36:
                self.state = 226
                _la = self._input.LA(1)
                if not(_la==35 or _la==36):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 227
                self.add_expr()
                self.state = 232
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




    def rel_expr(self):

        localctx = CrawLangParser.Rel_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_rel_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.shift_expr()
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 32212254720) != 0):
                self.state = 234
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32212254720) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 235
                self.shift_expr()
                self.state = 240
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




    def eq_expr(self):

        localctx = CrawLangParser.Eq_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_eq_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.rel_expr()
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29 or _la==30:
                self.state = 242
                _la = self._input.LA(1)
                if not(_la==29 or _la==30):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 243
                self.rel_expr()
                self.state = 248
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




    def lmul_expr(self):

        localctx = CrawLangParser.Lmul_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_lmul_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.eq_expr()
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 250
                self.match(CrawLangParser.T__7)
                self.state = 251
                self.eq_expr()
                self.state = 256
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




    def expr(self):

        localctx = CrawLangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.lmul_expr()
            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 258
                self.match(CrawLangParser.T__8)
                self.state = 259
                self.lmul_expr()
                self.state = 264
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




    def arg_list(self):

        localctx = CrawLangParser.Arg_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_arg_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(CrawLangParser.LPAREN)
            self.state = 266
            self.expr()
            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 267
                self.match(CrawLangParser.COMMA)
                self.state = 268
                self.expr()
                self.state = 273
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 274
            self.match(CrawLangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





