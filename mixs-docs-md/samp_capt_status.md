# Slot: samp_capt_status


_Reason for the sample_



URI: [MIXS:0000860](https://w3id.org/mixs/0000860)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HostAssociated](HostAssociated.md) |  |  no  |
[PlantAssociated](PlantAssociated.md) |  |  no  |







## Properties

* Range: [SAMPCAPTSTATUSENUM](SAMPCAPTSTATUSENUM.md)






## Examples

| Value |
| --- |
| farm sample |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: samp_capt_status
description: Reason for the sample
title: sample capture status
notes:
- sample
- status
examples:
- value: farm sample
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000860
multivalued: false
alias: samp_capt_status
domain_of:
- HostAssociated
- PlantAssociated
range: SAMP_CAPT_STATUS_ENUM
required: false
recommended: false

```
</details>