
import medical_data_visualizer
from unittest import main

# Generate categorical plot
medical_data_visualizer.draw_cat_plot()

# Generate heatmap
medical_data_visualizer.draw_heat_map()

# Run official unit tests
main(module='test_module', exit=False)
