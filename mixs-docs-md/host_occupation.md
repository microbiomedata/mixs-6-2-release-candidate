# Slot: host_occupation


_Most frequent job performed by subject_



URI: [MIXS:0000896](https://w3id.org/mixs/0000896)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HumanAssociated](HumanAssociated.md) |  |  no  |
[HumanGut](HumanGut.md) |  |  no  |
[HumanOral](HumanOral.md) |  |  no  |
[HumanSkin](HumanSkin.md) |  |  no  |
[HumanVaginal](HumanVaginal.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| veterinary |

## Comments

* Couldn't convert host_occupation with value veterinary to integer
* almost all host_occupation values in the NCBI biosample_set are strings, not integers

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: host_occupation
description: Most frequent job performed by subject
title: host occupation
notes:
- host
- host.
comments:
- Couldn't convert host_occupation with value veterinary to integer
- almost all host_occupation values in the NCBI biosample_set are strings, not integers
examples:
- value: veterinary
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000896
alias: host_occupation
domain_of:
- HumanAssociated
- HumanGut
- HumanOral
- HumanSkin
- HumanVaginal
range: string
required: false
recommended: false

```
</details>