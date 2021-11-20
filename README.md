
# Short-term Objective

I intend to use this repository as a tool to plan and verify the nutritional content of my diet.

# Long-term Objective

I would like to extend it the tool to include schedules for shopping/cooking, in addition to making the information accessible in a more presentable format (perhaps a nice Angular-based webpage).

# What's with the name?

*air-nayr-ungs-plan* is intended to sound like the German word "Ernährungsplan" when pronounced by an English-speaker. Ernährungsplan means "nutrition plan".

# Acronyms

* DRI: Dietary Reference Intake
* PAN: Physicians Association for Nutrition
* RDA: Recommended Dietary Allowances
* WWEIA: What We Eat In America

# Notes on relevant data formats

Data from USDA on a type of food is provided in one of 5 types:

> Includes five distinct data types that provide information on food and nutrient profiles: Foundation Foods, Food and Nutrient Database for Dietary Studies 2017-2018 (FNDDS 2017-2018), National Nutrient Database for Standard Reference Legacy Release (SR Legacy), USDA Global Branded Food Products Database (Branded Foods), and Experimental Foods. Each of these data types has a unique purpose and unique attributes.

(See [4])


# Rules of Thumb

The [TBV] annotation means that the fact/rule was taken from an unacademic source, such as a discussion forum like Reddit; it still needs to be verified by an analysis based on the nutrient database. In the meantime, the rules could be used to guide the selection of ingredients for the weekly diet plan, the nutrition content of which is verified using the USDA nutrition database.

* [TBV] [Sesame seeds have more bioavailable calcium than milk](https://www.reddit.com/r/AskReddit/comments/5fmhk6/comment/dalq6ts/?utm_source=share&utm_medium=web2x&context=3) when ease of consumption is considered
* [TBV] [Broccoli is a better source of vitamin C compared to oranges](https://www.reddit.com/r/AskReddit/comments/5fmhk6/broccoli_is_a_better_source_of_vitamin_c_compared/)
* [TBV] Bell Peppers are an excellent source of Vitamin C
  * [What are some cheap sources of Vitamin C?](https://www.reddit.com/r/EatCheapAndHealthy/comments/27mpps/what_are_some_cheap_sources_of_vitamin_c/)
  * [Vitamin C in some common foods](https://www.reddit.com/r/dataisbeautiful/comments/8fyu1i/vitamin_c_in_some_common_foods_oc/)


# From where does the nutrition information originate?

I intend to use https://github.com/jithesh82/noms, which was forked from https://github.com/noahtren/noms, which reads data from a nutritional database compiled by the USDA. To make it easy to work with noms (which I currently belive requires maintenance), I've included it in this project as a git submodule.

# Questions

* There are 21 amino acids used to build proteins in the human body. These proteins are essential for bodily functions in humans. Of the 21 types, 9 are essential, as the human body cannot synthesize them in any way. The other 12 can be synthesized by the human body. [13] Questions:
  * What is the effect of forcing the body to synthesize all the non-essential amino acids versus supplying all of them in the diet? 
  * Is the implementation of the mechanism which forms these non-essential amino acids dynamic in terms of the resources allocated to it? 
  * Is the body's ability to synthesize the non-essential amino acids reduced when all the amino acids are supplied regularly as part of the diet? 
* Should one abandon a traditional diet for one perceived to be healthier?  This is like a sensor fusion problem - adjustment of a prior based on new information. Here the state is the belief in what constitutes the optimal diet. Consider belief in the traditional diet to be the prior. Consider that any diet may have unintended side effects, which are some function of the interaction between the specifics of one person's body and the diet. Here, diet includes any mistakes or inconsistencies in preparation - i.e. it means the concrete nutritional delivery to the body after absorption, and not the content of the ingredients in their raw form. Decay, cooking, the digestive process, and the efficiency of the bodily transport systems seem to be the main candidates for loss or modification of nutritional content that exist between the raw ingredients (which are easiest to analyze) and the actual nutrients absorbed by the body. A traditional diet has been tested by time and on one's ancestors (assuming dietary habits are passed down from parents to children). This represents a long-running test on people whose genetic composition is similar to the person who inherits that diet. In contrast, adopting a diet currently believed to be optimal or better than traditional ones seems to represent an increased uncertainty w.r.t. the side effects of this new diet. Questions
  * How can one verify that a diet is having the desired effect on the body, and is not actually introducing long-term side effects that one wouldn't easily notice (for example heightened risk of cancer)? 
  * There are studies done on diet recommendations from various health bodies, such as the Harvard School of Public Health. 
    * How well do the results of these studies generalize across the human population? 
    * Could it be that genetic differences between humans can result in adverse effects not encountered in or predicted by the studies?
  * Is it reasonable to modify the human body as a system which simply requires a set of bioavailable nutrients to function correctly.

* Is the meaning of bioavailable that the body can absorb the nutrients from the diet?

# References

* [1] [DEU - PAN International](https://pan-int.org/resources/)
* [2] [USA - What We Eat In America (WWEIA)](https://data.nal.usda.gov/dataset/what-we-eat-america-wweia-database)
* [3] [Food and Nutrient Database for Dietary Studies (FNDDS)](https://data.nal.usda.gov/dataset/food-and-nutrient-database-dietary-studies-fndds)
* [4] [FoodData Central](https://fdc.nal.usda.gov/)
* [5] [Dietary Reference Intakes (DRIs): Estimated Average Requirements](https://www.nal.usda.gov/sites/default/files/fnic_uploads/recommended_intakes_individuals.pdf)
* [6] [Glycemic Index](https://glycemicindex.com/)
* [7] [Effects of cooking on vitamins](https://www.beyondveg.com/tu-j-l/raw-cooked/raw-cooked-2e.shtml)
* [8] [Comparison of vitamin levels in raw vs. cooked foods, Cooking's effect on bioavailability](https://www.beyondveg.com/tu-j-l/raw-cooked/raw-cooked-2f.shtml)
* [9] [Effects of cooking on minerals](https://www.beyondveg.com/tu-j-l/raw-cooked/raw-cooked-2g.shtml)
* [10] [Harvard School of Public Health: Vegetables and Fruits](https://www.hsph.harvard.edu/nutritionsource/what-should-you-eat/vegetables-and-fruits/)
* [11] [Harvard School of Public Health: Healthy Eating Plate](https://www.hsph.harvard.edu/nutritionsource/healthy-eating-plate/)
* [12] [Harvard School of Public Health: Healthy Weight](https://www.hsph.harvard.edu/nutritionsource/healthy-weight/)
* [13] [Harvard School of Public Health: Protein](https://www.hsph.harvard.edu/nutritionsource/what-should-you-eat/protein/)