# TITLE
TITLE = """Año 2048...
Durante los últimos años la Inteligencia Artificial 
ha reemplazado a los humanos en casi todas las labores...
Primero empezó con pequeñas tareas domésticas...
Pero pronto tomaron el control de todos los puestos 
de trabajo...
La Supercomputadora AI-3000 fue la encargada de conectar 
todos los dispositivos a un único núcleo central...
Su misión era asegurar la supervivencia de las 
futuras generaciones...
Pero pronto se volvió tan inteligente que comprendió 
cuál era la verdadera amenaza...
La raza humana....

Presiona ENTER para continuar...
"""

# FIRST SCENE
GAME_SCENE ="""
Es hora de que detengas 
a AI-3000....
Pero recuerda, AI-3000 puede 
verlo todo...
De cada decisión que tomas la 
supercomputadora aprenderá...
Prepárate para desafiar a la 
inteligencia artificial...
"""

GAME_SCENE_1 = """¿Cuál es tu nombre?"""

DICT_TEXT = {
    0: """Bienvienido a Ethernium, la ciudad
controlada por la 
Supercomputadora AI-3000""",

    '01-Preguntar Direcciones': """Te encuentras un androide que está
    probando sus circuitos. Te observa
    extraña por tu forma humana, casi con asco
    y Te pregunta...""",
        '01-Preguntar Direcciones1-AI-3000': """AI-3000 todo lo ve...""",
        '01-Preguntar Direcciones2-Robots': """¿Robots? Somos androides...""",
        '01-Preguntar Direcciones3-Humanos': """¿Humanos?"""
}

DICT_TEXT_DOWN = {
    0: """¿Estás listo {}?""",

    '01-Preguntar Direcciones': """¿En qué puedo ayudarte?""",
        '01-Preguntar Direcciones1-AI-3000': """¿Quieres saber más?""",
        '01-Preguntar Direcciones2-Robots': """¿Quieres saber más?""",
        '01-Preguntar Direcciones3-Humanos': """¿Quieres saber más?"""
}

DICT_BUTTON = {0: ['Preguntar Direcciones', 'Dirigirse al Campo', 'Ir a la Ciudad'],

                '01-Preguntar Direcciones': ['AI-3000', 'Robots', 'Humanos'],
                '01-Preguntar Direcciones1-AI-3000': ['Sí', 'No'],
                '01-Preguntar Direcciones2-Robots': ['Sí', 'No'],
                '01-Preguntar Direcciones3-Humanos': ['Sí', 'No']


}