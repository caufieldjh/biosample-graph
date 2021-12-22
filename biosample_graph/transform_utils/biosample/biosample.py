#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from typing import Optional

from biosample_graph.transform_utils.transform import Transform
from koza.cli_runner import transform_source #type: ignore

BIOSAMPLE_SOURCES = {
    'NMDC_Biosample_Table_Test': 'nmdc-biosample-table-for-ner-20201016.tsv',
}

BIOSAMPLE_CONFIGS = {
    'NMDC_Biosample_Table_Test': 'biosample_nmdc_test.yaml',
}

TRANSLATION_TABLE = "./biosample_graph/transform_utils/translation_table.yaml"

class BiosampleTransform(Transform):
    """
    """

    def __init__(self, input_dir: str = None, output_dir: str = None) -> None:
        source_name = "biosample"
        super().__init__(source_name, input_dir, output_dir) 

    def run(self, input_file: Optional[str] = None) -> None:  # type: ignore
        """
        Set up for Koza and call the parse function.
        """
        if input_file:
            for source in [input_file]:
                k = source.split('.')[0]
                data_file = os.path.join(self.input_base_dir, source)
                self.parse(k, data_file, k)
        else:
            for k in BIOSAMPLE_SOURCES.keys():
                name = BIOSAMPLE_SOURCES[k]
                data_file = os.path.join(self.input_base_dir, name)
                self.parse(name, data_file, k)

    def parse(self, name: str, data_file: str, source: str) -> None:
        """
        Transform file with Koza.
        Need to decompress it first.
        """
        print(f"Parsing {data_file}")
        config = os.path.join("biosample_graph/transform_utils/biosample/", BIOSAMPLE_CONFIGS[source])
        output = self.output_dir

        # If source is unknown then we aren't going to guess
        if source not in BIOSAMPLE_CONFIGS:
            raise ValueError(f"Source file {source} not recognized - not transforming.")
        else:
            print(f"Transforming using source in {config}")
            transform_source(source=config, output_dir=output,
                             output_format="tsv",
                             global_table=TRANSLATION_TABLE,
                             local_table=None)