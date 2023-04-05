class Trackable:
    def __init__(self, objectID1, centroid1):
        # store the object ID, then initialize a list of centroids
        # using the current centroid
        self.objectID1 = objectID1
        self.centroids1 = [centroid1]
        # initialize a boolean used to indicate if the object has
        # already been counted or not
        self.counted1 = False



