Objects in Kubernetes

Kubernetes objects are persistent entities in the Kubernetes system. Kubernetes uses these entities to represent the state of your cluster. Specifically, they can describe:

What containerized applications are running (and on which nodes)
The resources available to those applications
The policies around how those applications behave, such as restart policies, upgrades, and fault-tolerance


Object spec and status

Almost every Kubernetes object includes two nested object fields that govern the object's configuration:
Spec and Status





Describing a kubernetes object:
When you create an object in Kubernetes, you must provide the object spec that describes its desired state, as well as some basic information about the object (such as a name). When you use the Kubernetes API to create the object (either directly or via kubectl), that API request must include that information as JSON in the request body. Most often, you provide the information to kubectl in a file known as a manifest. By convention, manifests are YAML (you could also use JSON format). Tools such as kubectl convert the information from a manifest into JSON or another supported serialization format when making the API request over HTTP.


In sample.yaml file the template has been showed


Required fields

1.  apiVersion - Which version of the Kubernetes API you're using to create this object
2.  kind - What kind of object you want to create
3.  metadata - Data that helps uniquely identify the object, including a name string, UID, and optional namespace
4.  spec - What state you desire for the object



