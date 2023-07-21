# Slot: biocide_admin_method


_Method of biocide administration (dose, frequency, duration, time elapsed between last biociding and sampling) (e.g. 150 mg/l; weekly; 4 hr; 3 days)_



URI: [MIXS:0000456](https://w3id.org/mixs/0000456)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | measurement value;frequency;duration;duration || Preferred_unit | milligram per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: biocide_admin_method
annotations:
  Expected_value:
    tag: Expected_value
    value: measurement value;frequency;duration;duration
  Preferred_unit:
    tag: Preferred_unit
    value: milligram per liter
description: Method of biocide administration (dose, frequency, duration, time elapsed
  between last biociding and sampling) (e.g. 150 mg/l; weekly; 4 hr; 3 days)
title: biocide administration method
notes:
- administration
- method
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{float} {unit};{Rn/start_time/end_time/duration};{duration}'
slot_uri: MIXS:0000456
multivalued: false
alias: biocide_admin_method
domain_of:
- HydrocarbonResourcesFluidsSwabs
range: string
recommended: true

```
</details>