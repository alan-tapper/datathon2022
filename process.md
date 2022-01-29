#### [Abstract](index.md)            [Process and Insights](process.md)            [Visualizations](visuals.md)            [Next Steps](nextsteps.md)

<br>

# Process

<br>

We started the project by analyzing the data to search for simple patterns. We quickly realized that this was a pretty sparse graph, as about 1 in 3000 possible connections existed in the graph. This meant that some of our approaches had to be modified. We could just predict that no pair of nodes would be connected, and be right more than 99% of the time. But we wanted to do better than that.

<br>

Another thing we realized was that some page types had significantly more pages than others, and that those pages were not equally well-connected. Also, nodes of the same page type are significantly more likely to be connected than those with differing page types.

<br>

The sparseness of the graph was a major obstacle in creating any sort of model. One thing we tried was to take a random subgraph and analyze the properties.