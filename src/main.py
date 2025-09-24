import subprocess

mapping = {
    "చూపించు": "print", "chuppinchu": "print",
    "తీసుకో": "input", "tisuko": "input",
    "ఒకవేళ": "if", "okavela": "if",
    "ఒకవెలలేదా": "elif", "okavelaledha": "elif",
    "లేదా": "else", "ledha": "else",
    "కొసం": "for", "kosam": "for",
    "అయితే": "while", "ayithe": "while",
    "నివారణ్చు": "def", "nivarinchu": "def",
    "వర్గం": "class", "vargam": "class",
    "తిరిగి ఇవ్వు": "return", "tirigiivvu": "return",
    "అగ్గు": "break", "aggu": "break",
    "కొనసాగించు": "continue", "konasaginchu": "continue",
    "దిగుమతి": "import", "digumati": "import",
    "నుండి": "from", "nundi": "from",
    "గా": "as", "ga": "as",
    "తో": "with", "tho": "with",
    "ప్రయత్నించు": "try", "prayatninchu": "try",
    "తప్ప": "except", "tappa": "except",
    "చివరగా": "finally", "chivariga": "finally",
    "నిజం": "True", "nijam": "True",
    "అబద్ధం": "False", "abaddham": "False",
    "ఏదీ లేదు": "None", "ediledu": "None",
    "లేకపోతే": "or", "lekapothe": "or",
}

def translate(code: str) -> str:

    for tel, eng in mapping.items():
        code = code.replace(tel, eng)
    return code

def run_tlang_file(filename="test.tl"):
    with open(filename, "r", encoding="utf-8") as f:
        telugu_code = f.read()
    python_code = translate(telugu_code)
    with open("temp.py", "w", encoding="utf-8") as f:
        f.write(python_code)

    subprocess.run(["python3", "temp.py"])

if __name__ == "__main__":
    run_tlang_file()
