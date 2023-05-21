def aws_cloud_practitioner_data():
    """
    """
    data = {
        "cloud_computing": [
            ("Ahora que conoces más sobre la tecnología en la nube, ¿por qué es importante introducir sus distintos tipos de servicio en la industria para identificar sus diferencias?", "Es importante introducir los distintos tipos de servicio en la industria para identificar sus diferencias y elegir la opción más adecuada según las necesidades de cada negocio. Cada modelo de servicio en la nube ofrece diferentes funcionalidades y ventajas, por lo que conocerlos permitirá tomar decisiones informadas."),
            ("¿Cuáles son los distintos tipos de servicio informático que se pueden ofrecer en la tecnología en la nube?", "Los distintos tipos de servicio informático que se pueden ofrecer en la tecnología en la nube son: Infrastructure as a Service (IAAS), Platform as a Service (PAAS), Software as a Service (SAAS) y On-premises."),
            ("¿En qué consiste Infrastructure as a Service (IAAS)?", "Infrastructure as a Service (IAAS) consiste en proporcionar componentes básicos de IT en la nube, como redes, computación y almacenamiento. Permite una gran flexibilidad para adaptar la infraestructura a las necesidades específicas."),
            ("Menciona algunos ejemplos de servicios IAAS.", "Algunos ejemplos de servicios IAAS son: Azure Virtual Machines, Linode, Digital Ocean y AWS S2."),
            ("¿En qué consiste Platform as a Service (PAAS)?", "Platform as a Service (PAAS) consiste en ofrecer una plataforma para gestionar aplicaciones en la nube, eliminando la necesidad de administrar la infraestructura. Permite centrarse en el desarrollo y despliegue de aplicaciones."),
            ("Menciona algunos ejemplos de servicios PAAS.", "Algunos ejemplos de servicios PAAS son: Heroku, Google App Engine y AWS Elastic Beanstalk."),
            ("¿En qué consiste Software as a Service (SAAS)?", "Software as a Service (SAAS) consiste en brindar un producto de software terminado que es ejecutado y administrado por el proveedor del servicio. Los usuarios acceden al software a través de la nube sin necesidad de instalarlo localmente."),
            ("Menciona algunos ejemplos de servicios SAAS.", "Algunos ejemplos de servicios SAAS son: Amazon Rekognition, Dropbox, Zoom y Gmail."),
            ("¿Qué significa On-premises en el contexto de la tecnología en la nube?", "On-premises se refiere a una forma tradicional de cómputo en la cual nosotros somos responsables de gestionar nuestra propia infraestructura, en lugar de utilizar servicios en la nube."),
            ("¿Cuáles son las responsabilidades según el tipo de cómputo en la nube?", "Las responsabilidades según el tipo de cómputo en la nube pueden variar. En general, cuando utilizamos servicios en la nube, el proveedor se encarga de administrar ciertos componentes de IT, mientras que otros componentes son responsabilidad nuestra. En una tabla, se mostraría qué componentes están administrados por el proveedor (Sí) y cuáles son responsabilidad nuestra (No).")
            
        ],
        "seguridad_e_identidad" : [
            ("¿Qué aspecto es crucial al trasladar aplicaciones a la nube?", "Uno de los aspectos más importantes al trasladar aplicaciones a la nube es la seguridad."),
            ("¿Por qué es importante proteger nuestros datos al trasladar aplicaciones a la nube?", "Es importante proteger nuestros datos contra amenazas para garantizar que los usuarios accedan al sistema y encuentren solo los recursos que necesitan."),
            ("Menciona algunos servicios de protección de datos de AWS.", "Algunos servicios de protección de datos de AWS son: Amazon Macie, AWS Key Management Service, AWS CloudHSM, AWS Certificate Manager y AWS Secrets Manager."),
            ("¿Qué función cumple Amazon Macie?", "Amazon Macie permite descubrir y proteger datos sensibles."),
            ("¿Cuál es la función de AWS Key Management Service?", "AWS Key Management Service almacena y administra claves de cifrado."),
            ("¿En qué consiste AWS CloudHSM?", "AWS CloudHSM proporciona almacenamiento de claves basado en hardware."),
            ("¿Qué ofrece AWS Certificate Manager?", "AWS Certificate Manager provee, administra e implementa certificados SSL/TLS."),
            ("¿Cuál es la función de AWS Secrets Manager?", "AWS Secrets Manager permite trasladar, gestionar y recuperar datos como contraseñas."),
            ("¿Cuáles son algunos servicios de protección de la infraestructura de AWS?", "Algunos servicios de protección de la infraestructura de AWS son: AWS Shield, AWS Web Application Firewall (WAF) y AWS Firewall Manager."),
            ("¿Qué protege AWS Shield?", "AWS Shield protege contra ataques de Denegación de Servicio (DDOS)."),
            ("¿Cuál es la función de AWS Web Application Firewall (WAF)?", "AWS Web Application Firewall (WAF) filtra el tráfico de sitios web maliciosos."),
            ("¿Qué ofrece AWS Firewall Manager?", "AWS Firewall Manager administra las reglas del firewall de forma centralizada."),
            ("¿Cuáles son algunos servicios de detección de amenazas de AWS?", "Algunos servicios de detección de amenazas de AWS son: Amazon GuardDuty, Amazon Inspector, Amazon Config y Amazon CloudTrail."),
            ("¿Qué función cumple Amazon GuardDuty?", "Amazon GuardDuty detecta automáticamente las amenazas."),
            ("¿En qué consiste Amazon Inspector?", "Amazon Inspector analiza la seguridad de la aplicación."),
            ("¿Qué hace Amazon Config?", "Amazon Config registra y evalúa configuraciones de nuestros recursos."),
            ("¿Cuál es la función de Amazon CloudTrail?", "Amazon CloudTrail rastrea la actividad del usuario y el uso de las API en nuestra cuenta."),
            ("¿Cuáles son algunos servicios de gestión de identidad de AWS?", "Algunos servicios de gestión de identidad de AWS son: AWS Identity and Access Management (IAM), AWS Single Sign-On (SSO), Amazon Cognito, AWS Directory Service y AWS Organizations."),
            ("¿Qué permite hacer AWS Identity and Access Management (IAM)?", "AWS Identity and Access Management (IAM) permite administrar de forma segura el acceso a una cuenta, servicios y recursos."),
            ("¿En qué consiste AWS Single Sign-On (SSO)?", "AWS Single Sign-On (SSO) implementa el inicio de sesión único (Single Sign On/SSO)."),
            ("¿Cuál es la función de Amazon Cognito?", "Amazon Cognito permite a los usuarios administrar la identidad dentro de las aplicaciones."),
            ("¿Qué ofrece AWS Directory Service?", "AWS Directory Service implementa y administra un servicio de Directorio Activo (Active Directory Service)."),
            ("¿En qué consiste AWS Organizations?", "AWS Organizations funciona para gobernar y administrar distintas cuentas de AWS de forma centralizada.")
            ("¿Qué es IAM (Identity and Access Management)?", "Identity and Access Management (IAM) es un servicio gratuito que nos ayuda a administrar los accesos a los servicios y recursos de nuestra cuenta en AWS."),
            ("¿Cuáles son los principales componentes de IAM?", "Los principales componentes de IAM son los usuarios y grupos de usuarios."),
            ("¿Qué es un usuario Root en IAM?", "El usuario Root es el usuario proporcionado al crear la cuenta de AWS y tiene acceso a todos los recursos. Puede crear otros perfiles de usuarios con acceso único a distintos recursos."),
            ("¿Qué son las políticas en IAM?", "Las políticas en IAM son utilizadas para establecer permisos de acceso a los recursos. Definen qué acciones están permitidas o denegadas para los usuarios o grupos de usuarios."),
            ("¿Puedes proporcionar un ejemplo de una política que otorga acceso de administrador?", "Sí, aquí tienes un ejemplo de una política de IAM que otorga acceso de administrador:\n\n{\n    \"Version\": \"2012-10-17\",\n    \"Statement\": [\n        {\n            \"Effect\": \"Allow\",\n            \"Action\": \"*\",\n            \"Resource\": \"*\"\n        }\n    ],\n}"),
            ("¿Puedes proporcionar un ejemplo de políticas de acceso a un bucket de S3?", "Sí, aquí tienes un ejemplo de políticas de IAM para acceder a un bucket de S3:\n\n{\n    \"Version\": \"2012-10-17\",\n    \"Statement\": [\n        {\n            \"Effect\": \"Allow\",\n            \"Action\": [\n                \"s3:ListBucket\"\n            ],,\n            \"Resource\": \"arn:aws:s3:::bucket-name\"\n        },\n        {\n            \"Effect\": \"Allow\",\n            \"Action\": [\n                \"s3:GetObject\",\n                \"s3:PutObject\"\n            ],,\n            \"Resource\": \"arn:aws:s3:::bucket-name/*\"\n        }\n    ],\n}"),
            ("¿Qué son los roles en IAM?", "Los roles en IAM permiten asumir identidades y otorgar permisos a otras tecnologías. Por ejemplo, podemos conceder a una máquina virtual el acceso a una base de datos mediante un rol de IAM.")
            ("¿Qué es Secrets Manager de AWS?", "Secrets Manager es un servicio de AWS que nos ayuda a proteger los datos secretos necesarios para acceder a nuestras aplicaciones, servicios y recursos."),
            ("¿Qué tipo de datos secretos puede proteger Secrets Manager?", "Secrets Manager puede proteger contraseñas, claves y tokens necesarios para acceder a diferentes recursos."),
            ("¿Cuál es una ventaja de usar Secrets Manager?", "Una ventaja de usar Secrets Manager es que nos permite compartir automáticamente la información de los secretos cuando sea necesario, evitando tener que copiar y pegar los secretos directamente en nuestro código."),
            ("¿Qué problema resuelve Secrets Manager en relación a la gestión de secretos?", "Secrets Manager resuelve el problema de tener que almacenar y gestionar secretos sensibles de forma segura, ofreciendo un servicio centralizado para su administración y evitando riesgos como la exposición accidental de información confidencial."),
            ("¿Cómo puede ayudar Secrets Manager en el desarrollo de aplicaciones?", "Secrets Manager puede ayudar en el desarrollo de aplicaciones al proporcionar una forma segura de acceder a los secretos necesarios para la autenticación y el acceso a recursos, sin tener que almacenarlos directamente en el código fuente de la aplicación."),
            ("¿Qué otro servicio de AWS se puede integrar con Secrets Manager?", "Secrets Manager se puede integrar con otros servicios de AWS, como Amazon RDS, para proporcionar de forma segura las credenciales necesarias para acceder a bases de datos."),
            ("¿Cómo se pueden gestionar los secretos en Secrets Manager?", "En Secrets Manager, los secretos se pueden gestionar a través de la consola de administración de AWS, la CLI de AWS o mediante API, lo que nos brinda flexibilidad en su gestión y automatización.")

        ],
        "directorios" : [
            ("¿Qué es un directorio en el contexto de la administración de redes?", "Un directorio es una base de datos que contiene información de inicio de sesión de todos los usuarios de una red y puede implementar políticas de seguridad."),
            ("¿Qué es Active Directory de Microsoft?", "Active Directory es un servicio de Microsoft que permite a las empresas gestionar los inicios de sesión de sus empleados y implementar políticas de seguridad."),
            ("¿Qué es AWS Directory Service?", "AWS Directory Service es una oferta de servicio administrado de AWS que permite a los recursos utilizar Active Directory. Ofrece un directorio activo administrado sin necesidad de ejecutar servidores manualmente."),
            ("¿Cuáles son las opciones ofrecidas por AWS Directory Service?", "AWS Directory Service ofrece la opción de directorio activo simple y el conector AD, que permite a los usuarios iniciar sesión en aplicaciones de AWS con sus credenciales. También proporciona un servicio distribuido con tolerancia a fallos que funciona incluso en caso de fallas en los servidores."),
            ("¿Cuáles son las ventajas de utilizar AWS Directory Service?", "Al utilizar AWS Directory Service, se obtiene un directorio activo administrado sin la necesidad de gestionar servidores manualmente. Además, se pueden aprovechar otros servicios de AWS y se garantiza la tolerancia a fallos gracias al servicio distribuido."),
            ("¿El AWS Directory Service es compatible con otros servicios de AWS?", "Sí, el AWS Directory Service es compatible con otros servicios de AWS, lo que permite una integración fluida con el ecosistema de servicios de la plataforma."),
            ("¿Cómo se puede acceder y administrar el AWS Directory Service?", "El AWS Directory Service se puede acceder y administrar a través de la consola de administración de AWS, la CLI de AWS o mediante API, lo que brinda flexibilidad en su gestión y automatización.")
        ],
        "computo" : [
        ("¿Cómo define AWS su capacidad de cómputo?", "AWS define su capacidad de cómputo como 'cómputo para cualquier carga de trabajo'."),
        ("¿Qué son las máquinas virtuales en AWS?", "Las máquinas virtuales en AWS son servicios que proporcionan instancias seguras y redimensionables, como Amazon EC2, Amazon EC2 Spot, Amazon EC2 Auto Scaling y Amazon EC2 LightSail."),
        ("¿Qué son los contenedores en AWS?", "Los contenedores en AWS son unidades de software que empaquetan un software junto con sus dependencias. Los servicios de contenedores en AWS incluyen Amazon Elastic Container Service (ECS), Amazon Elastic Container Registry (ECR) y Amazon Elastic Kubernetes Service (EKS)."),
        ("¿Qué es la computación serverless en AWS?", "La computación serverless en AWS implica que la administración de servidores o máquinas virtuales se delega al proveedor de la nube. Amazon Lambda es un servicio que permite ejecutar código sin preocuparse por la infraestructura subyacente."),
        ("¿Cuáles son los servicios de borde o edge computing en AWS?", "Los servicios de borde o edge computing en AWS incluyen Amazon Outposts, Amazon Snow Family, AWS Wavelength, VMWare AWS y AWS Local Zones."),
        ("¿Cuáles son las ventajas de utilizar máquinas virtuales en AWS?", "Al utilizar máquinas virtuales en AWS, se obtienen instancias seguras y redimensionables que pueden adaptarse a las necesidades de carga de trabajo. Además, servicios como Amazon EC2 Auto Scaling permiten agregar o eliminar automáticamente la capacidad informática según la demanda."),
        ("¿Qué diferencias existen entre máquinas virtuales y contenedores?", "Las máquinas virtuales virtualizan el hardware y ejecutan programas en un sistema operativo simulado, mientras que los contenedores virtualizan el sistema operativo y empacan software junto con sus dependencias."),
        ("¿Cuáles son los servicios de contenedores en AWS?", "Los servicios de contenedores en AWS incluyen Amazon Elastic Container Service (ECS), Amazon Elastic Container Registry (ECR) y Amazon Elastic Kubernetes Service (EKS). Estos servicios permiten ejecutar y administrar contenedores confiables y escalables."),
        ("¿Qué es el Edge Computing en AWS?", "El Edge Computing en AWS se refiere al cómputo y procesamiento de datos en una ubicación cercana a la necesaria para el negocio. Los servicios de borde o edge computing en AWS incluyen Amazon Outposts, Amazon Snow Family, AWS Wavelength, VMWare AWS y AWS Local Zones."),
        ("¿Cómo se puede acceder y administrar los servicios de cómputo en AWS?", "Los servicios de cómputo en AWS se pueden acceder y administrar a través de la consola de administración de AWS, la CLI de AWS o mediante API, brindando flexibilidad en la gestión y automatización.")
    ],
        "servicios_de_computo" : [
            ("Amazon EC2", "Máquinas virtuales seguras y redimensionables."),
            ("Amazon EC2 Spot", "Cargas de trabajo tolerantes a fallas, por hasta el 90% del precio normal. Amazon puede reclamar estas instancias en cualquier momento con solo dos minutos de anticipación."),
            ("Amazon EC2 AutoScaling", "Agrega o elimina automáticamente la capacidad informática para satisfacer tus necesidades bajo demanda."),
            ("Amazon EC2 LightSail", "Plataforma en la nube fácil de usar para crear una aplicación o un sitio web."),
            ("Amazon Elastic Container Services (ECS)", "Servicio para correr contenedores confiables y escalables."),
            ("Amazon Elastic Container Registry (ECR)", "Servicio para almacenar, administrar e implementar imágenes de contenedores."),
            ("Amazon Elastic Kubernetes Service (EKS)", "Servicio de Kubernetes administrado por AWS."),
            ("Amazon Outposts", "Permite ejecutar los servicios de AWS en nuestros propios servidores en lugar de Amazon."),
            ("Amazon Snow Family", "Familia de dispositivos desde un disco duro portátil hasta un semi-remolque completo lleno de discos de almacenamiento. Estos dispositivos te permiten cargar archivos en ellos, para luego ser enviados a Amazon y cargados en sus servidores."),
            ("AWS Wavelength", "Permite acceder a los servicios AWS desde dispositivos 5G sin pasar por Internet."),
            ("VMWare AWS", "Permite migrar cargas de trabajo de VMWare a AWS."),
            ("AWS Local Zones", "Permite ejecutar las aplicaciones más cerca de los usuarios finales, a una menor latencia.")
        ],

        "EC2" : [
        ("¿Qué es EC2?", "EC2 es un servicio de AWS que permite alquilar máquinas virtuales, llamadas instancias EC2, para ejecutar aplicaciones y realizar tareas de cómputo en la nube."),
        ("¿Qué opciones ofrece EC2 en términos de tipos de instancias?", "EC2 ofrece diferentes tipos de instancias con características de CPU, RAM y almacenamiento variables. Puedes elegir instancias optimizadas para cómputo, memoria, almacenamiento y otras necesidades específicas."),
        ("¿Cómo se realiza el pago en EC2?", "El sistema de pago más común en EC2 es por hora o por segundo, dependiendo del tipo de instancia que elijas. El costo se calcula por el tiempo de uso de la instancia."),
        ("¿Cómo funciona el sistema de pago por hora en EC2?", "Si tienes una instancia que cuesta $0.1 por hora, puedes pagar por una instancia durante 24 horas y se te cobrará $2.4 en total. En este caso, el costo se mantiene constante independientemente de cuántas instancias utilices dentro de ese período de tiempo."),
        ("¿Qué ocurre si elijo pagar por segundo en EC2?", "Si el tipo de instancia admite el pago por segundo, el costo se calcula en función de los segundos reales de uso. Esto proporciona una mayor flexibilidad y precisión en el pago.")
    ],

        "contenedores" : [
            ("¿Cuál es el propósito de un contenedor?", "El propósito de un contenedor es crear un paquete que incluya tu programa, librerías y dependencias con versiones específicas. Esto permite ejecutar el programa en cualquier máquina sin preocuparse por las diferencias en las configuraciones del entorno."),
            ("¿Qué problema resuelve Docker?", "Docker resuelve el problema de gestionar y trabajar con diferentes versiones de librerías, lenguajes de programación y programas. Al utilizar contenedores, puedes encapsular tus aplicaciones con todas sus dependencias en una imagen que se puede ejecutar de manera consistente en diferentes entornos."),
            ("¿Qué es Amazon ECS?", "Amazon ECS (Elastic Container Service) es un servicio de contenedores proporcionado por AWS. Te permite implementar tus imágenes de contenedores en la nube de AWS. Al utilizar ECS, tus contenedores se ejecutan en el entorno de AWS sin diferencias significativas respecto a tu máquina local."),
            ("¿Cuáles son las ventajas de utilizar Amazon ECS?", "Al utilizar Amazon ECS, puedes aprovechar la escalabilidad y la flexibilidad de la nube de AWS para ejecutar tus contenedores. También se beneficia de la integración con otros servicios de AWS, como la gestión de clústeres, el balanceo de carga y la autoescalabilidad."),
        ],
        "aws_lambda" : [
        ("¿Qué es AWS Lambda?", "AWS Lambda es un servicio serverless que permite ejecutar código en respuesta a eventos sin preocuparse por la infraestructura subyacente. Puede responder a eventos como temporizadores, visitas a secciones de una aplicación o solicitudes HTTP."),
        ("¿Cuáles son los casos de uso comunes de AWS Lambda?", "AWS Lambda se utiliza comúnmente para el (pre)procesamiento de datos a escala y la ejecución de backends web, móviles e IoT interactivos. También se combina con otros servicios de AWS para crear experiencias en línea seguras, estables y escalables."),
        ("¿Cómo se factura AWS Lambda?", "AWS Lambda se factura por milisegundos de tiempo de ejecución y el costo varía según la cantidad de memoria asignada. Por ejemplo, si asignas 128 MB de RAM y tienes 30 millones de eventos al mes, el costo sería de $11.63 al mes."),
    ],
    "Almacenamiento" : [
        ("¿Qué es el almacenamiento de datos en la nube?", "El almacenamiento de datos en la nube consiste en subir tus datos a una red de servidores remotos, donde se te proporcionan herramientas para acceder a ellos de diferentes maneras."),
        ("¿Cuáles son los tipos de almacenamiento de datos en AWS?", "En AWS, existen tres tipos principales de almacenamiento de datos: basado en archivos, bloque y objetos. El almacenamiento basado en archivos organiza los datos en carpetas y subcarpetas, y servicios como Amazon EFS y Amazon FSx for Windows File Server pertenecen a esta categoría. El almacenamiento bloque almacena los datos en volúmenes como fragmentos de datos de igual tamaño, y Amazon EBS es un ejemplo de este tipo de almacenamiento. El almacenamiento de objetos almacena la información como objetos únicos con identificadores y utiliza un modelo de memoria plana, y Amazon S3 es un servicio de almacenamiento de objetos en AWS."),
        ("¿Qué es Amazon Backup?", "Amazon Backup es un servicio de AWS que administra y automatiza las copias de seguridad de forma centralizada en los servicios de AWS. Permite programar y realizar copias de seguridad de los datos almacenados en diferentes servicios y recuperarlos cuando sea necesario."),
        ("¿Qué es AWS Storage Gateway?", "AWS Storage Gateway es un conjunto de servicios de almacenamiento en la nube híbrida que proporciona acceso en las instalaciones al almacenamiento en la nube. Permite a las organizaciones integrar sus entornos locales con el almacenamiento en la nube de AWS, permitiendo el intercambio y la migración de datos de manera eficiente."),
        ("¿Qué es AWS DataSync?", "AWS DataSync es un servicio de AWS que acelera el traslado de datos desde y hacia AWS hasta diez veces más rápido de lo normal. Permite transferir grandes cantidades de datos de forma rápida y segura entre ubicaciones locales y servicios de almacenamiento en la nube de AWS."),
        ("¿Qué es AWS Transfer Family?", "AWS Transfer Family es un servicio de AWS que escala de forma segura las transferencias recurrentes de archivos entre Amazon S3, Amazon EFS y tus propios servidores utilizando los protocolos FTP, SFTP y FTPS. Proporciona una forma sencilla y segura de transferir archivos hacia y desde la nube de AWS."),
        ("¿Cuáles son los servicios de transferencia de datos de AWS?", "AWS ofrece varios servicios de transferencia de datos, incluyendo: AWS Storage Gateway, que proporciona acceso en las instalaciones al almacenamiento en la nube; AWS DataSync, que acelera el traslado de datos hacia y desde AWS; y AWS Transfer Family, que permite escalar de forma segura las transferencias de archivos utilizando los protocolos FTP, SFTP y FTPS con Amazon S3 y Amazon EFS."),
    ],
    "s3_and_s3_glacer" : [
        ("¿Qué características tiene S3 Standard?", "Almacenamiento de objetos de alta durabilidad, disponibilidad y rendimiento para datos a los que se obtiene acceso con frecuencia."),
        ("¿Cuándo se utiliza S3 Standard-IA?", "Se utiliza con datos a los que se accede con menos frecuencia, pero que requieren un acceso rápido cuando es necesario."),
        ("¿En qué se diferencia S3 Zone-IA de las demás clases de almacenamiento de S3?", "S3 Zone-IA almacena datos en una única zona de disponibilidad, a diferencia de las demás clases que utilizan un mínimo de tres zonas de disponibilidad."),
        ("¿Cuál es el propósito de S3 Glacier?", "S3 Glacier ofrece el almacenamiento de menor costo para los datos de larga duración y acceso poco frecuente. Tiene opciones de recuperación de datos estándar, masiva y acelerada."),
        ("¿Cuál es la principal característica de S3 Glacier Deep Archive?", "S3 Glacier Deep Archive es la clase de almacenamiento más económica de Amazon S3, diseñada para la retención a largo plazo y la conservación digital de datos a los que se accede una o dos veces al año."),
        ("¿Qué ofrece S3 Intelligent-Tiering?", "S3 Intelligent-Tiering es un tipo de almacenamiento que intenta ahorrar costos moviendo archivos entre los distintos tipos de almacenamiento S3, basado en los patrones de uso de los archivos.")
    ],

    "EFS" : [
        ("Amazon Elastic File System (EFS)", "Es un sistema de archivos elástico, sencillo, sin servidor y práctico basado en NFS para las máquinas virtuales de EC2."),
        ("NFS", "Es un protocolo de archivos en red que permite acceder a archivos y directorios que no están en tu sistema. Esto permite que miles de máquinas puedan conectarse a EFS y procesar los datos que allí se encuentran.")
        ("¿Qué características ofrece EFS?", "EFS es altamente disponible y duradero. Provee protección contra una interrupción de la zona de disponibilidad, replicando los archivos en múltiples zonas dentro de una región."),
        ("¿Cuáles son las dos clases de almacenamiento que brinda EFS?", "EFS brinda las clases de almacenamiento 'Standard' y 'Standard IA' (para acceso poco frecuente)."),
        ("¿Qué puedes implementar en EFS en relación a las políticas de almacenamiento?", "Puedes implementar políticas para que tus archivos se muevan de 'Standard' a 'Standard IA' después de cierto tiempo."),
        ("¿Cómo se encriptan los datos en EFS?", "Los datos en EFS se encriptan de manera automática.")
    ],
    "storage_gateway" : [
        ("AWS Storage Gateway", "Es un servicio que brinda acceso a almacenamiento en la nube prácticamente ilimitado desde tu propia infraestructura."),
        ("File Gateway", "Es una puerta de acceso de AWS Storage Gateway que provee interfaces SMB y NFS para Amazon S3, permitiendo verlo como un sistema de archivos montado en los sistemas operativos Windows y Linux."),
        ("Tape Gateway", "Es una puerta de acceso de AWS Storage Gateway que permite migrar copias de seguridad en cintas físicas a una biblioteca de cintas virtuales en AWS, almacenando los contenidos en S3."),
        ("Volume Gateway", "Es una puerta de acceso de AWS Storage Gateway que otorga almacenamiento en bloque respaldado en la nube con protocolo iSCSI, permitiendo almacenar datos en S3 en dos modos: caché y almacenado.")
        ("¿Qué ofrece File Gateway de AWS Storage Gateway?", "File Gateway provee interfaces SMB y NFS para Amazon S3, permitiendo verlo como un sistema de archivos montado en los sistemas operativos Windows y Linux."),
        ("¿Qué permite hacer Tape Gateway de AWS Storage Gateway?", "Tape Gateway permite migrar copias de seguridad en cintas físicas a una biblioteca de cintas virtuales en AWS, almacenando los contenidos en S3."),
        ("¿Cuáles son los modos de almacenamiento disponibles en Volume Gateway?", "Los modos de almacenamiento disponibles en Volume Gateway son caché (almacenamiento principal en S3 y datos de acceso frecuente en caché local) y almacenado (todos los datos se guardan localmente con copias de seguridad asíncronas en S3).")
    ],
    "bases_de_datos" : [
        ("Bases de datos relacionales", "Son servicios de bases de datos que se centran en el almacenamiento y gestión de datos estructurados. En AWS, los servicios de bases de datos relacionales incluyen Amazon Aurora, Amazon RDS y Amazon Redshift."),
        ("Amazon Aurora", "Es una base de datos relacional compatible con MySQL y PostgreSQL creada para la nube."),
        ("Amazon RDS", "Es un servicio de bases de datos relacionales administrado que facilita la configuración, el uso y el escalado de varios motores de bases de datos, como MySQL, PostgreSQL, MariaDB, Oracle BYOL y SQL Server."),
        ("Amazon Redshift", "Es una base de datos ideal para analítica que utiliza SQL para analizar datos estructurados y semiestructurados en diferentes almacenamientos y bases de datos, ofreciendo un rendimiento óptimo a cualquier escala."),
        ("Bases de datos clave-valor", "Son bases de datos que almacenan datos en pares clave-valor. En AWS, el servicio clave-valor es Amazon DynamoDB."),
        ("Amazon DynamoDB", "Es una base de datos de documentos y valores clave que ofrece un rendimiento rápido a cualquier escala, dirigida a aplicaciones de alto tráfico y sistemas en tiempo real."),
        ("Bases de datos en memoria", "Son bases de datos que almacenan datos en memoria para un acceso más rápido. En AWS, los servicios de bases de datos en memoria incluyen Amazon ElastiCache para Memcached y Amazon ElastiCache para Redis."),
        ("Amazon ElastiCache", "Es un servicio de almacenamiento de caché en memoria completamente administrado que admite casos de uso en tiempo real y flexible, utilizado para almacenar en caché datos como la administración de sesiones, tablas de clasificación de juegos y aplicaciones Geo-Espaciales."),
        ("Bases de datos basadas en documentos", "Son bases de datos que almacenan datos en forma de documentos. En AWS, el servicio de base de datos basada en documentos es Amazon DocumentDB."),
        ("Amazon DocumentDB", "Es un servicio de base de datos de larga duración, rápida y escalable para operar cargas de trabajo de MongoDB esenciales, utilizado en casos de uso como la gestión de contenidos, catálogos y perfiles de usuario.")
        ("¿Qué es Amazon Aurora?", "Amazon Aurora es una base de datos relacional compatible con MySQL y PostgreSQL creada para la nube."),
        ("¿Cuál es el objetivo principal de Amazon Redshift?", "El objetivo principal de Amazon Redshift es permitir el análisis de datos estructurados y semiestructurados a cualquier escala, utilizando SQL."),
        ("¿Qué tipos de bases de datos se encuentran en Amazon ElastiCache?", "Amazon ElastiCache ofrece dos tipos de bases de datos en memoria: ElastiCache para Memcached y ElastiCache para Redis."),
        ("¿Cuál es el caso de uso principal de Amazon DynamoDB?", "Amazon DynamoDB es utilizado principalmente en aplicaciones de web de alto tráfico, sistemas de comercio electrónico y aplicaciones de juego."),
        ("¿Cuál es el caso de uso común de Amazon DocumentDB?", "Un caso de uso común de Amazon DocumentDB es la gestión de contenidos, catálogos y perfiles de usuario en aplicaciones.")
        ("Amazon RDS", "Es un servicio de AWS que permite crear, ejecutar y administrar bases de datos relacionales en la nube. Proporciona diferentes motores de bases de datos y facilita la configuración y escalabilidad de las bases de datos relacionales."),
        ("Bases de datos relacionales", "Son bases de datos en las que los datos almacenados tienen relaciones entre sí. Utilizan un lenguaje de consulta llamado SQL (Structured Query Language) para consultar y manipular los datos."),
        ("Motores de bases de datos relacionales en Amazon RDS", "Amazon RDS ofrece varios motores de bases de datos relacionales, incluyendo MySQL, MariaDB, PostgreSQL, Oracle, SQL Server y Amazon Aurora. Estos motores proporcionan diferentes opciones y características para las bases de datos relacionales en la nube.")
        ("¿Qué es Amazon RDS?", "Amazon RDS es un servicio de AWS que permite crear, ejecutar y administrar bases de datos relacionales en la nube."),
        ("¿Qué caracteriza a las bases de datos relacionales?", "Las bases de datos relacionales se caracterizan por tener datos almacenados con relaciones entre sí y utilizar el lenguaje de consulta SQL."),
        ("¿Cuáles son los motores de bases de datos relacionales disponibles en Amazon RDS?", "Los motores de bases de datos relacionales disponibles en Amazon RDS son MySQL, MariaDB, PostgreSQL, Oracle, SQL Server y Amazon Aurora.")
        ("¿Qué facilita Amazon RDS?", "Amazon RDS facilita la configuración de bases de datos relacionales en la nube."),
        ("¿Qué ofrece escalabilidad en Amazon RDS?", "Amazon RDS es altamente escalable y puede utilizarse en múltiples zonas de disponibilidad."),
        ("¿Qué permite crear Amazon RDS?", "Amazon RDS permite crear réplicas de bases de datos de solo lectura."),
        ("¿Qué realiza Amazon RDS de manera automática?", "Amazon RDS realiza copias de seguridad automáticas de las bases de datos."),
        ("¿Cómo se realiza el pago en Amazon RDS?", "En Amazon RDS se paga únicamente por lo que se utiliza, siguiendo un modelo de pago por uso.")
        ("¿Qué tipo de base de datos es DynamoDB?", "DynamoDB es una base de datos NoSQL de documentos clave-valor."),
        ("¿Qué tipo de rendimiento ofrece DynamoDB?", "DynamoDB ofrece un rendimiento en milisegundos de un solo dígito."),
        ("¿Cuál es uno de los casos de uso de DynamoDB?", "Uno de los casos de uso de DynamoDB es el manejo de datos actualizados en tiempo real."),
        ("¿Qué tipo de estructura tiene una base de datos clave-valor?", "Una base de datos clave-valor almacena datos en forma de claves y valores/atributos."),
        ("¿Qué características pueden tener los atributos en DynamoDB?", "Los atributos en DynamoDB pueden tener diferentes tipos y valores para cada clave.")
        ("¿Qué tipo de servicio es DynamoDB?", "DynamoDB es un servicio completamente administrado (PAAS)."),
        ("¿En cuántas regiones funciona DynamoDB?", "DynamoDB funciona en múltiples regiones."),
        ("¿Cuántas solicitudes por segundo puede manejar DynamoDB?", "DynamoDB puede manejar hasta 20 millones de solicitudes por segundo."),
        ("¿Qué funcionalidades de seguridad tiene DynamoDB?", "DynamoDB cuenta con seguridad, respaldo y restauración integrados.")
        ("¿Qué es Amazon ElastiCache?", "Amazon ElastiCache es un servicio de almacenamiento en memoria 100% administrado que admite casos de uso flexibles y en tiempo real."),
        ("¿Qué función cumple una base de datos en memoria?", "Una base de datos en memoria almacena datos a los que se ha accedido previamente en memoria caché, mejorando la rapidez de acceso a esos datos."),
        ("¿Por qué es más rápido consultar datos en caché que consultar directamente la base de datos?", "Consultar datos en caché es más rápido debido a que la memoria tiene un acceso más rápido que los dispositivos de almacenamiento persistente, como los discos."),
        ("¿Puedes dar un ejemplo de caso de uso de ElastiCache?", "Un ejemplo de uso de ElastiCache es un sitio de noticias al cual se accede miles de veces al día. Al mantener los artículos en una base de datos en memoria, el acceso a ellos se vuelve mucho más rápido."),
        ("¿Cuáles son los dos motores de ElastiCache?", "Los dos motores de ElastiCache son Redis y Memcached."),
        ("¿Qué capacidades de autoscaling tiene ElastiCache?", "ElastiCache se monitorea a sí mismo continuamente y puede escalar hacia arriba o hacia abajo en función de la demanda de la aplicación.")
    ],
        "conceptos": [
            ("Amazon Virtual Private Cloud (Amazon VPC)", "Permite definir y aprovisionar una red privada para nuestros recursos de AWS."),
            ("AWS Transit Gateway", "Permite conectar VPC con los recursos locales (on-premises) mediante un hub central."),
            ("AWS PrivateLink", "Proporciona conectividad privada entre las VPC y aplicaciones locales, sin exponer el tráfico al Internet público."),
            ("Amazon Route 53", "Permite alojar nuestro propio DNS administrado."),
            ("Elastic Load Balancing", "Permite distribuir automáticamente el tráfico de red a través de un grupo de recursos, con el fin de mejorar la escalabilidad."),
            ("AWS Global Accelerator", "Redirige el tráfico a través de la red global de AWS para mejorar el rendimiento de las aplicaciones globales."),
            ("Amazon CloudFront", "Entrega de forma segura datos, videos y aplicaciones a clientes de todo el mundo con baja latencia.")
        ],
        "amazon_vpc_conceptos": [
            ("¿Para qué sirve Amazon VPC?", "Amazon VPC permite crear una red virtual para poder conectarnos a todos los servicios de AWS que existan en un rango de direcciones IP locales (por ejemplo, 10.0.0.0/24, que representa del rango de IP entre 10.0.0.0 y 10.0.0.255). Esta red virtual será como una pequeña comunidad cerrada para nuestras máquinas virtuales y todos los servicios que tengamos dentro de AWS."),
            ("¿Cuáles son los componentes de Amazon VPC?", "Amazon VPC posee los siguientes componentes para controlar el tráfico interno y externo de nuestras VPC:\n1. Nat Gateway: si deseamos que nuestras máquinas virtuales puedan acceder a internet, debemos utilizar este componente.\n2. Internet Gateway: permite que Internet pueda acceder a nuestra instancia de EC2.\n3. ACL Control List: controla el tráfico que vamos a permitir dentro y fuera de la VPC."),
            ("¿Qué componente de Amazon VPC se utiliza para permitir que las máquinas virtuales accedan a Internet?", "Nat Gateway"),
            ("¿Cuál es el componente de Amazon VPC que permite que Internet pueda acceder a las instancias de EC2?", "Internet Gateway"),
            ("¿Qué componente de Amazon VPC se utiliza para controlar el tráfico permitido dentro y fuera de la VPC?", "ACL Control List")
        ],
        "elasti_cache_conceptos" : [
            ("¿Cuál es la función de ElastiCache?", "ElastiCache almacena en memoria caché las solicitudes a la base de datos para evitar consultar la base de datos cada vez que se necesite acceder a información."),
            ("¿Dónde se ubica ElastiCache en la arquitectura?", "ElastiCache se ubica entre el sitio web y la base de datos."),
        ],
        "cloudfront_conceptos" : [
            ("¿Cuál es la función de CloudFront?", "CloudFront entrega datos, aplicaciones y sitios web en todo el mundo con baja latencia, actuando como un servicio intermedio entre el navegador o cliente y el sitio web."),
            ("¿Qué son las edge locations de CloudFront?", "Las edge locations son múltiples ubicaciones en el mundo desde las cuales CloudFront puede servir contenido, permitiendo una entrega rápida y eficiente."),
        ],
        "casos_uso_cloudfront" : [
            ("¿Cuál es el caso de uso de CloudFront?", "CloudFront se utiliza para almacenar en caché archivos y entregar contenido estático a los clientes desde ubicaciones de borde cercanas."),
            ("¿Cómo funciona la entrega de contenido en CloudFront?", "CloudFront redirige automáticamente la solicitud de archivo desde la edge location más cercana, y si el archivo está en caché, lo entrega directamente; de lo contrario, lo obtiene del servidor de origen."),
        ],
        "caracteristicas_cloudfront" : [
            ("¿Qué características ofrece CloudFront en términos de seguridad?", "CloudFront ofrece protección contra ataques DDOS y picos de tráfico, ya que los primeros servidores en recibir estos ataques son los de CloudFront y no los tuyos."),
            ("¿Qué permite hacer CloudFront con las ubicaciones de borde?", "CloudFront permite ejecutar funciones de AWS Lambda en las ubicaciones de borde, lo que brinda mayor flexibilidad en el procesamiento de las solicitudes."),
            ("¿Qué ventajas ofrece CloudFront en términos de métricas y costos?", "CloudFront proporciona múltiples métricas en tiempo real y es una solución rentable para la entrega de contenido."),
        ],
        "dns_concepto" : [
            ("¿Qué es DNS?", "DNS es un sistema que asigna direcciones IP a nombres de dominio."),
        ],
        "route53_concepto" : [
            ("¿Qué es Route 53?", "Route 53 es un servicio de alojamiento de DNS proporcionado por AWS."),
            ("¿Cuál es el costo de Route 53?", "Route 53 tiene un costo de $0.5 por nombre de dominio por mes."),
        ],
        "politicas_enrutamiento" : [
            ("¿Qué es el ruteo simple?", "El ruteo simple es una política de enrutamiento que utiliza el servicio de DNS estándar y enruta el tráfico hacia un recurso específico."),
            ("¿En qué consiste la política ponderada?", "La política ponderada permite asociar múltiples recursos con un solo nombre de dominio y determinar la cantidad de tráfico que se dirige a cada recurso en función de un número del 0 al 255."),
            ("¿Qué ofrece la política de geolocalización?", "La política de geolocalización permite servir contenido específico y restringir la distribución según la ubicación geográfica de los usuarios."),
            ("¿Cuál es el objetivo de la política de latencia?", "La política de latencia busca entregar los recursos desde la región de AWS más cercana a la ubicación del usuario para reducir el tiempo de respuesta."),
            ("¿En qué consiste la política de conmutación por error?", "La política de conmutación por error redirige el tráfico a un recurso alternativo cuando el recurso principal no está disponible."),
            ("¿Qué permite la política de respuesta de múltiples valores?", "La política de respuesta de múltiples valores permite devolver varios valores en respuesta a las consultas de DNS, mejorando la disponibilidad y el equilibrio de la carga."),
        ],
        "caracteristicas_route53" : [
            ("¿Qué características tiene Route 53?", "Route 53 es rentable, seguro, escalable y ofrece distintas opciones de enrutamiento para diferentes casos."),
        ],
        "dmin_cuentas_concepto" : [
            ("¿Qué es AWS Control Tower?", "AWS Control Tower es una solución que facilita la configuración y gobernanza de un entorno seguro de AWS con múltiples cuentas."),
            ("¿Qué es AWS Organizations?", "AWS Organizations es un servicio que permite gobernar y administrar de manera centralizada entornos en varias cuentas de AWS."),
            ("¿Qué proporciona AWS Budgets?", "AWS Budgets ayuda en la planificación y control de costos en AWS."),
        ],
        "aprovisionamiento_concepto" : [
            ("¿Qué es AWS CloudFormation?", "AWS CloudFormation permite modelar y aprovisionar recursos de AWS mediante código."),
            ("¿Qué es AWS OpsWorks?", "AWS OpsWorks ayuda a automatizar las operaciones utilizando herramientas como Chef y Puppet."),
            ("¿Qué ofrece AWS Service Catalog?", "AWS Service Catalog permite crear, organizar y gobernar un catálogo curado de productos de AWS en toda la organización."),
            ("¿Qué encontramos en el Marketplace de AWS?", "El Marketplace de AWS es un lugar donde se puede encontrar, probar e implementar software que se ejecuta en AWS."),
        ],
        "operar_entorno_concepto" : [
            ("¿Qué proporciona Amazon CloudWatch?", "Amazon CloudWatch permite observar servicios de AWS mediante métricas y registros."),
            ("¿Qué permite Amazon Config?", "Amazon Config permite registrar y evaluar las configuraciones de recursos en AWS."),
            ("¿Qué hace AWS CloudTrail?", "AWS CloudTrail rastrea toda la actividad del usuario en la cuenta de AWS para fines de seguridad e investigación."),
            ("¿Qué ofrece Systems Manager?", "Systems Manager optimiza el rendimiento y la seguridad al administrar un gran número de sistemas."),
            ("¿Qué hace Amazon X-Ray?", "Amazon X-Ray se utiliza para analizar y depurar aplicaciones en producción."),
        ],
        "cloudformation_concepto" : [
            ("¿Qué es CloudFormation?", "CloudFormation es un servicio de AWS que permite provisionar servicios y recursos mediante código."),
            ("¿Qué son las CloudFormation Templates?", "Las CloudFormation Templates son plantillas en formato JSON o YAML donde se especifican los recursos a desplegar."),
            ("¿Qué se define en una plantilla de CloudFormation?", "En una plantilla de CloudFormation se define un stack o pila de recursos a provisionar."),
        ],
        "beneficios_cloudformation" : [
            ("¿Cuál es el beneficio del control de versiones en CloudFormation?", "El control de versiones permite mantener un historial completo de los recursos en un solo archivo y facilita la colaboración en el despliegue de la infraestructura."),
            ("¿Cómo ayuda CloudFormation en la automatización de la creación de infraestructura?", "CloudFormation permite automatizar la creación de infraestructura y recursos en AWS, lo que agiliza las tareas de los encargados de DevOps."),
            ("¿Cómo se logra la escala con CloudFormation?", "Gracias a las plantillas de CloudFormation, es posible replicar la infraestructura en distintas cuentas de AWS y regiones ajustando los parámetros necesarios."),
        ],
        "cloudwatch_concepto" : [
            ("¿Qué es CloudWatch?", "CloudWatch es un servicio de AWS diseñado para la supervisión y observabilidad de los servicios en una cuenta de AWS."),
            ("¿Cuál es la función principal de CloudWatch?", "La función principal de CloudWatch es recopilar métricas y datos de servicios, integrándose con más de 80 servicios de AWS."),
            ("¿Qué ofrece CloudWatch en términos de métricas?", "CloudWatch ofrece métricas predefinidas y la posibilidad de recopilar y desplegar datos en una vista unificada con gráficos."),
            ("¿Qué se puede hacer con CloudWatch Logs?", "CloudWatch Logs permite enviar archivos de registro y buscar datos de manera interactiva, lo que facilita la detección y resolución de problemas."),
        ],
        "cloudwatch_caso_uso" : [
            ("¿Cuál es un caso de uso de CloudWatch?", "Un caso de uso de CloudWatch es monitorear intentos de inicio de sesión fallidos en una máquina virtual mediante el envío de los logs de inicio de sesión a CloudWatch y configurar una alarma para alertar sobre intentos fallidos que superen un límite definido."),
        ],
        "autoscaling_concepto" : [
            ("¿Qué es el autoescalamiento (autoscaling)?", "El autoescalamiento es una funcionalidad que permite escalar automáticamente la capacidad de las instancias de máquinas virtuales de acuerdo con las condiciones definidas."),
            ("¿Cuál es la ventaja del autoescalamiento?", "El autoescalamiento proporciona alta disponibilidad, tolerancia a fallos y ahorro de costos al aumentar o disminuir la cantidad de instancias en ejecución según la demanda."),
            ("¿Qué pasos se deben seguir para aplicar el autoescalamiento?", "Para aplicar el autoescalamiento, se deben crear un grupo de autoescalamiento que asocie las instancias, especificar un tamaño mínimo y una capacidad deseada, y agregar instancias adicionales según sea necesario hasta alcanzar un máximo."),
            ("¿Qué servicios en AWS implementan el autoescalamiento?", "Además de EC2, los servicios DynamoDB y Aurora también implementan el autoescalamiento."),
        ],
        "autoscaling_load_balancer" : [
            ("¿Qué rol juega el Load Balancer en el autoescalamiento?", "El Load Balancer de AWS permite distribuir automáticamente las conexiones a medida que las instancias aparecen y desaparecen, lo cual es fundamental para el funcionamiento efectivo del autoescalamiento."),
        ],
        "Amazon_recognition" : [
            ('¿Qué es Amazon Rekognition?', 'Amazon Rekognition es un servicio de AWS que permite analizar imágenes y videos mediante aprendizaje automático, devolviendo una lista de elementos detectados en la imagen y su porcentaje de confianza.'),
            ('¿Cuál es un caso de uso común de Amazon Rekognition?', 'Un caso de uso común de Amazon Rekognition es detectar imágenes con contenido para adultos o violento, para moderar el contenido que se sube en una plataforma.'),
            ('¿Cómo se explora Amazon Rekognition?', 'Para explorar Amazon Rekognition, se inicia sesión en AWS y se accede a la página de Rekognition. Luego, en la sección de Demos, se elige la opción de "Celebrity recognition" para reconocer celebridades en una imagen.'),
            ('¿Qué características devuelve Amazon Rekognition?', 'Además de la lista de elementos detectados en la imagen y su porcentaje de confianza, Amazon Rekognition devuelve un objeto Response que contiene características adicionales de la imagen, como la posición de los actores y un estimado de los sentimientos expresados en sus caras.'),
        ],
        "Amazon_polly" : [
            ('¿Qué es Amazon Polly?', 'Amazon Polly es un servicio de AWS que utiliza síntesis de voz avanzada para generar discursos realistas a partir de texto.'),
            ('¿Cómo se utiliza Amazon Polly?', 'Para utilizar Amazon Polly, se proporciona texto como entrada y se obtiene una respuesta de audio con el discurso generado.'),
            ('¿Qué configuraciones de voz ofrece Amazon Polly?', 'Amazon Polly ofrece una variedad de voces y estilos que se pueden personalizar para adaptarse a diferentes necesidades de discurso.'),
            ('¿En qué formatos se puede obtener el discurso generado por Amazon Polly?', 'Amazon Polly puede generar el discurso en varios formatos, como MP3 o PCM, lo que brinda flexibilidad en la reproducción y uso del audio.'),
            ('¿Cómo se integra Amazon Polly con aplicaciones y servicios?', 'Amazon Polly proporciona una API fácil de usar para integrar el servicio en aplicaciones y servicios existentes, lo que permite generar discursos realistas de manera programática.'),
            ('¿Cuáles son los beneficios de utilizar Amazon Polly?', 'Algunos de los beneficios de Amazon Polly incluyen la generación de voces naturales y realistas, la escalabilidad para satisfacer demandas de cualquier tamaño y la flexibilidad en la personalización del discurso.'),
            ('¿Es fácil de usar Amazon Polly?', 'Sí, Amazon Polly es fácil de usar. Proporciona documentación completa y herramientas claras para facilitar su integración y uso.'),
            ('¿Qué idiomas admite Amazon Polly?', 'Amazon Polly admite una amplia cobertura de idiomas y acentos, lo que permite generar discursos en diferentes contextos y regiones.'),
        ],
        "Amazon_transcribe" : [
            ('¿Qué es Amazon Transcribe?', 'Amazon Transcribe es un servicio de AWS que permite crear transcripciones de voz a texto de calidad para diversos casos de uso, como accesibilidad.'),
            ('¿Cómo podemos usar Amazon Transcribe?', 'Podemos usar Amazon Transcribe explorando las opciones y casos de uso en la página del servicio. También podemos probar el servicio creando una transcripción haciendo clic en "Create a transcript".'),
            ('¿Cómo se realiza una transcripción en tiempo real con Amazon Transcribe?', 'Para realizar una transcripción en tiempo real con Amazon Transcribe, en la página del servicio seleccionamos el lenguaje deseado y hacemos clic en "Start streaming". Luego, otorgamos el permiso al navegador para usar el micrófono y comenzamos a hablar, viendo cómo nuestro discurso se transcribe en tiempo real. Para detener la transcripción, simplemente damos clic en "Stop streaming".')
        ],
    }
    return data


