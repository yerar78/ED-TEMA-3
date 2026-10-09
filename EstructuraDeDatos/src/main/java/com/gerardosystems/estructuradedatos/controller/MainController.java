// Defines the package where this class is located.
package com.gerardosystems.estructuradedatos.controller;


// Imports the class used to manage the List structure.
import com.gerardosystems.estructuradedatos.model.ListModel;

// Imports the class used to manage the Queue structure.
import com.gerardosystems.estructuradedatos.model.QueueModel;

// Imports the class used to manage the Stack structure.
import com.gerardosystems.estructuradedatos.model.StackModel;


// Imports the FXML annotation.
import javafx.fxml.FXML;

// Imports Alert to display messages.
import javafx.scene.control.Alert;

// Imports Button to work with buttons.
import javafx.scene.control.Button;

// Imports Label to display text.
import javafx.scene.control.Label;

// Imports ListView to display elements.
import javafx.scene.control.ListView;

// Imports TextField to receive user input.
import javafx.scene.control.TextField;

// Imports VBox to manage vertical layouts.
import javafx.scene.layout.VBox;


// Controller class for the main interface.
public class MainController {


    // Creates an object to manage the Stack structure.
    private final StackModel stackModel = new StackModel();

    // Creates an object to manage the Queue structure.
    private final QueueModel queueModel = new QueueModel();

    // Creates an object to manage the List structure.
    private final ListModel listModel = new ListModel();


    // Connects the main menu VBox with the FXML file.
    @FXML
    private VBox mainMenu;


    // Connects the structure panel with the FXML file.
    @FXML
    private VBox structurePanel;


    // Connects the title label with the FXML file.
    @FXML
    private Label titleLabel;


    // Connects the description label with the FXML file.
    @FXML
    private Label descriptionLabel;


    // Connects the input field with the FXML file.
    @FXML
    private TextField inputField;


    // Connects the ListView with the FXML file.
    @FXML
    private ListView<String> listView;


    // Connects the add button with the FXML file.
    @FXML
    private Button addButton;


    // Connects the remove button with the FXML file.
    @FXML
    private Button removeButton;


    // Stores the structure currently selected by the user.
    private String currentStructure = "";


    // Displays the Stack structure.
    @FXML
    private void showStack() {

        // Stores Stack as the current structure.
        currentStructure = "stack";

        // Displays the structure panel.
        showStructurePanel();

        // Changes the title of the interface.
        titleLabel.setText("EJEMPLO DE PILA (STACK)");

        // Displays a description of the Stack.
        descriptionLabel.setText(
                "La pila utiliza LIFO: "
                        + "el último elemento en entrar es el primero en salir."
        );

        // Sets the placeholder text of the input field.
        inputField.setPromptText("Ingrese un elemento");

        // Changes the text of the add button.
        addButton.setText("Apilar");

        // Changes the text of the remove button.
        removeButton.setText("Desapilar");

        // Updates the ListView with Stack elements.
        updateStackView();
    }


    // Displays the Queue structure.
    @FXML
    private void showQueue() {

        // Stores Queue as the current structure.
        currentStructure = "queue";

        // Displays the structure panel.
        showStructurePanel();

        // Changes the title of the interface.
        titleLabel.setText("EJEMPLO DE COLA (QUEUE)");

        // Displays a description of the Queue.
        descriptionLabel.setText(
                "La cola utiliza FIFO: "
                        + "el primero en entrar es el primero en salir."
        );

        // Sets the placeholder text of the input field.
        inputField.setPromptText("Ingrese un elemento");

        // Changes the text of the add button.
        addButton.setText("Encolar");

        // Changes the text of the remove button.
        removeButton.setText("Desencolar");

        // Updates the ListView with Queue elements.
        updateQueueView();
    }


    // Displays the List structure.
    @FXML
    private void showList() {

        // Stores List as the current structure.
        currentStructure = "list";

        // Displays the structure panel.
        showStructurePanel();

        // Changes the title of the interface.
        titleLabel.setText("EJEMPLO DE LISTA");

        // Displays a description of the List.
        descriptionLabel.setText(
                "Una lista permite almacenar y modificar "
                        + "varios elementos."
        );

        // Sets the placeholder text of the input field.
        inputField.setPromptText("Ingrese un elemento");

        // Changes the text of the add button.
        addButton.setText("Agregar");

        // Changes the text of the remove button.
        removeButton.setText("Eliminar");

        // Updates the ListView with List elements.
        updateListView();
    }


    // Shows the panel containing the selected structure.
    private void showStructurePanel() {

        // Hides the main menu.
        mainMenu.setVisible(false);

        // Prevents the hidden menu from occupying space.
        mainMenu.setManaged(false);

        // Shows the structure panel.
        structurePanel.setVisible(true);

        // Allows the structure panel to occupy space.
        structurePanel.setManaged(true);
    }


    // Adds an element to the selected structure.
    @FXML
    private void addElement() {

        // Gets the text entered by the user.
        String value = inputField.getText().trim();


        // Checks if the input field is empty.
        if (value.isEmpty()) {

            // Displays a warning message.
            showMessage(
                    "Advertencia",
                    "Ingrese un elemento."
            );

            // Stops the method.
            return;
        }


        // Determines which structure is currently selected.
        switch (currentStructure) {


            // Executes when the selected structure is Stack.
            case "stack":

                // Adds the element to the Stack.
                stackModel.push(value);

                // Updates the Stack ListView.
                updateStackView();

                // Ends this case.
                break;


            // Executes when the selected structure is Queue.
            case "queue":

                // Adds the element to the Queue.
                queueModel.enqueue(value);

                // Updates the Queue ListView.
                updateQueueView();

                // Ends this case.
                break;


            // Executes when the selected structure is List.
            case "list":

                // Adds the element to the List.
                listModel.add(value);

                // Updates the List ListView.
                updateListView();

                // Ends this case.
                break;
        }


        // Clears the input field.
        inputField.clear();
    }


    // Removes an element from the selected structure.
    @FXML
    private void removeElement() {

        // Determines which structure is currently selected.
        switch (currentStructure) {


            // Executes when the selected structure is Stack.
            case "stack":

                // Removes the top element from the Stack.
                String stackValue = stackModel.pop();


                // Checks if the Stack is empty.
                if (stackValue == null) {

                    // Displays a message informing that the Stack is empty.
                    showMessage(
                            "Pila vacía",
                            "No hay elementos."
                    );

                    // Stops the method.
                    return;
                }


                // Updates the Stack ListView.
                updateStackView();

                // Ends this case.
                break;


            // Executes when the selected structure is Queue.
            case "queue":

                // Removes the first element from the Queue.
                String queueValue = queueModel.dequeue();


                // Checks if the Queue is empty.
                if (queueValue == null) {

                    // Displays a message informing that the Queue is empty.
                    showMessage(
                            "Cola vacía",
                            "No hay elementos."
                    );

                    // Stops the method.
                    return;
                }


                // Updates the Queue ListView.
                updateQueueView();

                // Ends this case.
                break;


            // Executes when the selected structure is List.
            case "list":

                // Gets the selected index from the ListView.
                int selectedIndex =
                        listView.getSelectionModel()
                                .getSelectedIndex();


                // Checks if no element was selected.
                if (selectedIndex == -1) {

                    // Displays a message asking the user to select an element.
                    showMessage(
                            "Seleccionar",
                            "Seleccione un elemento del ListView."
                    );

                    // Stops the method.
                    return;
                }


                // Removes the selected element from the List.
                listModel.remove(selectedIndex);

                // Updates the ListView.
                updateListView();

                // Ends this case.
                break;
        }
    }


    // Removes all elements from the selected structure.
    @FXML
    private void clearStructure() {

        // Determines which structure is currently selected.
        switch (currentStructure) {


            // Executes when the selected structure is Stack.
            case "stack":

                // Removes all elements from the Stack.
                stackModel.clear();

                // Updates the Stack ListView.
                updateStackView();

                // Ends this case.
                break;


            // Executes when the selected structure is Queue.
            case "queue":

                // Removes all elements from the Queue.
                queueModel.clear();

                // Updates the Queue ListView.
                updateQueueView();

                // Ends this case.
                break;


            // Executes when the selected structure is List.
            case "list":

                // Removes all elements from the List.
                listModel.clear();

                // Updates the ListView.
                updateListView();

                // Ends this case.
                break;
        }
    }


    // Updates the ListView with Stack elements.
    private void updateStackView() {

        // Removes all previous elements from the ListView.
        listView.getItems().clear();

        // Loops through all Stack elements.
        for (String value : stackModel.getStack()) {

            // Adds only the element without a number.
            listView.getItems().add(value);
        }
    }


    // Updates the ListView with Queue elements.
    private void updateQueueView() {

        // Removes all previous elements from the ListView.
        listView.getItems().clear();

        // Loops through all Queue elements.
        for (String value : queueModel.getQueue()) {

            // Adds only the element without a number.
            listView.getItems().add(value);
        }
    }


    // Updates the ListView with List elements.
    private void updateListView() {

        // Removes all previous elements from the ListView.
        listView.getItems().clear();

        // Loops through all List elements.
        for (String value : listModel.getList()) {

            // Adds only the element without a number.
            listView.getItems().add(value);
        }
    }


    // Returns to the main menu.
    @FXML
    private void backToMenu() {

        // Hides the structure panel.
        structurePanel.setVisible(false);

        // Prevents the hidden panel from occupying space.
        structurePanel.setManaged(false);

        // Shows the main menu.
        mainMenu.setVisible(true);

        // Allows the main menu to occupy space.
        mainMenu.setManaged(true);

        // Clears the input field.
        inputField.clear();
    }


    // Displays a message to the user.
    private void showMessage(
            String title,
            String message
    ) {

        // Creates an information alert.
        Alert alert = new Alert(
                Alert.AlertType.INFORMATION
        );

        // Sets the title of the alert.
        alert.setTitle(title);

        // Removes the header text.
        alert.setHeaderText(null);

        // Sets the message displayed in the alert.
        alert.setContentText(message);

        // Displays the alert and waits for the user.
        alert.showAndWait();
    }
}