# Slot: vis_media


_The building visual media_



URI: [MIXS:0000840](https://w3id.org/mixs/0000840)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| 3D scans |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | enumeration |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: vis_media
annotations:
  Expected_value:
    tag: Expected_value
    value: enumeration
description: The building visual media
title: visual media
examples:
- value: 3D scans
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '[photos|videos|commonly of the building|site context (adjacent
  buildings, vegetation, terrain, streets)|interiors|equipment|3D scans]'
slot_uri: MIXS:0000840
multivalued: false
alias: vis_media
domain_of:
- BuiltEnvironment
range: string
required: false
recommended: false

```
</details>