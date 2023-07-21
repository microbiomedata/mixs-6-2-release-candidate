# Slot: sc_lysis_method


_Name of the kit or standard protocol used for cell(s) or particle(s) lysis_



URI: [MIXS:0000054](https://w3id.org/mixs/0000054)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Misag](Misag.md) |  |  yes  |
[Miuvig](Miuvig.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| ambion single cell lysis kit |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | kit, protocol name |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: sc_lysis_method
annotations:
  Expected_value:
    tag: Expected_value
    value: kit, protocol name
description: Name of the kit or standard protocol used for cell(s) or particle(s)
  lysis
title: single cell or viral particle lysis kit protocol
notes:
- kit
- particle
- protocol
- single
examples:
- value: ambion single cell lysis kit
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text}'
slot_uri: MIXS:0000054
multivalued: false
alias: sc_lysis_method
domain_of:
- Misag
- Miuvig
range: string

```
</details>