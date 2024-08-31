export default [
  { 
    name: 'If', 
    code: 'if ($param1 $param2 $param3)', 
    description: 'Eine If-Anweisung, die eine Bedingung überprüft und den nachfolgenden Code nur ausführt, wenn die Bedingung wahr ist.', 
    params: ['Bedingung1', 'Operator', 'Bedingung2']
  },
  { 
    name: 'Else', 
    code: 'else', 
    description: 'Eine Else-Anweisung, die ausgeführt wird, wenn die vorangegangene If- oder Else-If-Bedingung nicht erfüllt wurde.', 
    params: [] 
  },
  { 
    name: 'Else If', 
    code: 'else if ($param1 $param2 $param3)', 
    description: 'Eine Else-If-Anweisung, die eine alternative Bedingung überprüft, wenn die ursprüngliche If-Bedingung nicht wahr ist.', 
    params: ['Bedingung1', 'Operator', 'Bedingung2']
  },
  { 
    name: 'Date Refactor', 
    code: 'refactorDate($param1)', 
    description: 'Funktion, die ein Datumsformat refaktoriert oder umwandelt, um es in einem bestimmten Format darzustellen.', 
    params: ['DatumString'] 
  },
  { 
    name: 'Substring', 
    code: 'substring($param1, $param2)', 
    description: 'Extrahiert einen Teilstring aus einem gegebenen String, basierend auf den angegebenen Start- und Endpositionen.', 
    params: ['String', 'Länge'] 
  },
  { 
    name: 'Variable', 
    code: 'var $param1 = $param2', 
    description: 'Deklariert eine Variable und weist ihr einen bestimmten Wert zu.', 
    params: ['Variablenname', 'Wert'] 
  },
  { 
    name: 'Set', 
    code: 'set($param1, $param2)', 
    description: 'Setzt einen Wert für einen bestimmten Schlüssel in einer Datenstruktur wie einem Wörterbuch oder einer Map.', 
    params: ['Schlüssel', 'Wert'] 
  },
  { 
    name: 'isType', 
    code: 'isType($param1, $param2)', 
    description: 'Überprüft, ob eine Variable einem bestimmten Typ entspricht, z.B. ob eine Variable ein String, eine Zahl, etc. ist.', 
    params: ['Variable', 'Typ'] 
  },
  { 
    name: 'Length', 
    code: 'length($param1)', 
    description: 'Gibt die Länge eines Arrays oder eines Strings zurück.', 
    params: ['ArrayOderString'] 
  },
  { 
    name: 'Math Operation', 
    code: 'mathOp($param1, $param2, $param3)', 
    description: 'Führt eine mathematische Operation durch, basierend auf den übergebenen Operanden und dem Operator.', 
    params: ['Operand1', 'Operator', 'Operand2'] 
  }
];
