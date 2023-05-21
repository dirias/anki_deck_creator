def generate_aws_questions2():
    """
    """
    redes_gobernanza_machine_learning = {
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
        ]
    }
    return redes_gobernanza_machine_learning


