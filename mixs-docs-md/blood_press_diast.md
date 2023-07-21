# Slot: blood_press_diast


_Resting diastolic blood pressure, measured as mm mercury_



URI: [MIXS:0000258](https://w3id.org/mixs/0000258)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HostAssociated](HostAssociated.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | millimeter mercury |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: blood_press_diast
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: millimeter mercury
description: Resting diastolic blood pressure, measured as mm mercury
title: host blood pressure diastolic
notes:
- host
- host.
- pressure
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000258
multivalued: false
alias: blood_press_diast
domain_of:
- HostAssociated
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>