import uuid

from biolink_model_pydantic.model import ( #type: ignore
    Protein,
    Predicate
)

from koza.cli_runner import koza_app #type: ignore

source_name="biosample_nmdc_test"
full_source_name = "NMCD Biosample Test"

row = koza_app.get_row(source_name)

# Entities


# Association
