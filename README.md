# **PROYECTO PYDEVOPS**
#### ***Ramón Sánchez & Leslie Aranibar***  *1r DAW DUAL* 
-------
***Índice:***

1. Introducción
   * Descripción del reto
   * Análisis de los objetivos   
2. Demostración del funcionamiento del proyecto
3. Descripción técnica
    * Arquitectura de la applicación (de momento¿?)
    * Tecnologías utilizadas 
    * Diagrama de compontes y sus funcionalidades
    * Diagrama E/R de la base de datos (o el que proceda).??????????¿¿¿¿¿¿¿
    * Fichero XML y Schema ???¿¿¿¿ (donde saco el XMML)
4. Metodología de desarrollo utilizada
5. Clockify del desarrollo de la app (esto lo haré  al final porque seguimos inputando)
   * Diagrama del trabajo hecho
   * Análisis y justificación del tiempo invertido
6. Conclusiones 
  * Principales dificultades encontradas
   * Posibles mejoras 
7. Turno de preguntas
---
## **1. Introducción**

**- Descripción del Reto:**  
El desafío que mi equipo abordó resolutivamente, en esencia, consiste en la refactorización de la web interna de una empresa determinada. La cuál era hecha con Wordpress y presentaba ciertas flaquezas. Sobretodo en los procesos de CRUD en su stock.

De manera que nosotros debemos de encargarnos de implementar un sistema de integración y entrega contínua (CI/CD) y mejorar, tanto el funcionamiento y la estética, de su web interna. Todo eso haciendo uso de los conocimientos adquiridos de Python, CSS y de BBDD.

Por suerte, el último becario pasó los ítems a documentos JSON. Y gracias a él, este es el punto de partida del trabajo de nuestro equipo.

**- Análisis de los objetivos:**

Los objetivos clave de este proyecto son:

1. Desarrollar una applicación Python para extraer los datos de MongoAtlas, diseñando una especificación del esquema de los  documentos JSON. 
   
2. Otra aplicación Python que transforme los documentos JSON en ficheros Markdown.
3. Una tercera aplicación Python que sitúe los ficheros MD en la estructura de directorios que establece el generador de contenidos estáticos HUGO
4. Personalizar los estilos CSS para que la empresa disponga de una web única y hermosa. 
5. Implementar las funcionalidades de CRUD. Para que cualquier cambio que la empresa realice sobre un ítem de la base de datos se actualice automátiamente en su web simplemente lanzando el sistema que hemos desarrollado. 
---
## **2. Demostración del funcionamiento del proyecto**

A continuación ejecutaremos nuestro programa para demostrar que cumple con todos los objetivos vistos préviamente. Y satisfae las necesidades que demandaba la empresa. 

---
## **3. Descripción técnica**

* **Arquitectura de la applicación:** 

La arquitectura del sistema de nuestra aplicación es modular. Cada módulo es independiente de los demás, de manera que presenta la lógica un bajo acoplamiento. Pero se encuentran todos conectados en el main.py y son ejecutados a la vez. 

Nuestras barricados las encontramos en los módulos dónde hemos utlizado las siguientes librerías: *Pymongo, Os, Shutill, Webbrowser y Certifi.* Ya que por algún error que se presente en ellas impedirá la ejecución de dichos módulos.
![arquitecturaCapas](./srcReadme/arquitecturaCapas.png)

* **Tecnologías utilizadas:**

Para desarrollar el proyecto nosotros hemos hecho uso de las siguientes herramientas:
|      Herramientas     |                         Funcionalidad                         |
|:---------------------:|:-------------------------------------------------------------:|
| Visual Studio Code    | codificar                                                     |
| Linter en VSC         | visualizar errores                                            |
| Conventional Commits  | proporciona mas significado y legibilidad a los commits       |
| Git Hub               | para compartir y trabajar juntos                              |
| Git Graphs            | permite ver el historial y el esquema de las ramas de trabajo |
| Live Share            | codificar conjuntamente                                       |
| Black                 | corrector de la sintaxis de programación                      |
| Hugo                  | gestor de sitios estáticos                                    |
| Python                | lenguaje de programación                                      |
| Mongo Atlas           | servicio global de base de datos de documentos en la nube     |
| Google Formularios    | para hacer formularios                                        |
| Discord y Whastapp              | conectarnos y hacer dailys                                    |


*   **Diagrama de compontes y sus funcionalidades:**

Nuestro diagrama de componentes consta de los siguientes módulos :

|          Módulo         |                                                                                                                              Proposito                                                                                                                              |
|:-----------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| Main.py                 | recoge y ejecuta todos los otros módulos, por lo tanto depende de los demás                                                                                                                                                                                         |
| conexionBasedatos.py    | conecta con la base de datos almacenada en MongoAtlas y depende de este mismo.                                                                                                                                                                                      |
| selectorDatos.py     | transforma la colección de los ítems en una lista python para su posterior manipulación. Depende del módulo anterior.                                                                                                                                               |
| selectorDatos.py        | localiza y classifica los menús por las 3 categorias que existen.                                                                                                                                                                                                   |
| convertirMarkdown.py    | recoge la primera lista de diccionarios con la misma categoria y los convierte a markdown                                                                                                                                                                                                                                                              |
| ingredientsArray.py     | transforma el array del valor de ingredients en un unico string                                                                                                                                                                                                                                  |
| stateCaracteristicas.py | transforma el diccionario del valor de state en un unico string                                                                                                                                                                                                                                                                    |
| conectarHugo.py         | traslada los archivos que se encuentran en la carpeta origen a la ruta destino deseada. En este caso es en el Post>Content>webComida.com, para que el gestor  de sitios estáticos lo publique. Depende de los archivos Markdown convertidos creados por ese módulo. |
| abrirHugo.py            | se posiciona dentro de la web con Hugo. Luego abre una ventana en el navegador  predeterminado de cada ordenador y ejecuta en la terminal el comando para ver la web.                                                                                               |
                                             
---
 ## **4. Metodología de desarrollo utilizada**
La metodología de desarrollo que hemos seleccionado conjuntamente es la SCRUM. Porque nos desenvolvemos bien dentro de este marco de proceso ligero y ágil. 

Este modelo intenta construir un mejor enfoque para manejar el desarrollo de software. Tiene una menos documentación que los otros métodos tradicionales y esto hace que sea menos complicado. Consta de un programa corto y fijo por ciclos con alcance ajustable, llamados sprints. Y cuenta con eventos, hitos y reuniones que se repiten.

El *Product owner* es David (tutor), el rol del *Scrum Master* nos lo hemos ido relevando, de un sprint a otro. Y el*Scrum team* somos nosotros: Ramón y Leslie.

Y para la organización del trabajo y potenciar nuestra productividad hemos utilizado la herramienta *Notion*. Gracias a esta herramienta hemos definido todo el backlog junto con sus historias de usuario correspondientes. Además hemos organizado el desarrollo del trabajo en 5 sprints con objetivos específicos, mesurables, alcanzables, relevantes y temporales, de acuerdo con el principio *SMART*. 
Por  otra parte, con la finalidad de llevar un ritmo de trabajo sincronizado, contamos con un calendario compartido dónde se visualiza la vida temporal de los *Epics* y algunas fechas destacables (como los *Sprint review meeting, Scrum retrospective meeting, etc.*)

Una pestaña que nos fué muy útil es la de *Task by Status*, la cual nos permitía ver el estado de las tareas de los sprints. Dividimos las tareas en 4  columnas: 
*  *Not started*: tareas por hacer
*  *In progress*: tareas que se estan haciendo.
*  *Completed*: tareas finalizadas
*  *Bugs:* tareas que tienen problemas o errores que hay que arreglar

De esta manera, la comunicación entre nosotros ha sido múy ágil, entendible y fluída. Y la diferencia horaria de trabajo que cada uno tiene no supuso ningún problema.

A continuación os mostraremos el 
[Notion del proyecto](https://efficient-governor-1bf.notion.site/dfb1bb2e4d4344e0979f03268fdf8333?v=8160853a846449f9add5f290d6cdfbd5)

---
## **5. Clockify del desarrollo de la app**
* *Diagrama del trabajo hecho:*
* *Análisis y justificación del tiempo invertido*:
---
## **6. Conclusiones**
* *Principales dificultades encontradas:*
  
Las principales dificultades que nos hemos encontrado fue familiarizarnos y trabajar con la estrategia de Git Flow y funcioanlidades de Git ya que tuvimos conflictos de ramas.
Otro factor a tener en cuenta es el tiempo ajustado que hemos dispuesto, la integación de nuevas funcionalidades sorpresas (los formularios) y la integración/planteamiento de casos tests en el código.

* *Posibles mejoras:*

Leer más libros sobre buenas prácticas en programación, como *The code complete o Clean Arquitecture*, nos leímos una parte y parece interesante. También aprender más sobre estrategias de *Git flow*. Y leer más el libro de Python y practicar.  

---
## **7.Turno de preguntas**
![ask me](./srcReadme/askMe.png)
