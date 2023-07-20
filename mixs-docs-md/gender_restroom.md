# Slot: gender_restroom


_The gender type of the restroom_



URI: [MIXS:0000808](https://w3id.org/mixs/0000808)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [GENDERRESTROOMENUM](GENDERRESTROOMENUM.md)






## Examples

| Value |
| --- |
| male |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: gender_restroom
description: The gender type of the restroom
title: gender of restroom
examples:
- value: male
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000808
multivalued: false
alias: gender_restroom
domain_of:
- BuiltEnvironment
range: GENDER_RESTROOM_ENUM
required: false
recommended: false

```
</details>