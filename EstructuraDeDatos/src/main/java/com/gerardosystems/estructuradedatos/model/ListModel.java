// Defines the package where this class is located.
package com.gerardosystems.estructuradedatos.model;

// Imports ArrayList to store elements.
import java.util.ArrayList;

// Imports List to work with the List structure.
import java.util.List;


// Class used to manage the List structure.
public class ListModel {

    // Creates the List where elements will be stored.
    private final List<String> list = new ArrayList<>();


    // Adds an element to the List.
    public void add(String value) {

        // Adds the element to the end of the List.
        list.add(value);
    }


    // Removes an element from the List.
    public String remove(int index) {

        // Checks if the selected index is valid.
        if (index < 0 || index >= list.size()) {

            // Returns null if the index does not exist.
            return null;
        }

        // Removes and returns the selected element.
        return list.remove(index);
    }


    // Removes all elements from the List.
    public void clear() {

        // Clears the entire List.
        list.clear();
    }


    // Returns the List.
    public List<String> getList() {

        // Returns the List so its elements can be displayed.
        return list;
    }
}