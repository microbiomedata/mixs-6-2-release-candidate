# Slot: cur_land_use


_Present state of sample site_



URI: [MIXS:0001080](https://w3id.org/mixs/0001080)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  no  |
[Soil](Soil.md) |  |  no  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| conifers |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | enumeration |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: cur_land_use
annotations:
  Expected_value:
    tag: Expected_value
    value: enumeration
description: Present state of sample site
title: current land use
notes:
- land
- use
examples:
- value: conifers
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '[cities|farmstead|industrial areas|roads/railroads|rock|sand|gravel|mudflats|salt
  flats|badlands|permanent snow or ice|saline seeps|mines/quarries|oil waste areas|small
  grains|row crops|vegetable crops|horticultural plants (e.g. tulips)|marshlands (grass,sedges,rushes)|tundra
  (mosses,lichens)|rangeland|pastureland (grasslands used for livestock grazing)|hayland|meadows
  (grasses,alfalfa,fescue,bromegrass,timothy)|shrub land (e.g. mesquite,sage-brush,creosote
  bush,shrub oak,eucalyptus)|successional shrub land (tree saplings,hazels,sumacs,chokecherry,shrub
  dogwoods,blackberries)|shrub crops (blueberries,nursery ornamentals,filberts)|vine
  crops (grapes)|conifers (e.g. pine,spruce,fir,cypress)|hardwoods (e.g. oak,hickory,elm,aspen)|intermixed
  hardwood and conifers|tropical (e.g. mangrove,palms)|rainforest (evergreen forest
  receiving >406 cm annual rainfall)|swamp (permanent or semi-permanent water body
  dominated by woody plants)|crop trees (nuts,fruit,christmas trees,nursery trees)]'
slot_uri: MIXS:0001080
multivalued: false
alias: cur_land_use
domain_of:
- Agriculture
- Soil
range: string
required: false
recommended: false

```
</details>