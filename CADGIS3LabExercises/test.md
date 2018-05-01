Article created with FME Desktop 2018.0

Introduction
============

### 

How your AutoCAD drawing file is interpreted by FME is largely dependent
on which reader parameters are selected. Additionally, why you want to
have your AutoCAD file interpreted a certain way is largely dependent on
the type of translation you are performing and what you want in the
output. Below are some brief descriptions of the main basic reader
parameter options.

The major ways that we choose to read an AutoCAD drawing file are based
on:

-   how we want to group our entities and
-   whether or not we want to explode blocks.

In this article we\'ll examine how we can group entities.

Downloads
=========

### 

[roads.dwg](https://knowledge.safe.com/storage/attachments/2185-roads.dwg)

Source Data
===========

### 

The data used in this tutorial originates from open data made available
by the [City of Vancouver](http://data.vancouver.ca/), British Columbia.
It contains information licensed under the Open Government License -
Vancouver.

Step-by-Step Instructions
=========================

### 

Let\'s take a closer look at what each of the entity grouping options
look like in the Data Inspector, and how that will affect your
translation. We will do this by examining the \'Group Entities By\'
parameter in the DWG/DXF reader.

**1) Group Entities By Layer Name**

Open the FME Data Inspector and select the Open Data Set icon, or use
the File \> Open Dataset menu option.

In the Open Dataset dialog, select Autodesk AutoCAD DWG/DXF for the
format and the roads.dwg file as the dataset.

Click on the Parameters button.

For Group Entities By, choose the Layer Name option (this is the
default).

[]{.image}

If a user chooses to group their AutoCAD entities by layer name, then
FME will treat each layer as an FME Feature Type in the workspace. Note
that when viewed in FME Data Inspector, you are not able to see the
associated attribute information in the layers. This is because the
attribute schema is not considered when grouping by Layer Name. This is
the default parameter for reading DWG files.

[]{.image}

*Group by Layer Name as viewed in the FME Data Inspector. Note that the
data is grouped by layer in the Display Control window, but there is no
attribute schema.*

### 

**2) Group Entities By Parameter Geometry**

Keep the Data Inspector open and open the dataset again (it will open in
a new View tab). Select the Open Data Set icon, or use the File \> Open
Dataset menu option.

In the Open Dataset dialog, select AutoCAD DWG/DXF for the format and
the roads.dwg file as the dataset.

Click on the Parameters button.

For **Group Entities By**, choose the **Geometry** option.

[]{.image}

If a user chooses to group entities by geometry, then entities will be
sorted by their geometry types (e.g. points, lines, text etc.) and these
geometry types will become the FME Feature Types in the workspace.

Note that in Workbench, all geometry types will be listed unless you
specifically select which geometry types you want to be read. When
inspecting data grouped by Geometry, the FME Data Inspector will
automatically only display the geometry types present in your DWG.

[]{.image}

*Group by Geometry as viewed in Workbench.*

[]{.image}

*Group by Geometry as viewed in the FME Data Inspector. Note that only
line geometries are read.*

**3) Group Entities By Attribute Schema***\
*

Keep the Data Inspector open and open the dataset again (it will open in
a new View tab). Select the Open Data Set icon, or use the File \> Open
Dataset menu option.

In the Open Dataset dialog, select AutoCAD DWG/DXF for the format and
the roads.dwg file as the dataset.

Click on the Parameters button.

For **Group Entities By**, choose the **Attribute Schema** option.

[]{.image}

If a user chooses to group entities by Attribute Schema, then FME will
group entities not only by their layer name, but also by their
associated attribute information. When viewed in the Data Inspector, the
data will be displayed much like when grouping by Layer Name, but will
also show the attribute schema in the Table View.

[]{.image}

*Group by Attribute Schema as viewed in the FME Data Inspector.* *Note
that the attribute data is now visible in the Table View and the data is
grouped by layer.*

[thub.nodes.view.add-new-comment](#)

[autocad
dwg](/topics/autocad+dwg.html){.tag}[cad](/topics/cad.html){.tag}

[gb-layername-noschema.png](/storage/attachments/1276-gb-layername-noschema.png)
(265.5 kB)

[gb-geometry-canvas.png](/storage/attachments/1277-gb-geometry-canvas.png)
(76.1 kB)

[gb-geometry-inspector.png](/storage/attachments/1278-gb-geometry-inspector.png)
(298.2 kB)

[gb-attributeschema-inspector.png](/storage/attachments/1279-gb-attributeschema-inspector.png)
(296.1 kB)

[1532-reader-parameters.png](/storage/attachments/2186-1532-reader-parameters.png)
(14.7 kB)

[geometry.png](/storage/attachments/2188-geometry.png) (15.1 kB)

[attrschema.png](/storage/attachments/2189-attrschema.png) (12.2 kB)

[roads.dwg](/storage/attachments/2185-roads.dwg) (583.3 kB)
