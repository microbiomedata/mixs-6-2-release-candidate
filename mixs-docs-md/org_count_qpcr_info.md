# Slot: org_count_qpcr_info


_If qpcr was used for the cell count, the target gene name, the primer sequence and the cycling conditions should also be provided. (Example: 16S rrna; FWD:ACGTAGCTATGACGT REV:GTGCTAGTCGAGTAC; initial denaturation:90C_5min; denaturation:90C_2min; annealing:52C_30 sec; elongation:72C_30 sec; 90 C for 1 min; final elongation:72C_5min; 30 cycles)_



URI: [MIXS:0000099](https://w3id.org/mixs/0000099)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  no  |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | gene name;FWD:forward primer sequence;REV:reverse primer sequence;initial denaturation:degrees_minutes;denaturation:degrees_minutes;annealing:degrees_minutes;elongation:degrees_minutes;final elongation:degrees_minutes; total cycles || Preferred_unit | number of cells per gram (or ml or cm^2) |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: org_count_qpcr_info
annotations:
  Expected_value:
    tag: Expected_value
    value: gene name;FWD:forward primer sequence;REV:reverse primer sequence;initial
      denaturation:degrees_minutes;denaturation:degrees_minutes;annealing:degrees_minutes;elongation:degrees_minutes;final
      elongation:degrees_minutes; total cycles
  Preferred_unit:
    tag: Preferred_unit
    value: number of cells per gram (or ml or cm^2)
description: 'If qpcr was used for the cell count, the target gene name, the primer
  sequence and the cycling conditions should also be provided. (Example: 16S rrna;
  FWD:ACGTAGCTATGACGT REV:GTGCTAGTCGAGTAC; initial denaturation:90C_5min; denaturation:90C_2min;
  annealing:52C_30 sec; elongation:72C_30 sec; 90 C for 1 min; final elongation:72C_5min;
  30 cycles)'
title: organism count qPCR information
notes:
- count
- information
- organism
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text};FWD:{dna};REV:{dna};initial denaturation:degrees_minutes;denaturation:degrees_minutes;annealing:degrees_minutes;elongation:degrees_minutes;final
  elongation:degrees_minutes; total cycles'
slot_uri: MIXS:0000099
multivalued: false
alias: org_count_qpcr_info
domain_of:
- HydrocarbonResourcesCores
- HydrocarbonResourcesFluidsSwabs
range: string
required: false
recommended: false

```
</details>