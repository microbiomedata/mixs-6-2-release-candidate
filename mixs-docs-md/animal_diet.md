# Slot: animal_diet


_If the isolate is from a food animal, the type of diet eaten by the food animal.  Please list the main food staple and the setting, if appropriate.  For a list of acceptable animal feed terms or categories, please see http://www.feedipedia.org.  Multiple terms may apply and can be separated by pipes |Food product for animal covers foods intended for consumption by domesticated animals. Consult http://purl.obolibrary.org/obo/FOODON_03309997. If the proper descriptor is not listed please use text to describe the food type. Multiple terms can be separated by one or more pipes. If the proper descriptor is not listed please use text to describe the food product type_



URI: [MIXS:0001130](https://w3id.org/mixs/0001130)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  yes  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | text or FOODON_03309997 |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: animal_diet
annotations:
  Expected_value:
    tag: Expected_value
    value: text or FOODON_03309997
description: If the isolate is from a food animal, the type of diet eaten by the food
  animal.  Please list the main food staple and the setting, if appropriate.  For
  a list of acceptable animal feed terms or categories, please see http://www.feedipedia.org.  Multiple
  terms may apply and can be separated by pipes |Food product for animal covers foods
  intended for consumption by domesticated animals. Consult http://purl.obolibrary.org/obo/FOODON_03309997.
  If the proper descriptor is not listed please use text to describe the food type.
  Multiple terms can be separated by one or more pipes. If the proper descriptor is
  not listed please use text to describe the food product type
title: food animal source diet
notes:
- animal
- diet
- food
- source
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text}'
slot_uri: MIXS:0001130
multivalued: true
alias: animal_diet
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFarmEnvironment
range: string
required: false
recommended: false

```
</details>