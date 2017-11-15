<h1>Safe Trip</h1>

Web platform that will help you to find not only the <b>fastest</b> but the <b>safest</b> route on the map in <b>Lviv</b><br />

<h3>How does it <b>work</b>?</h3>
* check the departure and destination points
* click "BUILD A ROUTE" button [example](examples/overall.jpg)

<b>ATTENTION</b><br />
It is a demo version, so you can get unwarranted errors. <br />
Just try to delete all the points and try again <br />

<h3>How do we <b>measure crime level</b> on the streets?<br /></h3>
We downloaded a database of crimes which includes:
* thefts
* frauds
* lootings
* car accidents
On each of the streets in Lviv<br />
After that we calculated the sum of all this crimes on particular street<br /> 

<h3>What routes do we offer?</h3><br />
* <b>fastest</b> route
* <b>safest route v1</b> - we calculate the "score"(level of danger) on the route
as the sum of all the crimes on the streets that you've covered
* <b>safest route v2</b> - we calculate the "score"(level of danger) on the route
as the sum of all the crimes on the streets that you've covered <b>in relation to the distance that you covered on particular street</b>.
So if you've covered half of the street that has 20 crimes on it, your score will be 10

<br />

<h3>Algorithm</h3>
We used simple <b>Dijkstra</b> approach to calculate the safest and shortest distance between points<br />
After rewriting the algorithm using <b>heaps</b> for rarified graphs, the productivity increased rapidly
