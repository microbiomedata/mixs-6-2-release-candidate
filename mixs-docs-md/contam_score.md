# Slot: contam_score


_The contamination score is based on the fraction of single-copy genes that are observed more than once in a query genome. The following scores are acceptable for; High Quality Draft: < 5%, Medium Quality Draft: < 10%, Low Quality Draft: < 10%. Contamination must be below 5% for a SAG or MAG to be deposited into any of the public databases_



URI: [MIXS:0000072](https://w3id.org/mixs/0000072)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Mimag](Mimag.md) |  |  yes  |
[Misag](Misag.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| 0.01 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | value |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: contam_score
annotations:
  Expected_value:
    tag: Expected_value
    value: value
description: 'The contamination score is based on the fraction of single-copy genes
  that are observed more than once in a query genome. The following scores are acceptable
  for; High Quality Draft: < 5%, Medium Quality Draft: < 10%, Low Quality Draft: <
  10%. Contamination must be below 5% for a SAG or MAG to be deposited into any of
  the public databases'
title: contamination score
notes:
- score
examples:
- value: '0.01'
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{float} percentage'
slot_uri: MIXS:0000072
multivalued: false
alias: contam_score
domain_of:
- Mimag
- Misag
range: string

```
</details>