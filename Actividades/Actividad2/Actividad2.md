# Actividad 2 - Del código a la producción: Infraestructura, contenedores, despliegue y observabilidad 

## Integrantes:
1. Luna Jaramilo, Christian
2. Mora Evangelista, Fernando
3. Osorio Tello, Jesus Diego

## A. Infraestructura como Código

> **Tarea teórica**
> - Investigar una herramienta de IaC (p. ej. Terraform) y describir cómo organiza sus módulos.

**1. Terraform - Organzación de módulos**

Los módulos en Terraform son conjuntos de archivos de configuración que crean una abstracción lógica de los recursos de Terraform, las cuales se usan para la creación de recursos de infraestructura y estos se pueden administrar de diferentes maneras: configuración de dependencias, uso repositorios git y registro de terraform.

- Configuración de dependencias: 
Surge cuando un recurso depende de la existencia de otro, Terraform debe comprender el uso de estas dependencias para garantizar que los recursos de creen en el orden correcto. 

    - Declaración ímplicita: 
        - Se declaran a través de referencias de expresión (Terraform analiza la expresión y automáticamente infiere la dependencia entre objetos, es decir no es necesario referenciar completamente un valor si el contexto ya lo define).
        - A menudo tienen mayor eficiencia, limpio y fácil de mantener
        
Ejemplo con declaración implícita

```
module "project_services" {
  source  = "terraform-google-modules/project-factory/google//modules/project_services"
  version = "~> 14.4"

  project_id = var.project_id
  activate_apis = [
    "bigquery.googleapis.com",
    "bigquerystorage.googleapis.com",
  ]
}
module "bigquery" {
  source       = "terraform-google-modules/bigquery/google"
  version      = "~> 5.4"

  dataset_id   = "demo_dataset"
  dataset_name = "demo_dataset"
  project_id   = module.project_services.project_id # <= implicit dependency
}

```

- Declaración explícita
    - Se especifican mediante el metaargumento depends_on (“especifica que Terraform debe completar todas las acciones en los objetos de los que depende un recurso o un módulo antes de continuar con el objeto dependiente”, solo es necesario si no hay una referencia directa dentro del recurso dependiente)  

```
module "project_services" {
  source  = "terraform-google-modules/project-factory/google//modules/project_services"
  version = "~> 14.4"

  project_id = var.project_id
  activate_apis = [
    "bigquery.googleapis.com",
    "bigquerystorage.googleapis.com",
  ]
}

module "bigquery" {
  source       = "terraform-google-modules/bigquery/google"
  version      = "~> 5.4"

  dataset_id   = "demo_dataset"
  dataset_name = "demo_dataset"
  project_id   = var.project_id
  depends_on = [module.project_services] # <= explicit dependency
}

```

- Uso de repositorios git
    - Guarda el código del módulo en un repositorio de Git
    - Etiqueta el módulo con versiones mediante etiquetas Git
- Registro de Terraform
    - Entrar al catálogo público de Terraform donde hay módulos disponibles para su uso

### Organización de módulos

- Los módulos de Terraform deben seguir la estructura de módulo estándar.
- Inicia cada módulo con un archivo main.tf, en el que los recursos se ubican de forma predeterminada.
- En cada módulo, incluye un archivo README.md en formato Markdown. En el archivo README.md, incluye la documentación básica sobre el módulo.
- Coloca los ejemplos en una carpeta examples/, con un subdirectorio separado para cada ejemplo. Para cada ejemplo, incluye un archivo README.md detallado.
- Crea grupos lógicos de recursos con sus propios archivos y nombres descriptivos, como network.tf, instances.tf o loadbalancer.tf.
- Evita darle a cada recurso su propio archivo. Agrupa los recursos según su propósito compartido. Por ejemplo, combina google_dns_managed_zone y google_dns_record_set en dns.tf.
- En el directorio raíz del módulo, incluye solo Terraform (*.tf) y los archivos de metadatos del repositorio (como README.md y CHANGELOG.md).

> Proponer la estructura de archivos y directorios para un proyecto hipotético.

```
Terraform_project/
|-- main.tf
|-- outputs.tf
|-- provider.tf
|-- terraform.tf
|-- variables.tff
|-- .terraform
|     |--modules
|         |-- network
|         |	   |-- main.tf
|         |    |-- outputs.tf
|         |    |-- variables.tf
|         |    |-- README.md
|         |
|         |-- database
|         |    |-- main.tf
|         |    |-- outputs.tf
|         |    |-- variables.tf
|         |    |-- README.md
|         |
|         |-- application
|         |    |-- main.tf
|         |    |-- outputs.tf
|         |    |-- variables.tf
|         |    |-- README.md
|-- .gitignore
|-- README.md

```

## B. Contenerización y despliegue de aplicaciones modernas

> Tarea teórica:
> - Describir un flujo simple de despliegue donde un desarrollador hace un cambio en el código, se construye una nueva imagen Docker y se actualiza un Deployment de Kubernetes.

- Flujo simple
    - El desarrollador actualiza el código y lo realiza un commit para subir la actualización
    - Comienza el proceso CI/CD, al pasar las pruebas, se genera una nueva imagen Docker con los cambios realizados
    - Se actualiza el deployment de Kubernetes para que apunte a la nueva imagen
    - Kubernetes realiza el despliegue de la nueva imagen
    - Se monitorea la aplicación con ayuda de Prometheus y Grafana, para recolectar las métricas actuales (Prometheus) y comparar con las métricas deseadas (Grafana)

> Explicar las ventajas de usar Kubernetes para escalar una aplicación en un evento de alto tráfico.

- Autoscaling:
    - Pueden actualizar la carga de trabajo automáticamente, permitiendo que los clusters reaccionen a los cambios de recursos de forma las efectivo y flexible
- Distribución de carga:
    - Balancea automáticamente las solicitudes entre los Pods usando diferentes servicios, reduciendo así la sobrecarga de un servidor y mejorando la disponibilidad.
- Seguridad:
    - Por sí solo, el DNS de Kubernetes llega a fallar cuando hay un alto tráfico, pero con su complemento NodeLocal DNSCache mejora el rendimiento de DNS del cluster usando un agente de almacenamiento en caché de DNS para lograr una comunicación con los pods que se ejecutan en el mismo nodo, evitando así un seguimiento


## C. Observabilidad y Troubleshooting

>  **Tarea teórica:** 
>    - Investigar y describir como Prometheus y Grafana se integran con Kubernetes para monitorear los contenedores y el cluster.

**1.** **Fuentes:**
- [Introducción a Kubernets](https://www.geeksforgeeks.org/introduction-to-kubernetes-k8s/).
- [Grafana para visualizar métricas de Kubernets](https://www.geeksforgeeks.org/how-to-use-grafana-to-visualize-kubernetes-metrics/).
- [Kubernets Prometheus](https://www.geeksforgeeks.org/kubernetes-prometheus/).
- [Monitoreo de clústeres de Kubernetes con Prometheus y Grafana](https://www.geeksforgeeks.org/monitoring-kubernetes-clusters-with-prometheus-and-grafana/).

**2. Integración de Prometheus y Grafana con Kubernets**

Prometheus se encarga de recoger métricas(CPU, memoria, errores, etc.) de los contenedores y del clúster. Mientras que Grafana es la herramienta de visualización de métricas recolectadas por Prometheus y lo muestra en dashboards interactivos.

- Para que se integren se instala Prometheus y Grafana con Helm que es la forma más fácil de hacerlo.
 
```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install kube-monitoring prometheus-community/kube-prometheus-stack
```

- Gracias a la Service Discovery nativa de Kubernetes, Prometheus encuentra servicios y Pods automáticamente.
- Grafana se conecta automáticamente con Prometheus ya que lo tiene configurado como fuente de datos.

> - Proponer un set de métricas y alertas mínimas para una aplicación web (por ejemplo, latencia de peticiones, uso de CPU/memoria, tasa de errores).

**Set de métricas para una aplicación Web**

| Métricas  | Descripción |
| ------------- |:-------------:|
| up | Verifica si el servicio está respondiendo (1 = OK, 0 = down)     |
| http_request_duration_seconds | Latencia(tiempo de rspta) de peticiones HTTP     |
| http_requests_total     | Tasa de errores 5xx      |
| container_cpu_usage_seconds_total | Uso de CPU por contenedor |
| container_memory_usage_bytes | Uso de memoria por contenedor |

**Alertas mínimas**

- Servicio caído    

```
- alert: ServiceUnavailable
  expr: up == 0
  for: 1m
  labels:
    severity: critical
  annotations:
    summary: "El servicio no está disponible"

```

- Errores 5xx elevados

```
 alert: HighErrosHTTP5xx
  expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.05
  for: 1m
  labels:
    severity: critical
  annotations:
    summary: "Más del 5% de las peticiones están fallando con errores 5xx"
```

- Alta latencia en respuestas HTTP
```
  alert: HighHTTPLatency
  expr: histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m])) > 1.5
  for: 2m
  labels:
    severity: warning
  annotations:
    summary: "La latencia del 95% de las peticiones supera 1.5 segundos"

```

## D. CI/CD (Integración continua / Despliegue continuo)

>  **Tarea teórica:** 
>    - Explicar la diferencia entre entrega continua (continuous delivery) y despliegue continuo (continuous deployment).

**Fuente**

- [Ciclo de vida de DevOps](https://www.geeksforgeeks.org/devops-lifecycle/).

### Entrega continua

Es el proceso de implementar manualmente una aplicación en servidores de producción una vez completadas las etapas de prueba y compilación. En este caso, automatizaremos los procesos de integración continua; sin embargo, la implementación en el entorno de producción aún requiere intervención manual.

### Despliegue continuo

Es el proceso de implementar automáticamente una aplicación en el entorno de producción una vez completadas las etapas de prueba y compilación. Aqui se automizará todo, desde la obtención del código fuente de la aplicación hasta su implementación.

Con esto notamos que la diferencia entre CD y CI, es que la entrega continua necesita la aprobación manual para empezar su despliegue, mientras que el despliegue continuo, solo necesita pasar las pruebas y luego de ello su despliegue será automático.


> - Describir la relevancia de implementar pruebas automáticas (unitarias, de integración, de seguridad) dentro del pipeline.

**Fuentes**
- [Pruebas de software automatizadas](https://www.atlassian.com/es/continuous-delivery/software-testing/automated-testing#:~:text=Las%20pruebas%20automatizadas%20garantizan%20la,para%20implementarse%20en%20todo%20momento.).
- [Pruebas automatizadas](https://kinsta.com/es/blog/pruebas-automatizadas/#:~:text=Integrar%20las%20pruebas%20automatizadas%20en,auditor%C3%ADas%20de%20SEO%20y%20accesibilidad).

Las pruebas automáticas en el pipeline de CI/CD aseguran la calidad y estabilidad del código, pero también permite que el software sea más seguro y fácil de mantener. Sin ellas, se incrementan los riesgos de introducir errores y vulnerabilidades, lo que puede afectar la experiencia del usuario y la confianza del sistema.

- **Pruebas unitarias:**
    - Validar los componentes y las funcionalidades individuales basándose en el código para verificar que funcionen según lo previsto.
    - JUnit (Java), Unidad (.NET), pytest (Python)

- **Pruebas de integración:**
    - Verificar que los módulos o servicios de la aplicación funcionen juntos correctamente
    - TestNG (Java), pytest (Python), JUnit (Java)

- **Pruebas de seguridad:**
    - Permite la identificación de vulnerabilidades y se asegura de que la aplicación sea segura contra ataques.
    - OWASP ZAP, Suite Burp, SonarQube

## Evaluación y discusión final
3. **Trabajo colaborativo**
    -    Diseñar un flujo teórico que combine IaC (para crear recursos en la nube), despliegue de contenedores en Kubernetes y monitoreo con Prometheus/Grafana.

- Flujo teórico
    - Aprovisionamiento de infraestructura con Terraform (configuración de red, creación de máquina virtual, definición de almacenamiento y configuración de los roles permitidos)
    - Despliegue de contenedores Kubernetes (construcción de imagen Docker y configuración de CI/CD para despliegues automáticos)
    - Configuración del monitoreo con Prometheus y Grafana (configuración de los servicios para recolección de métricas de los pods, establecimiento de métricas mínimas para verificar el estado de la aplicación)
 
> Presentar el flujo en un diagrama que incluya cada paso desde el commit hasta la visualización de métricas en tiempo real.

![Flujo](imagen.jpg)


