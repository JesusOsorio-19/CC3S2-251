### Actividad : Orquestador local de entornos de desarrollo simulados con Terraform

Demostraremos los conceptos y principios fundamentales de IaC utilizando Terraform para gestionar un entorno de desarrollo simulado completamente local. 

Aprenderemos a definir, aprovisionar y modificar "infraestructura" (archivos, directorios, scripts de configuración)  de forma reproducible y automatizada.

#### **Prerrequisitos:**

 - Terraform instalado localmente.
 - Python 3 instalado localmente.
 - Conocimientos básicos de la línea de comandos (Bash).
 - Un editor de texto o IDE.


#### Estructura del proyecto (archivos y directorios)

Puedes revisar las instrucciones adicionales y el código completo y sus modificaciones dependiendo de tu sistema operativo en [proyecto inicial de IaC](https://github.com/kapumota/DS/tree/main/2025-1/Proyecto_iac_local).

```
proyecto_iac_local/
├── main.tf                     # Configuración principal de Terraform
├── variables.tf                # Variables de entrada
├── outputs.tf                  # Salidas del proyecto
├── versions.tf                 # Versiones de Terraform y providers (local, random)
├── terraform.tfvars.example    # Ejemplo de archivo de variables
│
├── modules/
│   ├── application_service/    # Módulo para simular un "servicio"
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   │   └── templates/
│   │       └── config.json.tpl # Plantilla de configuración del servicio
│   │
│   └── environment_setup/      # Módulo para la configuración base del entorno
│       ├── main.tf
│       ├── variables.tf
│       └── scripts/
│           └── initial_setup.sh # Script de Bash para tareas iniciales
│
├── scripts/                    # Scripts globales
│   ├── python/
│   │   ├── generate_app_metadata.py # Genera metadatos complejos para apps
│   │   ├── validate_config.py       # Valida archivos de configuración generados
│   │   └── report_status.py         # Genera un reporte del "estado" del entorno
│   └── bash/
│       ├── start_simulated_service.sh # Simula el "arranque" de un servicio
│       └── check_simulated_health.sh  # Simula una "comprobación de salud"
│
└── generated_environment/      # Directorio creado por Terraform
    └── (aquí se crearán archivos y directorios)
```
       
#### Ejercicios

1. **Ejercicio de evolvabilidad y resolución de problemas - Solución**

    Se agrega el servicio database:

    ```terraform
    # Proyecto_iac_local/main.tf
    31 database = { 
    32   version           = "1.0.0" 
    33   port              = 1234 
    34   connection_string = "" 
    35 }
    ```

    Los valores que usa son: la versión, el puerto (como las apps) y connection_string.

    También se agrega un local `connection_string` en `main.tf`, para hacer un `lookup()` entre las variables para la db:

    ```terraform
    # Proyecto_iac_local/main.tf
    39 connection_string        = lookup(each.value, "connection_string", "") 
    ```

    En las variables se define el tipo y valor por defecto de `connection_string`:

    ```terraform
    # Proyecto_iac_local/variables.tf
    20 variable "connection_string" {
    21  type    = string
    22  default = ""
    23 }
    ```

    Adicionalmente se agrega `connection_string_tpl` para usar este valor (si existe usando condicionales en el archivo template `tpl`):

    ```terraform
    # Proyecto_iac_local/modules/application_service/templates/config.json.tpl
    7 %{ if connection_string_tpl != "" ~} 
    8 "connectionString": "${connection_string_tpl}", 
    9 %{ endif ~} 
    ```

    ```terraform
    # Proyecto_iac_local/modules/application_service/main.tf
    30 connection_string_tpl = var.connection_string 
    ```

    El valor se mapea desde las variables definidas anteriormente.

    Para validar que este valor se encuentre se modifica el script python `validate_config.py`, este valida si existe y si es `string`:

    ```python
    # Proyecto_iac_local/scripts/python/validate_config.py
    11 if app_name == "database": 
    12     if not isinstance(config.data.get("connectionString", str)) and not config.data.get("connection_string"): 
    13         errors.append(f"[{file_path} 'connectionString' debe ser string]") 
    ```

2. **Ejercicio de refactorización y principios - Solución**
   
    Se crea el script `generate_global_metada.py`, para generar ids de despliegues usando `uuid` (librera que viene con python):

    ```python
    # Proyecto_iac_local/scripts/python/generate_global_metadata.py
    import json 
    import uuid 
    from datetime import datetime 
    
    def main(): 
        deployment_id = str(uuid.uuid4()) 
        metadata = { 
            "deployment_id": deployment_id, 
            "deployment_timestamp": datetime.utcnow().isoformat() 
        } 
    
        print(json.dumps(metadata)) 
    
    if __name__ == "__main__": 
        main() 
    ```

    Este script sera ejecutado por terraform por lo que se debe imprimir en format json. Se ejecuta en terraform usando `data "external"`:

    ```terraform
    # Proyecto_iac_local/main.tf
    97 data "external" "deployment_info" { 
    98   program = [var.python_executable, "${path.cwd}/scripts/python/generate_global_metadata.py"] 
    99   query = { 
    100     deployment_id = "env_id" 
    101   } 
    102 }  
    ```

    Este valor de output luego se puede refernciar con la sintaxis de `result`:

    ```terraform
    # Proyecto_iac_local/main.tf
    38 module "simulated_apps" { 
    39   for_each = local.common_app_config 
    40    
    41    source                   = "./modules/application_service" 
    42    app_name                 = each.key 
    43    app_version              = each.value.version 
    44    app_port                 = each.value.port 
    45    base_install_path        = "${path.cwd}/generated_environment/services" 
    46    global_message_from_root = var.mensaje_global # Pasar la variable sensible 
    47    python_exe               = var.python_executable 
    48    deployment_id            = data.external.deployment_info.result.deployment_id 
    49 } 
    ```

    Aqui se envia este valor que se ejecuto con `main.tf` al modulo `application_service` donde se crearan los archivos de configurion `config.json` usando el template `config.json.tpl`:

    ```json
    # Proyecto_iac_local/modules/application_service/templates/config.json.tpl
    6  "globalDeploymentId": "${deployment_id_tpl}", 
    ```

    Para recibir este valor debe ser definido en el `main.tf` de `application_service`:

    ```terraform
    # Proyecto_iac_local/modules/application_service/main.tf
    30  deployment_id_tpl     = var.deployment_id  
    ```

    > ¿Cómo mejora esto la composabilidad y reduce la redundancia? ¿Cómo afecta la idempotencia?

    Al actualizar recursos este nuevo id global no afectara a los otros recursos dentro del sistema por lo que se cumple la composabilidad.

    Como el valor es el mismo para todas las aplicaciones que se crearan, este no tendra interferencia en la idempotencia puesto que quedara igual para los otros despues de distintas ejecuciones con `terraform apply`.
    
3. **Ejercicio de idempotencia y scripts externos - Solución**

   Se modifica el script de bash `initial_setup.sh`, este creara un archivo control (si es que no existe) y dentro se pondra un contador para verificar cuantas veces se corrio este script ( o el flujo de generacion de environments puesto que estan ligados ).

   ```sh
   # Proyecto_iac_local/modules/environment_setup/scripts/initial_setup.sh 
   19  if [ ! -f "$CONTROL_FILE" ]; then 
   20  echo "Ejecutando setup inicial para el entorno: $ENV_NAME" 
   21  echo "Creando placeholder_control.txt..." 
   22  echo "count=1" > "$CONTROL_FILE" 
   23 
   24  echo "Creando placeholder_$(date +%s).txt..." 
   25  touch "placeholder_$(date +%s).txt" 
   ```
   Ademas se crea el archivo `placeholder` con la fecha.

   En el caso que el archivo exista (inicialmente tendra el contenido `count=1`) entonces se parseara el archivo (usando grep) y se aumentara en uno el conteo. 

   ```sh
   # Proyecto_iac_local/modules/environment_setup/scripts/initial_setup.sh 
   28 else 
   29  echo "Control file existe" 
   30  echo "Aumentando contador en placeholder_control.txt..." 
   31  COUNT=$(grep -o '[0-9]*' "$CONTROL_FILE") 
   32  echo "count=$((COUNT + 1))" > "$CONTROL_FILE" 
   33 fi 
   ```

   Con este archivo `placeholder_control.txt` se podra revisar cuantas veces se ejecuto `terraform apply` y verificar la idempotencia puesto que solo se crea una vez y se usa una condicional para verificar su existencia.
 
4. **Ejercicio de seguridad simulada y validación - Solución**
   
    Para validar este mensaje se obtiene el valor `notes` de los archivos `config.json`. Se verifica que `string` y que tiene el mismo valor `sensitive=true` (definido en `vars.tf`) en el directorio root:

    ```python
    # Proyecto_iac_local/scripts/python/validate_config.py
    15 notes_config = config_data.get("notes", "") 
    16 if not isinstance(notes_config, str): 
    17    errors.append(f"[{file_path}] 'notes' debe ser un string.") 
    18 if "Configuración gestionada por Terraform." in notes_config: 
    19    warnings.append(f"[{file_path}] 'notes' tiene un fallo de seguridad critico") 
    ```

    Si el contenido del mensaje esta dentro de `notes` se agrega a la lista de `warnings` que este archivo `validate_config.py` entrega al ejecutar `terraform plan` y `terraform apply`

    Como este valor se esta mostrando por que esta mapeado en el archivo template `config.json.tpl` se revisara una condicion para saber si es sensitive (secreta). Para esto `terraform` tiene una funcion `issensitive()` en el cual recibe como argumento la variable. Se pasa este nuevo valor booleana al template de esta manera:

    ```terraform
   # Proyecto_iac_local/modules/application_service/main.tf
   31 issensitive_global_message_tpl = issensitive(var.global_message_from_root) 
   ```

   Con este valor se puede usar una condicional (ternario) en el archivo template para que el `mensaje_global` se muestre en caso de que esta nueva variable booleana sea falsa:

    ```json
   # Proyecto_iac_local/modules/application_service/templates/config.json.tpl
   7  "notes": "Este es un archivo de configuración autogenerado. ${issensitive_global_message_tpl? "Valor ofuscado" : message_tpl }", 
   ```

   Si es `sensitive` se mostrara `valor ofuscado` en los archivos config generados para cada aplicacion:

    ```json
   # Proyecto_iac_local/generated_environment/services/app1_v1.0.2/config.jsonjson.tpl
   7  "notes": "Este es un archivo de configuración autogenerado. Valor ofuscado",  
   ```
