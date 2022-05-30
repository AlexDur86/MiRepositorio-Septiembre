"""Este archivo sirve para corregir los ejercicios graduados."""
import os
import sys


def flake_comp(file_path):
    """Esta funcion computa los componentes de Flake8.
    
    Parameters
    ----------
        file_path:
            Ruta donde se encuentra el archivo.
    Returns
    -------
        None
    """
    max_complexity = "--max-complexity 4"
    max_lines = "--max-line-length 120"
    ignore = "--ignore W2,E226"
    max_doc = "--max-doc-length 400"
    f8_execution = os.popen(f"flake8 {max_complexity} {max_lines} {ignore} {max_doc} {file_path}")
    f8_summary = f8_execution.read()
    print("#"*5, "FLAKE8", "#"*5)
    print(f8_summary)
    print("\n")
    return f8_summary


def pds_comp(file_path):
    """Esta funcion computa los componentes de Pydocstyle.
    
    Parameters
    ----------
        file_path:
            Ruta donde se encuentra el archivo.
    Returns
    -------
        None
    """
    pds_execution = os.popen(f"pydocstyle {file_path}")
    pds_summary = pds_execution.read()
    print("#"*5, "PYDOCSTYLE", "#"*5)
    print(pds_summary)
    print("\n")
    return pds_summary


def pl_comp(file_path):
    """Esta funcion computa los componentes de Pylint.
    
    Parameters
    ----------
        file_path:
            Ruta donde se encuentra el archivo.
    Returns
    -------
        None
    """
    pl_execution = os.popen(f"pylint --disable all --enable C0103 {file_path}")
    pl_summary = pl_execution.read()
    print("#"*5, "PYLINT", "#"*5)
    print(pl_summary.split("------------------")[0])
    print("\n")
    return pl_summary.split("------------------")[0]


def correction(file_path):
    """Esta funcion sirve para corregir los ejercicios.

    Esta funcion analiza la complejidad de codigo, el estilo de escritura, el tiempo
    de ejecucion y que satisfaga la funcionalidad del enunciado.

    Parameters
    ----------
        file_path:
            Ruta donde se encuentra el archivo.
    Returns
    -------
        None
    """
    errors = 0
    # Flake8 components
    f8_s = flake_comp(file_path)
    errors += len(list(filter(lambda e: e != "", f8_s.strip().split("\n"))))
 
    # Pydocstyle components
    pds_s = pds_comp(file_path)
    errors += len(list(filter(lambda e: e != "", pds_s.strip().split("\n"))))

    # Pylint components
    pl_s = pl_comp(file_path)
    errors += len(list(filter(lambda e: e != "", pl_s.strip().split("\n"))))

    file = open(file_path)
    filer = file.read()
    file.close()
    total_lines = len(filer.split("\n"))
    print(f"El codigo tiene un {round(100*errors/total_lines, 2)}% de errores asi pues la nota es: {round(100*(1-errors/total_lines), 2)}%")


if __name__ == "__main__":
    FILE_PATH = sys.argv[1]
    correction(FILE_PATH)
