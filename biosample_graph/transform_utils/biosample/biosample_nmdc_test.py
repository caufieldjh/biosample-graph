import uuid

from biolink_model_pydantic.model import ( #type: ignore
    MaterialSample,
    MaterialSampleDerivationAssociation,
    EnvironmentalFeature,
    Predicate
)

from koza.cli_runner import koza_app #type: ignore

source_name="biosample_nmdc_test"
full_source_name = "NMDC Biosample Test"

row = koza_app.get_row(source_name)

# Entities
sample = MaterialSample(id='GOLD:' + row['GOLD_ID'],
                        name= row['BIOSAMPLE_NAME'],
                        source=full_source_name)

 # ENVO IDs are entities too but we get their metadata elsewhere

# Association
for envo_level in ['ENV_BROAD_SCALE','ENV_LOCAL_SCALE','ENV_MEDIUM']:
    if str(row[envo_level]) == '': # No ENVO for this level
        continue
    envo = EnvironmentalFeature(id=str(row[envo_level]).replace("_",":"))
    association = MaterialSampleDerivationAssociation(
        id="uuid:" + str(uuid.uuid1()),
        subject=sample.id,
        predicate=Predicate.derives_from,
        object=envo.id,
        relation="RO:0000086", #"has quality" - maybe not the best option
        source =full_source_name
    ) 

    koza_app.write(sample, association, envo)