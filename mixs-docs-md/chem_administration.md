# Slot: chem_administration


_List of chemical compounds administered to the host or site where sampling occurred, and when (e.g. Antibiotics, n fertilizer, air filter); can include multiple compounds. For chemical entities of biological interest ontology (chebi) (v 163), http://purl.bioontology.org/ontology/chebi_



URI: [MIXS:0000751](https://w3id.org/mixs/0000751)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[Air](Air.md) |  |  yes  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  yes  |
[HostAssociated](HostAssociated.md) |  |  yes  |
[HumanAssociated](HumanAssociated.md) |  |  yes  |
[HumanGut](HumanGut.md) |  |  yes  |
[HumanOral](HumanOral.md) |  |  yes  |
[HumanSkin](HumanSkin.md) |  |  yes  |
[HumanVaginal](HumanVaginal.md) |  |  yes  |
[MicrobialMatBiofilm](MicrobialMatBiofilm.md) |  |  yes  |
[MiscellaneousNaturalOrArtificialEnvironment](MiscellaneousNaturalOrArtificialEnvironment.md) |  |  yes  |
[PlantAssociated](PlantAssociated.md) |  |  yes  |
[Sediment](Sediment.md) |  |  yes  |
[SymbiontAssociated](SymbiontAssociated.md) |  |  yes  |
[WastewaterSludge](WastewaterSludge.md) |  |  yes  |
[Water](Water.md) |  |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| agar [CHEBI:2509];2018-05-11T20:00Z |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | CHEBI;timestamp |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: chem_administration
annotations:
  Expected_value:
    tag: Expected_value
    value: CHEBI;timestamp
description: List of chemical compounds administered to the host or site where sampling
  occurred, and when (e.g. Antibiotics, n fertilizer, air filter); can include multiple
  compounds. For chemical entities of biological interest ontology (chebi) (v 163),
  http://purl.bioontology.org/ontology/chebi
title: chemical administration
notes:
- administration
examples:
- value: agar [CHEBI:2509];2018-05-11T20:00Z
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{termLabel} [{termID}];{timestamp}'
slot_uri: MIXS:0000751
multivalued: true
alias: chem_administration
domain_of:
- Agriculture
- Air
- FoodFarmEnvironment
- HostAssociated
- HumanAssociated
- HumanGut
- HumanOral
- HumanSkin
- HumanVaginal
- MicrobialMatBiofilm
- MiscellaneousNaturalOrArtificialEnvironment
- PlantAssociated
- Sediment
- SymbiontAssociated
- WastewaterSludge
- Water
range: string

```
</details>