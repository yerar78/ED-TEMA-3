// Defines the package where this class is located.
package com.gerardosystems.estructuradedatos.model;

// Imports ArrayDeque to implement the Stack.
import java.util.ArrayDeque;

// Imports Deque to work with the Stack structure.
import java.util.Deque;


// Class used to manage the Stack structure.
public class StackModel {

    // Creates the Stack where elements will be stored.
    private final Deque<String> stack = new ArrayDeque<>();


    // Adds an element to the top of the Stack.
    public void push(String value) {

        // Inserts the element at the top of the Stack.
        stack.push(value);
    }


    // Removes an element from the top of the Stack.
    public String pop() {

        // Checks if the Stack is empty.
        if (stack.isEmpty()) {

            // Returns null when there are no elements.
            return null;
        }

        // Removes and returns the top element.
        return stack.pop();
    }


    // Removes all elements from the Stack.
    public void clear() {

        // Clears the entire Stack.
        stack.clear();
    }


    // Returns the Stack.
    public Deque<String> getStack() {

        // Returns the Stack so its elements can be displayed.
        return stack;
    }
}