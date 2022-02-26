
# How do ethnicity, poverty, and historical events influence education? — Visualization on NYC Graduation & Dropout Rates in 21st Century

February 25, 2022

As part of my coursework in information visualization class, I read [this article](https://www.nytimes.com/2016/06/12/magazine/choosing-a-school-for-my-daughter-in-a-segregated-city.html) about racial segregation in New York City schools and the impact it has on students as well as related historical topics and changes.

## Objectives

- Visualizing the change in graduation and drop-out rates from 2001 to 2016 to show the development of education outcomes for New York City students.
- Show the different rates with respect to students’ ethnicity and poverty, demonstrating the advantages and disadvantages that the demographical factors bring to NYC students.
- Most importantly, note important research findings, publications, historical events, and the establishment of policies against racial segregation in the timeline to verify whether the forces actually make a difference for NYC students, especially those disadvantaged.

• **Your design process**: What did you try? (feel free to include screenshots). What examples did you look at for inspiration? (again, screenshots are welcome). The expectation is that you tried multiple things and iterated over your design over the several weeks of this project. Describe what you liked or didn't like about your initial design, and how you arrived at your final implementation. 

## Design Process

### Initial sketches and making the choice

I have quite a few other ideas and sketches before finally landing on this one. To see complete previous sketches, click [here](https://www.notion.so/SI649-Individual-Project-f65dba0e2ab344c592f4b78c69ce9e9d). 

**1. Black & Hispanic Student Performance and Segregation** 

![IMG_1826.jpg](Blog%20Post%2038aea/IMG_1826.jpg)

In this first plot, I would like to look into how the percentage of black and Hispanic students in the school may affect the black and Hispanic students’ academic performance. However, during my implementation, I find that it is very difficult to deal with the values that are noted with ‘s’, which means that the students’ number is too small to be a convincing sample. Considering the fact that those smaller samples can also influence the overall result, I decide not to use this one.

**2. Graduation Rates Over the Years**

![IMG_1825.jpg](Blog%20Post%2038aea/IMG_1825.jpg)

Here I plan to draw a line plot to show the graduation rate for students with different ethnicity from 2001 to 2016 using the dataset. The plot should be pretty straightforward as different colors denote different ethnic groups. I will elaborate more on my iterations later in this blog.

**3. Geographic Distribution of Black and Hispanic Student Population in NYC and Test Results**

![IMG_1827.jpg](Blog%20Post%2038aea/IMG_1827.jpg)

I plan to make a visualization using color to denote the black and Hispanic student population by New York City boroughs. However, I find that it is difficult to make this visualization both effective and informative. The geographical division only by boroughs are not detailed enough, but to encode the data by school district is requiring outside datasets that I am extremely unfamiliar with; moreover, I am also not familiar with how to encode data into geographical information from external sources in either Tableau or Altair, so it is really difficult for me to actually implement this visualization.

### Iterations

After choosing the dataset on graduation rates, I also look at the dataset more closely to see whether there are more information fields worth exploring.

After reading the original article, my impression is that the visualizations should also focus on the impact of ethnicity on students’ study outcomes. Graduation rates, among many different factors, can represent the overall performance of students in a school. Generally speaking, we regard schools or student groups with higher graduation rates and lower drop-out rates to perform better in school so that they are able to graduate. Since I am exploring the impact of ethnicity, I group the students by their ethnicity in the visualization. Also, in the article, the author mentioned the gap in income levels between different ethnic groups and NYC geographical regions, so I made a similar visualization in terms of the different economic status rather than ethnic groups.

Another thing that I find particularly important in the article is how people in different positions are working together to promote NYC education and change the racial segregation issue. The author mentioned many pieces of research that are published,  new government policies, and people such as school principals’ response to the racial segregation during the time period. Therefore, Apart from the basic line plot of the percentage of graduate students, I also try to integrate the new pieces by the time so that we can try to see whether they actually make a difference to the students’ performance.

To represent the news more quantitatively, I counted how many pieces of news are mentioned in the corresponding year from 2001 to 2016 and use them as data on the y-axis. To clarify, I did not include the author’s personal actions about her daughter since those are not public news or events. To view the exact news each year, the user can simply hover on the bar to see the text content in the tooltip. 

### To be more interactive

To make the demonstration more clear and engaging, I also added more interactive elements in the visualization. To view the line of a specific ethnicity, you can simply click on the corresponding legend; to cancel the selection, click any white space. Hovering on bars and data points will also show the exact data in the tooltip. Since there are a lot of data points, and we are focusing on the trend rather than the absolute values, I use tooltip instead of labels.

Here is my visualization outcome (day mode recommended).

[https://share.streamlit.io/eugeniayang/si649/main/yangziqi.py](https://share.streamlit.io/eugeniayang/si649/main/yangziqi.py)

## Qualitative Self-evaluation

It looks to me that the visualization is reasonably clear and well-designed. In terms of conducting the information, it has successfully shown the changing graduation rates and the data-ink index is high. In terms of design principles, it follows data integrity and does not distort the data. The reference lines and markers on the axis also make it easier to read the data. Also, I use the default color palette for different ethnicities and economic statuses, which has a rather good aesthetic taste.

To elaborate more on the specific findings, we can infer from the visualization that the overall graduation rate is increasing and the drop-out rate decreasing over the years, which represents the development of NYC education in the decades. Also, we can see that the graduation rates of black and Hispanic students and students who are economically disadvantaged are overall less likely to graduate and more highly to drop out of school, which verifies their disadvantage. However, we are glad to see that the differences between those groups are decreasing. More importantly, we can see that in or after the years in which there are historical events against racial segregation in NYC schools, there is an increase in graduation rate (for example, in 2009 in the ethnicity graph ) and a decrease in drop-out rate(for example, in 2007 and 2014 in both visualizations). Therefore, we can infer that the research, policies, and responses from principals more or less make a difference in promoting educational equity among black and Hispanic students.

## Formal Evaluation Methodology

Firstly, to evaluate the visualization in terms of accessibility, I can use website design checking tools to evaluate elements such as contrast and title readability. Since the visualization is aimed at more professional audiences, though, the requirement for accessibility is not extremely high for the visualization.

The most effective evaluation method can be doing user interviews and usability testings to check if the users know how to read the visualization, interact with the visualization, and whether they think the intended objectives can be interpreted from the visualization. To be more specific, the interviews will focus on what information does the audience gets from the visualizations, and the user testing sessions will focus more on whether the audience is able to trigger the interactive elements either independently or with simple hints and assistants.

Lastly, to evaluate the visualization from a more professional point of view, we can set up focus groups consisting of data science students or professionals to discuss their views towards the visualization. The criteria will be in various different aspects, including ethical concerns, general design, aesthetic task, data-ink rate, etc...

## Reference

1. *NYC Moving Guide: The New York City Boroughs, Explained | PODS Blog*. (2019, March 28). Containing the Chaos. https://www.pods.com/blog/2019/03/nyc-moving-guide-the-new-york-city-boroughs-explained/
2. *Test Results*. (2019). Nyced.org. https://infohub.nyced.org/reports/academics/test-results
3. *Graduation Results*. (n.d.). Infohub.nyced.org. https://infohub.nyced.org/reports/academics/graduation-results
4. Bremer, N. (n.d.). *The Design Process of “Why Do Cats & Dogs ...?”* Visual Cinnamon. Retrieved February 25, 2022, from https://www.visualcinnamon.com/2019/04/designing-google-cats-and-dogs/
5. Hannah-Jones, N. (2016, June 9). Choosing a School for My Daughter in a Segregated City. *The New York Times*. https://www.nytimes.com/2016/06/12/magazine/choosing-a-school-for-my-daughter-in-a-segregated-city.html

‌