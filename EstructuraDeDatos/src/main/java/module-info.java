module com.gerardosystems.estructuradedatos {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires org.kordamp.ikonli.javafx;
    requires org.kordamp.bootstrapfx.core;

    opens com.gerardosystems.estructuradedatos to javafx.fxml;
    exports com.gerardosystems.estructuradedatos;
    exports com.gerardosystems.estructuradedatos.controller;
    opens com.gerardosystems.estructuradedatos.controller to javafx.fxml;
}