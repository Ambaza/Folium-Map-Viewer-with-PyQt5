import sys
import folium
from folium.plugins import MarkerCluster
from PyQt5.QtCore import Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton


class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Map Viewer")

        # Create the map
        self.map = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

        # Create a cluster of markers for the points
        self.marker_cluster = MarkerCluster().add_to(self.map)

        # Create a Qt WebEngineView to display the map
        self.web_view = QWebEngineView()
        self.web_view.setHtml(self.map._repr_html_())

        # Create text boxes and button to add a new point
        self.lat_box = QLineEdit()
        self.lat_box.setPlaceholderText("Enter latitude")
        self.lon_box = QLineEdit()
        self.lon_box.setPlaceholderText("Enter longitude")
        self.alt_box = QLineEdit()
        self.alt_box.setPlaceholderText("Enter altitude")
        self.add_button = QPushButton("Add Point")
        self.add_button.clicked.connect(self.add_point)

        # Create a layout to hold the widgets
        self.widget_layout = QVBoxLayout()
        self.widget_layout.addWidget(QLabel("Latitude:"))
        self.widget_layout.addWidget(self.lat_box)
        self.widget_layout.addWidget(QLabel("Longitude:"))
        self.widget_layout.addWidget(self.lon_box)
        self.widget_layout.addWidget(QLabel("Altitude:"))
        self.widget_layout.addWidget(self.alt_box)
        self.widget_layout.addWidget(self.add_button)

        # Create a widget to hold the layout and the web view
        self.widget = QWidget()
        self.widget_layout.addStretch()
        self.widget_layout.addWidget(self.web_view)
        self.widget.setLayout(self.widget_layout)

        # Set the widget as the central widget of the main window
        self.setCentralWidget(self.widget)

    def add_point(self):
        # Get the coordinates of the point to add
        lat = float(self.lat_box.text())
        lon = float(self.lon_box.text())
        alt = float(self.alt_box.text())

        # Add a marker for the new point
        folium.Marker(location=[lat, lon], popup=f"{lat}, {lon}, {alt}").add_to(self.marker_cluster)

        # Refresh the map view
        self.web_view.setHtml(self.map._repr_html_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MapWindow()
    window.show()
    sys.exit(app.exec_())
