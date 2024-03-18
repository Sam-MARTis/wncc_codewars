Here's how it's going to be:
Pirates are going to be assigned jobs.
```python
available_pirates = set()
resource_pirates = set()
defending_pirates = set()
sweeper_pirates = set()
offensive_pirates = set()
captured_islands = dict()
interns = set()
```
All sets are cleared and updated every game frame.
All alive pirates will be stored in the available_pirates set. Since there is no callback function when a pirate dies, this is a substitute. 

Resource pirates search for resources. Rum is crucial to create more pirates and gunpowder for fighting others.
Priority: Rum > Gunpowder(priority decreases with time) > Wood
Since gunpowder spawns randomly and continuously, I was planning on initially having a large number of resource pirates that collect rum and gunpowder and clear the map of resources once. Then, I change their jobs and only keep a few resource pirates, with their number gradually decreasing with time as they get reassigned jobs.

Defending pirates go to captured islands and patrol, preventing them from being captured. If under attack, will trigger signal to build walls. Initial number is 0

Sweepers are optional units that will patrol the whole map in a thorough manner in order to clear out any missed resources and to elimminate any enemy pirates

Offensive pirates actively attack uncaptured or enemy-captured islands and try to take them over. Initial number is few but increased once a certain pirate count is reached and strategy is switched to offensive.

Captured islands contains tuples of self-captured islands along with their respective number of defending pirates.

Interns are temporary storage locations for newly spawned pirates.



### Team
Team is responsible for clearing all sets and assigning priority for jobs. Is also repsonsible for strategy choosing and maintaining the game clock.


### Team signal
Format:

