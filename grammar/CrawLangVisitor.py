# Generated from CrawLang.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CrawLangParser import CrawLangParser
else:
    from CrawLangParser import CrawLangParser

# This class defines a complete generic visitor for a parse tree produced by CrawLangParser.

class CrawLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CrawLangParser#funclist.
    def visitFunclist(self, ctx:CrawLangParser.FunclistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#function_def.
    def visitFunction_def(self, ctx:CrawLangParser.Function_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#main_func.
    def visitMain_func(self, ctx:CrawLangParser.Main_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#func_header.
    def visitFunc_header(self, ctx:CrawLangParser.Func_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#func_name_decl.
    def visitFunc_name_decl(self, ctx:CrawLangParser.Func_name_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#formal_list.
    def visitFormal_list(self, ctx:CrawLangParser.Formal_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#base_type.
    def visitBase_type(self, ctx:CrawLangParser.Base_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#statement.
    def visitStatement(self, ctx:CrawLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#block.
    def visitBlock(self, ctx:CrawLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#decl.
    def visitDecl(self, ctx:CrawLangParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#assignment_statement.
    def visitAssignment_statement(self, ctx:CrawLangParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#if_stmt.
    def visitIf_stmt(self, ctx:CrawLangParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#else_part.
    def visitElse_part(self, ctx:CrawLangParser.Else_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#for_loop.
    def visitFor_loop(self, ctx:CrawLangParser.For_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#loop_cntrl.
    def visitLoop_cntrl(self, ctx:CrawLangParser.Loop_cntrlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#loop_init.
    def visitLoop_init(self, ctx:CrawLangParser.Loop_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#loop_cond.
    def visitLoop_cond(self, ctx:CrawLangParser.Loop_condContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#loop_incr.
    def visitLoop_incr(self, ctx:CrawLangParser.Loop_incrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#return_statement.
    def visitReturn_statement(self, ctx:CrawLangParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#primaryVariableName.
    def visitPrimaryVariableName(self, ctx:CrawLangParser.PrimaryVariableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#primaryLiteral.
    def visitPrimaryLiteral(self, ctx:CrawLangParser.PrimaryLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#primaryString.
    def visitPrimaryString(self, ctx:CrawLangParser.PrimaryStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:CrawLangParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#assignment.
    def visitAssignment(self, ctx:CrawLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#boolneg_expr.
    def visitBoolneg_expr(self, ctx:CrawLangParser.Boolneg_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#sign_expr.
    def visitSign_expr(self, ctx:CrawLangParser.Sign_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#mul_expr.
    def visitMul_expr(self, ctx:CrawLangParser.Mul_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#add_expr.
    def visitAdd_expr(self, ctx:CrawLangParser.Add_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#shift_expr.
    def visitShift_expr(self, ctx:CrawLangParser.Shift_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#rel_expr.
    def visitRel_expr(self, ctx:CrawLangParser.Rel_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#eq_expr.
    def visitEq_expr(self, ctx:CrawLangParser.Eq_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#lmul_expr.
    def visitLmul_expr(self, ctx:CrawLangParser.Lmul_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#expr.
    def visitExpr(self, ctx:CrawLangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#arg_list.
    def visitArg_list(self, ctx:CrawLangParser.Arg_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#print.
    def visitPrint(self, ctx:CrawLangParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#obj.
    def visitObj(self, ctx:CrawLangParser.ObjContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#site_func.
    def visitSite_func(self, ctx:CrawLangParser.Site_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#next_func.
    def visitNext_func(self, ctx:CrawLangParser.Next_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#domain_func.
    def visitDomain_func(self, ctx:CrawLangParser.Domain_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#has_subdomain_func.
    def visitHas_subdomain_func(self, ctx:CrawLangParser.Has_subdomain_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#function_call.
    def visitFunction_call(self, ctx:CrawLangParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#litINT.
    def visitLitINT(self, ctx:CrawLangParser.LitINTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#litCHAR.
    def visitLitCHAR(self, ctx:CrawLangParser.LitCHARContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#litFLOAT.
    def visitLitFLOAT(self, ctx:CrawLangParser.LitFLOATContext):
        return self.visitChildren(ctx)



del CrawLangParser