export default [
  { 
    name: 'If', 
    code: 'if ($param1 $param2 $param3)', 
    description: 'Überprüft eine Bedingung und führt den nachfolgenden Code nur aus, wenn die Bedingung wahr ist.',
    params: [
      { name: 'Bedingung1', description: 'Der erste Ausdruck, der überprüft wird. Erwartet: Zahl, String, Variable.' },
      { name: 'Operator', description: 'Der Vergleichsoperator. Erwartet: ==, !=, >, <, >=, <=.' },
      { name: 'Bedingung2', description: 'Der zweite Ausdruck, der überprüft wird. Erwartet: Zahl, String, Variable.' }
    ]
  },
  { 
    name: 'Else If', 
    code: 'else if ($param1 $param2 $param3)', 
    description: 'Überprüft eine alternative Bedingung, wenn die ursprüngliche If-Bedingung nicht wahr ist.',
    params: [
      { name: 'Bedingung1', description: 'Der erste Ausdruck, der überprüft wird. Erwartet: Zahl, String, Variable.' },
      { name: 'Operator', description: 'Der Vergleichsoperator. Erwartet: ==, !=, >, <, >=, <=.' },
      { name: 'Bedingung2', description: 'Der zweite Ausdruck, der überprüft wird. Erwartet: Zahl, String, Variable.' }
    ]
  },
  { 
    name: 'Else', 
    code: 'else', 
    description: 'Führt den nachfolgenden Code aus, wenn keine der vorangegangenen Bedingungen (If oder Else If) wahr war.',
    params: [] 
  },
  { 
    name: 'If Ende', 
    code: 'endIf', 
    description: 'Markiert das Ende einer If-Anweisung.',
    params: [] 
  },
  { 
    name: 'Else If Ende', 
    code: 'endElseIf', 
    description: 'Markiert das Ende einer Else-If-Anweisung.',
    params: [] 
  },
  { 
    name: 'Else Ende', 
    code: 'endElse', 
    description: 'Markiert das Ende einer Else-Anweisung.',
    params: [] 
  },
  { 
    name: 'Date Refactor', 
    code: 'refactorDate($param1, $param2)', 
    description: 'Wandelt ein Datumsformat in ein anderes Format um.',
    params: [
      { name: 'DatumString', description: 'Das Eingabedatum als String. Erwartet: Datum im String-Format.' },
      { name: 'Format', description: 'Das Zielformat für das Datum. Erwartet: String (z.B. "YYYY-MM-DD").' }
    ]
  },
  { 
    name: 'Substring', 
    code: 'substring($param1, $param2, $param3)', 
    description: 'Extrahiert einen Teilstring aus einem gegebenen String basierend auf Startposition und Länge.',
    params: [
      { name: 'String', description: 'Der Eingabestring. Erwartet: String.' },
      { name: 'StartPunkt', description: 'Die Startposition des Substrings. Erwartet: Zahl (0-basierter Index).' },
      { name: 'Länge', description: 'Die Anzahl der Zeichen im Substring. Erwartet: Zahl.' }
    ]
  },
  { 
    name: 'Variable', 
    code: 'var $param1 = $param2', 
    description: 'Deklariert eine Variable und weist ihr einen bestimmten Wert zu.',
    params: [
      { name: 'Variablenname', description: 'Der Name der zu deklarierenden Variable. Erwartet: String.' },
      { name: 'Wert', description: 'Der Wert, der der Variable zugewiesen wird. Erwartet: Zahl, String, Ausdruck.' }
    ]
  },
  { 
    name: 'isType', 
    code: 'isType($param1, $param2)', 
    description: 'Überprüft, ob eine Variable einem bestimmten Typ entspricht.',
    params: [
      { name: 'Variable/Wert', description: 'Der zu überprüfende Wert oder die Variable. Erwartet: Zahl, String, Variable.' },
      { name: 'Typ', description: 'Der erwartete Datentyp. Erwartet: "String", "Number", "Boolean".' }
    ]
  },
  { 
    name: 'Length', 
    code: 'length($param1)', 
    description: 'Gibt die Länge eines Arrays oder eines Strings zurück.',
    params: [
      { name: 'ArrayOderString', description: 'Das Eingabearray oder der String. Erwartet: Array, String.' }
    ]
  },
  { 
    name: 'Math Operation', 
    code: 'mathOp($param1, $param2, $param3)', 
    description: 'Führt eine mathematische Operation basierend auf den übergebenen Operanden und dem Operator durch.',
    params: [
      { name: 'Operand1', description: 'Der erste Operand. Erwartet: Zahl, Variable.' },
      { name: 'Operator', description: 'Der mathematische Operator. Erwartet: +, -, *, /, %.' },
      { name: 'Operand2', description: 'Der zweite Operand. Erwartet: Zahl, Variable.' }
    ]
  },
  { 
    name: 'Concat', 
    code: 'concat($param1, $param2, $param3, $param4, $param5)', 
    description: 'Verkettet zwei bis 5 Strings und gibt das Ergebnis zurück.',
    params: [
      { name: 'String1', description: 'Der erste String. Erwartet: String.' },
      { name: 'String2', description: 'Der zweite String. Erwartet: String.' },
      { name: 'String2', description: 'Der dritte String. Erwartet: String.' },
      { name: 'String2', description: 'Der vierte String. Erwartet: String.' },
      { name: 'String2', description: 'Der fünfte String. Erwartet: String.' }
    ]
  },
  { 
    name: 'To UpperCase', 
    code: 'toUpperCase($param1)', 
    description: 'Wandelt einen String in Großbuchstaben um.',
    params: [
      { name: 'String', description: 'Der umzuwandelnde String. Erwartet: String.' }
    ]
  },
  { 
    name: 'To LowerCase', 
    code: 'toLowerCase($param1)', 
    description: 'Wandelt einen String in Kleinbuchstaben um.',
    params: [
      { name: 'String', description: 'Der umzuwandelnde String. Erwartet: String.' }
    ]
  },
  { 
    name: 'Replace', 
    code: 'replace($param1, $param2, $param3)', 
    description: 'Ersetzt ein bestimmtes Teilstück eines Strings durch ein anderes.',
    params: [
      { name: 'String', description: 'Der Eingabestring. Erwartet: String.' },
      { name: 'ZuErsetzen', description: 'Das Teilstück, das ersetzt werden soll. Erwartet: String.' },
      { name: 'Ersetzung', description: 'Das neue Teilstück, das eingesetzt werden soll. Erwartet: String.' }
    ]
  },
  { 
    name: 'Round', 
    code: 'round($param1)', 
    description: 'Rundet eine Zahl auf die nächste Ganzzahl.',
    params: [
      { name: 'Zahl', description: 'Die zu rundende Zahl. Erwartet: Zahl.' }
    ]
  },
  { 
    name: 'Floor', 
    code: 'floor($param1)', 
    description: 'Rundet eine Zahl auf die nächste ganze Zahl ab.',
    params: [
      { name: 'Zahl', description: 'Die zu rundende Zahl. Erwartet: Zahl.' }
    ]
  },
  { 
    name: 'Abs', 
    code: 'abs($param1)', 
    description: 'Gibt den absoluten Wert einer Zahl zurück.',
    params: [
      { name: 'Zahl', description: 'Die Zahl, deren absoluter Wert benötigt wird. Erwartet: Zahl.' }
    ]
  },
  { 
    name: 'Pow', 
    code: 'pow($param1, $param2)', 
    description: 'Berechnet die Potenz einer Zahl.',
    params: [
      { name: 'Basis', description: 'Die Basiszahl. Erwartet: Zahl.' },
      { name: 'Exponent', description: 'Der Exponent, auf den die Basis erhöht wird. Erwartet: Zahl.' }
    ]
  },
  { 
    name: 'Sqrt', 
    code: 'sqrt($param1)', 
    description: 'Berechnet die Quadratwurzel einer Zahl.',
    params: [
      { name: 'Zahl', description: 'Die Zahl, deren Quadratwurzel berechnet werden soll. Erwartet: Zahl.' }
    ]
  },
  {
    name: 'Trim',
    code: 'trim($param1)',
    description: 'Entfernt Leerzeichen vom Anfang und Ende eines Strings.',
    params: [
      { name: 'String', description: 'Der String, der getrimmt werden soll. Erwartet: String.' }
    ]
  },
];
