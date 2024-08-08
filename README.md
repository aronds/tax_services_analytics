
<h1 align="center">
   Database Management System & Analytics for Tax Services Business
</h>

<p align="center">
  <img src="imagenes/portada2.jpg" />
</p>


---

## Contenido
1. [Título Portada](#título-portada)
2. [Descripción](#descripción)
3. [Instalación](#instalacion)
3. [Introducción](#introducción)
4. [Objetivos](#objetivos)
5. [Organización del Proyecto](#organización-del-proyecto)
6. [Instalación](#instalación)
7. [Uso](#uso)
8. [Metodología](#metodología)
9. [Análisis Exploratorio de Datos (EDA)](#análisis-exploratorio-de-datos-eda)
10. [Modelado Predictivo](#modelado-predictivo)
11. [Resultados y Discusión](#resultados-y-discusión)
12. [Conclusiones y Recomendaciones](#conclusiones-y-recomendaciones)
13. [Contribuciones](#contribuciones)
14. [Licencia](#licencia)
15. [Contacto](#contacto)

---

## Descripción
Este proyecto está enfocado en la creación de un sistema de gestión de bases de datos (DBMS) y un conjunto de herramientas de análisis de datos específicamente diseñado para optimizar los servicios de impuestos en los Estados Unidos. Utilizando técnicas avanzadas de ciencia de datos, el proyecto se centra en mejorar la eficiencia y precisión del proceso de declaración de impuestos, abordando los desafíos que enfrentan tanto los contribuyentes como las empresas que ofrecen servicios de impuestos.

El proyecto se construye sobre una base de datos relacional que incluye tablas detalladas sobre contribuyentes, dependientes, ingresos, deducciones, créditos, pagos, reembolsos y montos adeudados. Se utiliza un conjunto de datos sintético que permite simular escenarios reales, facilitando el análisis y el desarrollo de soluciones sin comprometer la privacidad de los datos.

Además de la creación del DBMS, el proyecto incluye un análisis exploratorio de datos (EDA) para identificar patrones y relaciones clave en los datos fiscales. A partir de estos análisis, se desarrollan modelos predictivos para predecir comportamientos futuros y optimizar la toma de decisiones en la gestión de impuestos.

El proyecto es modular y está organizado en varios documentos que detallan el desarrollo del sistema, el análisis de datos y las respuestas a preguntas de negocio específicas. También se proporciona una guía detallada para la instalación y uso del sistema, facilitando su implementación en entornos reales.

## **Estructura del Proyecto**
Descripción de los documentos y directorios incluidos en el proyecto.
- `README.md`: Descripción general del proyecto.
- `1 Creacion del Laboratorio y Database Management System.ipynb`: Desarrollo del proyecto - Parte 1.
- `2 Analisi y Respuesta a las Preguntas de Negocio.ipynb`: Desarrollo del proyecto - Parte 2.
- `imagenes/`: Directorio que contiene imágenes utilizadas en los documentos.
- `tablas/`: Directorio que contiene tablas de datos utilizadas en los análisis.

## Instalación
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/aronds/tax_services_analytics.git
2. Instalar las dependencias:
    ```bash
    pip install -r requirements.txt
## **Uso**
    python main.py
## **Introducción**
**Antecedentes**
El sistema de recaudación de impuestos en los Estados Unidos es complejo y presenta múltiples desafíos tanto para los contribuyentes como para los servicios de impuestos.
**Contexto y Relevancia del Problema**
Este proyecto busca mejorar la eficiencia y precisión del proceso de declaración de impuestos mediante técnicas avanzadas de análisis de datos.
Alcance y Limitaciones
**Alcance y limitaciones**
Alcance: Optimización de servicios de impuestos utilizando análisis de datos y modelado predictivo.
Limitaciones: Disponibilidad y calidad de los datos.
## **Objetivos**
* Crear un ecosystem artificial controlado para la simulacion de problemas de
* Realizar un análisis exploratorio de datos (EDA) para identificar patrones y responder pregunas iniciales.
* Crear Datasets spesificos para responder las preguntas del negocio. 
* Desarrollar modelos predictivos basados en los hallazgos del EDA.
* Evaluar la efectividad de diferentes modelos de clasificación y regresión.
## **Descripción de los Datos**
Para fines prácticos, hemos creado un dataset sintético que nos permite omitir procesos previos como la limpieza de datos. Esto ahorra tiempo, procesamiento y recursos, y nos permite enfocarnos en el análisis y las soluciones. En un entorno con datos reales, algunas de las tareas necesarias incluirían:

- Limpieza de datos para eliminar inconsistencias y errores.
- Validación de datos para asegurar la precisión.
- Transformación de datos para adecuarlos a los requisitos del análisis.
- Entre otros errores:
* Inconsistencias en los datos personales:
Solución: Implementar validaciones de datos al ingresar información, como verificaciones de formato para el SSN y direcciones.
* Duplicidad de registros:
Solución: Utilizar claves únicas y controles de integridad referencial para evitar la duplicación de registros.
* Cálculos incorrectos de impuestos:
Solución: Desarrollar algoritmos de verificación para recalcular automáticamente los impuestos basados en los datos ingresados y compararlos con los cálculos del IRS.
* Seguridad de los datos:
Solución: Encriptar los datos sensibles y restringir el acceso a los datos personales únicamente al personal autorizado.
* Errores en la categorización de ingresos y deducciones:
Solución: Crear listas desplegables con opciones predefinidas para los tipos de ingresos y deducciones, minimizando los errores de categorización.
* Actualización de datos
Solución: Implementar un sistema de versionado para mantener un historial de cambios en los datos y permitir la restauración de versiones anteriores si es necesario.
---
## RDMS (Relational Database Management System)
**Taxpayers and Dependents**

<table>
    <tr>
        <td>
            <pre>
+------------------------+
|  Taxpayers             |
+------------------------+
| taxpayer_id PK         |
| first_name             |
| last_name              |
| ssn                    |
| filing_status          |
| address                |
| city                   |
| state                  |
| zip_code               |
| email                  |
| phone_number           |
| employer_name          |
| employer_address       |
| job_title              |
| employment_start_date  |
| employment_end_date    |
| tax_return_id          |
| tax_year               |
| filing_date            |
| return_type            |
| income_source          |
| income_frequency       |
| taxable_amount         |
| deduction_category     |
| deduction_description  |
| credit_description     |
| credit_eligibility     |
| payment_date           |
| payment_method         |
| refund_date            |
| refund_reason          |
| amount_owed_due_date   |
| amount_owed_reason     |
| property_type          |
| property_value         |
| mortgage_interest_paid |
| taxpayer_occupation    |
| previous_year_income   |
| state_tax_refund       |
| local_tax_refund       |
| estimated_tax_payments_made |
| tax_liability          |
+------------------------+
            </pre>
        </td>
        <td>
            <pre>
+----------------------+
|  Dependents          |
+----------------------+
| taxpayer_id FK       |
| dependent_id PK      |
| first_name           |
| last_name            |
| ssn                  |
| relationship         |
| qualifies_for_credit |
+----------------------+
            </pre>
        </td>
    </tr>
</table>

---

**Income and Deductions**

<table>
    <tr>
        <td>
            <pre>
+---------------+
|   Income      |
+---------------+
| IncomeID PK   |
| TaxpayerID FK |
| IncomeType    |
| Amount        |
+---------------+
            </pre>
        </td>
        <td>
            <pre>
+-----------------+
| Deductions      |
+-----------------+
| TaxpayerID FK   |
| DeductionID PK  |
| DeductionType   |
| Amount          |
+-----------------+
            </pre>
        </td>
    </tr>
</table>

---

**Credits and Payments**

<table>
    <tr>
        <td>
            <pre>
+---------------+
|   Credits     |
+---------------+
| CreditID PK   |
| TaxpayerID FK |
| CreditType    |
| Amount        |
+---------------+
            </pre>
        </td>
        <td>
            <pre>
+-----------------+
| Payments        |
+-----------------+
| TaxpayerID FK   |
| PaymentID PK    |
| PaymentType     |
| Amount          |
+-----------------+
            </pre>
        </td>
    </tr>
</table>

---

**Refunds and Amounts Owed**

<table>
    <tr>
        <td>
            <pre>
+---------------+
|  Refunds      |
+---------------+
| RefundID PK   |
| TaxpayerID FK |
| RefundAmount  |
+---------------+
            </pre>
        </td>
        <td>
            <pre>
+-----------------+
| AmountsOwed     |
+-----------------+
| TaxpayerID FK   |
| AmountOwedID PK |
| Amount          |
+-----------------+
            </pre>
        </td>
    </tr>
</table>

## Metadata
**Resumen del Sistema**
- **Cantidad de Tablas**: 8
- **Total de Columnas**: 68
- **Total de Filas (estimado con datos sintéticos)**: 1000 por tabla (ajustable según necesidades)

## Detalle de Tablas y Campos

#### Tabla: Taxpayers
**Descripción**: Almacena información básica sobre los contribuyentes.

**Columnas**: 42
- **taxpayer_id**: `INT` (Primary Key) - Identificador único del contribuyente.
- **first_name**: `VARCHAR(50)` - Nombre del contribuyente.
- **last_name**: `VARCHAR(50)` - Apellido del contribuyente.
- **ssn**: `CHAR(11)` - Número de Seguro Social del contribuyente.
- **filing_status**: `VARCHAR(50)` - Estado de presentación (por ejemplo, Soltero, Casado presentando conjuntamente).
- **address**: `VARCHAR(100)` - Dirección del contribuyente.
- **city**: `VARCHAR(50)` - Ciudad del contribuyente.
- **state**: `CHAR(2)` - Estado del contribuyente.
- **zip_code**: `CHAR(5)` - Código postal del contribuyente.
- **email**: `VARCHAR(100)` - Correo electrónico del contribuyente.
- **phone_number**: `VARCHAR(15)` - Número de teléfono del contribuyente.
- **employer_name**: `VARCHAR(100)` - Nombre del empleador.
- **employer_address**: `VARCHAR(100)` - Dirección del empleador.
- **job_title**: `VARCHAR(50)` - Título del trabajo del contribuyente.
- **employment_start_date**: `DATE` - Fecha de inicio del empleo.
- **employment_end_date**: `DATE` - Fecha de fin del empleo.
- **tax_return_id**: `INT` - Identificador de la declaración de impuestos.
- **tax_year**: `INT` - Año fiscal.
- **filing_date**: `DATE` - Fecha de presentación.
- **return_type**: `VARCHAR(50)` - Tipo de declaración (por ejemplo, Individual, Conjunta, Enmendada).
- **income_source**: `VARCHAR(50)` - Fuente de ingresos.
- **income_frequency**: `VARCHAR(10)` - Frecuencia de ingresos (Mensual, Anual).
- **taxable_amount**: `DECIMAL(10, 2)` - Monto imponible.
- **deduction_category**: `VARCHAR(50)` - Categoría de deducción.
- **deduction_description**: `VARCHAR(100)` - Descripción de la deducción.
- **credit_description**: `VARCHAR(100)` - Descripción del crédito.
- **credit_eligibility**: `VARCHAR(20)` - Elegibilidad para el crédito (Eligible, Not Eligible).
- **payment_date**: `DATE` - Fecha de pago.
- **payment_method**: `VARCHAR(50)` - Método de pago.
- **refund_date**: `DATE` - Fecha de reembolso.
- **refund_reason**: `VARCHAR(50)` - Razón del reembolso.
- **amount_owed_due_date**: `DATE` - Fecha de vencimiento del monto adeudado.
- **amount_owed_reason**: `VARCHAR(50)` - Razón del monto adeudado.
- **property_type**: `VARCHAR(50)` - Tipo de propiedad.
- **property_value**: `DECIMAL(10, 2)` - Valor de la propiedad.
- **mortgage_interest_paid**: `DECIMAL(10, 2)` - Intereses hipotecarios pagados.
- **taxpayer_occupation**: `VARCHAR(50)` - Ocupación del contribuyente.
- **previous_year_income**: `DECIMAL(10, 2)` - Ingresos del año anterior.
- **state_tax_refund**: `DECIMAL(10, 2)` - Reembolso de impuestos estatales.
- **local_tax_refund**: `DECIMAL(10, 2)` - Reembolso de impuestos locales.
- **estimated_tax_payments_made**: `DECIMAL(10, 2)` - Pagos de impuestos estimados realizados.
- **tax_liability**: `DECIMAL(10, 2)` - Obligación tributaria.
![](imagenes/taxpayer_table1.png)
![](imagenes/taxpayer_table2.png)
![](imagenes/taxpayer_table3.png)
![](imagenes/taxpayer_table4.png)
![](imagenes/taxpayer_table5.png)
---
#### Tabla: Dependents
**Descripción**: Almacena información sobre los dependientes de los contribuyentes.
**Columnas**: 7
- **dependent_id**: `INT` (Primary Key) - Identificador único del dependiente.
- **taxpayer_id**: `INT` (Foreign Key) - Identificador del contribuyente asociado.
- **first_name**: `VARCHAR(50)` - Nombre del dependiente.
- **last_name**: `VARCHAR(50)` - Apellido del dependiente.
- **ssn**: `CHAR(11)` - Número de Seguro Social del dependiente.
- **relationship**: `VARCHAR(50)` - Relación del dependiente con el contribuyente.
- **qualifies_for_credit**: `BOOLEAN` - Indica si el dependiente califica para créditos fiscales.
![](imagenes/dependents_table.png)
---
#### Tabla: Income
**Descripción**: Almacena información sobre los ingresos de los contribuyentes.

**Columnas**: 4
- **income_id**: `INT` (Primary Key) - Identificador único del ingreso.
- **taxpayer_id**: `INT` (Foreign Key) - Identificador del contribuyente asociado.
- **income_type**: `VARCHAR(50)` - Tipo de ingreso.
- **amount**: `DECIMAL(10, 2)` - Monto del ingreso.
![](imagenes/income_table.png)
---
#### Tabla: Deductions
**Descripción**: Almacena información sobre las deducciones de los contribuyentes.
**Columnas**: 4
- **deduction_id**: `INT` (Primary Key) - Identificador único de la deducción.
- **taxpayer_id**: `INT` (Foreign Key) - Identificador del contribuyente asociado.
- **deduction_type**: `VARCHAR(50)` - Tipo de deducción.
- **amount**: `DECIMAL(10, 2)` - Monto de la deducción.
![](imagenes/deductions_table.png)
---
#### Tabla: Credits
**Descripción**: Almacena información sobre los créditos fiscales de los contribuyentes.

**Columnas**: 4
- **credit_id**: `INT` (Primary Key) - Identificador único del crédito.
- **taxpayer_id**: `INT` (Foreign Key) - Identificador del contribuyente asociado.
- **credit_type**: `VARCHAR(50)` - Tipo de crédito.
- **amount**: `DECIMAL(10, 2)` - Monto del crédito.
![](imagenes/credits_table.png)
---
#### Tabla: Payments
**Descripción**: Almacena información sobre los pagos realizados por los contribuyentes.

**Columnas**: 4
- **payment_id**: `INT` (Primary Key) - Identificador único del pago.
- **taxpayer_id**: `INT` (Foreign Key) - Identificador del contribuyente asociado.
- **payment_type**: `VARCHAR(50)` - Tipo de pago.
- **amount**: `DECIMAL(10, 2)` - Monto del pago.
![](imagenes/payments_table.png)

#### Tabla: Refunds
**Descripción**: Almacena información sobre los reembolsos recibidos por los contribuyentes.

**Columnas**: 3
- **refund_id**: `INT` (Primary Key) - Identificador único del reembolso.
- **taxpayer_id**: `INT` (Foreign Key) - Identificador del contribuyente asociado.
- **refund_amount**: `DECIMAL(10, 2)` - Monto del reembolso.
![](imagenes/refunds_table.png)
---
#### Tabla: Amounts Owed
**Descripción**: Almacena información sobre los montos adeudados por los contribuyentes.

**Columnas**: 3
- **amount_owed_id**: `INT` (Primary Key) - Identificador único del monto adeudado.
- **taxpayer_id**: `INT` (Foreign Key) - Identificador del contribuyente asociado.
- **amount**: `DECIMAL(10, 2)` - Monto adeudado.
![](imagenes/amountowed_table.png)
---
## **Metodología**
   - Descripción de los métodos y técnicas utilizadas en esta fase del proyecto.
## **Análisis Exploratorio de Datos (EDA)**
   - Descripción y visualización de los datos.
   - Tipos de deducciones y créditos.
   - Gráficos de distribución de ingresos.
   - Mapas de calor para identificar correlaciones.
## **Resultados Iniciales**
   - Hallazgos preliminares del análisis.
   - Identificación de patrones de ingresos por estado.
   - Correlaciones entre tipos de deducciones y créditos.
## **Modelado Predictivo**
   - Descripción de los modelos utilizados, su entrenamiento y evaluación.
## **Validación y Evaluación**
   - Resultados de la validación cruzada y métricas de evaluación.
## **Resultados y Discusión**
   - Interpretación de los resultados obtenidos.
   - Resultados de la validación cruzada y métricas de evaluación.
   - Interpretación de los resultados obtenidos.
   - Comparación con estudios previos.
   - Implicaciones de los hallazgos.
## **Conclusiones y Recomendaciones**
   - Principales conclusiones del proyecto:
   - Recomendaciones para la implementación práctica y futuros trabajos:
   Este proyecto crea una base sólida para gestionar y analizar datos de servicios de impuestos, utilizando un enfoque estructurado y datos sintéticos para garantizar la privacidad y seguridad de la información. El sistema permite la identificación y solución de problemas comunes en la industria de los servicios de impuestos, proporcionando una plataforma robusta para análisis y mejoras continuas.
   
## **Estructura de Directorios**

<pre>
tu_proyecto/
│
├── README.md
├── 1_Creación del Laboratorio y Database Management System.ipynb
├── 2_Análisis y Respuesta a las Preguntas de Negocio.ipynb
├── imagenes/
│   ├── portada.jpg
│   ├── taxpayer_table1.png
│   ├── taxpayer_table2.png
│   ├── taxpayer_table3.png
│   ├── taxpayer_table4.png
│   ├── taxpayer_table5.png
│   ├── dependents_table.png
│   ├── income_table.png
│   ├── deductions_table.png
│   ├── credits_table.png
│   ├── payments_table.png
│   ├── refunds_table.png
│   ├── amountowed_table.png
│
├── tablas/
│   ├── tabla1.csv
│   ├── tabla2.csv
│   └── ...
├── scripts/
│   ├── main.py
│   ├── eda.py
│   └── modelado.py
└── data/
    ├── datos_crudos.csv
    ├── datos_limpios.csv
    └── ...
</pre>

## **Contribuciones**
     Para contribuir, por favor abre un issue o envía un pull request.
## **Licencia**
   Este proyecto está bajo la Licencia MIT.
## **Contacto**
   Para más información, contactar a Arom Antinao a través de coregroup.proyect@gmail.com
---

"""


