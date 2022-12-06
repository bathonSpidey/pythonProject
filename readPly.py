import numpy as np
import open3d

def main():
    cloud = open3d.io.read_point_cloud("test.ply") # Read the point cloud
    open3d.visualization.draw_geometries([cloud]) # Visualize the point cloud

if __name__ == "__main__":
    main()