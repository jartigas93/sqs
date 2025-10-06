# SQS Python — Producer & Consumer (sin Dockerfile)

Pequeño proyecto de **portfolio** en Python que muestra un flujo asincrónico _Producer → Queue → Consumer_ utilizando **Amazon SQS** a través de `boto3`. El objetivo es mantener una arquitectura modular (con un paquete `App/`) y ejecutar **localmente** (sin Dockerfile), con soporte para **AWS real** u **opcionalmente LocalStack**.

---

## 🧱 Estructura del proyecto

```
sqs/
├── App/
│   ├── Consumer/
│   │   ├── __init__.py
│   │   └── consumer.py
│   ├── Producer/
│   │   ├── __init__.py
│   │   └── producer.py
│   └── functions/
│       ├── __init__.py
│       └── functions.py
├── requirements.txt
└── README.md
```

> Nota: los módulos importan como `from App.functions import functions as fn`, por eso es **importante ejecutar con `python -m` desde la raíz** del repo.

---

## 🚀 Quickstart

### 1) Requisitos
- Python 3.10+ (probado con 3.12)
- Cuenta AWS configurada desde AWS CLI:
```
$ aws configure
AWS Access Key ID [None]: accesskey
AWS Secret Access Key [None]: secretkey
Default region name [None]: us-west-2
Default output format [None]:
```
### 2) Instalación

# instalar dependencias
pip install -r requirements.txt
```

---

## ▶️ Ejecución

> **IMPORTANTE**: ejecuta siempre desde la raíz del repo usando `python -m` para que los imports funcionen.

### Producer
El **producer** envía mensajes JSON a la cola indicada. Puedes elegir el nombre de la cola con `--queue`.

```bash
# Windows
python -m App.Producer.producer --queue Demo-Queue

# Linux/Mac
python -m App.Producer.producer --queue Demo-Queue
```

### Consumer
El **consumer** lee mensajes de la cola y los elimina. Si tu consumer tiene un nombre de cola fijo, ajusta el valor en el código o usa el mismo nombre que en el producer.

```bash
# Windows / Linux / Mac
python -m App.Consumer.consumer
```

---

## ⚙️ ¿Cómo funciona? (resumen)

- `functions.py` centraliza la lógica de SQS: **listar/crear/obtener** la cola.
- `producer.py` asegura la existencia de la cola y **publica mensajes** JSON.
- `consumer.py` **recibe** hasta `MaxNumberOfMessages=10` con **long polling** y **borra** los mensajes procesados.

> Puedes adaptar fácilmente el contenido del mensaje (por ejemplo, tareas, IDs, u otros atributos) y la política de visibilidad/retención de la cola en `functions.py`.

