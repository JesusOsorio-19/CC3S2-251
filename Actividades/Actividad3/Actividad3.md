# Actividad 3 - Computación en la nube

## 2. Instrucciones de la actividad

### A. Cuestionario

#### **1. Motivaciones para la nube**

- **(a) ¿Qué problemas o limitaciones existían antes del surgimiento de la computación en la nube y cómo los solucionó la centralización de servidores en data centers?**

| Problema  | Solución |
| ------------- |:-------------:|
| Costos elevados de infraestructura | Modelos de pago por uso, es decir, pagar solo por los recursos que realmente se usan. Esto elimina los grandes gastos iniciales en infraestuctura. |
| Escalabilidad limitada | La centralización de servidores en data centers permite a los proveedores de la nube gestionar grandes infraestructuras, lo que les permite ajustar los recursos de manera instantánea y según demanda. |
| Seguridad     | Los principales proveedores de la nube invierten enormes recursos en garantizar altos niveles de seguridad como cifrado de datos, controles de acceso, autenticación multifaco, etc.      |
| Limitaciones de acceso | Los proveedores de servicios en la nube operan globalmente, lo que permite que se pueda acceder desde cualquier lugar con internet, facilitando el trabajo remoto y la colaboración. |

- **(b) ¿Por qué se habla de “The Power Wall” y cómo influyó la aparición de procesadores multi-core en la evolución hacia la nube?**

Se habla de The Power Wall ya que era una técnica antigua a la que se enfrentaban los procesadores tradicionales al intentar aumentar la velocidad de la frecuencia. Esto generaba un consumo de energía y una producción de calor insostenibles, lo que impedía que los procesadores mejoren su rendimiento de manera lineal. Para superar esta limitación la industria adoptó procesadores con múltiples núcleos (multi-core), que permite ejecutar varias tareas en paralelo en lugar de depender únicamente de un núcleo más rápido. Mejorando la eficiencia energética y el rendimiento en general. 

 La computación en la nube se benefició de esta evolución, ya que los data centers pudieron aprovechar procesadores multi-core para manejar múltiples máquinas virtuales y cargas de trabajo simultáneamente.

#### **2. Clusters y load balancing**  
- **(a) Explica cómo la necesidad de atender grandes volúmenes de tráfico en sitios web condujo a la adopción de clústeres y balanceadores de carga.**

La creciente demanda de sitios web con altos volúmenes de tráfico nos mostró que un solo servidor no era suficiente para manejar todas las solicitudes eficientement. Así que esto nos trajo los clústeres, que consisten en múltiples servidores trabajando juntos como si fueran uno solo, distribuyendo las cargas de trabajo entre todos los servidores. Y para gestionar esta distribución de manera eficiente, se implementaron balanceadores de carga, que son intermediarios para dirigir las solicitudes de los usuarios al servidor más adecuado dentro del clúster. Esto garantiza un mejor rendimiento, evitando que un único servidor se sobrecargue y falle. [What is Load Balancing?](https://aws.amazon.com/what-is/load-balancing/)

- **(b) Describe un ejemplo práctico de cómo un desarrollador de software puede beneficiarse del uso de load balancers para una aplicación web.**

  - **Caso:** Un desarrollador trabaja en una tienda online de productos X, sabe que hay alto tráfico en sitios web en épocas festivas o fechas de descuento. Así que decide implementar un balanceador de carga para su beneficio.

  - **Beneficios:** El balanceador de carga se encargará de distribuir todas las solicitudes de los usuarios entre varios servidores, asegurando así que la tienda online siga rápida y accesible incluso si tiene grandes volúmenes de tráfico.

#### **3.Elastic computing**  
- **(a) Define con tus propias palabras el concepto de Elastic Computing.**  

Elastic Computing es la capacidad de ajustar automáticamente los recursos de cómputo (como servidores, almacenamiento o redes) según la demanda, aumentando o disminuyendo su uso en tiempo real para optimizar costos y rendimiento. [What is elastic computing?](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-elastic-computing)

- **(b) ¿Por qué la virtualización es una pieza clave para la elasticidad en la nube?**  

Porque nos permite crear máquinas virtuales las cuales se pueden configurar, escalar y mover fácilmente dentro de un data center. Esto hace posible asignar recursos según las necesidades, lo cual es esencial para la elasticidad ya que permite a los proveedores de nube ofrecer recursos eficientemente dependiendo de la demanda.

- **(c) Menciona un escenario donde, desde la perspectiva de desarrollo, sería muy difícil escalar la infraestructura sin un entorno elástico.**

Un escenario ejemplo sería alguna plataforma de streaming (Disney+, Netflix, PrimeVideo, etc.) que experimenta picos de tráfico durante un evento en vivo. Sin un entorno elástico, se tendría que adquirir y mantener servidores adicionales para mantener estable la plataforma en estos picos, lo cual es costoso e ineficiente ya que quedarían en desuso cuando no hay mucha demanda.

#### **4.Modelos de servicio (IaaS, PaaS, SaaS, DaaS)**  
- **(a) Diferencia cada uno de estos modelos. ¿En qué casos un desarrollador optaría por PaaS en lugar de IaaS?**  

[SaaS vs PaaS vs IaaS vs DaaS](https://www.indeed.com/career-advice/career-development/saas-vs-paas-vs-iaas-vs-daas)

| Modelo | Descripción |
|--------|-------------|
| **IaaS** (Infraestructura como Servicio) | Proporciona recursos de infraestructura bajo demanda a las empresas a través de la nube, como almacenamiento, redes y virtualización. |
| **PaaS** (Plataforma como Servicio) | Proporciona y gestiona todos los recursos de hardware y software para desarrollar aplicaciones a través de la nube. |
| **SaaS** (Software como Servicio) | Proporciona toda la pila de aplicaciones para ofrecer una aplicación completa basada en la nube que los clientes pueden utilizar. |
| **DaaS** (Desktop como Servicio) | Proporciona a usuarios un escritorio virtual y les permite acceder a él desde distintos dispositivos. |


Un desarrollador optaría por PaaS en lugar de IaaS cuando desea enfocarse en el desarrollo y despliegue de aplicaciones sin preocuparse por la gestión de la infraestructura subyacente.

- **(b) Enumera tres ejemplos concretos de proveedores o herramientas que correspondan a cada tipo de servicio.**

| Modelo | Ejemplos |
|--------|-------------|
| **IaaS** (Infraestructura como Servicio) | AWS EC2, Google Compute Engine, Microsoft Azure |
| **PaaS** (Plataforma como Servicio) | Google App Engine, AWS Elastic Beanstalk, Heroku |
| **SaaS** (Software como Servicio) | Google Workspace, Microsoft 365, Salesforce |
| **DaaS** (Desktop como Servicio) | VMware Horizon Cloud, Amazon WorkSpaces, Citrix Virtual Apps and Desktops |

#### **5.Tipos de nubes (Pública, Privada, Híbrida, Multi-Cloud)**  
- **(a) ¿Cuáles son las ventajas de implementar una nube privada para una organización grande?** 

  - Mayor control sobre los datos y la infraestructura.
  - Mejor seguridad y cumplimiento normativo.
  - Rendimiento optimizado.

- **(b) ¿Por qué una empresa podría verse afectada por el “provider lock-in”?**  

[Vendor lock-in](https://www.ionos.com/digitalguide/hosting/technical-matters/vendor-lock-in/)

Porque esto ocurre cuando una empresa depende tanto de un proveeder de nube que le resulta difícil o costoso cambiar a otro. Y esto puede suceder debido a: 
  - Herramientas o servicios que no son compatibles con otros proveedores.
  - Costos elevados de migración.
  - Dependencia de API's específicas que dificultan la migración. 



- **(c) ¿Qué rol juegan los “hyperscalers” en el ecosistema de la nube?**

[What is a hyperscalers cloud?](https://www.digitalocean.com/resources/articles/hyperscaler-cloud)

Los hyperscalers son los grandes proveedores de servicios en la nube que ofrecen infraestructuras y servicios a escala masiva, y el rol que tienen es:

  - Proveer recursos escalables y bajo demanda para distintas empresas dependiente de su tamaño.

  - Innovar constantemente en tecnologías de nube, como IA, big data o machine learning.

  - Reducir costos operativos para las empresas debido a  las economías de escala.

### B. Actividades de investigación y aplicación

#### **1. Estudio de casos**  
   - Busca dos o tres casos de empresas (startups o grandes organizaciones) que hayan migrado parte de su infraestructura a la nube. Describe:

     1. Sus motivaciones para la migración. 
     2. Los beneficios obtenidos (por ejemplo, reducción de costos, escalabilidad, flexibilidad).
     3. Los desafíos o dificultades enfrentadas (ej. seguridad, cumplimiento normativo).

     - [Netflix se muda a la nube](https://about.netflix.com/es/news/completing-the-netflix-cloud-migration)

     - [Airbnb en AWS](https://aws.amazon.com/es/solutions/case-studies/innovators/airbnb/)

     - [Spotify se sube a la nube de Google](https://www.datacenterdynamics.com/es/noticias/spotify-se-sube-a-la-nube-de-google/#:~:text=El%20servicio%20de%20m%C3%BAsica%20en,servicios%20de%20almacenamiento%20de%20Amazon.)

| Empresa  | Motivaciones | Beneficios | Desafíos |
|----------|--------------|------------|----------|
| **Netflix**  | - Necesidad de manejar grandes volúmenes de tráfico globalmente. <br>- Escalabilidad para soportar los picos de demanda.<br>- Reducción de costos y mayor flexibilidad. | - Escalabilidad global para atender millones de usuarios en simultáneo.<br>- Alta disponibilidad y rendimiento optimizado.<br>- Reducción de tiempo en la gestión de la infraestructura. | - Migración de datos y servicios sin interrupciones para los usuarios.<br>- Garantizar la seguridad y protección de los datos de los usuarios. |
| **Airbnb**   | - Necesidad de una infraestructura flexible para manejar la demanda fluctuante de reservas. <br>- Reducción de costos.<br>- Escalabilidad para expandirse a nivel global. | - Capacidad de escalar recursos automáticamente durante temporadas altas.<br>- Reducción de costos operativos al usar un modelo de pago por uso.<br>- Mayor velocidad en el desarrollo y despliegue de nuevas funcionalidades. | - Adaptación de sus sistemas internos a la infraestructura en la nube.<br>- Cumplimiento de normativas locales en diferentes países. |
| **Spotify** | - Necesidad de procesar grandes volúmenes de datos para recomendaciones por usuario.<br>- Escalabilidad para soportar millones de usuarios activos diarios.<br>- Reducción de la complejidad operativa. | - Procesamiento eficiente de datos para mejorar algoritmos de recomendación.<br>- Escalabilidad para manejar el crecimiento de usuarios globalmente.<br>- Mayor agilidad en el desarrollo de nuevas características para la aplicación. | - Migración de datos masivos sin afectar la experiencia del usuario.<br>- Garantizar la seguridad de los datos sensibles de los usuarios. |

   
