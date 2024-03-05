# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = """ Agglomerative hierarchical clustering is more flexible in terms of cluster shape and can thus better accommodate outliers than k-means, which assumes clusters to be spherical and often assigns outliers to a cluster based on the nearest mean, potentially skewing the cluster's attributes."""

    # type: bool (True/False)
    answers["(b)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = """ K-means clustering can produce different clusterings on different runs because it starts with randomly chosen centroids, affecting the final clusters. In contrast, agglomerative hierarchical clustering procedures are deterministic, producing the same clustering every time when given the same data set and parameters, as they build clusters step by step based on a clear set of rules without randomness in the initial conditions."""

    # type: bool (True/False)
    answers["(c)"] = -1

    # type: explanatory string (at least four words)
    answers["(c) explain"] = """While K-means is generally more efficient than agglomerative hierarchical clustering in terms of time and memory, it's not correct to label it the most efficient algorithm universally. Efficiency varies with the task and dataset."""

    # type: bool (True/False)
    answers["(d)"] = -1

    # type: explanatory string (at least four words)
    answers["(d) explain"] = """SSE is decreased when splitting; for the same amount and configuration of points we have now two centroids. It allows points to be closer to a centroid, thus reducing the total squared distance within the cluster. This process typically results in a more refined clustering where the internal cohesion of each cluster is increased, and the overall variation within clusters, as measured by SSE, is decreased."""

    # type: bool (True/False)
    answers["(e)"] = 1

    # type: explanatory string (at least four words)
    answers["(e) explain"] = """In K-means clustering, a decrease in SSE (Sum of Squared Errors) indicates that data points are closer to their respective centroids, which directly implies an increase in cluster cohesion."""

    # type: bool (True/False)
    answers["(f)"] = 1

    # type: explanatory string (at least four words)
    answers["(f) explain"] = """In K-means clustering, an increase in SSB (the Between-Cluster Sum of Squares) indicates that clusters are further apart from each other, which directly implies an increase in cluster separation."""

    # type: bool (True/False)
    answers["(g)"] = -1

    # type: explanatory string (at least four words)
    answers["(g) explain"] = """Improving cohesion by reducing SSE does not necessarily improve separation (increase SSB) in K-means, as these metrics can be influenced by changes in cluster assignments and centroids, yet their relationship is complex and context-dependent."""

    # type: bool (True/False)
    answers["(h)"] = 1

    # type: explanatory string (at least four words)
    answers["(h) explain"] = """For a fixed dataset and number of clusters, the sum of SSE (within-cluster variance) and SSB (between-cluster variance) remains constant, reflecting the partitioning of total variance."""

    # type: bool (True/False)
    answers["(i)"] = 1

    # type: explanatory string (at least four words)
    answers["(i) explain"] = """An increase in cohesion, by reducing within-cluster variance (SSE), can indirectly lead to an increase in separation (SSB), as the total variance is partitioned between SSE and SSB, maintaining a balance."""

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = """The clusters appear to be way too distant to attract points from the another."""

    # type: bool (True/False)
    answers["(b)"] = -1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = """The resulting clusters will have points from both shaded regions as they are too close to each other and not in circular or global shape. KMeans doesn't work well with non globular shapes and this is a prime example."""

    # type: bool (True/False)
    answers["(c)"] = 1

    # type: explanatory string (at least four words)
    answers["(c) explain"] = """The central centroid is too far away from the other points and will attract none, so it will contain an empty cluster."""

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = """(R^2) * 4"""

    # type: a string that evaluates to a float
    answers["(b) SSE"] = """(a^2 + b^2 + c^2) * 4"""

    # type: a string that evaluates to a float
    answers["(c) SSE"] = """(R^2 + (R/2)^2) * 4"""

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 1

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = """All of the circles are sufficiently close to each other. One centroid will go to C, one will go to A but will be skewed to the right, and one will be in B and will be very skewed to the right."""

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = """The points from A will go to A. One centroid from B will move to C but will be skewed to the left, while the remaining will be kept in B but will be skewed to the left."""

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "Circle C has too many points and is too far away from everything else. No other centroids will be attached to it. The left-most centroid will move to the middle. "

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = {'GROUP A', 'GROUP B'}

    # type: explanatory string (at least four words)
    answers["(a) explain"] = """Group A and B have their closest minimum distance. The rightmost GROUP A element and leftmost GROUPB element."""

    # type: set
    answers["(b)"] = {'GROUP A', 'GROUP C'}

    # type: explanatory string (at least four words)
    answers["(b) explain"] = """Group A's middle element and Group C's bottomost element have the best max link distance. It is too big between A and B's extremes and B's extreme is just too far away"""

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = {'B','C','E', 'F', 'I', 'J', 'L', 'M'}

    # type: set
    answers["(a) boundary"] = {'G', 'D'}

    # type: set
    answers["(a) noise"] = {'H','A'}

    # type: set
    answers["(b) cluster 1"] = {'I', 'J', 'L', 'M'}

    # type: set
    answers["(b) cluster 2"] = {'B','C','E', 'F', 'G', 'D'}

    # type: set
    answers["(b) cluster 3"] = {}

    # type: set
    answers["(b) cluster 4"] = {}

    # type: set
    answers["(c)-a core"] = {'B','C','E', 'F','I', 'J', 'L', 'M'}
    # type: set
    answers["(c)-a boundary"] = {'G', 'D', 'A', 'H'}

    # type: set
    answers["(c)-a noise"] = {}

    # type: set
    answers["(c)-b cluster 1"] = {'I', 'J', 'L', 'M', 'H'}

    # type: set
    answers["(c)-b cluster 2"] = {'B','C','E', 'F', 'G', 'D', 'A'}

    # type: set
    answers["(c)-b cluster 3"] = {}

    # type: set
    answers["(c)-b cluster 4"] = {}

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "Cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Cluster 4 has the most diverse composition of land cover classifications compared to the other clusters."

    # type: string
    answers["(b)"] = "Cluster 2"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "It has the least diverse composition of land cover classifications compared to the other clusters."

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = """Dataset Z"""

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = """Very defined. Very short distance between each dataset. we should find a dataset that shows four clusters of equal size, with each cluster tightly grouped to correspond to the low distances within clusters. Dataset Z is the best one for this."""

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = """We do see great distances between Row 2 column 4 and Row 4 column 2. Row 1 and Row3 also all have different colors, indicating many types of different distances. Those should
    correspond to the two clusters closest to each other (A and C). With this information, we have found clusters sufficiently spaced apart to correspond to the high distances between them"""

    # type: string
    answers["(a) Matrix 2"] = """Dataset X"""

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = """Two central blocks are bluer, indicating much better cohesion. These are clusters B and C. The other 2 do not have this attribute, and this is shown in Dataset X, where B and C are much more orderly."""

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = """Row 1 and 4 have all different colors. No 2 distances are the same. Red clusters are not very red, meaning smaller distance between the clusters."""

    # type: string
    answers["(a) Matrix 3"] = """Dataset Y"""

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = """Once again, bluer blocks in the middle. Representing B and C. Less blue blocks on the extremes, in fact the lightest blue of all  three diagonals, indicating
    the less coherent clusters,  such as Dataset Y's A and D."""

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] ="""Row 1 and 2 have all different colors, and all blocks are impure, many differnet colors together,
    tending to the blue. This mean that all clusters must have 2 cluster close by with the third one being distant."""

    # type: string
    answers["(b) Row 1"] = """Cluster A"""

    # type: string
    answers["(b) Row 2"] = """Cluster B"""

    # type: string
    answers["(b) Row 3"] = """Cluster C"""

    # type: string
    answers["(b) Row 4"] = """Cluster D"""

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = """Less crisp, so either A or D. All blocks have different colors, meaning very different distances. Last block is red, meaning greatest distance from the last element, which is Cluster D. So it is Cluster A"""

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = """More crisp, so either B or C. Same color for the adjacent diagonal-blocks, meaning same distance. Last block is yellow, so  the furthest block (Cluster D), is the furthest, meaning this is cluster B."""

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = """More crisp, so either B or C. Same color for the adjacent diagonal-blocks, meaning same distance. First block is yellow, so  the first block (Cluster A), is the furthest, meaning this is cluster C."""

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = """Less crisp, so either A or D. All blocks have different colors, meaning very different distances. First block is red, meaning greatest distance from the first element, which is Cluster A. So it is Cluster D"""

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ["hierarchical", "overlapping", "complete"]
    
    # type: list
    answers["(b)"] = ["partitional", "exclusive", "complete"]

    # type: list
    answers["(c)"] = ["partitional", "fuzzy", "partial"]

    # type: list
    answers["(d)"] = ["hierarchical", "overlapping", "partial"]

    # type: list
    answers["(e)"] = ["partitional", "exclusive", "complete"]

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "Partitional because students are partitioned into distinct letter grades. Exclusive because each student can receive at max one letter grade. Complete because every student gets assigned to a cluster based on their letter grade."

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "No"

    # type: string
    answers["(a) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "You could only really use it for b. You could use it for a as well, but the results would not be that good. B has defined clusters of higher density in lesser dense areas."

    # type: string
    answers["(b) Figure (a)"] = "No"

    # type: string
    answers["(b) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The clusters are not well defined enough and the shapes are not globular in figure a. In figure b, we have 3 globular shapes (eyes and node) and the mouth shape, so as long as there are k=4 clusters and hopefully the centroids migrate well enough, it should provide a success."

    # type: string
    answers["(c)"] = ""

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
