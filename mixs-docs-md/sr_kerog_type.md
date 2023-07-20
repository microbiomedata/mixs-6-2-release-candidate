# Slot: sr_kerog_type


_Origin of kerogen. Type I: Algal (aquatic), Type II: planktonic and soft plant material (aquatic or terrestrial), Type III: terrestrial woody/ fibrous plant material (terrestrial), Type IV: oxidized recycled woody debris (terrestrial) (additional information: https://en.wikipedia.org/wiki/Kerogen). If "other" is specified, please propose entry in "additional info" field_



URI: [MIXS:0000994](https://w3id.org/mixs/0000994)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  no  |







## Properties

* Range: [SRKEROGTYPEENUM](SRKEROGTYPEENUM.md)






## Examples

| Value |
| --- |
| Type IV |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: sr_kerog_type
description: 'Origin of kerogen. Type I: Algal (aquatic), Type II: planktonic and
  soft plant material (aquatic or terrestrial), Type III: terrestrial woody/ fibrous
  plant material (terrestrial), Type IV: oxidized recycled woody debris (terrestrial)
  (additional information: https://en.wikipedia.org/wiki/Kerogen). If "other" is specified,
  please propose entry in "additional info" field'
title: source rock kerogen type
notes:
- source
- type
examples:
- value: Type IV
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000994
multivalued: false
alias: sr_kerog_type
domain_of:
- HydrocarbonResourcesCores
range: SR_KEROG_TYPE_ENUM
required: false
recommended: false

```
</details>