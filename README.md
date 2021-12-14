biosample-graph
================================================
See https://github.com/INCATools/biosample-analysis

Documentation
------------------------------------------------

**Components**

- Download: The [download.yaml](download.yaml) contains all the URLs for the source data.
- Transform: The [transform_utils](project_name/transform_utils) contains the code relevant to transformations of the raw data into nodes and edges (tsv format)
- Merge: Implementation of the 'merge' function from [KGX](https://github.com/biolink/kgx) using [merge.yaml](merge.yaml) as a source file.

**Utilities**

The code for these are found in the [utils](project_name/utils) folder.

- NLP using [OGER](https://github.com/OntoGene/OGER)
- [ROBOT](https://github.com/ontodev/robot) for transforming ontology.OWL to ontology.JSON
