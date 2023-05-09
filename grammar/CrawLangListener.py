# Generated from CrawLang.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CrawLangParser import CrawLangParser
else:
    from CrawLangParser import CrawLangParser

# This class defines a complete listener for a parse tree produced by CrawLangParser.
class CrawLangListener(ParseTreeListener):

    # Enter a parse tree produced by CrawLangParser#funclist.
    def enterFunclist(self, ctx:CrawLangParser.FunclistContext):
        pass

    # Exit a parse tree produced by CrawLangParser#funclist.
    def exitFunclist(self, ctx:CrawLangParser.FunclistContext):
        pass


    # Enter a parse tree produced by CrawLangParser#function_def.
    def enterFunction_def(self, ctx:CrawLangParser.Function_defContext):
        pass

    # Exit a parse tree produced by CrawLangParser#function_def.
    def exitFunction_def(self, ctx:CrawLangParser.Function_defContext):
        pass


    # Enter a parse tree produced by CrawLangParser#main_func.
    def enterMain_func(self, ctx:CrawLangParser.Main_funcContext):
        pass

    # Exit a parse tree produced by CrawLangParser#main_func.
    def exitMain_func(self, ctx:CrawLangParser.Main_funcContext):
        pass


    # Enter a parse tree produced by CrawLangParser#func_header.
    def enterFunc_header(self, ctx:CrawLangParser.Func_headerContext):
        pass

    # Exit a parse tree produced by CrawLangParser#func_header.
    def exitFunc_header(self, ctx:CrawLangParser.Func_headerContext):
        pass


    # Enter a parse tree produced by CrawLangParser#func_name_decl.
    def enterFunc_name_decl(self, ctx:CrawLangParser.Func_name_declContext):
        pass

    # Exit a parse tree produced by CrawLangParser#func_name_decl.
    def exitFunc_name_decl(self, ctx:CrawLangParser.Func_name_declContext):
        pass


    # Enter a parse tree produced by CrawLangParser#formal_list.
    def enterFormal_list(self, ctx:CrawLangParser.Formal_listContext):
        pass

    # Exit a parse tree produced by CrawLangParser#formal_list.
    def exitFormal_list(self, ctx:CrawLangParser.Formal_listContext):
        pass


    # Enter a parse tree produced by CrawLangParser#base_type.
    def enterBase_type(self, ctx:CrawLangParser.Base_typeContext):
        pass

    # Exit a parse tree produced by CrawLangParser#base_type.
    def exitBase_type(self, ctx:CrawLangParser.Base_typeContext):
        pass


    # Enter a parse tree produced by CrawLangParser#statement.
    def enterStatement(self, ctx:CrawLangParser.StatementContext):
        pass

    # Exit a parse tree produced by CrawLangParser#statement.
    def exitStatement(self, ctx:CrawLangParser.StatementContext):
        pass


    # Enter a parse tree produced by CrawLangParser#block.
    def enterBlock(self, ctx:CrawLangParser.BlockContext):
        pass

    # Exit a parse tree produced by CrawLangParser#block.
    def exitBlock(self, ctx:CrawLangParser.BlockContext):
        pass


    # Enter a parse tree produced by CrawLangParser#decl.
    def enterDecl(self, ctx:CrawLangParser.DeclContext):
        pass

    # Exit a parse tree produced by CrawLangParser#decl.
    def exitDecl(self, ctx:CrawLangParser.DeclContext):
        pass


    # Enter a parse tree produced by CrawLangParser#assignment_statement.
    def enterAssignment_statement(self, ctx:CrawLangParser.Assignment_statementContext):
        pass

    # Exit a parse tree produced by CrawLangParser#assignment_statement.
    def exitAssignment_statement(self, ctx:CrawLangParser.Assignment_statementContext):
        pass


    # Enter a parse tree produced by CrawLangParser#if_stmt.
    def enterIf_stmt(self, ctx:CrawLangParser.If_stmtContext):
        pass

    # Exit a parse tree produced by CrawLangParser#if_stmt.
    def exitIf_stmt(self, ctx:CrawLangParser.If_stmtContext):
        pass


    # Enter a parse tree produced by CrawLangParser#else_part.
    def enterElse_part(self, ctx:CrawLangParser.Else_partContext):
        pass

    # Exit a parse tree produced by CrawLangParser#else_part.
    def exitElse_part(self, ctx:CrawLangParser.Else_partContext):
        pass


    # Enter a parse tree produced by CrawLangParser#for_loop.
    def enterFor_loop(self, ctx:CrawLangParser.For_loopContext):
        pass

    # Exit a parse tree produced by CrawLangParser#for_loop.
    def exitFor_loop(self, ctx:CrawLangParser.For_loopContext):
        pass


    # Enter a parse tree produced by CrawLangParser#loop_cntrl.
    def enterLoop_cntrl(self, ctx:CrawLangParser.Loop_cntrlContext):
        pass

    # Exit a parse tree produced by CrawLangParser#loop_cntrl.
    def exitLoop_cntrl(self, ctx:CrawLangParser.Loop_cntrlContext):
        pass


    # Enter a parse tree produced by CrawLangParser#loop_init.
    def enterLoop_init(self, ctx:CrawLangParser.Loop_initContext):
        pass

    # Exit a parse tree produced by CrawLangParser#loop_init.
    def exitLoop_init(self, ctx:CrawLangParser.Loop_initContext):
        pass


    # Enter a parse tree produced by CrawLangParser#loop_cond.
    def enterLoop_cond(self, ctx:CrawLangParser.Loop_condContext):
        pass

    # Exit a parse tree produced by CrawLangParser#loop_cond.
    def exitLoop_cond(self, ctx:CrawLangParser.Loop_condContext):
        pass


    # Enter a parse tree produced by CrawLangParser#loop_incr.
    def enterLoop_incr(self, ctx:CrawLangParser.Loop_incrContext):
        pass

    # Exit a parse tree produced by CrawLangParser#loop_incr.
    def exitLoop_incr(self, ctx:CrawLangParser.Loop_incrContext):
        pass


    # Enter a parse tree produced by CrawLangParser#return_statement.
    def enterReturn_statement(self, ctx:CrawLangParser.Return_statementContext):
        pass

    # Exit a parse tree produced by CrawLangParser#return_statement.
    def exitReturn_statement(self, ctx:CrawLangParser.Return_statementContext):
        pass


    # Enter a parse tree produced by CrawLangParser#primaryVariableName.
    def enterPrimaryVariableName(self, ctx:CrawLangParser.PrimaryVariableNameContext):
        pass

    # Exit a parse tree produced by CrawLangParser#primaryVariableName.
    def exitPrimaryVariableName(self, ctx:CrawLangParser.PrimaryVariableNameContext):
        pass


    # Enter a parse tree produced by CrawLangParser#primaryLiteral.
    def enterPrimaryLiteral(self, ctx:CrawLangParser.PrimaryLiteralContext):
        pass

    # Exit a parse tree produced by CrawLangParser#primaryLiteral.
    def exitPrimaryLiteral(self, ctx:CrawLangParser.PrimaryLiteralContext):
        pass


    # Enter a parse tree produced by CrawLangParser#primaryString.
    def enterPrimaryString(self, ctx:CrawLangParser.PrimaryStringContext):
        pass

    # Exit a parse tree produced by CrawLangParser#primaryString.
    def exitPrimaryString(self, ctx:CrawLangParser.PrimaryStringContext):
        pass


    # Enter a parse tree produced by CrawLangParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:CrawLangParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by CrawLangParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:CrawLangParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by CrawLangParser#assignment.
    def enterAssignment(self, ctx:CrawLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by CrawLangParser#assignment.
    def exitAssignment(self, ctx:CrawLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by CrawLangParser#boolneg_expr.
    def enterBoolneg_expr(self, ctx:CrawLangParser.Boolneg_exprContext):
        pass

    # Exit a parse tree produced by CrawLangParser#boolneg_expr.
    def exitBoolneg_expr(self, ctx:CrawLangParser.Boolneg_exprContext):
        pass


    # Enter a parse tree produced by CrawLangParser#sign_expr.
    def enterSign_expr(self, ctx:CrawLangParser.Sign_exprContext):
        pass

    # Exit a parse tree produced by CrawLangParser#sign_expr.
    def exitSign_expr(self, ctx:CrawLangParser.Sign_exprContext):
        pass


    # Enter a parse tree produced by CrawLangParser#mul_expr.
    def enterMul_expr(self, ctx:CrawLangParser.Mul_exprContext):
        pass

    # Exit a parse tree produced by CrawLangParser#mul_expr.
    def exitMul_expr(self, ctx:CrawLangParser.Mul_exprContext):
        pass


    # Enter a parse tree produced by CrawLangParser#add_expr.
    def enterAdd_expr(self, ctx:CrawLangParser.Add_exprContext):
        pass

    # Exit a parse tree produced by CrawLangParser#add_expr.
    def exitAdd_expr(self, ctx:CrawLangParser.Add_exprContext):
        pass


    # Enter a parse tree produced by CrawLangParser#shift_expr.
    def enterShift_expr(self, ctx:CrawLangParser.Shift_exprContext):
        pass

    # Exit a parse tree produced by CrawLangParser#shift_expr.
    def exitShift_expr(self, ctx:CrawLangParser.Shift_exprContext):
        pass


    # Enter a parse tree produced by CrawLangParser#rel_expr.
    def enterRel_expr(self, ctx:CrawLangParser.Rel_exprContext):
        pass

    # Exit a parse tree produced by CrawLangParser#rel_expr.
    def exitRel_expr(self, ctx:CrawLangParser.Rel_exprContext):
        pass


    # Enter a parse tree produced by CrawLangParser#eq_expr.
    def enterEq_expr(self, ctx:CrawLangParser.Eq_exprContext):
        pass

    # Exit a parse tree produced by CrawLangParser#eq_expr.
    def exitEq_expr(self, ctx:CrawLangParser.Eq_exprContext):
        pass


    # Enter a parse tree produced by CrawLangParser#lmul_expr.
    def enterLmul_expr(self, ctx:CrawLangParser.Lmul_exprContext):
        pass

    # Exit a parse tree produced by CrawLangParser#lmul_expr.
    def exitLmul_expr(self, ctx:CrawLangParser.Lmul_exprContext):
        pass


    # Enter a parse tree produced by CrawLangParser#expr.
    def enterExpr(self, ctx:CrawLangParser.ExprContext):
        pass

    # Exit a parse tree produced by CrawLangParser#expr.
    def exitExpr(self, ctx:CrawLangParser.ExprContext):
        pass


    # Enter a parse tree produced by CrawLangParser#arg_list.
    def enterArg_list(self, ctx:CrawLangParser.Arg_listContext):
        pass

    # Exit a parse tree produced by CrawLangParser#arg_list.
    def exitArg_list(self, ctx:CrawLangParser.Arg_listContext):
        pass


    # Enter a parse tree produced by CrawLangParser#print.
    def enterPrint(self, ctx:CrawLangParser.PrintContext):
        pass

    # Exit a parse tree produced by CrawLangParser#print.
    def exitPrint(self, ctx:CrawLangParser.PrintContext):
        pass


    # Enter a parse tree produced by CrawLangParser#obj.
    def enterObj(self, ctx:CrawLangParser.ObjContext):
        pass

    # Exit a parse tree produced by CrawLangParser#obj.
    def exitObj(self, ctx:CrawLangParser.ObjContext):
        pass


    # Enter a parse tree produced by CrawLangParser#site_func.
    def enterSite_func(self, ctx:CrawLangParser.Site_funcContext):
        pass

    # Exit a parse tree produced by CrawLangParser#site_func.
    def exitSite_func(self, ctx:CrawLangParser.Site_funcContext):
        pass


    # Enter a parse tree produced by CrawLangParser#next_func.
    def enterNext_func(self, ctx:CrawLangParser.Next_funcContext):
        pass

    # Exit a parse tree produced by CrawLangParser#next_func.
    def exitNext_func(self, ctx:CrawLangParser.Next_funcContext):
        pass


    # Enter a parse tree produced by CrawLangParser#domain_func.
    def enterDomain_func(self, ctx:CrawLangParser.Domain_funcContext):
        pass

    # Exit a parse tree produced by CrawLangParser#domain_func.
    def exitDomain_func(self, ctx:CrawLangParser.Domain_funcContext):
        pass


    # Enter a parse tree produced by CrawLangParser#has_subdomain_func.
    def enterHas_subdomain_func(self, ctx:CrawLangParser.Has_subdomain_funcContext):
        pass

    # Exit a parse tree produced by CrawLangParser#has_subdomain_func.
    def exitHas_subdomain_func(self, ctx:CrawLangParser.Has_subdomain_funcContext):
        pass


    # Enter a parse tree produced by CrawLangParser#function_call.
    def enterFunction_call(self, ctx:CrawLangParser.Function_callContext):
        pass

    # Exit a parse tree produced by CrawLangParser#function_call.
    def exitFunction_call(self, ctx:CrawLangParser.Function_callContext):
        pass


    # Enter a parse tree produced by CrawLangParser#litINT.
    def enterLitINT(self, ctx:CrawLangParser.LitINTContext):
        pass

    # Exit a parse tree produced by CrawLangParser#litINT.
    def exitLitINT(self, ctx:CrawLangParser.LitINTContext):
        pass


    # Enter a parse tree produced by CrawLangParser#litCHAR.
    def enterLitCHAR(self, ctx:CrawLangParser.LitCHARContext):
        pass

    # Exit a parse tree produced by CrawLangParser#litCHAR.
    def exitLitCHAR(self, ctx:CrawLangParser.LitCHARContext):
        pass


    # Enter a parse tree produced by CrawLangParser#litFLOAT.
    def enterLitFLOAT(self, ctx:CrawLangParser.LitFLOATContext):
        pass

    # Exit a parse tree produced by CrawLangParser#litFLOAT.
    def exitLitFLOAT(self, ctx:CrawLangParser.LitFLOATContext):
        pass



del CrawLangParser