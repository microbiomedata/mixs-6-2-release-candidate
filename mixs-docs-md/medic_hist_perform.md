# Slot: medic_hist_perform


_Whether full medical history was collected_



URI: [MIXS:0000897](https://w3id.org/mixs/0000897)



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

* Range: [Boolean](Boolean.md)






## Examples

| Value |
| --- |
| 1 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: medic_hist_perform
description: Whether full medical history was collected
title: medical history performed
notes:
- history
examples:
- value: '1'
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000897
multivalued: false
alias: medic_hist_perform
domain_of:
- HumanAssociated
- HumanGut
- HumanOral
- HumanSkin
- HumanVaginal
range: boolean
required: false
recommended: false

```
</details>