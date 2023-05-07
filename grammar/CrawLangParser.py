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
        4,1,37,286,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,5,0,66,8,0,
        10,0,12,0,69,9,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,3,2,79,8,2,1,2,
        1,2,1,3,1,3,1,3,1,3,3,3,87,8,3,1,4,1,4,1,4,1,4,1,4,1,4,5,4,95,8,
        4,10,4,12,4,98,9,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,109,8,
        6,1,7,1,7,5,7,113,8,7,10,7,12,7,116,9,7,1,7,5,7,119,8,7,10,7,12,
        7,122,9,7,1,7,1,7,1,8,1,8,1,8,1,8,5,8,130,8,8,10,8,12,8,133,9,8,
        1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,147,
        8,10,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,
        1,13,1,14,1,14,1,14,1,14,3,14,166,8,14,1,15,1,15,1,15,1,15,3,15,
        172,8,15,1,16,1,16,3,16,176,8,16,1,17,1,17,1,17,1,17,1,18,1,18,1,
        18,1,18,1,18,1,18,3,18,188,8,18,1,19,1,19,3,19,192,8,19,1,19,1,19,
        1,20,1,20,3,20,198,8,20,1,21,5,21,201,8,21,10,21,12,21,204,9,21,
        1,21,1,21,1,22,1,22,1,22,3,22,211,8,22,1,23,1,23,1,23,5,23,216,8,
        23,10,23,12,23,219,9,23,1,24,1,24,1,24,5,24,224,8,24,10,24,12,24,
        227,9,24,1,25,1,25,1,25,5,25,232,8,25,10,25,12,25,235,9,25,1,26,
        1,26,1,26,5,26,240,8,26,10,26,12,26,243,9,26,1,27,1,27,1,27,5,27,
        248,8,27,10,27,12,27,251,9,27,1,28,1,28,1,28,5,28,256,8,28,10,28,
        12,28,259,9,28,1,29,1,29,1,29,5,29,264,8,29,10,29,12,29,267,9,29,
        1,30,1,30,1,30,1,30,5,30,273,8,30,10,30,12,30,276,9,30,1,30,1,30,
        1,31,1,31,1,31,1,31,1,31,1,31,1,31,0,0,32,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,
        62,0,6,1,0,1,2,1,0,26,28,1,0,24,25,1,0,36,37,1,0,32,35,1,0,30,31,
        284,0,67,1,0,0,0,2,72,1,0,0,0,4,75,1,0,0,0,6,86,1,0,0,0,8,88,1,0,
        0,0,10,99,1,0,0,0,12,108,1,0,0,0,14,110,1,0,0,0,16,125,1,0,0,0,18,
        136,1,0,0,0,20,139,1,0,0,0,22,148,1,0,0,0,24,151,1,0,0,0,26,155,
        1,0,0,0,28,165,1,0,0,0,30,171,1,0,0,0,32,175,1,0,0,0,34,177,1,0,
        0,0,36,187,1,0,0,0,38,191,1,0,0,0,40,195,1,0,0,0,42,202,1,0,0,0,
        44,210,1,0,0,0,46,212,1,0,0,0,48,220,1,0,0,0,50,228,1,0,0,0,52,236,
        1,0,0,0,54,244,1,0,0,0,56,252,1,0,0,0,58,260,1,0,0,0,60,268,1,0,
        0,0,62,279,1,0,0,0,64,66,3,2,1,0,65,64,1,0,0,0,66,69,1,0,0,0,67,
        65,1,0,0,0,67,68,1,0,0,0,68,70,1,0,0,0,69,67,1,0,0,0,70,71,5,0,0,
        1,71,1,1,0,0,0,72,73,3,4,2,0,73,74,3,14,7,0,74,3,1,0,0,0,75,76,3,
        6,3,0,76,78,5,20,0,0,77,79,3,8,4,0,78,77,1,0,0,0,78,79,1,0,0,0,79,
        80,1,0,0,0,80,81,5,21,0,0,81,5,1,0,0,0,82,87,5,14,0,0,83,84,3,10,
        5,0,84,85,5,14,0,0,85,87,1,0,0,0,86,82,1,0,0,0,86,83,1,0,0,0,87,
        7,1,0,0,0,88,89,3,10,5,0,89,96,5,14,0,0,90,91,5,18,0,0,91,92,3,10,
        5,0,92,93,5,14,0,0,93,95,1,0,0,0,94,90,1,0,0,0,95,98,1,0,0,0,96,
        94,1,0,0,0,96,97,1,0,0,0,97,9,1,0,0,0,98,96,1,0,0,0,99,100,7,0,0,
        0,100,11,1,0,0,0,101,109,3,14,7,0,102,109,3,62,31,0,103,109,3,18,
        9,0,104,109,3,20,10,0,105,109,3,24,12,0,106,109,3,34,17,0,107,109,
        5,19,0,0,108,101,1,0,0,0,108,102,1,0,0,0,108,103,1,0,0,0,108,104,
        1,0,0,0,108,105,1,0,0,0,108,106,1,0,0,0,108,107,1,0,0,0,109,13,1,
        0,0,0,110,114,5,22,0,0,111,113,3,16,8,0,112,111,1,0,0,0,113,116,
        1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,115,120,1,0,0,0,116,114,
        1,0,0,0,117,119,3,12,6,0,118,117,1,0,0,0,119,122,1,0,0,0,120,118,
        1,0,0,0,120,121,1,0,0,0,121,123,1,0,0,0,122,120,1,0,0,0,123,124,
        5,23,0,0,124,15,1,0,0,0,125,126,3,10,5,0,126,131,5,14,0,0,127,128,
        5,18,0,0,128,130,5,14,0,0,129,127,1,0,0,0,130,133,1,0,0,0,131,129,
        1,0,0,0,131,132,1,0,0,0,132,134,1,0,0,0,133,131,1,0,0,0,134,135,
        5,19,0,0,135,17,1,0,0,0,136,137,3,38,19,0,137,138,5,19,0,0,138,19,
        1,0,0,0,139,140,5,3,0,0,140,141,5,20,0,0,141,142,3,58,29,0,142,143,
        5,21,0,0,143,146,3,12,6,0,144,147,3,22,11,0,145,147,1,0,0,0,146,
        144,1,0,0,0,146,145,1,0,0,0,147,21,1,0,0,0,148,149,5,4,0,0,149,150,
        3,12,6,0,150,23,1,0,0,0,151,152,5,5,0,0,152,153,3,26,13,0,153,154,
        3,12,6,0,154,25,1,0,0,0,155,156,5,20,0,0,156,157,3,28,14,0,157,158,
        3,30,15,0,158,159,3,32,16,0,159,160,5,21,0,0,160,27,1,0,0,0,161,
        166,5,19,0,0,162,163,3,38,19,0,163,164,5,19,0,0,164,166,1,0,0,0,
        165,161,1,0,0,0,165,162,1,0,0,0,166,29,1,0,0,0,167,172,5,19,0,0,
        168,169,3,58,29,0,169,170,5,19,0,0,170,172,1,0,0,0,171,167,1,0,0,
        0,171,168,1,0,0,0,172,31,1,0,0,0,173,176,1,0,0,0,174,176,3,38,19,
        0,175,173,1,0,0,0,175,174,1,0,0,0,176,33,1,0,0,0,177,178,5,6,0,0,
        178,179,3,58,29,0,179,180,5,19,0,0,180,35,1,0,0,0,181,188,5,14,0,
        0,182,188,5,15,0,0,183,184,5,20,0,0,184,185,3,58,29,0,185,186,5,
        21,0,0,186,188,1,0,0,0,187,181,1,0,0,0,187,182,1,0,0,0,187,183,1,
        0,0,0,188,37,1,0,0,0,189,190,5,14,0,0,190,192,5,29,0,0,191,189,1,
        0,0,0,191,192,1,0,0,0,192,193,1,0,0,0,193,194,3,58,29,0,194,39,1,
        0,0,0,195,197,3,36,18,0,196,198,3,60,30,0,197,196,1,0,0,0,197,198,
        1,0,0,0,198,41,1,0,0,0,199,201,5,7,0,0,200,199,1,0,0,0,201,204,1,
        0,0,0,202,200,1,0,0,0,202,203,1,0,0,0,203,205,1,0,0,0,204,202,1,
        0,0,0,205,206,3,40,20,0,206,43,1,0,0,0,207,211,3,42,21,0,208,209,
        5,25,0,0,209,211,3,42,21,0,210,207,1,0,0,0,210,208,1,0,0,0,211,45,
        1,0,0,0,212,217,3,44,22,0,213,214,7,1,0,0,214,216,3,44,22,0,215,
        213,1,0,0,0,216,219,1,0,0,0,217,215,1,0,0,0,217,218,1,0,0,0,218,
        47,1,0,0,0,219,217,1,0,0,0,220,225,3,46,23,0,221,222,7,2,0,0,222,
        224,3,46,23,0,223,221,1,0,0,0,224,227,1,0,0,0,225,223,1,0,0,0,225,
        226,1,0,0,0,226,49,1,0,0,0,227,225,1,0,0,0,228,233,3,48,24,0,229,
        230,7,3,0,0,230,232,3,48,24,0,231,229,1,0,0,0,232,235,1,0,0,0,233,
        231,1,0,0,0,233,234,1,0,0,0,234,51,1,0,0,0,235,233,1,0,0,0,236,241,
        3,50,25,0,237,238,7,4,0,0,238,240,3,50,25,0,239,237,1,0,0,0,240,
        243,1,0,0,0,241,239,1,0,0,0,241,242,1,0,0,0,242,53,1,0,0,0,243,241,
        1,0,0,0,244,249,3,52,26,0,245,246,7,5,0,0,246,248,3,52,26,0,247,
        245,1,0,0,0,248,251,1,0,0,0,249,247,1,0,0,0,249,250,1,0,0,0,250,
        55,1,0,0,0,251,249,1,0,0,0,252,257,3,54,27,0,253,254,5,8,0,0,254,
        256,3,54,27,0,255,253,1,0,0,0,256,259,1,0,0,0,257,255,1,0,0,0,257,
        258,1,0,0,0,258,57,1,0,0,0,259,257,1,0,0,0,260,265,3,56,28,0,261,
        262,5,9,0,0,262,264,3,56,28,0,263,261,1,0,0,0,264,267,1,0,0,0,265,
        263,1,0,0,0,265,266,1,0,0,0,266,59,1,0,0,0,267,265,1,0,0,0,268,269,
        5,20,0,0,269,274,3,58,29,0,270,271,5,18,0,0,271,273,3,58,29,0,272,
        270,1,0,0,0,273,276,1,0,0,0,274,272,1,0,0,0,274,275,1,0,0,0,275,
        277,1,0,0,0,276,274,1,0,0,0,277,278,5,21,0,0,278,61,1,0,0,0,279,
        280,5,10,0,0,280,281,5,20,0,0,281,282,3,58,29,0,282,283,5,21,0,0,
        283,284,5,19,0,0,284,63,1,0,0,0,25,67,78,86,96,108,114,120,131,146,
        165,171,175,187,191,197,202,210,217,225,233,241,249,257,265,274
    ]

class CrawLangParser ( Parser ):

    grammarFileName = "CrawLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'char'", "'int'", "'if'", "'else'", "'for'", 
                     "'return'", "'not'", "'and'", "'or'", "'print'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "','", "';'", "'('", "')'", 
                     "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'<<'", 
                     "'>>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "SPACE", "COMMENT_BLOCK", 
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
    RULE_print = 31

    ruleNames =  [ "funclist", "function_def", "func_header", "func_name_decl", 
                   "formal_list", "base_type", "statement", "block", "decl", 
                   "assignment_statement", "if_stmt", "else_part", "for_loop", 
                   "loop_cntrl", "loop_init", "loop_cond", "loop_incr", 
                   "return_statement", "primary_expr", "assignment", "postfix_expr", 
                   "boolneg_expr", "sign_expr", "mul_expr", "add_expr", 
                   "shift_expr", "rel_expr", "eq_expr", "lmul_expr", "expr", 
                   "arg_list", "print" ]

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
    SPACE=11
    COMMENT_BLOCK=12
    COMMENT_LINE=13
    VALID_VARIABLE_NAME=14
    LITERAL=15
    INT=16
    CHAR=17
    COMMA=18
    SEMICOLON=19
    LPAREN=20
    RPAREN=21
    LCURL=22
    RCURL=23
    PLUS=24
    MINUS=25
    TIMES=26
    DIVIDE=27
    MOD=28
    ASSIGN=29
    EQ=30
    NEQ=31
    LTHAN=32
    GTHAN=33
    LEQ=34
    GEQ=35
    SHIFT_LEFT=36
    SHIFT_RIGHT=37

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunclist" ):
                return visitor.visitFunclist(self)
            else:
                return visitor.visitChildren(self)




    def funclist(self):

        localctx = CrawLangParser.FunclistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_funclist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16390) != 0):
                self.state = 64
                self.function_def()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
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
            self.state = 72
            self.func_header()
            self.state = 73
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
        self.enterRule(localctx, 4, self.RULE_func_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.func_name_decl()
            self.state = 76
            self.match(CrawLangParser.LPAREN)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1 or _la==2:
                self.state = 77
                self.formal_list()


            self.state = 80
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
        self.enterRule(localctx, 6, self.RULE_func_name_decl)
        try:
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.match(CrawLangParser.VALID_VARIABLE_NAME)
                pass
            elif token in [1, 2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.base_type()
                self.state = 84
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
        self.enterRule(localctx, 8, self.RULE_formal_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.base_type()
            self.state = 89
            self.match(CrawLangParser.VALID_VARIABLE_NAME)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 90
                self.match(CrawLangParser.COMMA)
                self.state = 91
                self.base_type()
                self.state = 92
                self.match(CrawLangParser.VALID_VARIABLE_NAME)
                self.state = 98
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
        self.enterRule(localctx, 10, self.RULE_base_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
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
        self.enterRule(localctx, 12, self.RULE_statement)
        try:
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.block()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.print_()
                pass
            elif token in [7, 14, 15, 20, 25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 103
                self.assignment_statement()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 104
                self.if_stmt()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 105
                self.for_loop()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 6)
                self.state = 106
                self.return_statement()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 7)
                self.state = 107
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = CrawLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(CrawLangParser.LCURL)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==2:
                self.state = 111
                self.decl()
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 39372008) != 0):
                self.state = 117
                self.statement()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 123
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
        self.enterRule(localctx, 16, self.RULE_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.base_type()
            self.state = 126
            self.match(CrawLangParser.VALID_VARIABLE_NAME)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 127
                self.match(CrawLangParser.COMMA)
                self.state = 128
                self.match(CrawLangParser.VALID_VARIABLE_NAME)
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 134
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
        self.enterRule(localctx, 18, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.assignment()
            self.state = 137
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
        self.enterRule(localctx, 20, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(CrawLangParser.T__2)
            self.state = 140
            self.match(CrawLangParser.LPAREN)
            self.state = 141
            self.expr()
            self.state = 142
            self.match(CrawLangParser.RPAREN)
            self.state = 143
            self.statement()
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 144
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
        self.enterRule(localctx, 22, self.RULE_else_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(CrawLangParser.T__3)
            self.state = 149
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
        self.enterRule(localctx, 24, self.RULE_for_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(CrawLangParser.T__4)
            self.state = 152
            self.loop_cntrl()
            self.state = 153
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
        self.enterRule(localctx, 26, self.RULE_loop_cntrl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(CrawLangParser.LPAREN)
            self.state = 156
            self.loop_init()
            self.state = 157
            self.loop_cond()
            self.state = 158
            self.loop_incr()
            self.state = 159
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
        self.enterRule(localctx, 28, self.RULE_loop_init)
        try:
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.match(CrawLangParser.SEMICOLON)
                pass
            elif token in [7, 14, 15, 20, 25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.assignment()
                self.state = 163
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
        self.enterRule(localctx, 30, self.RULE_loop_cond)
        try:
            self.state = 171
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.match(CrawLangParser.SEMICOLON)
                pass
            elif token in [7, 14, 15, 20, 25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.expr()
                self.state = 169
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
        self.enterRule(localctx, 32, self.RULE_loop_incr)
        try:
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [7, 14, 15, 20, 25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
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
        self.enterRule(localctx, 34, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(CrawLangParser.T__5)
            self.state = 178
            self.expr()
            self.state = 179
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
        self.enterRule(localctx, 36, self.RULE_primary_expr)
        try:
            self.state = 187
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.match(CrawLangParser.VALID_VARIABLE_NAME)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.match(CrawLangParser.LITERAL)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 183
                self.match(CrawLangParser.LPAREN)
                self.state = 184
                self.expr()
                self.state = 185
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
        self.enterRule(localctx, 38, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 189
                localctx.variable_name = self.match(CrawLangParser.VALID_VARIABLE_NAME)
                self.state = 190
                self.match(CrawLangParser.ASSIGN)


            self.state = 193
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
        self.enterRule(localctx, 40, self.RULE_postfix_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.primary_expr()
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 196
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
        self.enterRule(localctx, 42, self.RULE_boolneg_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 199
                self.match(CrawLangParser.T__6)
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 205
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
        self.enterRule(localctx, 44, self.RULE_sign_expr)
        try:
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 14, 15, 20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.boolneg_expr()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.match(CrawLangParser.MINUS)
                self.state = 209
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
            self.state = 212
            self.sign_expr()
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0):
                self.state = 213
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 214
                self.sign_expr()
                self.state = 219
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
            self.state = 220
            self.mul_expr()
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24 or _la==25:
                self.state = 221
                _la = self._input.LA(1)
                if not(_la==24 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 222
                self.mul_expr()
                self.state = 227
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
            self.state = 228
            self.add_expr()
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36 or _la==37:
                self.state = 229
                _la = self._input.LA(1)
                if not(_la==36 or _la==37):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 230
                self.add_expr()
                self.state = 235
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
            self.state = 236
            self.shift_expr()
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 64424509440) != 0):
                self.state = 237
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 64424509440) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 238
                self.shift_expr()
                self.state = 243
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
            self.state = 244
            self.rel_expr()
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30 or _la==31:
                self.state = 245
                _la = self._input.LA(1)
                if not(_la==30 or _la==31):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 246
                self.rel_expr()
                self.state = 251
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
            self.state = 252
            self.eq_expr()
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 253
                self.match(CrawLangParser.T__7)
                self.state = 254
                self.eq_expr()
                self.state = 259
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
        self.enterRule(localctx, 58, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.lmul_expr()
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 261
                self.match(CrawLangParser.T__8)
                self.state = 262
                self.lmul_expr()
                self.state = 267
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
        self.enterRule(localctx, 60, self.RULE_arg_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(CrawLangParser.LPAREN)
            self.state = 269
            self.expr()
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 270
                self.match(CrawLangParser.COMMA)
                self.state = 271
                self.expr()
                self.state = 276
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 277
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
        self.enterRule(localctx, 62, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(CrawLangParser.T__9)
            self.state = 280
            self.match(CrawLangParser.LPAREN)
            self.state = 281
            self.expr()
            self.state = 282
            self.match(CrawLangParser.RPAREN)
            self.state = 283
            self.match(CrawLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





