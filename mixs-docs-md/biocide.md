# Slot: biocide


_List of biocides (commercial name of product and supplier) and date of administration_



URI: [MIXS:0001011](https://w3id.org/mixs/0001011)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True






## Examples

| Value |
| --- |
| ALPHA 1427;Baker Hughes;2008-01-23 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | name;name;timestamp |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: biocide
annotations:
  Expected_value:
    tag: Expected_value
    value: name;name;timestamp
description: List of biocides (commercial name of product and supplier) and date of
  administration
title: biocide administration
notes:
- administration
examples:
- value: ALPHA 1427;Baker Hughes;2008-01-23
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text};{text};{timestamp}'
slot_uri: MIXS:0001011
multivalued: false
alias: biocide
domain_of:
- HydrocarbonResourcesFluidsSwabs
range: string
recommended: true

```
</details>