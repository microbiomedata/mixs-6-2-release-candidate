# Slot: ihmc_medication_code


_Can include multiple medication codes_



URI: [MIXS:0000884](https://w3id.org/mixs/0000884)



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

* Range: [Integer](Integer.md)

* Multivalued: True






## Examples

| Value |
| --- |
| 810 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: ihmc_medication_code
description: Can include multiple medication codes
title: IHMC medication code
notes:
- code
examples:
- value: '810'
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000884
multivalued: true
alias: ihmc_medication_code
domain_of:
- HumanAssociated
- HumanGut
- HumanOral
- HumanSkin
- HumanVaginal
range: integer
required: false
recommended: false

```
</details>