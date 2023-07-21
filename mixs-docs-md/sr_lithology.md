# Slot: sr_lithology


_Lithology of source rock (https://en.wikipedia.org/wiki/Source_rock). If "other" is specified, please propose entry in "additional info" field_



URI: [MIXS:0000995](https://w3id.org/mixs/0000995)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  no  |







## Properties

* Range: [SRLITHOLOGYENUM](SRLITHOLOGYENUM.md)






## Examples

| Value |
| --- |
| Coal |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: sr_lithology
description: Lithology of source rock (https://en.wikipedia.org/wiki/Source_rock).
  If "other" is specified, please propose entry in "additional info" field
title: source rock lithology
notes:
- lithology
- source
examples:
- value: Coal
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000995
multivalued: false
alias: sr_lithology
domain_of:
- HydrocarbonResourcesCores
range: SR_LITHOLOGY_ENUM
required: false
recommended: false

```
</details>