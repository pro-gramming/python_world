##### Difference between regular method , classmethods , staticmethods:

* Names starting with the '@' signs are called the decorators

* Regular methods within class are the ones that expect "self"
* Classmethods expect "cls"
* Staticmethods don't expect anything except "the argument itself"

##### Giveaway:

* If the methods don't include anything related to "self" or "cls" then, it safe to declare it as static.
