# Slot: chem_treat_method


_Method of chemical administration(dose, frequency, duration, time elapsed between administration and sampling) (e.g. 50 mg/l; twice a week; 1 hr; 0 days)_



URI: [MIXS:0000457](https://w3id.org/mixs/0000457)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | measurement value;frequency;duration;duration || Preferred_unit | milligram per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: chem_treat_method
annotations:
  Expected_value:
    tag: Expected_value
    value: measurement value;frequency;duration;duration
  Preferred_unit:
    tag: Preferred_unit
    value: milligram per liter
description: Method of chemical administration(dose, frequency, duration, time elapsed
  between administration and sampling) (e.g. 50 mg/l; twice a week; 1 hr; 0 days)
title: chemical treatment method
notes:
- method
- treatment
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{float} {unit};{Rn/start_time/end_time/duration};{duration};{duration}'
slot_uri: MIXS:0000457
multivalued: false
alias: chem_treat_method
domain_of:
- HydrocarbonResourcesFluidsSwabs
range: string
required: false
recommended: false

```
</details>