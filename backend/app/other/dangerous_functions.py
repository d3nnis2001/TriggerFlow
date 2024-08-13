DANGEROUS_FUNCTIONS = [
    # Ausführung von Code
    'eval', 'exec', 'compile',

    # System und Prozesse
    'os.system', 'os.popen', 'os.spawn', 'os.execl', 'subprocess.call', 'subprocess.Popen',

    # Datei-Operationen
    'open', 'file', 'os.open', 'os.mkdir', 'os.remove', 'os.rmdir', 'os.unlink',
    'shutil.rmtree', 'os.rename', 'os.link', 'os.symlink',

    # Netzwerk-Operationen
    'socket.socket', 'urllib.request.urlopen', 'requests.get', 'requests.post',

    # Modul-Importe
    '__import__', 'importlib.import_module',

    # Objektinspektion und -manipulation
    'globals', 'locals', 'vars', 'getattr', 'setattr', 'delattr',

    # Speichermanipulation
    'ctypes', 'mmap',

    # Serialisierung (kann zu RCE führen)
    'pickle.loads', 'yaml.load', 'marshal.loads',

    # Sonstige potenziell gefährliche Operationen
    'sys.exit', 'os.chmod', 'os.chown', 'os.setuid', 'os.setgid',

    # Datenbankoperationen (je nach Kontext)
    'sqlite3.connect', 'mysql.connector.connect', 'psycopg2.connect',

    # Debugging und Inspektion
    'sys._getframe', 'traceback.print_stack',

    # Reflection und Metaprogrammierung
    'type', 'isinstance', 'issubclass', 'callable',

    # Garbage Collection und Speichermanagement
    'gc.collect', 'sys.set_trace_function',
]
