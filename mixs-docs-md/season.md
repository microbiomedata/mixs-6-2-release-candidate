# Slot: season


_The season when sampling occurred. Any of the four periods into which the year is divided by the equinoxes and solstices. This field accepts terms listed under season (http://purl.obolibrary.org/obo/NCIT_C94729)_



URI: [MIXS:0000829](https://w3id.org/mixs/0000829)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[BuiltEnvironment](BuiltEnvironment.md) |  |  yes  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  yes  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\S+.*\S+ \[[a-zA-Z]{2,}:[a-zA-Z0-9]+\]$`






## Examples

| Value |
| --- |
| autumn [NCIT:C94733] |

## Comments

* autumn [NCIT:C94733] does not match ^\\S+.*\\S+ \\[[a-zA-Z]{2,}:\\d+\\]$
* would require ^\\S+.*\\S+ \\[[a-zA-Z]{2,}:[a-zA-Z0-9]\\]$

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: season
description: The season when sampling occurred. Any of the four periods into which
  the year is divided by the equinoxes and solstices. This field accepts terms listed
  under season (http://purl.obolibrary.org/obo/NCIT_C94729)
title: season
notes:
- season
comments:
- autumn [NCIT:C94733] does not match ^\\S+.*\\S+ \\[[a-zA-Z]{2,}:\\d+\\]$
- would require ^\\S+.*\\S+ \\[[a-zA-Z]{2,}:[a-zA-Z0-9]\\]$
examples:
- value: autumn [NCIT:C94733]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000829
alias: season
domain_of:
- Agriculture
- BuiltEnvironment
- FoodFarmEnvironment
range: string
required: false
recommended: false
pattern: ^\S+.*\S+ \[[a-zA-Z]{2,}:[a-zA-Z0-9]+\]$

```
</details>