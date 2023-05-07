grammar CrawLang;

SPACE:          [ \t\r\n]+    -> channel(HIDDEN);
COMMENT_BLOCK:  '/*' .*? '*/' -> channel(HIDDEN);
COMMENT_LINE:  '//' .*? '\r\n'  -> channel(HIDDEN);


// точка входа в программу (я бы переименовал)
funclist
  : ( function_def )* EOF
  ;

// обьявление функции
function_def
  : func_header block
  ;

// заголовок функции (тип, имя и лист аргументов)
func_header
  : func_name_decl LPAREN ( formal_list )? RPAREN
  ;

// тип функции(опционально) и имя функции
func_name_decl
  : VALID_VARIABLE_NAME
  | base_type VALID_VARIABLE_NAME
  ;

// лист аргументов
formal_list
  : base_type VALID_VARIABLE_NAME ( COMMA base_type VALID_VARIABLE_NAME )*
  ;

// типы (лол)
base_type
  : ( 'char' | 'int' )
  ;

statement
  : block
  | print
  | assignment_statement
  | if_stmt
  | for_loop
  | return_statement
  | SEMICOLON
  ;


// блок с фигурными скобочками
block
  : LCURL (decl)* (statement)* RCURL
  ;

// деклорация переменных
decl
  : base_type VALID_VARIABLE_NAME ( COMMA VALID_VARIABLE_NAME )* SEMICOLON
  ;

// присваивание
assignment_statement
  : assignment SEMICOLON
  ;

if_stmt
  : 'if' LPAREN expr RPAREN statement
    ( else_part
      | () // nothing
     )
  ;

else_part
  : 'else' statement
  ;

for_loop
  : 'for' loop_cntrl statement
  ;

// инициализация цикла
loop_cntrl
  : LPAREN loop_init loop_cond loop_incr RPAREN
  ;

loop_init
  : SEMICOLON
  | assignment SEMICOLON
  ;

loop_cond
  : SEMICOLON
  | expr SEMICOLON
  ;

loop_incr
  : () // empry
  | assignment
  ;

return_statement
  : 'return' expr SEMICOLON
  ;

primary_expr
  : VALID_VARIABLE_NAME
  | LITERAL
  | (LPAREN expr RPAREN )
  ;

assignment
  : (variable_name=VALID_VARIABLE_NAME ASSIGN)? expr
  ;

postfix_expr: primary_expr ( arg_list )?
            ;

boolneg_expr
  : ( 'not' )* postfix_expr
  ;

sign_expr
  : boolneg_expr
  | MINUS boolneg_expr
  ;

mul_expr
  : sign_expr (( TIMES | DIVIDE | MOD ) sign_expr)*
  ;

add_expr
  : mul_expr ( ( PLUS | MINUS ) mul_expr )*
  ;

shift_expr
  : add_expr (( SHIFT_LEFT | SHIFT_RIGHT )  add_expr )*
  ;

rel_expr
  : shift_expr (( LTHAN | GTHAN | GEQ | LEQ ) shift_expr)*
  ;

eq_expr
  : rel_expr (( EQ | NEQ ) rel_expr)*
  ;

lmul_expr
  : eq_expr ( 'and' eq_expr )*
  ;

expr
  : lmul_expr ('or' lmul_expr)*
  ;


arg_list
  : LPAREN expr ( COMMA expr )* RPAREN
  ;

print
  : 'print' LPAREN expr RPAREN SEMICOLON
  ;

VALID_VARIABLE_NAME : [a-zA-Z] [a-zA-Z_0-9]* ;

LITERAL: (INT | CHAR);

// типы данных нашего языка
INT : [0-9]+;
CHAR : [a-zA-Z];

COMMA : ',' ;
SEMICOLON  : ';' ;

//скобочки
LPAREN : '(' ;
RPAREN : ')' ;
LCURL : '{' ;
RCURL : '}' ;

//знаки операторов
PLUS : '+' ;
MINUS : '-' ;
TIMES : '*' ;
DIVIDE : '/' ;
MOD : '%' ;
ASSIGN : '=' ;

EQ : '==' ;
NEQ : '!=' ;
LTHAN :  '<' ;
GTHAN :  '>' ;
LEQ :  '<=' ;
GEQ :  '>=' ;
SHIFT_LEFT : '<<' ;
SHIFT_RIGHT  : '>>' ;
