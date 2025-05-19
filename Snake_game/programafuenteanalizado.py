"""
Integrantes: Durán Breceda Lourdes Jamileth - Gracida Tapia Bryan
PLY - Analizador léxico
Este analizador léxico usa PLY para procesar archivos fuente de Python o pseudocódigo.
"""

import ply.lex as lex

# Lista de errores léxicos
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

t_ignore = ' \t'

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

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_CADENA(t):
    r'\#.*?\#'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value.lower(), 'ID')
    return t

def t_REAL_NUM(t):
    r'(\d+\.\d+|\.\d+)'
    t.value = float(t.value)
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_comentario(t):
    r'\/\/.*?\/\/'
    pass  # Se ignora el comentario

def t_error(t):
    errores_lexicos.append(f"Símbolo no válido '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()

def analisis(codigo):
    lexer.input(codigo)
    resultado = []
    lexer.lineno = 1

    for tok in lexer:
        columna = tok.lexpos - codigo.rfind('\n', 0, tok.lexpos)
        resultado.append((tok.value, tok.type, tok.lineno, columna))

    return resultado

# Analiza el archivo especificado
if __name__ == '__main__':
    ruta_archivo = "suma.py"  # Cambia esto a la ruta de tu archivo

    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            codigo_prueba = f.read()

        resultado_tokens = analisis(codigo_prueba)

        print("\nTokens encontrados:")
        for token in resultado_tokens:
            print(token)

        if errores_lexicos:
            print("\nErrores léxicos:")
            for error in errores_lexicos:
                print(error)

    except FileNotFoundError:
        print(f"\n❌ Error: El archivo '{ruta_archivo}' no fue encontrado.")
