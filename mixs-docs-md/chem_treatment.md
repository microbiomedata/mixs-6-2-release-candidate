# Slot: chem_treatment


_List of chemical compounds administered upstream the sampling location where sampling occurred (e.g. Glycols, H2S scavenger, corrosion and scale inhibitors, demulsifiers, and other production chemicals etc.). The commercial name of the product and name of the supplier should be provided. The date of administration should also be included_



URI: [MIXS:0001012](https://w3id.org/mixs/0001012)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| ACCENT 1125;DOW;2010-11-17 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | name;name;timestamp |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: chem_treatment
annotations:
  Expected_value:
    tag: Expected_value
    value: name;name;timestamp
description: List of chemical compounds administered upstream the sampling location
  where sampling occurred (e.g. Glycols, H2S scavenger, corrosion and scale inhibitors,
  demulsifiers, and other production chemicals etc.). The commercial name of the product
  and name of the supplier should be provided. The date of administration should also
  be included
title: chemical treatment
notes:
- treatment
examples:
- value: ACCENT 1125;DOW;2010-11-17
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text};{text};{timestamp}'
slot_uri: MIXS:0001012
multivalued: false
alias: chem_treatment
domain_of:
- HydrocarbonResourcesFluidsSwabs
range: string
required: false
recommended: false

```
</details>