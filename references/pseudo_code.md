```javascript
// Pseudocode for Pathfinding Algorithm

OPEN // the set of nodes to be evaluated
CLOSED // the set of nodes already evaluated

// Add the start node to OPEN
add the start node to OPEN

loop
    // Set current to the node in OPEN with the lowest f_cost
    current = node in OPEN with the lowest f_cost
    remove current from OPEN
    add current to CLOSED

    // If the current node is the target node, path has been found
    if current is the target node
        return

    // For each neighbor of the current node
    foreach neighbor of the current node
        // If neighbor is not traversable or neighbor is in CLOSED
        if neighbor is not traversable or neighbor is in CLOSED
            skip to the next neighbor

        // If new path to neighbor is shorter or neighbor is not in OPEN
        if new path to neighbor is shorter OR neighbor is not in OPEN
            // Update the f_cost of neighbor
            set f_cost of neighbor
            // Set the parent of neighbor to current
            set parent of neighbor to current
            // If neighbor is not in OPEN, add neighbor to OPEN
            if neighbor is not in OPEN
                add neighbor to OPEN

```
