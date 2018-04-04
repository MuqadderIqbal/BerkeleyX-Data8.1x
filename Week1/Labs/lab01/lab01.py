
# coding: utf-8

# # Lab 1: Introduction to Python
# 
# Welcome to Lab 1!  Each week you will complete a lab assignment like this one. In this lab, you'll get started with the Python programming language through numbers, names, and expressions.
# 
# As you go, please regularly select **Save and Checkpoint** from the `File` menu below the Jupyter logo to save your work.

# ## 1. Numbers
# 
# Quantitative information arises everywhere in data science. In addition to representing commands to print out lines, expressions can represent numbers and methods of combining numbers. The expression `3.2500` evaluates to the number 3.25. (Run the cell and see.)

# In[1]:


3.2500


# Notice that we didn't have to `print`. When you run a notebook cell, if the last line has a value, then Jupyter helpfully prints out that value for you. However, it won't print out prior lines automatically. If you want to print out a prior line, you need to add the `print` statement. Run the cell below to check.

# In[2]:


print(2)
3
4


# Above, you should see that 4 is the value of the last expression, 2 is printed, but 3 is lost forever because it was neither printed nor last.
# 
# You don't want to print everything all the time anyway.  But if you feel sorry for 3, change the cell above to print it.

# ### 1.1. Arithmetic
# The line in the next cell subtracts.  Its value is what you'd expect.  Run it.

# In[3]:


3.25 - 1.5


# Many basic arithmetic operations are built in to Python.  The textbook section on [Expressions](http://www.inferentialthinking.com/chapters/03/1/expressions.html) describes all the arithmetic operators used in the course.  The common operator that differs from typical math notation is `**`, which raises one number to the power of the other. So, `2**3` stands for $2^3$ and evaluates to 8. 
# 
# The order of operations is what you learned in elementary school, and Python also has parentheses.  For example, compare the outputs of the cells below. Use parentheses for a happy new year!

# In[4]:


2+6*5-6*3**2*2**3/4*7


# In[5]:


2+(6*5-(6*3))**2*((2**3)/4*7)


# In standard math notation, the first expression is
# 
# $$2 + 6 \times 5 - 6 \times 3^2 \times \frac{2^3}{4} \times 7,$$
# 
# while the second expression is
# 
# $$2 + (6 \times 5 - (6 \times 3))^2 \times (\frac{(2^3)}{4} \times 7).$$
# 
# **Question 1.1.1.** <br /> Write a Python expression in this next cell that's equal to $5 \times (3 \frac{10}{11}) - 49 \frac{1}{3} + 2^{.5 \times 22} - \frac{7}{33}$.  That's five times three and ten elevenths, minus 49 and a third, plus two to the power of half of 22, minus 7 33rds.  By "$3 \frac{10}{11}$" we mean $3+\frac{10}{11}$, not $3 \times \frac{10}{11}$.
# 
# Replace the ellipses (`...`) with your expression.  Try to use parentheses only when necessary.
# 
# *Hint:* The correct output should be a familiar number.

# In[6]:


...


# ## 2. Names
# In natural language, we have terminology that lets us quickly reference very complicated concepts.  We don't say, "That's a large mammal with brown fur and sharp teeth!"  Instead, we just say, "Bear!"
# 
# Similarly, an effective strategy for writing code is to define names for data as we compute it, like a lawyer would define terms for complex ideas at the start of a legal document to simplify the rest of the writing.
# 
# In Python, we do this with *assignment statements*. An assignment statement has a name on the left side of an `=` sign and an expression to be evaluated on the right.

# In[7]:


ten = 3 * 2 + 4


# When you run that cell, Python first evaluates the first line.  It computes the value of the expression `3 * 2 + 4`, which is the number 10.  Then it gives that value the name `ten`.  At that point, the code in the cell is done running.
# 
# After you run that cell, the value 10 is bound to the name `ten`:

# In[8]:


ten


# The statement `ten = 3 * 2 + 4` is not asserting that `ten` is already equal to `3 * 2 + 4`, as we might expect by analogy with math notation.  Rather, that line of code changes what `ten` means; it now refers to the value 10, whereas before it meant nothing at all.
# 
# If the designers of Python had been ruthlessly pedantic, they might have made us write
# 
#     define the name ten to hereafter have the value of 3 * 2 + 4 
# 
# instead.  You will probably appreciate the brevity of "`=`"!  But keep in mind that this is the real meaning.
# 
# **Question 2.1.** <br /> Try writing code that uses a name (like `eleven`) that hasn't been assigned to anything.  You'll see an error!

# A common pattern in Jupyter notebooks is to assign a value to a name and then immediately evaluate the name in the last line in the cell so that the value is displayed as output. 

# In[9]:


close_to_pi = 355/113
close_to_pi


# Another common pattern is that a series of lines in a single cell will build up a complex computation in stages, naming the intermediate results.

# In[10]:


bimonthly_salary = 840
monthly_salary = 2 * bimonthly_salary
number_of_months_in_a_year = 12
yearly_salary = number_of_months_in_a_year * monthly_salary
yearly_salary


# Names in Python can have letters (upper- and lower-case letters are both okay and count as different letters), underscores, and numbers.  The first character can't be a number (otherwise a name might look like a number).  And names can't contain spaces, since spaces are used to separate pieces of code from each other.
# 
# Other than those rules, what you name something doesn't matter *to Python*.  For example, this cell does the same thing as the above cell, except everything has a different name:

# In[11]:


a = 840
b = 2 * a
c = 12
d = c * b
d


# **However**, names are very important for making your code *readable* to yourself and others.  The cell above is shorter, but it's totally useless without an explanation of what it does.
# 
# According to a famous joke among computer scientists, naming things is one of the two hardest problems in computer science.  (The other two are cache invalidation and "off-by-one" errors.  And people say computer scientists have an odd sense of humor...)

# **Question 2.2.** <br /> Assign the name `seconds_in_a_decade` to the number of seconds between midnight January 1, 2010 and midnight January 1, 2020. Use Python to perform any required arithmetic.
# 
# *Hint:* If you're stuck, the next section shows you how to get hints.

# In[12]:


# Change the next line so that it computes the number of
# seconds in a decade and assigns that number the name
# seconds_in_a_decade.
seconds_in_a_decade = ...

# We've put this line in this cell so that it will print
# the value you've given to seconds_in_a_decade when you
# run it.  You don't need to change this.
seconds_in_a_decade


# ### 2.1. Checking your code
# Now that you know how to name things, you can start using the built-in *tests* to check whether your work is correct. Try not to change the contents of the test cells. 
# 
# The cell below appears only once in the notebook and loads all of the tests so that they can be run later. You can load all of the tests before you answer all questions in the notebook. You will run tests as you go to check your work along the way, and you can also run all of the tests at the end to make sure that you will receive full credit on the lab.

# In[13]:


# These lines load the tests.
from client.api.notebook import Notebook
ok = Notebook('lab01.ok')


# Running the following cell will test whether you have assigned `seconds_in_a_decade` correctly in Question 2.2. 
# 
# Sometimes the tests will give hints about what went wrong. If the test doesn't pass, read the output, adjust your answer to the question, run the answer cell again to update the name `seconds_in_a_decade`, then run this test cell again.
# 
# Sometimes the tests will tell you the answer. Rather than copying the answer, try to understand how it was reached. 

# In[14]:


# Test cell; please do not change!
_ = ok.grade('q22')


# ### 2.2. Comments
# You may have noticed this line in the cell above:
# 
#     # Test cell; please do not change!
# 
# That is called a *comment*.  It doesn't make anything happen in Python; Python ignores anything on a line after a #.  Instead, it's there to communicate something about the code to you, the human reader.  Comments are extremely useful.
# 
# <img src="http://imgs.xkcd.com/comics/future_self.png" alt="comic about comments">

# ### 2.3. Application: A physics experiment
# 
# On the Apollo 15 mission to the Moon, astronaut David Scott famously replicated Galileo's physics experiment in which he showed that gravity accelerates objects of different mass at the same rate. Because there is no air resistance for a falling object on the surface of the Moon, even two objects with very different masses and densities should fall at the same rate. David Scott compared a feather and a hammer.
# 
# You can run the following cell to watch a video of the experiment.

# In[15]:


from IPython.display import YouTubeVideo
# The original URL is:
#   https://www.youtube.com/watch?v=U7db6ZeLR5s
YouTubeVideo("U7db6ZeLR5s")


# Here's the transcript of the video:
# 
# **167:22:06 Scott**: Well, in my left hand, I have a feather; in my right hand, a hammer. And I guess one of the reasons we got here today was because of a gentleman named Galileo, a long time ago, who made a rather significant discovery about falling objects in gravity fields. And we thought where would be a better place to confirm his findings than on the Moon. And so we thought we'd try it here for you. The feather happens to be, appropriately, a falcon feather for our Falcon. And I'll drop the two of them here and, hopefully, they'll hit the ground at the same time. 
# 
# **167:22:43 Scott**: How about that!
# 
# **167:22:45 Allen**: How about that! (Applause in Houston)
# 
# **167:22:46 Scott**: Which proves that Mr. Galileo was correct in his findings.

# **Newton's Law.** Using this footage, we can also attempt to confirm another famous bit of physics: Newton's law of universal gravitation. Newton's laws predict that any object dropped near the surface of the Moon should fall
# 
# $$\frac{1}{2} G \frac{M}{R^2} t^2 \text{ meters}$$
# 
# after $t$ seconds, where $G$ is a universal constant, $M$ is the moon's mass in kilograms, and $R$ is the moon's radius in meters.  So if we know $G$, $M$, and $R$, then Newton's laws let us predict how far an object will fall over any amount of time.
# 
# To verify the accuracy of this law, we will calculate the difference between the predicted distance the hammer drops and the actual distance.  (If they are different, it might be because Newton's laws are wrong, or because our measurements are imprecise, or because there are other factors affecting the hammer for which we haven't accounted.)
# 
# Someone studied the video and estimated that the hammer was dropped 113 cm from the surface. Counting frames in the video, the hammer falls for 1.2 seconds (36 frames).

# **Question 2.3.1.** <br /> Complete the code in the next cell to fill in the *data* from the experiment.

# In[16]:


# t, the duration of the fall in the experiment, in seconds.
# Fill this in.
time = ...

# The estimated distance the hammer actually fell, in meters.
# Fill this in.
estimated_distance_m = ...


# In[17]:


_ = ok.grade('q231')


# **Question 2.3.2.** <br /> Now, complete the code in the next cell to compute the difference between the predicted and estimated distances (in meters) that the hammer fell in this experiment.
# 
# This just means translating the formula above ($\frac{1}{2}G\frac{M}{R^2}t^2$) into Python code.  You'll have to replace each variable in the math formula with the name we gave that number in Python code.

# In[18]:


# First, we've written down the values of the 3 universal
# constants that show up in Newton's formula.

# G, the universal constant measuring the strength of gravity.
gravity_constant = 6.674 * 10**-11

# M, the moon's mass, in kilograms.
moon_mass_kg = 7.34767309 * 10**22

# R, the radius of the moon, in meters.
moon_radius_m = 1.737 * 10**6

# The distance the hammer should have fallen over the
# duration of the fall, in meters, according to Newton's
# law of gravity.  The text above describes the formula
# for this distance given by Newton's law.
# **YOU FILL THIS PART IN.**
predicted_distance_m = ...

# Here we've computed the difference between the predicted
# fall distance and the distance we actually measured.
# If you've filled in the above code, this should just work.
difference = predicted_distance_m - estimated_distance_m
difference


# In[19]:


_ = ok.grade('q232')


# ## 3. Calling functions
# 
# The most common way to combine or manipulate values in Python is by calling functions. Python comes with many built-in functions that perform common operations.
# 
# For example, the `abs` function takes a single number as its argument and returns the absolute value of that number.  The absolute value of a number is its distance from 0 on the number line, so `abs(5)` is 5 and `abs(-5)` is also 5.

# In[20]:


abs(5)


# In[21]:


abs(-5)


# ### 3.1. Application: Computing walking distances
# Chunhua is on the corner of 7th Avenue and 42nd Street in Midtown Manhattan, and she wants to know far she'd have to walk to get to Gramercy School on the corner of 10th Avenue and 34th Street.
# 
# She can't cut across blocks diagonally, since there are buildings in the way.  She has to walk along the sidewalks.  Using the map below, she sees she'd have to walk 3 avenues (long blocks) and 8 streets (short blocks).  In terms of the given numbers, she computed 3 as the difference between 7 and 10, *in absolute value*, and 8 similarly.  
# 
# Chunhua also knows that blocks in Manhattan are all about 80m by 274m (avenues are farther apart than streets).  So in total, she'd have to walk $(80 \times |42 - 34| + 274 \times |7 - 10|)$ meters to get to the park.
# 
# <img src="map.jpg" alt="visual map about distance calculation"/>
# 
# **Question 3.1.1.** <br /> Finish the line `num_avenues_away = ...` in the next cell so that the cell calculates the distance Chunhua must walk and gives it the name `manhattan_distance`.  Everything else has been filled in for you.  **Use the `abs` function.**

# In[22]:


# Here's the number of streets away:
num_streets_away = abs(42-34)

# Compute the number of avenues away in a similar way:
num_avenues_away = ...

street_length_m = 80
avenue_length_m = 274

# Now we compute the total distance Chunhua must walk.
manhattan_distance = street_length_m*num_streets_away + avenue_length_m*num_avenues_away

# We've included this line so that you see the distance
# you've computed when you run this cell.  You don't need
# to change it, but you can if you want.
manhattan_distance


# Be sure to run the next cell to test your code.

# In[23]:


_ = ok.grade('q311')


# ##### Multiple arguments
# Some functions take multiple arguments, separated by commas. For example, the built-in `max` function returns the maximum argument passed to it.

# In[24]:


max(2, -3, 4, -5)


# ## 4. Understanding nested expressions
# Function calls and arithmetic expressions can themselves contain expressions.  You saw an example in the last question:
# 
#     abs(42-34)
# 
# has 2 number expressions in a subtraction expression in a function call expression.  And you probably wrote something like `abs(7-10)` to compute `num_avenues_away`.
# 
# Nested expressions can turn into complicated-looking code. However, the way in which complicated expressions break down is very regular.
# 
# Suppose we are interested in heights that are very unusual.  We'll say that a height is unusual to the extent that it's far away on the number line from the average human height.  [An estimate](http://press.endocrine.org/doi/full/10.1210/jcem.86.9.7875?ck=nck&) of the average adult human height (averaging, we hope, over all humans on Earth today) is 1.688 meters.
# 
# So if Aditya is 1.21 meters tall, then his height is $|1.21 - 1.688|$, or $.478$, meters away from the average.  Here's a picture of that:
# 
# <img src="numberline_0.png" alt="number line showing height difference and teaching abs value">
# 
# And here's how we'd write that in one line of Python code:

# In[25]:


abs(1.21 - 1.688)


# What's going on here?  `abs` takes just one argument, so the stuff inside the parentheses is all part of that *single argument*.  Specifically, the argument is the value of the expression `1.21 - 1.688`.  The value of that expression is `-.478`.  That value is the argument to `abs`.  The absolute value of that is `.478`, so `.478` is the value of the full expression `abs(1.21 - 1.688)`.
# 
# Picture simplifying the expression in several steps:
# 
# 1. `abs(1.21 - 1.688)`
# 2. `abs(-.478)`
# 3. `.478`
# 
# In fact, that's basically what Python does to compute the value of the expression.

# **Question 4.1.** <br /> Say that Botan's height is 1.85 meters.  In the next cell, use `abs` to compute the absolute value of the difference between Botan's height and the average human height.  Give that value the name `botan_distance_from_average_m`.
# 
# <img src="numberline_1.png" alt="number line showing height difference and teaching abs value">

# In[26]:


# Replace the ... with an expression to compute the absolute
# value of the difference between Botan's height (1.85m) and
# the average human height.
botan_distance_from_average_m = ...

# Again, we've written this here so that the distance you
# compute will get printed when you run this cell.
botan_distance_from_average_m


# In[27]:


_ = ok.grade('q41')


# ### 4.1. More nesting
# Now say that we want to compute the most unusual height among Aditya's and Botan's heights.  We'll use the function `max`, which (again) takes two numbers as arguments and returns the larger of the two arguments.  Combining that with the `abs` function, we can compute the biggest distance from the average among the two heights:

# In[28]:


# Just read and run this cell.

aditya_height_m = 1.21
botan_height_m = 1.85
average_adult_human_height_m = 1.688

# The biggest distance from the average human height, among the two heights:
biggest_distance_m = max(abs(aditya_height_m - average_adult_human_height_m), abs(botan_height_m - average_adult_human_height_m))

# Print out our results in a nice readable format:
print("The biggest distance from the average height among these two people is", biggest_distance_m, "meters.")


# The line where `biggest_distance_m` is computed looks complicated, but we can break it down into simpler components just like we did before.
# 
# The basic recipe is repeated simplification of small parts of the expression:
# * We start with the simplest components whose values we know, like plain names or numbers.  (Examples: `aditya_height_m` or `5`.)
# * **Find a simple-enough group of expressions:** We look for a group of simple expressions that are directly connected to each other in the code, for example by arithmetic or as arguments to a function call.
# * **Evaluate that group:** We evaluate the arithmetic expressions or function calls they're part of, and replace the whole group with whatever we compute.  (Example: `aditya_height_m - average_adult_human_height_m` becomes `-.478`.)
# * **Repeat:** We continue this process, using the values of the glommed-together stuff as our new basic components.  (Example: `abs(-.478)` becomes `.478`, and `max(.478, .162)` later becomes `.478`.)
# * We keep doing that until we've evaluated the whole expression.
# 
# You can run the next cell to see a slideshow of that process.

# In[29]:


from IPython.display import IFrame
IFrame('https://docs.google.com/presentation/d/1urkX-nRsD8VJvcOnJsjmCy0Jpv752Ssn5Pphg2sMC-0/embed?start=false&loop=false&delayms=3000', 800, 600)


# Ok, your turn. 
# 
# **Question 4.1.1.** <br /> Given the heights of the Splash Triplets from the Golden State Warriors, write an expression that computes the smallest difference between any of the three heights. Your expression shouldn't have any numbers in it, only function calls and the names `klay`, `steph`, and `kevin`. Give the value of your expression the name `min_height_difference`.

# In[30]:


# The three players' heights, in meters:
klay =  2.01 # Klay Thompson is 6'7"
steph = 1.91 # Steph Curry is 6'3"
kevin = 2.06 # Kevin Durant is officially 6'9", but many suspect that he is taller.
             # (Further complicating matters, membership of the "Splash Triplets" 
             #  is disputed, since it was originally used in reference to 
             #  Klay Thompson, Steph Curry, and Draymond Green.)

# We'd like to look at all 3 pairs of heights, compute the absolute
# difference between each pair, and then find the smallest of those
# 3 absolute differences.  This is left to you!  If you're stuck,
# try computing the value for each step of the process (like the
# difference between Klay's heigh and Steph's height) on a separate
# line and giving it a name (like klay_steph_height_diff).
min_height_difference = ...


# In[31]:


_ = ok.grade('q411')


# ## 5. Tables

# A website called [Gapminder](https://www.gapminder.org/) collects a large variety of measurements of human health, education, and progress. Each measurement is published in a table that has one row per country and one column per year, describing how the measurement varies over time and place.
# 
# For example, [this table](https://docs.google.com/spreadsheets/d/1kmnYQzXLGVF9RbKB3Y-WuUsJFumnE4s2UWdmlskv6r4/pub#) describes the average number of years of school attended by all women 25 and older. The table has a row for each of 175 countries and a column for each year from 1970 through 2009. The data were estimated for a study by the [Institute for Health Metrics and Evaluation](http://www.healthmetricsandevaluation.org/) called "Increased educational attainment and its impact on child mortality: a systematic analysis in 175 countries from 1970 to 2009" ([link](http://www.healthmetricsandevaluation.org/resources/datasets/2010/education_attainment/education_attainment.html&sa=D&ust=1522644678563000&usg=AFQjCNG-Rn_hO868jLLBz6FRLT8LSqwUVA)).
# 
# To load tables into Python, you must first import the `datascience` module. The second line below makes sure that charts appear on the screen when you create them. You only need to execute these lines once per notebook (and each time you restart your kernel).

# In[32]:


# Don't change this cell
from datascience import *
get_ipython().run_line_magic('matplotlib', 'inline')


# Now, run the next cell in order to load the table describing years of school attended by women around the world and over time. Only the first 10 rows of the table will be displayed.

# In[33]:


school = Table.read_table('school.csv')
school


# **Question 5.1.**
# Assign the name `top_1970` to a two-column table that has the column of country names (labeled `"Row Labels"`) and the years in school in 1970, sorted by the second column in decreasing order. Notice the large difference between the country with the most average years of school and the rest in the top 10.
# 
# *Hint*: Even though 1970 is a number, treat it as text by placing it within quotation marks when using it as a label. For example, `school.select("1970")` rather than `school.select(1970)`. Column labels are always text.

# In[34]:


top_1970 = ...
top_1970


# In[35]:


_ = ok.grade('q51')


# You can create a bar chart of all the countries in the data set using the expression below.

# In[36]:


top_1970.barh('Row Labels')


# **Question 5.2** Now, to see how much these numbers have changed, assign `top_1970_with_2009` to a table with the rows in the same order, but include a third column for 2009 as well. The differences between countries are much smaller in 2009.

# In[37]:


top_1970_with_2009 = ...
top_1970_with_2009


# In[38]:


_ = ok.grade('q52')


# A bar chart for this three-column table will compare 1970 to 2009 for each country. Everywhere in the world, the average number of years that women attend school has increased, in some cases dramatically!

# In[39]:


top_1970_with_2009.barh('Row Labels')


# The [Gapminder data browser](https://www.gapminder.org/data/) includes many other tables that you can explore as well. For more information on how to load a table from the web, try the course discussion forum.

# ## 6. Completion

# Congratulations, you're done with lab 1! You can check that all tests pass by running the next cell. If all the tests are passing in your notebook when we score everybody's assignment, then you will receive full credit.

# In[40]:


# For your convenience, you can run this cell to run all the tests at once!
import os
_ = [ok.grade(q[:-3]) for q in os.listdir("tests") if q.startswith('q')]


# Finally, select **Save and Checkpoint** from the `File` menu below the Jupyter logo to save your work.
