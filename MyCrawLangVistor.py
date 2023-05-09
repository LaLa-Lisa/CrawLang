from SuperCode import _next, site, has_subdomain, domain, print_all_stats
from grammar.CrawLangParser import CrawLangParser
from grammar.CrawLangVisitor import CrawLangVisitor


class LangMemory:
    base_types = ['int', 'char', 'float', 'str']

    global_variables = dict()
    function_scope = list()
    defined_functions = dict()

    # вернёт переменную если она есть None в противном случае
    @classmethod
    def check_variable(cls, variable_name: str):
        if len(cls.function_scope):
            for for_s in reversed(cls.function_scope[-1]['for']):
                if for_s.get(variable_name) is not None:
                    return for_s[variable_name]
            if cls.function_scope[-1]['variables'].get(variable_name) is not None:
                return cls.function_scope[-1]['variables'][variable_name]
        if cls.global_variables.get(variable_name) is not None:
            return cls.global_variables[variable_name]
        return None

    @classmethod
    def assign_variable(cls, variable_name: str, value):
        if len(cls.function_scope):
            for for_s in reversed(cls.function_scope[-1]['for']):
                if for_s.get(variable_name) is not None:
                    for_s[variable_name] = value
                    return

            if cls.function_scope[-1]['variables'].get(variable_name) is not None \
                    or not len(cls.function_scope[-1]['for']):
                cls.function_scope[-1]['variables'][variable_name] = value
            else:
                cls.function_scope[-1]['for'][-1][variable_name] = value
        else:
            cls.global_variables[variable_name] = value

    @classmethod
    def add_function(cls, fun_name, block, arg_list):
        assert cls.defined_functions.get(fun_name) is None
        cls.defined_functions[fun_name] = {'block': block, 'arg_list': arg_list}

    @classmethod
    def call_function(cls, fun_name):
        assert cls.defined_functions.get(fun_name) is not None
        return cls.defined_functions[fun_name]['block']

    @classmethod
    def get_function_arg_list(cls, fun_name):
        assert cls.defined_functions.get(fun_name) is not None
        return cls.defined_functions[fun_name]['arg_list']

    @classmethod
    def open_function_scope(cls, scope):
        cls.function_scope.append({'variables': scope, 'for': []})

    @classmethod
    def close_function_scope(cls):
        cls.function_scope.pop()

    @classmethod
    def open_for_scope(cls, scope):
        cls.function_scope[-1]['for'].append(scope)

    @classmethod
    def close_for_scope(cls):
        cls.function_scope[-1]['for'].pop()

class MyCrawLangVisitor(CrawLangVisitor):
    # Visit a parse tree produced by CrawLangParser#funclist.
    def visitFunclist(self, ctx: CrawLangParser.FunclistContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CrawLangParser#function_def.
    def visitFunction_def(self, ctx: CrawLangParser.Function_defContext):
        child_gen = ctx.getChildren()
        fun_name, arg_list = self.visit(next(child_gen))
        block = next(child_gen)
        LangMemory.add_function(fun_name, block, arg_list)
        return None

    # Visit a parse tree produced by CrawLangParser#func_header.
    def visitFunc_header(self, ctx: CrawLangParser.Func_headerContext):
        child_gen = ctx.getChildren()
        func_name = self.visit(next(child_gen))
        lparen_keyword = next(child_gen).getText()
        assert lparen_keyword == '('
        arg_list = None
        arg_child = next(child_gen)
        if arg_child.getText() != ')':
            arg_list = self.visit(arg_child)
        return func_name, arg_list

    # Visit a parse tree produced by CrawLangParser#func_name_decl.
    def visitFunc_name_decl(self, ctx: CrawLangParser.Func_name_declContext):
        child_gen = ctx.getChildren()
        name = next(child_gen).getText()
        if name in LangMemory.base_types:
            name = next(child_gen).getText()
        return name

    # Visit a parse tree produced by CrawLangParser#function_call.
    def visitFunction_call(self, ctx: CrawLangParser.Function_callContext):
        child_gen = ctx.getChildren()
        name = next(child_gen).getText()

        lparen_keyword = next(child_gen).getText()
        assert lparen_keyword == '('

        # область видимости открывается
        new_scope = dict()
        LangMemory.open_function_scope(new_scope)
        new_scope['return'] = None  # добавил переменную для ретурна

        # переменные из списка аргументов добавляются в область видимости
        args_child = next(child_gen)
        args_values = None
        if args_child.getText() != ')':
            args_values = self.visit(args_child)
            args_names = LangMemory.get_function_arg_list(name)
            assert len(args_values) == len(args_names)
            for v_name, v_value in zip(args_names, args_values):
                LangMemory.assign_variable(v_name, v_value)

        # вызов функции
        fun_block = LangMemory.call_function(name)
        self.visit(fun_block)
        # область видимости закрывается
        return_val = LangMemory.check_variable('return')
        LangMemory.close_function_scope()
        return return_val

    # Visit a parse tree produced by CrawLangParser#formal_list.
    def visitFormal_list(self, ctx: CrawLangParser.Formal_listContext):
        arg_list = []
        for child in ctx.getChildren():
            value = child.getText()
            if value != ',' and value not in LangMemory.base_types:
                arg_list.append(value)
        return arg_list

    # Visit a parse tree produced by CrawLangParser#base_type.
    def visitBase_type(self, ctx: CrawLangParser.Base_typeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CrawLangParser#statement.
    def visitStatement(self, ctx: CrawLangParser.StatementContext):
        return self.visit(next(ctx.getChildren()))

    # Visit a parse tree produced by CrawLangParser#block.
    def visitBlock(self, ctx: CrawLangParser.BlockContext):
        for child in ctx.getChildren():
            self.visit(child)
            text = child.getText()
            if len(text) > 6 and text[0:6] == 'return':
                return
        return

    # Visit a parse tree produced by CrawLangParser#decl.
    def visitDecl(self, ctx: CrawLangParser.DeclContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CrawLangParser#assignment_statement.
    def visitAssignment_statement(self, ctx: CrawLangParser.Assignment_statementContext):
        return self.visit(next(ctx.getChildren()))

    # Visit a parse tree produced by CrawLangParser#if_stmt.
    def visitIf_stmt(self, ctx: CrawLangParser.If_stmtContext):
        l = ctx.getChildren()
        if_clause = next(l)
        if_clause = next(l)
        if_clause = next(l)
        expr_ = next(l)
        expr_ = next(l)
        if self.visitChildren(if_clause):
            return self.visit(expr_)

        try:
            else_clause = next(l)
            return self.visit(else_clause)
        except:
            return

    # Visit a parse tree produced by CrawLangParser#else_part.
    def visitElse_part(self, ctx: CrawLangParser.Else_partContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CrawLangParser#for_loop.
    def visitFor_loop(self, ctx: CrawLangParser.For_loopContext):
        child_gen = ctx.getChildren()
        for_keyword = next(child_gen).getText()
        assert for_keyword == 'for'
        loop_cntrl = next(child_gen)
        loop_statement = next(child_gen)
        # открываем область видимости фора
        new_scope = dict()
        new_scope['initialization'] = True
        LangMemory.open_for_scope(new_scope)
        # имитация цикла
        while self.visit(loop_cntrl):
            self.visit(loop_statement)

        # закрываем область видимости фора
        LangMemory.close_for_scope()
        # из цикла ничего не возвращаем
        return None

    # Visit a parse tree produced by CrawLangParser#loop_cntrl.
    def visitLoop_cntrl(self, ctx: CrawLangParser.Loop_cntrlContext):
        child_gen = ctx.getChildren()
        lparen_keyword = next(child_gen).getText()
        assert lparen_keyword == '('

        loop_init = next(child_gen)
        loop_cond = next(child_gen)
        loop_incr = next(child_gen)

        rparen_keyword = next(child_gen).getText()
        assert rparen_keyword == ')'

        if LangMemory.check_variable('initialization'):
            self.visit(loop_init)
            LangMemory.assign_variable('initialization', False)
        else:
            self.visit(loop_incr)

        # нужно вернуть нужна ли остановка
        return self.visit(loop_cond)

    # Visit a parse tree produced by CrawLangParser#loop_init.
    def visitLoop_init(self, ctx: CrawLangParser.Loop_initContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CrawLangParser#loop_cond.
    def visitLoop_cond(self, ctx: CrawLangParser.Loop_condContext):
        child_gen = next(ctx.getChildren())
        if child_gen.getText() == ';':
            return True
        return self.visit(child_gen)

    # Visit a parse tree produced by CrawLangParser#loop_incr.
    def visitLoop_incr(self, ctx: CrawLangParser.Loop_incrContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CrawLangParser#return_statement.
    def visitReturn_statement(self, ctx: CrawLangParser.Return_statementContext):
        child_gen = ctx.getChildren()
        return_str = next(child_gen).getText()
        assert return_str == 'return'
        return_val = self.visit(next(child_gen))
        LangMemory.assign_variable('return', return_val)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CrawLangParser#primaryVariableName.
    def visitPrimaryVariableName(self, ctx:CrawLangParser.PrimaryVariableNameContext):
        name = ctx.getText()
        value = LangMemory.check_variable(name)
        #print(LangMemory.function_scope)
        assert value is not None, "invalid variable name " + name
        return value


    # Visit a parse tree produced by CrawLangParser#primaryLiteral.
    def visitPrimaryLiteral(self, ctx:CrawLangParser.PrimaryLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#primaryString.
    def visitPrimaryString(self, ctx:CrawLangParser.PrimaryStringContext):
        value = ctx.getText()[1:-1]
        return value


    # Visit a parse tree produced by CrawLangParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:CrawLangParser.PrimaryExpressionContext):
        child_gen = ctx.getChildren()
        lparen_keyword = next(child_gen).getText()
        assert lparen_keyword == '('

        value = self.visit(next(child_gen))

        rparen_keyword = next(child_gen).getText()
        assert rparen_keyword == ')'
        return value

    # Visit a parse tree produced by CrawLangParser#litINT.
    def visitLitINT(self, ctx: CrawLangParser.LitINTContext):
        return int(ctx.getText())

    # Visit a parse tree produced by CrawLangParser#litCHAR.
    def visitLitCHAR(self, ctx: CrawLangParser.LitCHARContext):
        return str(ctx.getText())

    # Visit a parse tree produced by CrawLangParser#litFLOAT.
    def visitLitFLOAT(self, ctx: CrawLangParser.LitFLOATContext):
        return float(ctx.getText())

    # Visit a parse tree produced by CrawLangParser#assignment.
    def visitAssignment(self, ctx: CrawLangParser.AssignmentContext):
        new_value = 0
        do_assignment = False
        save_name = 'no_name'
        for child in ctx.getChildren():
            value = self.visit(child)
            if child.getText() == '=':
                do_assignment = True
            else:
                if do_assignment:
                    LangMemory.assign_variable(save_name, value)
                new_value = value
                save_name = child.getText()
        return new_value

    # Visit a parse tree produced by CrawLangParser#boolneg_expr.
    def visitBoolneg_expr(self, ctx: CrawLangParser.Boolneg_exprContext):
        check = self.visit(next(ctx.getChildren()))
        if not isinstance(check, str | int | float):
            return check
        text = ctx.getText()
        res = self.visitChildren(ctx)
        if isinstance(res, str):
            return res
        if len(text) > 3 and text[0:3] == 'not':
            return not res
        return res

    # Visit a parse tree produced by CrawLangParser#sign_expr.
    def visitSign_expr(self, ctx: CrawLangParser.Sign_exprContext):
        child_gen = ctx.getChildren()
        sign = next(child_gen)
        text = sign.getText()
        if text == '-':
            return -1 * self.visit(next(child_gen))
        return self.visit(sign)

    # Visit a parse tree produced by CrawLangParser#mul_expr.
    def visitMul_expr(self, ctx: CrawLangParser.Mul_exprContext):
        check = self.visit(next(ctx.getChildren()))
        if not isinstance(check, str | int | float):
            return check

        mult = 1
        is_mult = True

        for child in ctx.getChildren():
            value = self.visit(child)
            if isinstance(value, str):
                return value
            if child.getText() == '*':
                is_mult = True
            elif child.getText() == '/':
                is_mult = False
            else:
                if is_mult:
                    mult *= value
                else:
                    mult /= value
        return mult

    # Visit a parse tree produced by CrawLangParser#add_expr.
    def visitAdd_expr(self, ctx: CrawLangParser.Add_exprContext):
        check = self.visit(next(ctx.getChildren()))
        if not isinstance(check, str | int | float):
            return check

        if isinstance(check, str):
            new_str = ""
            for child in ctx.getChildren():
                value = self.visit(child)
                if child.getText() != '+':
                    assert child.getText() != '-', 'string subtraction'
                    new_str += value
            return new_str

        add = 0
        is_add = True
        for child in ctx.getChildren():
            value = self.visit(child)
            if child.getText() == '+':
                is_add = True
            elif child.getText() == '-':
                is_add = False
            else:
                if is_add:
                    add += value
                else:
                    add -= value
        return add

    # Visit a parse tree produced by CrawLangParser#shift_expr.
    def visitShift_expr(self, ctx: CrawLangParser.Shift_exprContext):
        first_value = self.visit(next(ctx.getChildren()))
        if isinstance(first_value, str):
            assert ctx.getChildCount() == 1
            return first_value
        shift = 0
        not_shifted = True
        shift_left = True
        for child in ctx.getChildren():
            value = self.visit(child)
            if child.getText() == '>>':
                shift_left = True
            elif child.getText() == '<<':
                shift_left = False
            else:
                if not_shifted:
                    not_shifted = False
                    shift = value
                elif shift_left:
                    shift >>= value
                else:
                    shift <<= value
        return shift

    # Visit a parse tree produced by CrawLangParser#rel_expr.
    def visitRel_expr(self, ctx: CrawLangParser.Rel_exprContext):
        child_gen = ctx.getChildren()

        first_value = self.visit(next(child_gen))
        if ctx.getChildCount() == 1:
            return first_value

        action = next(child_gen).getText()
        assert action in ['>', '<', '>=', '<=']

        second_value = self.visit(next(child_gen))

        grater = 0
        match action:
            case '>':
                grater = first_value > second_value
            case '<':
                grater = first_value < second_value
            case '>=':
                grater = first_value >= second_value
            case '<=':
                grater = first_value <= second_value

        return grater

    # Visit a parse tree produced by CrawLangParser#eq_expr.
    def visitEq_expr(self, ctx: CrawLangParser.Eq_exprContext):
        child_gen = ctx.getChildren()

        first_value = self.visit(next(child_gen))
        if ctx.getChildCount() == 1:
            return first_value

        action = next(child_gen).getText()
        assert action in ['==', '!=']

        second_value = self.visit(next(child_gen))

        equal = 0
        match action:
            case '==':
                grater = first_value == second_value
            case '!=':
                grater = first_value != second_value

        return equal

    # Visit a parse tree produced by CrawLangParser#lmul_expr.
    def visitLmul_expr(self, ctx: CrawLangParser.Lmul_exprContext):
        check = self.visit(next(ctx.getChildren()))
        if not isinstance(check, str | int | float):
            return check

        first_value = check
        if isinstance(first_value, str):
            assert ctx.getChildCount() == 1, 'string logical multiplication'
            return first_value

        lmult = 0
        first = True
        for child in ctx.getChildren():
            value = self.visit(child)
            if child.getText() != 'and':
                if first:
                    lmult = value
                    first = False
                else:
                    lmult = lmult and value
        return lmult

    # Visit a parse tree produced by CrawLangParser#expr.
    def visitExpr(self, ctx: CrawLangParser.ExprContext):
        ladd = 0
        first = True
        for child in ctx.getChildren():
            value = self.visit(child)
            if child.getText() != 'or':
                if first:
                    ladd = value
                    first = False
                else:
                    ladd = ladd and value
        return ladd

    # Visit a parse tree produced by CrawLangParser#arg_list.
    def visitArg_list(self, ctx: CrawLangParser.Arg_listContext):
        arg_list = []
        for child in ctx.getChildren():
            if child.getText() != ',':
                arg_list.append(self.visit(child))
        return arg_list


    # Visit a parse tree produced by CrawLangParser#print.
    def visitPrint(self, ctx:CrawLangParser.PrintContext):
        for child in ctx.getChildren():
            value = self.visit(child)
            if child.getText() not in ['(', ')', 'print', ';']:
                print(value)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#print_all_stats_func.
    def visitPrint_all_stats_func(self, ctx:CrawLangParser.Print_all_stats_funcContext):
        print_all_stats()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#obj.
    def visitObj(self, ctx:CrawLangParser.ObjContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CrawLangParser#site_func.
    def visitSite_func(self, ctx:CrawLangParser.Site_funcContext):
        args = []
        for child in ctx.getChildren():
            value = self.visit(child)
            if child.getText() not in ['(', ')', 'site', ';', ',']:
                args.append(value)
        return site(*args)


    # Visit a parse tree produced by CrawLangParser#next_func.
    def visitNext_func(self, ctx:CrawLangParser.Next_funcContext):
        for child in ctx.getChildren():
            value = self.visit(child)
            if child.getText() not in ['(', ')', 'next', ';']:
                return _next(value)


    # Visit a parse tree produced by CrawLangParser#domain_func.
    def visitDomain_func(self, ctx:CrawLangParser.Domain_funcContext):
        for child in ctx.getChildren():
            value = self.visit(child)
            if child.getText() not in ['(', ')', 'domain', ';']:
                return domain(value)


    # Visit a parse tree produced by CrawLangParser#has_subdomain_func.
    def visitHas_subdomain_func(self, ctx:CrawLangParser.Has_subdomain_funcContext):
        for child in ctx.getChildren():
            value = self.visit(child)
            if child.getText() not in ['(', ')', 'has_subdomain', ';']:
                return has_subdomain(value)
