import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error en {description}: {e}")
        return False

def check_python_version():
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("Se requiere Python 3.8 o superior")
        return False
    
    if version.major == 3 and version.minor >= 12:
        print("Python 3.12+ detectado. Se instalará setuptools para compatibilidad.")
        return "needs_setuptools"
    
    return True

def install_setuptools():
    return run_command(
        "pip install setuptools",
        "Instalando setuptools"
    )

def create_virtual_environment():
    venv_path = Path(".venv")
    if not venv_path.exists():
        print("Creando entorno virtual...")
        if run_command("python -m venv .venv", "Creando entorno virtual"):
            print("Entorno virtual creado exitosamente")
            return True
        else:
            return False
    else:
        print("Entorno virtual ya existe")
        return True

def activate_and_install():
    if os.name == 'nt':  # Windows
        activate_cmd = ".venv\\Scripts\\activate"
        pip_cmd = ".venv\\Scripts\\pip"
    else:  # Unix/Linux/Mac
        activate_cmd = "source .venv/bin/activate"
        pip_cmd = ".venv/bin/pip"
    
    if not run_command(f"{pip_cmd} install --upgrade pip", "Actualizando pip"):
        return False
    
    if check_python_version() == "needs_setuptools":
        if not install_setuptools():
            return False
    
    if not run_command(f"{pip_cmd} install -r requirements.txt", "Instalando dependencias principales"):
        return False
    
    dev_install = input("¿Deseas instalar dependencias de desarrollo? (y/n): ").lower().strip()
    if dev_install in ['y', 'yes', 's', 'si']:
        if not run_command(f"{pip_cmd} install -r requirements-dev.txt", "Instalando dependencias de desarrollo"):
            print("Algunas dependencias de desarrollo no se pudieron instalar")
    
    return True

def main():
    python_check = check_python_version()
    if python_check is False:
        sys.exit(1)
    
    if not create_virtual_environment():
        print("No se pudo crear el entorno virtual")
        sys.exit(1)
    
    if not activate_and_install():
        print("Error durante la instalación de dependencias")
        sys.exit(1)
    
    print("\nInstalación completada exitosamente!")
    if os.name == 'nt':  # Windows
        print("   .venv\\Scripts\\activate")
    else:
        print("   source .venv/bin/activate")
    

if __name__ == "__main__":
    main()
