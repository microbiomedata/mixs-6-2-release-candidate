# Slot: cult_root_med


_Name or reference for the hydroponic or in vitro culture rooting medium; can be the name of a commonly used medium or reference to a specific medium, e.g. Murashige and Skoog medium. If the medium has not been formally published, use the rooting medium descriptors_



URI: [MIXS:0001041](https://w3id.org/mixs/0001041)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PlantAssociated](PlantAssociated.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| http://himedialabs.com/TD/PT158.pdf |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | name, PMID,DOI or url |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: cult_root_med
annotations:
  Expected_value:
    tag: Expected_value
    value: name, PMID,DOI or url
description: Name or reference for the hydroponic or in vitro culture rooting medium;
  can be the name of a commonly used medium or reference to a specific medium, e.g.
  Murashige and Skoog medium. If the medium has not been formally published, use the
  rooting medium descriptors
title: culture rooting medium
notes:
- culture
examples:
- value: http://himedialabs.com/TD/PT158.pdf
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text}|{PMID}|{DOI}|{URL}'
slot_uri: MIXS:0001041
multivalued: false
alias: cult_root_med
domain_of:
- PlantAssociated
range: string
required: false
recommended: false

```
</details>