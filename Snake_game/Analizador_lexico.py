"""
Integrantes: Durán Breceda Lourdes Jamileth - Gracida Tapia Bryan
PLY - Analizador léxico
- PLY es una biblioteca de Python para la creación de analizadores léxicos y sintácticos.
Está inspirado en herramientas tradicionales como Lex y Yacc, usadas con lenguajes como C y C++.
"""

import ply.lex as lex

# Lista para registrar errores léxicos
errores_lexicos = []

# Palabras reservadas
reservadas = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'return': 'RETURN',
    'import': 'IMPORT',
    'from': 'FROM',
    'fun': 'FUN',
    'true': 'TRUE',
    'false': 'FALSE',
    'int': 'INT',
    'real': 'REAL',
    'bool': 'BOOL',
    'stg': 'STG',
    'begin': 'BEGIN',
    'end': 'END',
}

# Lista de tokens
tokens = list(reservadas.values()) + [
    'ID',
    'NUMERO',
    'REAL_NUM',
    'SUMA',
    'RESTA',
    'DIVISION',
    'MULTIPLICACION',
    'ASIGNACION',
    'IGUAL',
    'DIFERENTE',
    'MAYOR_QUE',
    'MENOR_QUE',
    'MAYOR_IGUAL',
    'MENOR_IGUAL',
    'PUNTO',
    'COMA',
    'DOS_PUNTOS',
    'PUNTO_COMA',
    'COMILLA_SIMPLE',
    'COMILLA_DOBLE',
    'PARENTESIS_IZQ',
    'PARENTESIS_DER',
    'LLAVE_IZQ',
    'LLAVE_DER',
    'CORCHETE_IZQ',
    'CORCHETE_DER',
    'MAS_MAS',
    'MENOS_MENOS',
    'AND',
    'OR',
    'NOT',
    'CADENA',
]

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Expresiones regulares para tokens simples
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_ASIGNACION = r'='
t_IGUAL = r'=='
t_DIFERENTE = r'!='
t_MAYOR_QUE = r'>'
t_MENOR_QUE = r'<'
t_MAYOR_IGUAL = r'>='
t_MENOR_IGUAL = r'<='
t_PUNTO = r'\.'
t_COMA = r','
t_DOS_PUNTOS = r':'
t_PUNTO_COMA = r';'
t_COMILLA_SIMPLE = r'\''
t_COMILLA_DOBLE = r'\"'
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_CORCHETE_IZQ = r'\['
t_CORCHETE_DER = r'\]'
t_MAS_MAS = r'\+\+'
t_MENOS_MENOS = r'--'
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'

# Manejo de saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Cadena entre almohadillas
def t_CADENA(t):
    r'\#.*?\#'
    return t

# Identificadores y palabras reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value.lower(), 'ID')
    return t

# Números reales
def t_REAL_NUM(t):
    r'(\d+\.\d+|\.\d+)'
    t.value = float(t.value)
    return t

# Números enteros
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Comentarios de una sola línea estilo // comentario //
def t_comentario(t):
    r'\/\/.*?\/\/'
    pass  # Se ignoran los comentarios

# Manejo de errores
def t_error(t):
    errores_lexicos.append(f"Símbolo no válido '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()

# Función para analizar código fuente
def analisis(codigo):
    lexer.input(codigo)
    resultado = []
    lexer.lineno = 1

    for tok in lexer:
        columna = tok.lexpos - codigo.rfind('\n', 0, tok.lexpos)
        resultado.append((tok.value, tok.type, tok.lineno, columna))

    return resultado

# Ejemplo de uso
if __name__ == '__main__':
    codigo_prueba = "/programafuente.py"

    resultado_tokens = analisis(codigo_prueba)

    print("Tokens encontrados:")
    for token in resultado_tokens:
        print(token)

    if errores_lexicos:
        print("\nErrores léxicos:")
        for error in errores_lexicos:
            print(error)

