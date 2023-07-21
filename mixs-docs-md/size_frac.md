# Slot: size_frac


_Filtering pore size used in sample preparation_



URI: [MIXS:0000017](https://w3id.org/mixs/0000017)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Mimag](Mimag.md) |  |  yes  |
[MimarksS](MimarksS.md) |  |  yes  |
[Mims](Mims.md) |  |  yes  |
[Misag](Misag.md) |  |  yes  |
[Miuvig](Miuvig.md) |  |  yes  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| 0-0.22 micrometer |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | filter size value range |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: size_frac
annotations:
  Expected_value:
    tag: Expected_value
    value: filter size value range
description: Filtering pore size used in sample preparation
title: size fraction selected
notes:
- fraction
- size
examples:
- value: 0-0.22 micrometer
in_subset:
- nucleic acid sequence source
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{float}-{float} {unit}'
slot_uri: MIXS:0000017
multivalued: false
alias: size_frac
domain_of:
- Mimag
- MimarksS
- Mims
- Misag
- Miuvig
range: string

```
</details>