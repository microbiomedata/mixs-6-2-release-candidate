# Slot: biotic_relationship


_Description of relationship(s) between the subject organism and other organism(s) it is associated with. E.g., parasite on species X; mutualist with species Y. The target organism is the subject of the relationship, and the other organism(s) is the object_



URI: [MIXS:0000028](https://w3id.org/mixs/0000028)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[MigsBa](MigsBa.md) |  |  yes  |
[MigsEu](MigsEu.md) |  |  yes  |
[MigsVi](MigsVi.md) |  |  yes  |
[MimarksC](MimarksC.md) |  |  yes  |
[Miuvig](Miuvig.md) |  |  yes  |







## Properties

* Range: [BIOTICRELATIONSHIPENUM](BIOTICRELATIONSHIPENUM.md)






## Examples

| Value |
| --- |
| free living |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: biotic_relationship
description: Description of relationship(s) between the subject organism and other
  organism(s) it is associated with. E.g., parasite on species X; mutualist with species
  Y. The target organism is the subject of the relationship, and the other organism(s)
  is the object
title: observed biotic relationship
notes:
- observed
- relationship
examples:
- value: free living
in_subset:
- nucleic acid sequence source
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000028
multivalued: false
alias: biotic_relationship
domain_of:
- Agriculture
- MigsBa
- MigsEu
- MigsVi
- MimarksC
- Miuvig
range: BIOTIC_RELATIONSHIP_ENUM

```
</details>