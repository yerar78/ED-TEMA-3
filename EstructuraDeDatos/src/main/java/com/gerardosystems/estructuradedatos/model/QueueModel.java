// Defines the package where this class is located.
package com.gerardosystems.estructuradedatos.model;

// Imports LinkedList to implement the Queue.
import java.util.LinkedList;

// Imports Queue to work with the Queue structure.
import java.util.Queue;


// Class used to manage the Queue structure.
public class QueueModel {

    // Creates the Queue where elements will be stored.
    private final Queue<String> queue = new LinkedList<>();


    // Adds an element to the Queue.
    public void enqueue(String value) {

        // Adds the element to the end of the Queue.
        queue.offer(value);
    }


    // Removes an element from the Queue.
    public String dequeue() {

        // Checks if the Queue is empty.
        if (queue.isEmpty()) {

            // Returns null when there are no elements.
            return null;
        }

        // Removes and returns the first element.
        return queue.poll();
    }


    // Removes all elements from the Queue.
    public void clear() {

        // Clears the entire Queue.
        queue.clear();
    }


    // Returns the Queue.
    public Queue<String> getQueue() {

        // Returns the Queue so its elements can be displayed.
        return queue;
    }
}