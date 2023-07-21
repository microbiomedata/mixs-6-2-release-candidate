# Slot: samp_preserv


_Preservative added to the sample (e.g. Rnalater, alcohol, formaldehyde, etc.). Where appropriate include volume added (e.g. Rnalater; 2 ml)_



URI: [MIXS:0000463](https://w3id.org/mixs/0000463)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | milliliter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: samp_preserv
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: milliliter
description: Preservative added to the sample (e.g. Rnalater, alcohol, formaldehyde,
  etc.). Where appropriate include volume added (e.g. Rnalater; 2 ml)
title: preservative added to sample
notes:
- sample
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000463
multivalued: false
alias: samp_preserv
domain_of:
- HydrocarbonResourcesFluidsSwabs
range: string
required: false
recommended: false
structured_pattern:
  syntax: '{name};{float} {unit}'
  interpolated: true
  partial_match: true

```
</details>