# Estudio de Proyectos de Construcción publica en Chile (2018-2023): Un Análisis Integral

## Contexto y motivación

### Transparencia al publico general sobre este tema
El buen funcionamiento de un gobierno se basa del trabajo en conjunto de todos sus ministerios, nosotros en este proyecto buscamos hacer una crítica constructiva al ministerio de obras públicas, el cual, si bien, hace transparente sus datos, no hace posible que cualquier persona pueda entenderlos, para eso, nosotros vamos a proponer unas preguntas y por mediante de la ciencia de datos vamos a responderlas lo más verídicas posibles, acompañadas de una conclusión general para cada una de estas

## Objetivos

### Evaluar la eficiencia del manejo de las obras publicas del estado
A través de los datos utilizados podremos conseguir informacion sobre que tan eficiente ha sido el estado teniendo en cuenta las empresas que ofrecieron sus servicios a realizar esta obra.

### Crear un sistema de calculo el cual pueda ofrecer un porcentaje de exito de una obra segun datos anteriores
Al momento de medir el porcentaje de exito de una obra, se tratara de predecir gracias a los casos anteriores con similares caracteristicas a la obra que se tratara de medir teniendo encuenta por ejemplo: lugar, fecha, las posibles ofertas de empresas constructoras teniendo en cuenta su especialidad, etc. 

### Analizar los casos en los cuales el estado ha hecho un mal manejo de los recursos y averiguar los motivos
En caso de que haya caso con baja eficiencia trataremos de descubrir los factores que hayan podido afectar a la eficiencia de esta obra.

### Realizar una critica constructiva al sistema de obras publicas
Gracias a los análisis hechos podremos calificar como la eleccion del sistemas de obras publicas, en base a las empresas.

### Hacer publico nuestro proyecto para el publico general
Realizaremos que este sistema pueda ser utilizado para otras personas que quieran revisar de manera mas facil.

## Datos

### Archivos:

1. 2018-sociedades-por-fecha-rut-constitucion-v2

2. 2019-sociedades-por-fecha-rut-constitucion-v3

3. 2020-sociedades-por-fecha-rut-constitucion

4. 2021-sociedades-por-fecha-rut-constitucion

5. 2022-sociedades-por-fecha-rut-constitucion

6. 2023-sociedades-por-fecha-rut-constitucion

7. contratos

8. ofertas

9. pagos

10. proyectos

11. requisitos

### Variables:

1. Nombre del proyecto: (Nombre de la obra pública)

2. Fecha de inicio: (Fecha en que comenzó la obra)

3. Fecha estimada de finalización: (fecha proyectada para la finalización)

4. Fecha real de finalización: (Fecha en que realmente se completó la obra)

5. Presupuesto estimado: (Monto inicial destinado al proyecto)

6. Costo final: (Costo real del proyecto al finalizar)

8. Región: (Ubicado del proyecto)

9. Tipo de proyecto (infraestructura, edificación pública, etc.)

### Formato:
Los archivos CSV son formatos de texto plano en los que los datos están estructurados en filas y columnas. Cada fila representa un proyecto, y cada columna es una variable que describe una característica de ese proyecto

### Volumen:
Dado que trabajaremos en un periodo de 5 años (2018-2023) y muchos proyectos de obras públicas, el volumen de los datos puede ser significativo. En este caso, el tamaño de todos los archivos (ubicados en la carpeta "data") es de 165MB

### Origen:
Los datos provienen de datos. Gob.cl, una plataforma de datos abiertos del gobierno chileno, lo que garantiza que son públicos y accesibles para su análisis.

### Forma de recolección:
Los archivos CSV fueron descargados de manera manual desde la plataforma de datos. Gob.cl

## Preguntas de investigación 

- ¿Cuál es el porcentaje de atraso de las obras publicas? 

- ¿Qué tipo de obras tarda mas en realizarse?

- ¿Qué tipo de obra es mas cara?

- ¿Como varia el presupuesto de las obras públicas según el año?

- ¿Qué empresa fue mas contratada por el ministerio?

## Diseño Tentativo
Para llevar a cabo un análisis integral de los proyectos de construcción pública en Chile (2018-2023), se emplearán diferentes métodos computacionales y estadísticos. A continuación, se detalla brevemente la propuesta:

1. Limpieza y preparación de datos:
Objetivo: Detectar y manejar valores faltantes, duplicados o erróneos (e.g., fechas inconsistentes o presupuestos incompletos). Formatear las fechas y convertir las variables numéricas a sus tipos correspondientes.
Método:
Imputación de valores faltantes en caso de ser necesario (media, mediana).
Filtrado de registros incompletos o atípicos.
2. Análisis exploratorio de datos (EDA):
Objetivo: Visualizar las distribuciones de las variables clave (tiempos de ejecución, presupuestos, tipos de proyectos) y detectar patrones iniciales.
Método:
Histogramas para distribución de costos y tiempos.
Boxplots para identificar outliers.
Gráficos de barras para proyectos más frecuentes por tipo y región.
Mapas de calor para analizar correlaciones entre las variables (e.g., presupuesto y tiempo de finalización).
3. Análisis estadístico:
Objetivo: Evaluar si existen diferencias significativas entre distintos grupos de proyectos en cuanto a su duración, costo y atrasos.
Método:
Pruebas de hipótesis para comparar medias entre diferentes tipos de proyectos (e.g., t-test o ANOVA).
Regresión lineal simple o múltiple para modelar la relación entre costos y tiempo de finalización o entre el tipo de proyecto y los atrasos.
4. Evaluación de atrasos y sobrecostos:
Objetivo: Calcular el porcentaje de proyectos que sufren atrasos y sobrecostos.
Método:
Comparar fechas reales de finalización vs. fechas estimadas.
Calcular el porcentaje de desviación en los presupuestos (sobre/infraejecución).
5. Visualización de resultados:
Objetivo: Crear visualizaciones interactivas y gráficas que resuman el análisis para facilitar la comprensión y comunicación de los resultados.
Método:
Gráficos interactivos para visualizar el progreso de los proyectos a lo largo del tiempo y su distribución geográfica.
Dashboards que muestren los proyectos con mayores atrasos y sobrecostos.
Este enfoque integral te permitirá identificar los proyectos más problemáticos y explorar las causas subyacentes de los retrasos y sobrecostos.


