Are there empty folders in images dataset?

```bash
find images -type d -empty

```

None.

```bash
cd ./data/images; \
find . -type d -maxdepth 1 -mindepth 1
```

./disposable_plastic_cutlery
./food_waste
./office_paper
./glass_food_jars
./aluminum_soda_cans
./magazines
./clothing
./plastic_shopping_bags
./plastic_soda_bottles
./styrofoam_food_containers
./aerosol_cans
./aluminum_food_cans
./newspaper
./eggshells
./glass_cosmetic_containers
./paper_cups
./plastic_water_bottles
./coffee_grounds
./steel_food_cans
./plastic_cup_lids
./cardboard_packaging
./cardboard_boxes
./plastic_straws
./styrofoam_cups
./glass_beverage_bottles
./shoes
./plastic_trash_bags
./tea_bags
./plastic_food_containers
./plastic_detergent_bottles


```bash
for DIR in images/*; do 
  echo "\nCLASS: $(basename "$DIR")";
  echo " default: $(find "$DIR/default" -type f | wc -l)";
  echo " real_world: $(find "$DIR/real_world" -type f | wc -l)";
done
```

250 images in each class and mode


```bash
find images -type f -name "*.png" | wc -l
```

15000


```bash
find images -type f -name "*.png" | head -n 20 | xargs file
```

images/disposable_plastic_cutlery/real_world/Image_15.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
images/disposable_plastic_cutlery/real_world/Image_29.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
images/disposable_plastic_cutlery/real_world/Image_178.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
images/disposable_plastic_cutlery/real_world/Image_144.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
images/disposable_plastic_cutlery/real_world/Image_150.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
images/disposable_plastic_cutlery/real_world/Image_187.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
images/disposable_plastic_cutlery/real_world/Image_193.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
images/disposable_plastic_cutlery/real_world/Image_232.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
images/disposable_plastic_cutlery/real_world/Image_226.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
images/disposable_plastic_cutlery/real_world/Image_227.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
images/disposable_plastic_cutlery/real_world/Image_233.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
images/disposable_plastic_cutlery/real_world/Image_192.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
images/disposable_plastic_cutlery/real_world/Image_186.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
images/disposable_plastic_cutlery/real_world/Image_151.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
images/disposable_plastic_cutlery/real_world/Image_145.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
images/disposable_plastic_cutlery/real_world/Image_179.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
images/disposable_plastic_cutlery/real_world/Image_28.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
images/disposable_plastic_cutlery/real_world/Image_14.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
images/disposable_plastic_cutlery/real_world/Image_16.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
images/disposable_plastic_cutlery/real_world/Image_153.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

Install core utils to get gshuf command. It allows to select N files randomly.

```bash
brew update
brew install coreutils
```

```bash
for DIR in */*; do
  echo "\nFOLDER: $DIR"
  find "$DIR" -type f -name "*.png" | gshuf -n 5 | xargs file
done
```

FOLDER: aerosol_cans/default
aerosol_cans/default/Image_235.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
aerosol_cans/default/Image_244.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
aerosol_cans/default/Image_217.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
aerosol_cans/default/Image_71.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
aerosol_cans/default/Image_105.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: aerosol_cans/real_world
aerosol_cans/real_world/Image_151.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
aerosol_cans/real_world/Image_26.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
aerosol_cans/real_world/Image_83.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
aerosol_cans/real_world/Image_125.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
aerosol_cans/real_world/Image_66.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: aluminum_food_cans/default
aluminum_food_cans/default/Image_87.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
aluminum_food_cans/default/Image_124.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
aluminum_food_cans/default/Image_123.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
aluminum_food_cans/default/Image_144.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
aluminum_food_cans/default/Image_77.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: aluminum_food_cans/real_world
aluminum_food_cans/real_world/Image_94.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
aluminum_food_cans/real_world/Image_157.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
aluminum_food_cans/real_world/Image_230.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
aluminum_food_cans/real_world/Image_148.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
aluminum_food_cans/real_world/Image_24.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: aluminum_soda_cans/default
aluminum_soda_cans/default/Image_55.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
aluminum_soda_cans/default/Image_78.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
aluminum_soda_cans/default/Image_140.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
aluminum_soda_cans/default/Image_177.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
aluminum_soda_cans/default/Image_210.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: aluminum_soda_cans/real_world
aluminum_soda_cans/real_world/Image_186.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
aluminum_soda_cans/real_world/Image_89.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
aluminum_soda_cans/real_world/Image_208.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
aluminum_soda_cans/real_world/Image_206.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
aluminum_soda_cans/real_world/Image_112.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: cardboard_boxes/default
cardboard_boxes/default/Image_13.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
cardboard_boxes/default/Image_223.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
cardboard_boxes/default/Image_100.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
cardboard_boxes/default/Image_213.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
cardboard_boxes/default/Image_37.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: cardboard_boxes/real_world
cardboard_boxes/real_world/Image_250.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
cardboard_boxes/real_world/Image_167.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
cardboard_boxes/real_world/Image_219.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
cardboard_boxes/real_world/Image_124.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
cardboard_boxes/real_world/Image_152.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: cardboard_packaging/default
cardboard_packaging/default/Image_217.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
cardboard_packaging/default/Image_228.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
cardboard_packaging/default/Image_138.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
cardboard_packaging/default/Image_72.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
cardboard_packaging/default/Image_226.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: cardboard_packaging/real_world
cardboard_packaging/real_world/Image_37.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
cardboard_packaging/real_world/Image_208.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
cardboard_packaging/real_world/Image_28.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
cardboard_packaging/real_world/Image_172.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
cardboard_packaging/real_world/Image_180.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: clothing/default
clothing/default/Image_44.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
clothing/default/Image_133.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
clothing/default/Image_66.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
clothing/default/Image_138.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
clothing/default/Image_86.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: clothing/real_world
clothing/real_world/Image_182.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
clothing/real_world/Image_169.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
clothing/real_world/Image_236.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
clothing/real_world/Image_3.png:   PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
clothing/real_world/Image_55.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: coffee_grounds/default
coffee_grounds/default/Image_249.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
coffee_grounds/default/Image_110.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
coffee_grounds/default/Image_52.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
coffee_grounds/default/Image_178.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
coffee_grounds/default/Image_46.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: coffee_grounds/real_world
coffee_grounds/real_world/Image_216.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
coffee_grounds/real_world/Image_186.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
coffee_grounds/real_world/Image_41.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
coffee_grounds/real_world/Image_34.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
coffee_grounds/real_world/Image_185.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: disposable_plastic_cutlery/default
disposable_plastic_cutlery/default/Image_66.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
disposable_plastic_cutlery/default/Image_139.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
disposable_plastic_cutlery/default/Image_110.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
disposable_plastic_cutlery/default/Image_195.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
disposable_plastic_cutlery/default/Image_144.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: disposable_plastic_cutlery/real_world
disposable_plastic_cutlery/real_world/Image_29.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
disposable_plastic_cutlery/real_world/Image_211.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
disposable_plastic_cutlery/real_world/Image_106.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
disposable_plastic_cutlery/real_world/Image_159.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
disposable_plastic_cutlery/real_world/Image_237.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: eggshells/default
eggshells/default/Image_249.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
eggshells/default/Image_35.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
eggshells/default/Image_224.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
eggshells/default/Image_78.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
eggshells/default/Image_170.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: eggshells/real_world
eggshells/real_world/Image_75.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
eggshells/real_world/Image_82.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
eggshells/real_world/Image_132.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
eggshells/real_world/Image_156.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
eggshells/real_world/Image_35.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: food_waste/default
food_waste/default/Image_216.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
food_waste/default/Image_184.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
food_waste/default/Image_214.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
food_waste/default/Image_52.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
food_waste/default/Image_200.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: food_waste/real_world
food_waste/real_world/Image_178.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
food_waste/real_world/Image_99.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
food_waste/real_world/Image_189.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
food_waste/real_world/Image_242.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
food_waste/real_world/Image_203.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: glass_beverage_bottles/default
glass_beverage_bottles/default/Image_77.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
glass_beverage_bottles/default/Image_10.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
glass_beverage_bottles/default/Image_44.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
glass_beverage_bottles/default/Image_197.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
glass_beverage_bottles/default/Image_60.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: glass_beverage_bottles/real_world
glass_beverage_bottles/real_world/Image_132.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
glass_beverage_bottles/real_world/Image_153.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
glass_beverage_bottles/real_world/Image_109.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
glass_beverage_bottles/real_world/Image_241.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
glass_beverage_bottles/real_world/Image_74.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: glass_cosmetic_containers/default
glass_cosmetic_containers/default/Image_100.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
glass_cosmetic_containers/default/Image_224.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
glass_cosmetic_containers/default/Image_158.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
glass_cosmetic_containers/default/Image_183.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
glass_cosmetic_containers/default/Image_43.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: glass_cosmetic_containers/real_world
glass_cosmetic_containers/real_world/Image_134.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
glass_cosmetic_containers/real_world/Image_196.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
glass_cosmetic_containers/real_world/Image_103.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
glass_cosmetic_containers/real_world/Image_99.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
glass_cosmetic_containers/real_world/Image_222.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: glass_food_jars/default
glass_food_jars/default/Image_149.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
glass_food_jars/default/Image_91.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
glass_food_jars/default/Image_48.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
glass_food_jars/default/Image_196.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
glass_food_jars/default/Image_43.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: glass_food_jars/real_world
glass_food_jars/real_world/Image_226.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
glass_food_jars/real_world/Image_173.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
glass_food_jars/real_world/Image_194.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
glass_food_jars/real_world/Image_99.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
glass_food_jars/real_world/Image_233.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: magazines/default
magazines/default/Image_177.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
magazines/default/Image_157.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
magazines/default/Image_180.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
magazines/default/Image_217.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
magazines/default/Image_33.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: magazines/real_world
magazines/real_world/Image_240.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
magazines/real_world/Image_163.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
magazines/real_world/Image_149.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
magazines/real_world/Image_233.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
magazines/real_world/Image_135.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: newspaper/default
newspaper/default/Image_211.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
newspaper/default/Image_95.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
newspaper/default/Image_124.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
newspaper/default/Image_187.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
newspaper/default/Image_94.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: newspaper/real_world
newspaper/real_world/Image_15.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
newspaper/real_world/Image_217.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
newspaper/real_world/Image_234.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
newspaper/real_world/Image_247.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
newspaper/real_world/Image_20.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: office_paper/default
office_paper/default/Image_234.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
office_paper/default/Image_24.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
office_paper/default/Image_128.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
office_paper/default/Image_28.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
office_paper/default/Image_36.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: office_paper/real_world
office_paper/real_world/Image_30.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
office_paper/real_world/Image_106.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
office_paper/real_world/Image_236.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
office_paper/real_world/Image_77.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
office_paper/real_world/Image_190.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: paper_cups/default
paper_cups/default/Image_155.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
paper_cups/default/Image_83.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
paper_cups/default/Image_178.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
paper_cups/default/Image_116.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
paper_cups/default/Image_180.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: paper_cups/real_world
paper_cups/real_world/Image_42.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
paper_cups/real_world/Image_16.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
paper_cups/real_world/Image_205.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
paper_cups/real_world/Image_24.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
paper_cups/real_world/Image_208.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: plastic_cup_lids/default
plastic_cup_lids/default/Image_97.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_cup_lids/default/Image_35.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_cup_lids/default/Image_238.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_cup_lids/default/Image_231.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_cup_lids/default/Image_58.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: plastic_cup_lids/real_world
plastic_cup_lids/real_world/Image_199.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_cup_lids/real_world/Image_150.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_cup_lids/real_world/Image_209.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_cup_lids/real_world/Image_218.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_cup_lids/real_world/Image_197.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: plastic_detergent_bottles/default
plastic_detergent_bottles/default/Image_27.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_detergent_bottles/default/Image_149.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_detergent_bottles/default/Image_12.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_detergent_bottles/default/Image_248.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_detergent_bottles/default/Image_137.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: plastic_detergent_bottles/real_world
plastic_detergent_bottles/real_world/Image_58.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_detergent_bottles/real_world/Image_29.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_detergent_bottles/real_world/Image_102.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_detergent_bottles/real_world/Image_85.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_detergent_bottles/real_world/Image_216.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: plastic_food_containers/default
plastic_food_containers/default/Image_14.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_food_containers/default/Image_52.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_food_containers/default/Image_175.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_food_containers/default/Image_124.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_food_containers/default/Image_113.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: plastic_food_containers/real_world
plastic_food_containers/real_world/Image_239.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_food_containers/real_world/Image_236.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_food_containers/real_world/Image_10.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_food_containers/real_world/Image_55.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_food_containers/real_world/Image_84.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: plastic_shopping_bags/default
plastic_shopping_bags/default/Image_67.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_shopping_bags/default/Image_68.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_shopping_bags/default/Image_234.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_shopping_bags/default/Image_179.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_shopping_bags/default/Image_41.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: plastic_shopping_bags/real_world
plastic_shopping_bags/real_world/Image_118.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_shopping_bags/real_world/Image_90.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_shopping_bags/real_world/Image_53.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_shopping_bags/real_world/Image_247.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_shopping_bags/real_world/Image_241.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: plastic_soda_bottles/default
plastic_soda_bottles/default/Image_212.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_soda_bottles/default/Image_102.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_soda_bottles/default/Image_149.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_soda_bottles/default/Image_153.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_soda_bottles/default/Image_240.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: plastic_soda_bottles/real_world
plastic_soda_bottles/real_world/Image_188.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_soda_bottles/real_world/Image_183.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_soda_bottles/real_world/Image_195.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_soda_bottles/real_world/Image_33.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_soda_bottles/real_world/Image_174.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: plastic_straws/default
plastic_straws/default/Image_77.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_straws/default/Image_104.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_straws/default/Image_35.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_straws/default/Image_103.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_straws/default/Image_90.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: plastic_straws/real_world
plastic_straws/real_world/Image_68.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_straws/real_world/Image_229.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_straws/real_world/Image_121.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_straws/real_world/Image_195.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_straws/real_world/Image_41.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: plastic_trash_bags/default
plastic_trash_bags/default/Image_236.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_trash_bags/default/Image_178.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_trash_bags/default/Image_47.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_trash_bags/default/Image_89.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_trash_bags/default/Image_160.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: plastic_trash_bags/real_world
plastic_trash_bags/real_world/Image_101.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_trash_bags/real_world/Image_204.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_trash_bags/real_world/Image_31.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_trash_bags/real_world/Image_54.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_trash_bags/real_world/Image_163.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: plastic_water_bottles/default
plastic_water_bottles/default/Image_8.png:   PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_water_bottles/default/Image_195.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_water_bottles/default/Image_86.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_water_bottles/default/Image_183.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_water_bottles/default/Image_9.png:   PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: plastic_water_bottles/real_world
plastic_water_bottles/real_world/Image_53.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_water_bottles/real_world/Image_215.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_water_bottles/real_world/Image_113.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_water_bottles/real_world/Image_85.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
plastic_water_bottles/real_world/Image_211.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: shoes/default
shoes/default/Image_177.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
shoes/default/Image_223.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
shoes/default/Image_10.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
shoes/default/Image_15.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
shoes/default/Image_25.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: shoes/real_world
shoes/real_world/Image_92.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
shoes/real_world/Image_108.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
shoes/real_world/Image_59.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
shoes/real_world/Image_120.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
shoes/real_world/Image_101.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: steel_food_cans/default
steel_food_cans/default/Image_26.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
steel_food_cans/default/Image_121.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
steel_food_cans/default/Image_194.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
steel_food_cans/default/Image_108.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
steel_food_cans/default/Image_130.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: steel_food_cans/real_world
steel_food_cans/real_world/Image_27.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
steel_food_cans/real_world/Image_147.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
steel_food_cans/real_world/Image_12.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
steel_food_cans/real_world/Image_7.png:   PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
steel_food_cans/real_world/Image_216.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: styrofoam_cups/default
styrofoam_cups/default/Image_195.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
styrofoam_cups/default/Image_6.png:   PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
styrofoam_cups/default/Image_95.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
styrofoam_cups/default/Image_110.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
styrofoam_cups/default/Image_244.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: styrofoam_cups/real_world
styrofoam_cups/real_world/Image_129.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
styrofoam_cups/real_world/Image_109.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
styrofoam_cups/real_world/Image_105.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
styrofoam_cups/real_world/Image_76.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
styrofoam_cups/real_world/Image_58.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: styrofoam_food_containers/default
styrofoam_food_containers/default/Image_86.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
styrofoam_food_containers/default/Image_244.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
styrofoam_food_containers/default/Image_79.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
styrofoam_food_containers/default/Image_119.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
styrofoam_food_containers/default/Image_73.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: styrofoam_food_containers/real_world
styrofoam_food_containers/real_world/Image_183.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
styrofoam_food_containers/real_world/Image_57.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
styrofoam_food_containers/real_world/Image_188.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
styrofoam_food_containers/real_world/Image_19.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
styrofoam_food_containers/real_world/Image_50.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: tea_bags/default
tea_bags/default/Image_8.png:   PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
tea_bags/default/Image_109.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
tea_bags/default/Image_94.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
tea_bags/default/Image_121.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
tea_bags/default/Image_24.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

FOLDER: tea_bags/real_world
tea_bags/real_world/Image_139.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
tea_bags/real_world/Image_2.png:   PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
tea_bags/real_world/Image_75.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
tea_bags/real_world/Image_18.png:  PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced
tea_bags/real_world/Image_225.png: PNG image data, 256 x 256, 8-bit/color RGB, non-interlaced

Is there a need to normalize file names?

```bash
find . -maxdepth 2 -type d | grep ' '

```

No filenames with spaces.

```bash
find . -maxdepth 2 -type d | grep -E '[^A-Za-z0-9_./-]'

```

No filenames with special symbols.

```bash
find . -maxdepth 2 -type d \
  | awk -F/ 'length($NF) > 30 { print $0 }'

```

No filenames longer than 30 symbols.


```bash
find . -print | LC_CTYPE=C grep -n '[^ -~]'

```

No unicode symbols in filenames.

----

Are there classes with less than 50 images? 

```bash
find . -type f -name "*.png" | sed 's|/[^/]*$||' | sort | uniq -c | sort -n

```

 250 ./aerosol_cans/default
 250 ./aerosol_cans/real_world
 250 ./aluminum_food_cans/default
 250 ./aluminum_food_cans/real_world
 250 ./aluminum_soda_cans/default
 250 ./aluminum_soda_cans/real_world
 250 ./cardboard_boxes/default
 250 ./cardboard_boxes/real_world
 250 ./cardboard_packaging/default
 250 ./cardboard_packaging/real_world
 250 ./clothing/default
 250 ./clothing/real_world
 250 ./coffee_grounds/default
 250 ./coffee_grounds/real_world
 250 ./disposable_plastic_cutlery/default
 250 ./disposable_plastic_cutlery/real_world
 250 ./eggshells/default
 250 ./eggshells/real_world
 250 ./food_waste/default
 250 ./food_waste/real_world
 250 ./glass_beverage_bottles/default
 250 ./glass_beverage_bottles/real_world
 250 ./glass_cosmetic_containers/default
 250 ./glass_cosmetic_containers/real_world
 250 ./glass_food_jars/default
 250 ./glass_food_jars/real_world
 250 ./magazines/default
 250 ./magazines/real_world
 250 ./newspaper/default
 250 ./newspaper/real_world
 250 ./office_paper/default
 250 ./office_paper/real_world
 250 ./paper_cups/default
 250 ./paper_cups/real_world
 250 ./plastic_cup_lids/default
 250 ./plastic_cup_lids/real_world
 250 ./plastic_detergent_bottles/default
 250 ./plastic_detergent_bottles/real_world
 250 ./plastic_food_containers/default
 250 ./plastic_food_containers/real_world
 250 ./plastic_shopping_bags/default
 250 ./plastic_shopping_bags/real_world
 250 ./plastic_soda_bottles/default
 250 ./plastic_soda_bottles/real_world
 250 ./plastic_straws/default
 250 ./plastic_straws/real_world
 250 ./plastic_trash_bags/default
 250 ./plastic_trash_bags/real_world
 250 ./plastic_water_bottles/default
 250 ./plastic_water_bottles/real_world
 250 ./shoes/default
 250 ./shoes/real_world
 250 ./steel_food_cans/default
 250 ./steel_food_cans/real_world
 250 ./styrofoam_cups/default
 250 ./styrofoam_cups/real_world
 250 ./styrofoam_food_containers/default
 250 ./styrofoam_food_containers/real_world
 250 ./tea_bags/default
 250 ./tea_bags/real_world

